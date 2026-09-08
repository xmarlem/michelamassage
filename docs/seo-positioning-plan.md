# SEO Positioning Plan

Last updated: 2026-08-15

Canonical website: https://michelamassage.ch/

## Goal

Improve Michela Massage's qualified organic visibility in Zürich and Oerlikon while preserving the site's focused boutique positioning, static architecture, accessibility, and cautious health and insurance language.

The initial objective is not to rank for the broad term “massage Zürich”. The practical objective is to become discoverable for specific service-plus-location searches that closely match the real offer, such as:

- `Massage Oerlikon`;
- `Klassische Massage Oerlikon`;
- `Lymphdrainage Oerlikon`;
- `Lymphdrainage Zürich`;
- `Schwangerschaftsmassage Zürich`;
- `Schwangerschaftsmassage Oerlikon`;
- `ASCA Massage Zürich`;
- `EMR Massage Oerlikon`.

## Principles

- Prioritise local relevance and qualified enquiries over raw traffic.
- Publish only verified business, qualification, availability, price, and insurance information.
- Avoid unsupported clinical outcomes, guaranteed reimbursement language, keyword stuffing, and thin location pages.
- Keep visible content, metadata, structured data, forms, email templates, and policies consistent.
- Preserve a static-first implementation; do not introduce a framework or booking platform without a demonstrated operational need.
- Measure results before expanding the page set.

## Current baseline

Audit observations from 2026-08-15:

- the live custom domain serves the homepage;
- `robots.txt` and `sitemap.xml` returned 404 before this plan's first implementation set;
- the homepage did not contain an explicit HTML canonical URL or `og:url`;
- `HealthAndBeautyBusiness` JSON-LD was already present;
- German, Italian, and English are available to visitors through client-side switching on one URL;
- the site is currently a single page;
- the booking request still depends on a `mailto:` flow;
- the site's source-level accessibility and static runtime are strong foundations;
- a `site:michelamassage.ch` search did not return results in the search provider used for the audit; this is a signal to verify in Google Search Console, not definitive proof of non-indexing.

## Phase 1 — Technical discovery and canonical domain

Priority: immediate

Status: in progress

### Repository changes

- [x] Add a self-referencing canonical URL to the homepage.
- [x] Add canonical `og:url` and an absolute Open Graph image URL.
- [x] Add the canonical URL and image to `HealthAndBeautyBusiness` JSON-LD.
- [x] Add `robots.txt` allowing public crawling and referencing the sitemap.
- [x] Add `sitemap.xml` containing the canonical homepage.
- [x] Configure permanent redirects from the Netlify hostname and `www` hostname to `https://michelamassage.ch/`.
- [x] Add automated validation for canonical metadata, robots, sitemap, and redirects.
- [ ] Deploy the changes to production.
- [ ] Verify the production responses for the homepage, robots, sitemap, Netlify hostname, and `www` hostname.

### External actions

These actions require access to third-party accounts and cannot be completed solely in the repository:

- [ ] Verify a domain property for `michelamassage.ch` in Google Search Console.
- [ ] Inspect the canonical homepage URL in Search Console.
- [ ] Submit `https://michelamassage.ch/sitemap.xml`.
- [ ] Check the Google-selected canonical and indexing status.
- [ ] Register or verify the site in Bing Webmaster Tools and submit the sitemap.
- [ ] Verify the custom-domain TLS certificate from a correctly synchronised external client.

## Phase 2 — Local business presence and trust

Priority: high

### Google Business Profile

- [ ] Claim and verify the Google Business Profile.
- [ ] Use the exact business name, address, phone number, and canonical website URL shown on the site.
- [ ] Select the most accurate primary and secondary categories.
- [ ] Add real availability rather than generic opening hours.
- [ ] Add treatment information and prices where appropriate.
- [ ] Upload authentic practitioner and practice photographs.
- [ ] Add an appointment-request link.
- [ ] Review profile accuracy monthly.

### Professional and local evidence

- [ ] Ensure consistent business details on ASCA/EMR or other applicable professional registries.
- [ ] Request a practitioner link from Therapie Oerlikon if operationally appropriate.
- [ ] Add only relevant, reputable local directory or partner citations.
- [ ] Document verified public-transport, arrival, and accessibility information.

### Reviews

- [ ] Create a direct Google review link after the profile is verified.
- [ ] Request honest reviews without incentives or scripted ratings.
- [ ] Respond without exposing customer health information.
- [ ] Publish testimonials on the site only with explicit permission and transparent provenance.
- [ ] Do not add self-serving `AggregateRating` markup for the local business.

## Phase 3 — Focused German service pages

Priority: high after Phase 1 production verification

German is the primary local-market language and should be implemented first. Create a small set of substantial pages rather than a city/keyword matrix.

Recommended first routes:

- `/de/klassische-massage-zuerich-oerlikon/`;
- `/de/lymphdrainage-zuerich-oerlikon/`;
- `/de/schwangerschaftsmassage-zuerich/`;
- `/de/reset-massage-zuerich/`;
- `/de/preise-und-termin/`.

Each page should answer:

- who the treatment may suit;
- what happens before, during, and after the appointment;
- Michela's verified approach and qualifications;
- duration and current price;
- location and Tuesday availability;
- preparation and practical arrival information;
- relevant treatment boundaries and contraindication discussion;
- cautious ASCA/EMR reimbursement guidance;
- how to request an appointment;
- which related page should be visited next.

Every page must have:

- a unique descriptive title and meta description;
- one H1 aligned with the visible topic;
- a self-referencing canonical URL;
- page-specific Open Graph metadata;
- crawlable internal links;
- an entry in the sitemap;
- consistent visible and structured business data;
- meaningful image alternatives where images convey information.

## Phase 4 — Multilingual organic discovery

Priority: medium

The current JavaScript language switch helps visitors but exposes one canonical document to search engines. If organic discovery in all three languages is confirmed as a business goal, migrate to stable localized paths:

- `/de/`;
- `/it/`;
- `/en/`.

For each localized page:

- [ ] render the correct language in static HTML;
- [ ] set the correct `<html lang>` value;
- [ ] provide localized title, description, heading, and navigation;
- [ ] self-canonicalise;
- [ ] add reciprocal `hreflang` links;
- [ ] add an appropriate `x-default` link;
- [ ] include the canonical localized URL in the sitemap;
- [ ] keep all translations and business-critical details synchronized.

Do not multiply service pages into Italian and English until the German structure is stable and translations can be maintained reliably.

## Phase 5 — Conversion improvements

SEO earns relevant visits; conversion turns those visits into appointment requests.

- [ ] Add a direct WhatsApp CTA with a privacy-conscious prefilled message.
- [ ] Add a short “How booking works” sequence.
- [ ] Explain the expected response and confirmation process without making an unreliable time promise.
- [ ] Publish payment, cancellation, rescheduling, package, and first-visit information.
- [ ] Add a persistent but unobtrusive mobile appointment action.
- [ ] Evaluate an in-browser request form that does not require a configured email client.
- [ ] Preserve phone and email fallbacks.
- [ ] Avoid customer accounts, online payment, or a large booking platform until measured demand justifies them.

## Phase 6 — Measurement and iteration

Establish a baseline after production deployment and review monthly.

### Search Console

Track:

- indexed canonical pages;
- queries;
- impressions;
- clicks;
- click-through rate;
- average position;
- pages with impressions but weak click-through rate;
- crawl or canonical exclusions.

### Google Business Profile

Track where available:

- website clicks;
- calls;
- direction requests;
- appointment-link interactions;
- review count and response coverage.

### Business outcomes

Track without collecting unnecessary health data:

- phone, WhatsApp, and email clicks;
- appointment requests by channel;
- completed appointments attributable to organic discovery;
- answers to “How did you find the practice?”.

Publish additional pages based on real search queries and client questions, not speculative keyword volume.

## First 90-day sequence

### Days 1–14

- complete and deploy Phase 1;
- verify Search Console and submit the sitemap;
- verify or create the Google Business Profile;
- confirm business details and professional claims;
- prepare legal/privacy/cancellation content;
- add a direct appointment CTA.

### Days 15–45

- publish the German lymphatic-drainage page;
- publish the German prenatal-massage page;
- add practical Oerlikon arrival information;
- expand verified practitioner credentials;
- begin a permission-based review process.

### Days 46–90

- review Search Console query and indexing data;
- improve titles or snippets with impressions but weak click-through rate;
- publish the next page only when evidence supports it;
- decide whether localized `/it/` and `/en/` structures are maintainable;
- evaluate whether manual appointment coordination is a measurable bottleneck.

## Success criteria

The first implementation cycle is successful when:

- the canonical homepage, robots file, and sitemap return HTTP 200 in production;
- Netlify and `www` hostnames redirect permanently to the canonical domain;
- Search Console reports the homepage as indexable with the intended canonical;
- the sitemap is accepted without errors;
- the Google Business Profile is accurate and linked to the canonical domain;
- qualified local impressions and enquiries can be measured;
- no business-critical data or health claims become inconsistent across surfaces.

## Authoritative references

- Google SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Localized versions and `hreflang`: https://developers.google.com/search/docs/specialty/international/localized-versions
- LocalBusiness structured data: https://developers.google.com/search/docs/appearance/structured-data/local-business
- Sitemap guidance: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Google local ranking guidance: https://support.google.com/business/answer/7091
