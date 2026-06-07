# AGENTS.md

This file contains operating instructions for AI agents working on this project.
Hermes Agent automatically loads `AGENTS.md` from the working directory at the beginning of a session, so these rules should stay concise, stable, and maintenance-oriented.

## Project context

This repository contains the static website for Michela Massage, deployed on Netlify.

Stack:

- Static HTML: `index.html`
- CSS: `assets/css/styles.css`
- Vanilla JavaScript: `assets/js/main.js`
- Images: `assets/images/`
- Netlify config: `netlify.toml`
- Documentation: `docs/`

Do not introduce frameworks, bundlers, or npm dependencies unless there is a clear need.
The site must remain easy to deploy on Netlify with publish directory `.` and no build command.

## Change principles

- Prefer small, explicit, easy-to-review changes.
- Do not perform full rewrites when a targeted patch is enough.
- Keep content, styling, and behavior separated:
  - markup in `index.html`;
  - styling in `assets/css/styles.css`;
  - behavior in `assets/js/main.js`.
- Avoid unnecessary duplication, but keep the code understandable.
- Update `docs/` when structure, deploy, workflow, or visible behavior changes.
- Before considering a task complete, run at least `make check` when available.

## Accessibility

Every UI change must preserve or improve accessibility.

Minimum checklist:

- Keep a single primary `<h1>`.
- Preserve the `<main id="main-content">` landmark.
- Preserve the skip link to the main content.
- Every form input must have a `label for="..."` connected to a valid `id`.
- Form fields must have `name` and, when useful, `autocomplete`.
- Every image must have an `alt` attribute; use `alt=""` only for decorative images.
- Interactive controls must be keyboard-accessible.
- Visible focus must not be removed.
- Respect `prefers-reduced-motion` for animations and transitions.
- Do not rely on color alone to communicate important information.

## SEO and content

- Keep `title` and meta description descriptive.
- Preserve or update Open Graph metadata when main content changes.
- Preserve or update the `HealthAndBeautyBusiness` JSON-LD when contacts, address, or prices change.
- Keep consistency across:
  - service cards;
  - pricing table;
  - form options;
  - email/QR-code text.
- For bilingual text, always update both `data-i` and `data-d`, plus the initial visible German text.

## Performance

- Do not reintroduce base64 inline images in `index.html`.
- New images must live in `assets/images/`.
- Use `loading="lazy"` for below-the-fold images.
- Avoid external libraries when vanilla JavaScript/CSS is sufficient.
- When adding static assets, verify that paths are relative and work on Netlify.

## JavaScript

- Use vanilla JavaScript compatible with modern browsers.
- Avoid additional global state unless clearly necessary.
- Provide fallbacks for external dependencies, as currently done for QRCode.js.
- Do not convert the form to server-side submission without explicit request; it currently opens a `mailto:` link.
- After JavaScript changes, verify with `make lint-js` or `make check`.

## CSS

- Reuse the CSS variables in `:root`.
- Preserve the navy/gold/cream visual theme.
- Avoid overly specific or fragile selectors.
- Verify desktop layout and mobile layout below `768px`.
- After CSS changes, verify with `make lint-css` or `make check`.

## Netlify and deploy

The linked Netlify project is:

- Site URL: `https://michelamassage.netlify.app`
- Site ID: `ae891950-b3cc-4a6f-baa4-f483277b32f5`
- Deploy mode: manual, without Git remote

Commands:

```bash
make check
make deploy       # preview
make deploy-prod  # production
```

If the Netlify CLI asks for the directory to deploy, use:

```text
.
```

If it asks for a build command, leave it empty.

## Verification

Before finalizing significant changes:

```bash
make check
```

Before ending a task or session that changed code, content, configuration, deploy workflow, accessibility, SEO, or operations:

```bash
make final-check
```

For local development:

```bash
make serve
```

If `make check` fails, fix the real cause instead of ignoring the check.

## End-of-task checklist

Before considering work complete:

- Update `docs/` when behavior, structure, deployment, workflow, accessibility, SEO, content, or operational assumptions changed.
- Run `make final-check` for non-trivial changes.
- If documentation was not updated, be ready to explain why no stable docs change was needed.
- Mention which checks were run and which documentation files changed in the final response.

## Documentation

Update documentation in `docs/` when a stable behavior or workflow changes:

- `docs/netlify-deploy.md` for deploy, Netlify, and Makefile workflow;
- `docs/architecture.md` for technical structure;
- `docs/content-map.md` for content, services, prices, and contacts;
- `docs/maintenance.md` for editing procedures;
- `docs/accessibility-seo-review.md` for review notes and recommendations.

## Avoid

- Do not add frameworks or build steps just for convenience.
- Do not mark unverified changes as complete.
- Do not leave prices inconsistent across different sections.
- Do not break the static Netlify deployment.
- Do not remove existing accessibility checks.
