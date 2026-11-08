# Original application inventory — 8 November 2026

This audit preserves the original application's educational purpose: exploring uke's attack directions and possible follow-ups after an initial attack, rather than teaching detailed execution or replacing the maps with a generic technique encyclopedia.

**Scope:** read-only inventory of [lesthomassolutions/judo-gokyo-mind-maps](https://github.com/lesthomassolutions/judo-gokyo-mind-maps) at commit [f57e44c45a753d0a7680c45021010e72425533a1](https://github.com/lesthomassolutions/judo-gokyo-mind-maps/commit/f57e44c45a753d0a7680c45021010e72425533a1). Tracking and documentation only in this private V2 repository. No original files, branches, settings or website content were changed; no redesign implemented or deployed.

## Concrete baseline

| Item | Verified result |
|---|---|
| Repository | 273 files, 17 directory entries; 290 entries total |
| Pages | 56 HTML files: 40 techniques, 5 Gokyo groups, 7 classification/category pages, 1 overview, 1 Ne-waza page, 2 identical introduction entry files |
| Other source | 61 CSS, 54 JavaScript, 85 GIF, 13 PNG, 1 ICO, README, .gitattributes and .nojekyll |
| Gokyo coverage | All 40 present; each of five groups contains the correct eight distinct techniques against Kodokan's revised 1920 list |
| Technique-to-technique links | 1,211 anchor placements; 1,151 distinct directed page pairs, including one Tai-otoshi self-pair |
| Local content media | 40 direction diagrams + 40 technique illustrations + overview diagram + 2 help diagrams = 83 GIFs in Files/Image |
| Videos | 40 distinct YouTube IDs, one per technique; all 40 return HTTP 200 metadata with matching technique titles |
| Internal references | 2,364 distinct source/target pairs from HTML/CSS; all target files exist with exact case |
| External resources | Five of six credit/resource URLs return HTTP 200; openElement unresolved (TLS error plus independent fetch timeout) |
| Hosted introduction | HTTP 200; metadata/title matches the project |
| Verification | All 273 downloaded source files match the repository's Git blob SHA values |

These counts preserve repeated links and include hidden/modal content where present. Repeated links are not automatically duplicate defects: Okuri-ashi-harai and Yoko-gake occur on both sides of the overview. The 1,151 page pairs are **not 1,151 validated judo combinations**.

## Evidence and reusable inventory files

- [TECHNIQUES.md](TECHNIQUES.md): all 40 names/translations, source group/category memberships, diagram arrows/sectors, illustration/video paths, and every per-technique outgoing target in source order.
- [techniques.json](techniques.json): machine-readable per-technique inventory, including source classification versus Kodokan classification and review statuses.
- [relationships.csv](relationships.csv): every technique-to-technique anchor placement with source, target, label, generated element ID, CSS and content/footer coordinate context. Footer positions are relative to a different container; do not treat their top values as page coordinates.
- [organization.json](organization.json): exact group/category/overview link memberships and classification differences.
- [internal-references.csv](internal-references.csv): resolved local HTML/CSS dependency pairs, including page, image, script and stylesheet references.
- [repository-manifest.json](repository-manifest.json): complete original file/directory paths, sizes and Git blob identifiers.
- [external-checks.json](external-checks.json): dated external HTTP checks, YouTube metadata titles/uploaders and exact errors.
- [STANCE-REQUIREMENT.md](STANCE-REQUIREMENT.md): complete right/left requirement, also tracked in [#1](https://github.com/lesthomassolutions/judo-gokyo-mind-maps-v2/issues/1).

## Organization

The overview is [gokyo_no_waza.htm](https://github.com/lesthomassolutions/judo-gokyo-mind-maps/blob/f57e44c45a753d0a7680c45021010e72425533a1/gokyo_no_waza.htm). The introduction is available as both index.html and index.htm (identical source content). Group selection uses separate pages rather than a shared data-driven filter.

- Group 1 — [Dai_Ikkyo.htm](https://github.com/lesthomassolutions/judo-gokyo-mind-maps/blob/f57e44c45a753d0a7680c45021010e72425533a1/Dai_Ikkyo.htm): O Soto Gari; O Uchi Gari; Deashi Harai; Uki Goshi; Sasae Tsurikomi Ashi; Hiza Guruma; O Goshi; Seoi Nage.
- Group 2 — [Dai_Nikyo.htm](https://github.com/lesthomassolutions/judo-gokyo-mind-maps/blob/f57e44c45a753d0a7680c45021010e72425533a1/Dai_Nikyo.htm): Ko Uchi Gari; Ko Soto Gari; Okuriashi Harai; Harai Goshi; Tai Otoshi; Uchi Mata; Koshi Guruma; Tsurikomi Goshi.
- Group 3 — [Dai_Sankyo.htm](https://github.com/lesthomassolutions/judo-gokyo-mind-maps/blob/f57e44c45a753d0a7680c45021010e72425533a1/Dai_Sankyo.htm): Ko Soto Gake; Harai Tsurikomi Ashi; Yoko Otoshi; Ashi Guruma; Hane Goshi; Kata Guruma; Tomoe Nage; Tsuri Goshi.
- Group 4 — [Dai_Yonkyo.htm](https://github.com/lesthomassolutions/judo-gokyo-mind-maps/blob/f57e44c45a753d0a7680c45021010e72425533a1/Dai_Yonkyo.htm): Tani Otoshi; Sukui Nage; Hane Makikomi; Sumi Gaeshi; Soto Makikomi; O Guruma; Uki Otoshi; Utsuri Goshi.
- Group 5 — [Dai_Gokyo.htm](https://github.com/lesthomassolutions/judo-gokyo-mind-maps/blob/f57e44c45a753d0a7680c45021010e72425533a1/Dai_Gokyo.htm): Ushiro Goshi; Ura Nage; O Soto Guruma; Sumi Otoshi; Yoko Gake; Yoko Wakare; Uki Waza; Yoko Guruma.

| Classification page | Source distinct techniques | Expected within the 40 | Finding |
|---|---:|---:|---|
| Te-waza | 6 | 6 | Membership matches |
| Koshi-waza | 10 | 9 | Extra O-soto-guruma |
| Ashi-waza | 17 | 14 | Extra Sumi-otoshi, Yoko-otoshi, Soto-makikomi |
| Ma-sutemi-waza | 3 | 3 | Membership matches |
| Yoko-sutemi-waza | 7 | 8 | Missing Yoko-otoshi |
| Tachi-waza | 31 | 29 | Extra Yoko-otoshi, Soto-makikomi |
| Sutemi-waza | 10 | 11 | Missing Yoko-otoshi |

The expected memberships come from [Kodokan's names/classification and revised Gokyo list](https://kdkjudo.org/en/techniques/names-of-judo-techniques/). This comparison verifies membership, not the validity of every depicted transition.

## Prioritized findings

### P1 — Content classification discrepancies ([#2](https://github.com/lesthomassolutions/judo-gokyo-mind-maps-v2/issues/2))

The category filters disagree with Kodokan as shown above. Two additional errors are baked into illustration pixels:
- [o_soto_gari_i.gif](https://github.com/lesthomassolutions/judo-gokyo-mind-maps/blob/f57e44c45a753d0a7680c45021010e72425533a1/Files/Image/o_soto_gari_i.gif) labels O-soto-gari as Koshi-waza; Kodokan classifies it as Ashi-waza.
- [ushiro_goshi_i.gif](https://github.com/lesthomassolutions/judo-gokyo-mind-maps/blob/f57e44c45a753d0a7680c45021010e72425533a1/Files/Image/ushiro_goshi_i.gif) labels Ushiro-goshi as Ashi-waza; Kodokan classifies it as Koshi-waza.

All 40 illustration classification labels were visually inspected; these two differ from the checked classification. Preserve original evidence while preparing reviewed corrections for V2.

### P1 — Direction and relationship meaning require review ([#3](https://github.com/lesthomassolutions/judo-gokyo-mind-maps-v2/issues/3))

Arrows, highlighted sectors, technique names and some classification text are inside raster GIFs, while surrounding options are positioned HTML links. There is no explicit semantic relationship database.

The inventory transcribes screen coordinates (N=up, S=down, W=left, E=right); these must not be silently treated as anatomical kuzushi. Many images have one arrow, some show adjacent boundary arrows and a sector, and Harai-tsurikomi-ashi shows two sectors/four boundary arrows. Hiza-guruma highlights both lower sectors but only one downward black arrow. Retain these differences for content review.

For every source relationship, establish continuation/counter/navigation meaning, initiating side, uke stance/reaction, grips, footwork, applicable direction and evidence. Preserve the Tai-otoshi self-link pending review. A link resolving successfully does not validate its judo mechanics.

### P1 — User-selectable stance ([#1](https://github.com/lesthomassolutions/judo-gokyo-mind-maps-v2/issues/1))

Right-handed remains default. Left-handed must consistently adapt reviewed kuzushi/attack directions, diagrams, feet/stance indicators, labels and imagery; remember the user's selection across navigation/visits. Keep writing readable and technique identity/classification stable. Review each combination independently for each side; require explicit exceptions or unavailable/unreviewed states. No whole-page/image flip or universal combination mirroring assumption is acceptable. Full future acceptance criteria are in the tracked requirement.

### P1 — Media preservation and player validation ([#4](https://github.com/lesthomassolutions/judo-gokyo-mind-maps-v2/issues/4))

All 40 video IDs return metadata and technique-matching titles. Most are Mercuryu Judo; Tani-otoshi and Sumi-otoshi are Hispaconsulting, Seoi-nage is JUDO AND YOU, and Harai-tsurikomi-ashi is Dario Rodríguez Palomares. These are reference checks, not technical endorsement or playback testing.

Technique pages retain Flash/ActiveX code and 37 use HTTP youtube-nocookie movie URLs; Ashi-guruma, Deashi-harai and Yoko-wakare instead contain youtu.be URLs in Flash movie/embed markup. All also contain HTTPS iframe generation for non-Flash browsers. Video triggers are wired to existing modal/element IDs on all 40 pages.

The overview's instructions explicitly warn that audio may continue after closing a video modal. This is a source-documented issue, not newly reproduced behavior. Future browser testing must cover playback, embedding restrictions, close/Escape/navigation stopping audio, focus and fallback behavior.

Existing credits identify image sources as unknown and state noncommercial-use/attribution conditions. Preserve those notices, review provenance per asset, and do not infer permission merely from possession of a file. Case-sensitive special filenames are retained in the inventory.

### P2 — Incomplete content and navigation ([#5](https://github.com/lesthomassolutions/judo-gokyo-mind-maps-v2/issues/5))

Ne-waza exists and is explicitly under construction; its grappling technique lists are text without detail-page links. 38 technique pages link there (Uki-goshi and Sumi-gaeshi do not). This is incomplete coverage, not a missing-file error.

Ko-soto-gari's Start button returns to index.htm (Introduction), while the other 39 return to the overview. Both files exist. Yoko-gake and Yoko-otoshi share the source English label Side Drop; review translations/aliases while preserving Japanese identities.

### P2 — Responsive use, accessibility, printing and maintenance ([#5](https://github.com/lesthomassolutions/judo-gokyo-mind-maps-v2/issues/5))

All 56 HTML files lack a viewport declaration. Generated CSS uses a 900px body and absolute coordinates, including negative offsets and large artwork. This supports a responsive-layout concern, but actual mobile behavior has not been acceptance-tested.

38 technique pages lack document titles; Ashi-guruma and Deashi-harai are the exceptions. Content diagrams use empty alternative text. Video/Instructions anchors depend on generated modal event behavior. Keyboard, focus, dialog accessibility and meaningful alternative explanations need verification.

Print controls are present on all technique pages, using window.print(); no dedicated @media print rules were found. Preserve printing as a learning workflow.

The site is openElement 1.57.9 HTML/CSS/JavaScript with jQuery 1.10.2 and old IE/Flash compatibility code. No build configuration or automated test suite was found. WECounter/OEDB framework scripts contain optional references to absent PHP endpoints but are not loaded by the audited HTML; they are not active broken page dependencies. No confirmed exploitable vulnerability is asserted.

## Missing/broken references: exact conclusion and limits

- **Confirmed missing active local target files:** zero in the audited HTML/CSS and configured modal references. Exact-case checks passed.
- **Confirmed unavailable YouTube metadata references:** zero of 40 checked.
- **Unresolved external reference:** openElement; observed TLS/fetch failures do not establish permanent deletion.
- **Confirmed content gap:** Ne-waza under construction, with no linked grappling details.
- **Legacy invalid/obsolete media path:** Flash fallbacks above; modern iframe references are separately preserved.
- **Unperformed:** browser playback/embedding tests, rendered desktop/mobile/print/keyboard acceptance, and qualified validation of every judo transition. Root HTTP success and metadata success do not stand in for these checks.

## Method and previous assessment

Read the prior chat and the user's pasted initial assessment. Its educational framing, architecture concerns and preservation priorities were retained. The earlier approximate 290-entry count is now exact: 273 files plus 17 directory entries. Its sampled observations were expanded to all techniques and pages, with specific content discrepancies and reference results added.

Fetched the complete source tree/text through GitHub read APIs and downloaded a commit-pinned read-only snapshot for binary image inspection. Verified all 273 Git blob hashes. Extracted actual anchor instances (not duplicated onclick handlers), resolved HTML/CSS dependency paths with query strings removed and case preserved, checked configured modal IDs, visually inspected 40 direction diagrams and 40 illustration classification headers, checked six external resource links, hosted introduction and 40 YouTube oEmbed endpoints. A jQuery internal test string resembling src='/a' was excluded as a library probe, not treated as a deployed asset reference.

These documents are a migration baseline and prioritized backlog, not an implementation design or a completed acceptance test.
