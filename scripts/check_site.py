#!/usr/bin/env python3
import argparse
import json
import re
import sys
import tomllib
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_URL = "https://michelamassage.ch/"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.ids = set()
        self.labels = []
        self.images = []
        self.scripts = []
        self.links = []
        self.jsonld_blocks = []
        self._in_jsonld = False
        self._jsonld_buf = []
        self.has_main = False
        self.has_skip_link = False

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            self.ids.add(d["id"])
        if tag == "main":
            self.has_main = True
        if tag == "a" and d.get("class") == "skip-link":
            self.has_skip_link = True
        if tag in {"img", "script"} and "src" in d:
            self.refs.append(d["src"])
        if tag == "link" and "href" in d:
            self.refs.append(d["href"])
        if tag == "label":
            self.labels.append(d)
        if tag == "img":
            self.images.append(d)
        if tag == "script":
            self.scripts.append(d)
            if d.get("type") == "application/ld+json":
                self._in_jsonld = True
                self._jsonld_buf = []
        if tag == "link":
            self.links.append(d)

    def handle_endtag(self, tag):
        if tag == "script" and self._in_jsonld:
            self._in_jsonld = False
            self.jsonld_blocks.append("".join(self._jsonld_buf))

    def handle_data(self, data):
        if self._in_jsonld:
            self._jsonld_buf.append(data)


def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    return False


def parse_html():
    html_path = ROOT / "index.html"
    if not html_path.exists():
        raise SystemExit("index.html not found")
    html = html_path.read_text(encoding="utf-8")
    parser = SiteParser()
    parser.feed(html)
    return html, parser


def check_refs():
    html, parser = parse_html()
    ok = True

    missing = []
    for ref in parser.refs:
        if ref.startswith(("http://", "https://", "mailto:", "tel:", "#")):
            continue
        if not (ROOT / ref).exists():
            missing.append(ref)
    if missing:
        ok = fail("Missing local references: " + ", ".join(missing))

    if "data:image/" in html:
        ok = fail("Found inline data:image URI in index.html")
    if "<style" in html.lower():
        ok = fail("Found inline <style> block in index.html")

    return ok


def check_html():
    html, parser = parse_html()
    ok = True

    if not parser.has_main:
        ok = fail("Missing <main> landmark")
    if not parser.has_skip_link:
        ok = fail("Missing .skip-link")

    bad_labels = [label for label in parser.labels if "for" not in label or label["for"] not in parser.ids]
    if bad_labels:
        ok = fail(f"Labels without valid for/id: {bad_labels}")

    images_without_alt = [img.get("src", "<unknown>") for img in parser.images if "alt" not in img]
    if images_without_alt:
        ok = fail("Images without alt attribute: " + ", ".join(images_without_alt))

    if "aria-label=\"Language selection\"" not in html:
        ok = fail("Missing language switcher aria-label")
    if "aria-pressed" not in html:
        ok = fail("Missing aria-pressed on language buttons")

    return ok


def check_css():
    css_path = ROOT / "assets/css/styles.css"
    if not css_path.exists():
        return fail("assets/css/styles.css not found")
    css = css_path.read_text(encoding="utf-8")
    ok = True

    if ".skip-link" not in css:
        ok = fail("Missing .skip-link styles")
    if "focus-visible" not in css:
        ok = fail("Missing focus-visible styles")
    if "prefers-reduced-motion" not in css:
        ok = fail("Missing prefers-reduced-motion styles")

    # Simple brace balance catches common accidental truncations.
    if css.count("{") != css.count("}"):
        ok = fail("CSS brace count mismatch")

    return ok


def check_validate():
    html, parser = parse_html()
    ok = True

    try:
        netlify_config = tomllib.loads((ROOT / "netlify.toml").read_text(encoding="utf-8"))
    except Exception as exc:
        ok = fail(f"netlify.toml parse error: {exc}")
        netlify_config = {}

    for block in parser.jsonld_blocks:
        try:
            json.loads(block)
        except Exception as exc:
            ok = fail(f"JSON-LD parse error: {exc}")

    if not re.search(r'<meta name="description"', html):
        ok = fail("Missing meta description")
    if not re.search(r'<meta property="og:title"', html):
        ok = fail("Missing og:title")

    canonical_links = [
        link for link in parser.links
        if link.get("rel") == "canonical" and link.get("href") == CANONICAL_URL
    ]
    if len(canonical_links) != 1:
        ok = fail(f"Expected one canonical link to {CANONICAL_URL}")
    if f'<meta property="og:url" content="{CANONICAL_URL}">' not in html:
        ok = fail(f"Missing og:url for {CANONICAL_URL}")

    robots_path = ROOT / "robots.txt"
    if not robots_path.exists():
        ok = fail("robots.txt not found")
    else:
        robots = robots_path.read_text(encoding="utf-8")
        if "User-agent: *" not in robots or "Allow: /" not in robots:
            ok = fail("robots.txt must allow public crawling")
        if f"Sitemap: {CANONICAL_URL}sitemap.xml" not in robots:
            ok = fail("robots.txt does not reference the canonical sitemap")

    sitemap_path = ROOT / "sitemap.xml"
    if not sitemap_path.exists():
        ok = fail("sitemap.xml not found")
    else:
        try:
            sitemap_root = ET.parse(sitemap_path).getroot()
            namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            sitemap_urls = [element.text for element in sitemap_root.findall("sm:url/sm:loc", namespace)]
            if sitemap_urls != [CANONICAL_URL]:
                ok = fail(f"Unexpected sitemap URLs: {sitemap_urls}")
        except Exception as exc:
            ok = fail(f"sitemap.xml parse error: {exc}")

    redirects = netlify_config.get("redirects", [])
    expected_redirects = {
        "https://michelamassage.netlify.app/*": "https://michelamassage.ch/:splat",
        "https://www.michelamassage.ch/*": "https://michelamassage.ch/:splat",
    }
    actual_redirects = {redirect.get("from"): redirect.get("to") for redirect in redirects}
    for source, destination in expected_redirects.items():
        if actual_redirects.get(source) != destination:
            ok = fail(f"Missing canonical-domain redirect: {source} -> {destination}")

    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refs", action="store_true")
    ap.add_argument("--validate", action="store_true")
    ap.add_argument("--html-only", action="store_true")
    ap.add_argument("--css-only", action="store_true")
    args = ap.parse_args()

    checks = []
    if args.refs:
        checks.append(check_refs)
    if args.validate:
        checks.append(check_validate)
    if args.html_only:
        checks.append(check_html)
    if args.css_only:
        checks.append(check_css)
    if not checks:
        checks = [check_refs, check_validate, check_html, check_css]

    ok = all(check() for check in checks)
    if ok:
        print("check_site=ok")
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
