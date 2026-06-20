# CLAUDE.md — Norge på langs, restored static site (02-restored-static/)

This file is the source of truth for decisions made about this project.
Read it before starting any work session. Update it when a decision changes
or a task completes. If something here conflicts with an earlier instruction
in chat, THIS FILE WINS unless the person explicitly says otherwise in the
current session.

## Hard rules (apply to 02-restored-static/ ONLY)

- **Never touch `03-modernized/` or `01-original-php/`.** Confirm no files
  outside `02-restored-static/` changed before every commit.
- **This site is done and faithful to the original 2009 site.** Do not add
  features, change layouts, or modify content not covered by a specific decision.
  Be precise and conservative — only change what is described.
- **Never alter visible text or image content when unlinking dead links.** Strip
  the `<a href>` wrapper only; keep inner text/image exactly as is (same alt
  text, same position, same markup otherwise).
- **Never invent content.** Every word, image, and link must trace back to the
  original 2009 site or an explicit decision in this file.

## What this site is

A static HTML restoration of the original Norge på langs site (PHP/MySQL, 2008–2009,
now defunct). All 16 pages recovered from the Wayback Machine and cleaned up.
The PHP-generated content (Turlogg diary entries) lived in a MySQL database
(mysql.stud.ntnu.no, closed) — those entries are permanently lost except for
4 recovered entry titles/timestamps shown on turlogg.html. The guestbook
(Bravenet embed) is also gone — shown as a static placeholder on gjestebok.html.

## Site structure (16 pages)

index.html, omoss.html, reisebrev.html, reisebrev1–6.html, reiserute.html,
sponsorer.html, utstyr.html, turlogg.html, galleri.html, videogalleri.html,
vid1–6.html, gjestebok.html

## Live URL

https://arneskeie.github.io/norgepalangs-2009/ (repo: arneskeie/norgepalangs-2009)

Paired with modernized site: https://arneskeie.github.io/norgepalangs/
(repo: arneskeie/norgepalangs)

## Version switcher

All 16 pages share an identical version-switcher component at the bottom (inline `<style>`
+ `<div>` markup, no external JS or CSS). It lets users toggle between this restored site
and the modernized site. Implementation:
- Outer pill: `rgba(0,0,0,0.9)` background
- Active side (Original nettside): `bg #ffffff / color #1e1e1e`
- Inactive side link: `color: rgba(255,255,255,0.85)`, hover to full white `#ffffff`
- Hover is text-color-only (no background tint on hover)
- `color` and `transition` MUST be in the `<style>` CSS block (`.npls-link { color: ...; transition: color 0.15s; }`),
  NOT in inline `style` attribute (inline style has higher CSS specificity than `:hover`)
- Vertical padding: 32px top/bottom
- Version-switcher pill inner padding: `8px 18px`

## Sponsor URL status (last verified 2026-06-20)

These are the root/canonical sponsor URLs as they appeared on the original site.
Links on index.html, reisebrev.html, reiserute.html, and reisebrev1-6 sidebar
point to root domains. Links on sponsorer.html point to root domains.
Links on utstyr.html include product-specific subpaths (all treated as dead in audit).

| Sponsor          | Original URL                             | Status (2026-06-20)                                  |
|------------------|------------------------------------------|------------------------------------------------------|
| XXL              | http://www.xxl.no/                       | Live ✓                                               |
| Janus            | http://www.janus.no/                     | Live ✓                                               |
| Sportsbua        | http://www.sportsbua.no/                 | Dead — connection refused                            |
| Helsport         | http://www.helsport.no/                  | Dead — 404                                           |
| Cappelen Damm    | http://www.cappelendamm.no/              | Live ✓                                               |
| Alfasko          | http://www.alfasko.no/                   | Dead — rebranded, domain gone                        |
| Åsnes            | http://www.asnes.com/                    | Live ✓                                               |
| Fjellpulken      | http://www.fjellpulken.no/               | Live (redirects to fjellpulken.com) ✓                |
| Rottefella       | http://www.rottefella.no/                | Live (redirects to rottefella.com) ✓                 |
| Amfibi           | http://www.amfibi.no/                    | Live ✓                                               |
| Adidas Eyewear   | http://www.adidas.com/…Eyewear           | Live (403 = bot-detection) ✓                         |
| MX Sport         | http://www.mx-sport.no/                  | Root: redirects to fjellandsport.no (different company); original subpath /medlemmer/telemark/ → 404 on fjellandsport.no. Treated as redirect-to-unrelated-domain → dead |
| Skaidi Hotel     | http://www.skaidihotel.no/               | Live ✓                                               |
| Breidablikk      | http://www.breidablikk.no/               | Live ✓                                               |
| Lundhøgda        | http://www.lundhogdacamping.no/          | Live ✓                                               |
| Femund Fjellstue | http://www.femundfjellstue.no/           | Dead — suspended account (curl: /cgi-sys/suspendedpage.cgi) |
| Umbukta Fjellstue| http://www.umbuktafjellstue.no/          | Live ✓                                               |
| Jule Ferie       | (no URL on original site)                | N/A                                                  |
| Dokka Camping    | http://www.dokkacamping.no/              | Live ✓                                               |
| Gudbrandsdal     | http://www.sgh.no/                       | Live ✓                                               |
| Repstad.net      | http://www.repstad.net/                  | Live ✓ (sidebar link, not a sponsor)                 |
| frederikpaatur   | http://frederikpaatur.blogspot.com/      | Live ✓ (sidebar link)                                |

## Decision changelog

- 2026-06-20: Footer credit — removed hyperlink from Arne's WEBMASTER entry
  (`folk.ntnu.no/arnesigm` is outdated and no longer linked). "WEBMASTER: ARNE S. SKEIE"
  is now plain text. Marius's omoss.html link unaffected. Applied across all 16 HTML pages.
- 2026-06-20: Version-switcher added to all 16 pages. Outer dark pill floats on page bg.
  Inner white pill on active side. Inactive side is a link. Labels: "Original nettside"
  (left, active) / "Oppdatert nettside" (right, links to modernized site).
  Font 14px. Vertical padding 20px (later raised to 32px).
- 2026-06-20: Version-switcher pill inner padding set to 7px 18px → 8px 18px (on 4/8pt grid).
  Applied simultaneously to all 16 HTML pages and SiteFooter.jsx (03-modernized).
- 2026-06-20: Version-switcher hover regression fixed on all 16 pages. Root cause: CSS
  specificity — inline `style` attributes override `:hover` pseudo-class selectors.
  Moved `color` and `transition` from inline `style` into the `<style>` CSS block.
- 2026-06-20: Dead external link audit — entire site (16 pages).
  Scope: all external links (not relative internal navigation). Verified via HTTP.
  Method: strip `<a href>` wrapper, keep inner content exactly (text or image); no visible
  change to the page — only the clickability is removed.

  **Links unlinked (reason):**

  *index.html (14 links unlinked):*
  - Lenker sidebar: norgepaakryssogtvers.net (404/gone), halddetoppen.no (404/gone),
    friluftsliv.no/ekspedisjoner (dead subpath)
  - Ekspedisjoner sidebar: keeperifokus.no (404/gone), tureroveralt.no (404/gone)
  - Presse sidebar: arcticfemme.com (flagged unsafe — see 2b below),
    saltenposten.no article (dead URL), eventyrblogg.com (404/gone)
  - Sponsor sidebar (6): sportsbua.no (dead), helsport.no (404), alfasko.no (dead/rebranded),
    mx-sport.no/members/telemark/ (404 + redirect-to-unrelated-domain),
    femundfjellstue.no (suspended account), rlb.no/seng/info/2924 (dead subpath)

  *sponsorer.html (6 links unlinked):*
  - sportsbua.no, helsport.no, femundfjellstue.no, alfasko.no,
    rlb.no/seng/info/2924, mx-sport.no/members/telemark/ (same reasons as above)

  *utstyr.html (31 links; href="#" not removed — see regression fix below):*
  - Sponsor sidebar (6): same 6 as index.html
  - Product links (25): quechua.com, lowealpine.com, helsport.no product pages (4×),
    norrona.com, janus.no product pages (6×), sasta.fi, sportsdeal.no (2×),
    alfasko.no product page, asnes.com/ProductDetails (2×), crispi.no,
    rottefella.no product, swix.no, komplett.no (2×), sikkerhetsbutikken.net

  *reisebrev.html (6 sponsor sidebar links unlinked):*
  - Same 6 dead sponsors as index.html sidebar

  *reiserute.html (6 sponsor sidebar links unlinked):*
  - Same 6 dead sponsors as index.html sidebar
  - Google Maps embed link kept (live)

  **Links kept live (representative sample):**
  - Sidebar: repstad.net ✓, frederikpaatur.blogspot.com ✓, nordlys.no article ✓
  - Sponsors (sidebar + sponsorer.html): xxl.no, janus.no, cappelendamm.no, asnes.com,
    fjellpulken.no, rottefella.no, amfibi.no, adidas.com/eyewear, skaidihotel.no,
    breidablikk.no, lundhogdacamping.no, umbuktafjellstue.no, dokkacamping.no, sgh.no

  **Pages with no external links (not audited beyond version switcher):**
  reisebrev1–6.html (individual post pages), galleri.html, turlogg.html, omoss.html,
  gjestebok.html, videogalleri.html, vid1–6.html — all confirmed clean of external links
  other than the version-switcher (github.io, not audited as content).

- 2026-06-20: Arctic Femme link removal (Part 2b). The arcticfemme.com link under
  "Presse" on index.html was removed regardless of HTTP status — flagged as potentially
  unsafe. The press image (arcticfemme.jpg) remains in place at the same position; it is
  no longer clickable. This is the same treatment as the Arne S. Skeie webmaster link
  removal: keep the visible element, strip only the anchor.
- 2026-06-20: Utstyr hover-reveal regression fix. The dead-link audit initially removed
  `<a href>` wrappers entirely from dead product links on utstyr.html. This broke the
  hover-triggered image reveal: the CSS rule `#utstyrbolk a.utstyr:hover span { display: block }`
  (and `#utstyrbolk a.utstyr span { display: none }`) is keyed to the `<a class="utstyr">`
  element being present in the DOM. With the anchor removed, the `<span><img/>` elements
  became permanently visible instead of hover-only.
  Fix: restored utstyr.html to its pre-audit DOM structure (full `<a class="utstyr">`
  wrappers intact) then changed dead URLs to `href="#"` instead of removing the anchor.
  The `<a>` element, its `class="utstyr"`, and `target="_blank"` are all preserved exactly.
  `target="_blank"` was subsequently removed from all 31 dead links (keeping only
  `href="#"`), so clicking a dead link now does nothing at all — no new tab, no
  navigation, no scroll-to-top. Live links retain their original `target="_blank"`.
  31 links total: 6 dead sponsor sidebar + 25 dead product links.
  **Future link audit rule for this site:** Any page using CSS/JS hover behavior keyed
  to anchor presence (like `a.utstyr:hover`) must use `href="#"` for dead links rather
  than removing the `<a>` element. Only pages where no hover behavior depends on anchor
  presence (index.html, sponsorer.html, reisebrev.html, reiserute.html) may remove
  anchors outright.
