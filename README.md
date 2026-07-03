# Michela Massage Website

Static landing page for Michela Massage in Zürich. The site presents Michela's massage and lymphatic drainage services, prices, contact details, and booking flow in German and Italian.

Production site:

```text
https://michelamassage.netlify.app
```

## What this project is

This is intentionally a simple static website:

- no framework;
- no bundler;
- no required npm install;
- no build step;
- deployable directly to Netlify from the repository root.

The site is built from plain HTML, CSS, and vanilla JavaScript.

## Project structure

```text
.
├── index.html                         # Main single-page HTML document
├── netlify.toml                       # Netlify publish/cache/security config
├── Makefile                           # Local development, checks, deploy targets
├── AGENTS.md                          # Project instructions for Hermes/AI agents
├── assets/
│   ├── css/styles.css                 # Site styles
│   ├── js/main.js                     # Language switcher, QR code, form, reveal logic
│   └── images/                        # Logo, atmosphere image, extracted inline images
├── scripts/
│   ├── check_site.py                  # HTML/CSS/metadata/reference checks
│   ├── check_docs.py                  # Documentation/project checklist checks
│   └── smoke_test.py                  # Temporary local HTTP smoke test
└── docs/
    ├── README.md                      # Documentation index
    ├── architecture.md                # Technical architecture notes
    ├── content-map.md                 # Content, services, prices, contacts
    ├── maintenance.md                 # Editing and maintenance guide
    ├── accessibility-seo-review.md    # Accessibility/SEO/performance review
    ├── netlify-deploy.md              # Netlify setup and deploy workflow
    ├── session-log.md                 # Concise latest work summary
    ├── current-task.md                # Next recommended step
    └── development-workflow.excalidraw # Editable workflow diagram
```

## Requirements

Minimum:

- `make`
- `python3`

Optional:

- `node`, for `node --check assets/js/main.js`
- Netlify CLI, for `make deploy` and `make deploy-prod`
- `htmlhint` / `stylelint`, if you want stricter external linters

The built-in checks work without installing Node packages.

## Local development

Start a local static server:

```bash
make serve
```

Open:

```text
http://127.0.0.1:8000
```

Use a different port if needed:

```bash
make serve PORT=8080
```

Print all available Make targets:

```bash
make help
```

## Recommended workflow with Hermes / AI

Use this workflow for normal changes:

```text
1. Start from the project root.
2. Review `AGENTS.md` for project-specific rules.
3. Run `make serve` for local preview when changing UI/content.
4. Make small, focused changes.
5. Run targeted checks while editing when useful:
   - make lint-js
   - make lint-css
   - make refs
   - make validate
6. Run `make check` before considering the technical work done.
7. Update `docs/` if behavior, content, workflow, deploy, SEO, accessibility, or architecture changed.
8. Run `make final-check` before handoff or deploy.
9. Deploy only after checks pass.
```

The editable workflow diagram is available at:

```text
docs/development-workflow.excalidraw
```

Open it by dragging the file into https://excalidraw.com.

## Quality gates

Run the main technical checks:

```bash
make check
```

This runs:

- `make refs` — verifies local CSS/JS/image references and prevents inline base64 image regressions;
- `make validate` — validates `netlify.toml`, JSON-LD, and basic metadata;
- `make lint` — runs HTML/CSS/JS checks with built-in fallbacks;
- `make smoke` — starts a temporary local server and verifies key endpoints.

Run the close-out check before finishing a non-trivial task:

```bash
make final-check
```

This runs `make check` plus:

- `make docs-check` — verifies required docs and project checklist markers.

If a check fails, fix the root cause and rerun the target. Do not bypass failing checks.

## Netlify deployment

This site is linked to Netlify in manual deploy mode, without a Git remote.

Netlify project:

```text
Site URL: https://michelamassage.netlify.app
Site ID:  ae891950-b3cc-4a6f-baa4-f483277b32f5
```

Netlify settings:

```text
Build command:     <empty>
Directory to deploy: .
```

Preview deploy:

```bash
make deploy
```

Production deploy:

```bash
make deploy-prod
```

Print the production URL:

```bash
make deploy-open
```

See `docs/netlify-deploy.md` for detailed deploy notes.

## Content and maintenance notes

When changing visible content, keep these areas consistent:

- service cards;
- pricing table;
- form options;
- QR/email text;
- JSON-LD structured data, when business details change;
- German and Italian text attributes (`data-d` and `data-i`).

For bilingual text, update:

1. `data-i` for Italian;
2. `data-d` for German;
3. the initial visible text, which is German by default.

For images:

- keep assets under `assets/images/`;
- do not reintroduce base64 inline images in `index.html`;
- use `loading="lazy"` for below-the-fold images.

## Accessibility and SEO baseline

Preserve these existing features:

- single primary `<h1>`;
- `<main id="main-content">` landmark;
- skip link to main content;
- visible keyboard focus;
- `prefers-reduced-motion` support;
- labeled form fields with `name` and `autocomplete`;
- Open Graph metadata;
- `HealthAndBeautyBusiness` JSON-LD;
- Netlify security headers.

See `docs/accessibility-seo-review.md` for the detailed review.

## Documentation map

Start here:

```text
docs/README.md
```

Important docs:

- `docs/architecture.md` — technical structure and dependencies;
- `docs/content-map.md` — content, services, pricing, contact flow;
- `docs/maintenance.md` — how to edit text, prices, contacts, images;
- `docs/netlify-deploy.md` — Netlify and Makefile workflow;
- `docs/accessibility-seo-review.md` — accessibility, SEO, performance notes;
- `docs/session-log.md` — concise latest work summary;
- `docs/current-task.md` — next recommended step.

## Current known follow-ups

Before production/business review, confirm:

- whether prenatal massage prices and pregnancy package prices are still current;
- whether all phone/email details are final;
- whether Google Fonts, QRCode.js, and the remote Unsplash hero image should be self-hosted for stronger privacy/performance.
