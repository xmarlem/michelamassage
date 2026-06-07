#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DOCS = [
    "README.md",
    "architecture.md",
    "content-map.md",
    "maintenance.md",
    "accessibility-seo-review.md",
    "netlify-deploy.md",
    "session-log.md",
    "current-task.md",
]

REQUIRED_AGENTS_MARKERS = [
    "## End-of-task checklist",
    "Update `docs/`",
    "make final-check",
]

REQUIRED_NETLIFY_MARKERS = [
    "https://michelamassage.netlify.app",
    "ae891950-b3cc-4a6f-baa4-f483277b32f5",
    "make final-check",
]

REQUIRED_README_MARKERS = [
    "# Michela Massage Website",
    "make check",
    "make final-check",
    "make deploy-prod",
    "docs/development-workflow.excalidraw",
]


def fail(message: str) -> bool:
    print(f"ERROR: {message}", file=sys.stderr)
    return False


def contains_all(path: Path, markers: list[str]) -> bool:
    text = path.read_text(encoding="utf-8")
    missing = [marker for marker in markers if marker not in text]
    if missing:
        return fail(f"{path.relative_to(ROOT)} missing markers: {', '.join(missing)}")
    return True


def main() -> int:
    ok = True

    docs_dir = ROOT / "docs"
    if not docs_dir.is_dir():
        return 1 if fail("docs/ directory not found") else 0

    for name in REQUIRED_DOCS:
        path = docs_dir / name
        if not path.exists():
            ok = fail(f"missing docs/{name}")
            continue
        if not path.read_text(encoding="utf-8").strip():
            ok = fail(f"docs/{name} is empty")

    agents = ROOT / "AGENTS.md"
    if not agents.exists():
        ok = fail("AGENTS.md not found")
    else:
        ok = contains_all(agents, REQUIRED_AGENTS_MARKERS) and ok

    readme = ROOT / "README.md"
    if not readme.exists():
        ok = fail("README.md not found")
    else:
        ok = contains_all(readme, REQUIRED_README_MARKERS) and ok

    netlify_doc = docs_dir / "netlify-deploy.md"
    if netlify_doc.exists():
        ok = contains_all(netlify_doc, REQUIRED_NETLIFY_MARKERS) and ok

    if ok:
        print("docs_check=ok")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
