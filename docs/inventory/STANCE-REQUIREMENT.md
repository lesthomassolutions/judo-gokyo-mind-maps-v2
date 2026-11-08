# Right-handed / Left-handed stance requirement

Tracked as [issue #1](https://github.com/lesthomassolutions/judo-gokyo-mind-maps-v2/issues/1).

Planning requirement only; no redesign or implementation authorized. All development/tracking belongs in this private V2 repository. The original repository and hosted site remain read-only.

## Behavior and scope
- Provide an accessible, user-selectable **Right-handed / Left-handed stance perspective**. Right-handed remains the default and reproduces the original maps.
- Define the coordinate frame explicitly: uke versus tori, anatomical left/right versus screen left/right, stance/grips, attack direction versus kuzushi. The current GIFs encode arrows and sometimes sectors; a single direction enum would lose information.
- Mirror appropriate kuzushi/attack arrows, sectors, feet/stance indicators, placement of directional options, and directional descriptions consistently. A screen reflection exchanges E/W, NE/NW and SE/SW while keeping N/S, but is only a geometric operation until the judo interpretation is validated.
- Review every technique illustration and video for handedness. Use validated left-handed assets, or an explicitly labeled right-handed demonstration if no validated left-handed asset exists. Never flip an entire image containing text: technique names, classification, credits and other writing must stay readable and correct. Preserve correct names/classifications; update side-specific labels only where applicable.
- Persist the user's selected stance between navigation and visits (storage choice to be decided during design); handle unavailable storage gracefully; allow changing/resetting the choice. Selection must remain visible, including on printed maps.

## Combinations and content review
- Do **not** assume all 1,151 distinct directed page-link pairs are confirmed combinations, or that combinations/counters mirror identically.
- Review each transition in context: initiating technique/side, uke stance and reaction, grips, footwork, follow-up side, counter versus continuation, prerequisites and limitations.
- Track right/left validation independently, with source/reviewer evidence and explicit statuses (unreviewed, approved, modified, unsupported). Unverified left-handed transitions must be identified or withheld, never silently presented as validated.
- Preserve the current educational purpose: directional options after an attack; the maps alone do not teach the detailed execution of transitions.

## Acceptance criteria for future implementation
1. First visit defaults to right-handed; switching is keyboard/screen-reader accessible and updates the entire visible map consistently.
2. Validate all 40 techniques and all approved relationships in both modes, including multiple arrows/sectors, bilateral options and transitions that require exceptions.
3. Verify anatomical labels against a declared uke/tori frame; names/classification/credits remain readable; imagery and videos show the declared side or are clearly labeled otherwise.
4. Verify persistence after navigation, reload, browser restart, and changing the selection; exercise missing/corrupt/unavailable storage.
5. Verify left→right round trips restore the baseline exactly without duplicate/missing nodes, stale highlights or changed technique identity.
6. Verify mobile, desktop, print, keyboard and assistive-technology behavior in both modes. Record instructor/content review separately from software tests.

Dependencies: baseline inventory; taxonomy/image-label corrections; transition review and media provenance. No automatic mirroring of unreviewed technical relationships.
