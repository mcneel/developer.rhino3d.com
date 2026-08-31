---
description: Review a developer.rhino3d.com doc page for structure, TOC, links, frontmatter and prose consistency, one finding at a time
---

# Review a doc page

Review the page at `$ARGUMENTS` for inconsistencies, contradictions and gaps. If no path is given, ask which page.

## Delivery protocol

This matters more than any individual check. A doc review is a conversation, not a report.

- **One finding per turn.** State what's wrong, the one-line fix, then stop and ask. Wait for the answer.
- **Never dump the full list.** A wall of findings is unreadable and unactionable.
- **Batch only decision-free work.** Typos, punctuation and spelling can go in one approved pass. Anything needing a judgement call is its own turn.
- **Order by impact:** rendering breakage, then factual and link errors, then contradictions, then gaps, then terminology, then typos.
- **Re-read the file before each finding.** The author edits between turns, so line numbers drift and items fix themselves. Verify by content (`grep`), not by remembered line number.
- **Their call, not yours.** If they say something is correct or out of scope, drop it and move on. Do not relitigate.
- **Ask about domain facts.** Much of what looks wrong is knowledge only the author has. Ask rather than assert.
- **Say when the list is done**, so they know the review has an end.

## Authority

`content/en/guides/general/developer-docs-style-guide/index.md` is the style authority for this site, and it can change. Exactly four rules in this file are restated from it. **The doc wins over this file.** Confirm the rules still say what is claimed here before reporting a finding that rests on one:

```bash
grep -n 'reserved for the title of the page only\|TOCs are only generated from\|numeric suffix\|Avoid writing the latest Rhino version' \
  content/en/guides/general/developer-docs-style-guide/index.md
```

Four hits expected. A missing hit means that rule moved or changed, so read the relevant section of the doc before relying on it. Cite the quoted phrase, never a line number, since line numbers drift with every edit to the style guide.

Everything else in this file is either **observed convention** (measured across sibling pages, no documented rule) or a **verified site fact** (checked against the live site). Those are labelled where it matters, so a reader can tell what is enforceable from what is merely typical.

## 1. Headings and the TOC

Print the tree first: `grep -n '^#' <file>`

- **H1 is the page title only**, supplied by frontmatter. A `# Heading` in the body breaks the style guide, which says H1 is *"reserved for the title of the page only"*. Bodies start at H2. *(style guide rule)*
- **The TOC is built from H2 and H3 only.** The style guide: *"TOCs are only generated from H2 and H3 headers"*, and H4 and smaller are ignored. So if a section's real content sits at H4, that section is invisible in the TOC while its siblings are listed. This is the most commonly missed defect. *(style guide rule)*
- **Wrapper sections are a trap.** A `## Changes` parent with version sections beneath pushes everything down a level and can empty the TOC. Promoting the children to H2 usually beats keeping the label. *(consequence of the rule above)*
- **Duplicate heading text gets positional anchors.** The style guide notes repeat headings get a *"numeric suffix"* (`-1`, `-2`), so inserting a section silently retargets deep links. Fine when the parent heading disambiguates in the TOC. Flag the anchor fragility once, then let it go. *(style guide rule)*
- Heading case should be consistent across the page. *(observed convention: Title Case, no documented rule)*

## 2. Section index pages

- `layout = "single"` means Hugo does **not** list child pages. Check for children with `ls -d */` and confirm something on the page links to each one, or they are unreachable.
- The convention for outbound links is a `## Related Topics` list at the end. See `content/en/guides/general/rhino-technology-overview/_index.md`.

## 3. Links

Verified facts about the help site:

- Form used across this repo: `https://docs.mcneel.com/rhino/<N>/help/en-us/index.htm#<path>#(null)` *(observed convention)*
- **`/en-us` is required.** Dropping it returns 403. *(verified site fact)*
- **`/rhino/latest/` does not exist** (403). *(verified site fact)*
- For a current-version link use the shortcode `{{< latest-rhino-version >}}`, backed by `latestRhinoVersion` in `config/_default/config.toml`. It works inside a URL. The style guide asks for this over a hardcoded number: *"Avoid writing the latest Rhino version in text"*. *(style guide rule)*
- Version-specific sections should link their own version; a general or overview section uses the shortcode. *(observed convention)*
- Command links are bolded and labelled with the real command name: `**[Name](url)** command`. *(observed convention)*

Check every URL resolves:

```bash
grep -oE 'https://[^)]+' <file> | sed 's/{{< latest-rhino-version >}}/8/' | while read u; do
  printf "%-70s " "$u"; curl -s -o /dev/null -w "%{http_code}\n" -L "${u%%#*}"
done
```

Fragments are not sent to the server, so 200 proves only that the page exists, not the anchor. **Read the target path and ask whether it matches the label.** A resolving link can still point at completely the wrong topic, which is the usual result of a copy-paste.

For internal links, a missing page returns 404, but an alias stub returns 200 with its `<title>` set to the redirect target. Check the title to tell a real page from a redirect:

```bash
curl -s -L <url> | grep -oiE '<title>[^<]*</title>'
```

## 4. Frontmatter

- `title`: survey siblings before judging, `grep -h '^title = ' */index.md */_index.md | sort`. No leading "The", no appended explainer after a dash or colon.
- `description`: one sentence, and it should still agree with the body's opening line.
- `aliases`: compare against sibling pages; an odd-one-out is usually a mistake.
- **Never edit translations.** `content/de`, `es`, `fr`, `it`, `cn`, `jp`, `kr`, `tw` are generated. Only `content/en` is hand-edited. If a finding spans languages, report it, do not fix it.

## 5. Prose consistency

**Measure before enforcing.** A spelling is only wrong on this site if the site disagrees with it:

```bash
cd content/en && grep -roE '\b(behaviour|behavior)\b' --include="*.md" . | sed -E 's#.*:##' | tr 'A-Z' 'a-z' | sort | uniq -c
```

- Repo genuinely split (behaviour 43, behavior 28)? Leave it alone.
- Page is the sole outlier (synchronise 2 repo-wide, both on this page, against synchronize 15)? Fix it.

Other passes:

- **Curly punctuation.** The repo prefers straight quotes, measured at roughly 387 files to 55, no documented rule. Find with `grep -nP '[^\x00-\x7F]'`. Fix with `perl -CSD -i -pe "s/\x{2019}/'/g"`. The `-CSD` matters; without it the pattern silently fails to match. *(observed convention)*
- **Bullet punctuation.** Each list internally consistent. Fragments take no full stop, complete sentences do. Watch for the single odd bullet in an otherwise consistent list, often left behind by an earlier edit.
- **Defined terms.** Consistent capitalization, and one canonical name per concept. Where synonyms are used interchangeably, ask which is canonical rather than picking for them, but do offer a recommendation with reasons (existing usage in the page, collisions with other terms on the page, searchability).
- **Acronyms** expanded at first use, not halfway down the page.
- **Jargon introduced only to say it is gone** still needs defining, or should be cut.
- No em dashes or en dashes. *(Callum's personal preference, not a site rule)*

## 6. Content

- **Contradictions** between a version-neutral overview and version-specific sections, and between two sections describing the same mechanism in different words.
- **Duplicated sentences or links** within a section, especially a repeated "X can be managed using the Y command" line.
- **Overclaiming intros**, for example "lists any and all changes" on a page that covers three versions in summary.
- **Version-history sections**: newest first, parallel subsection sets across versions, past tense for historical versions, and one tense within a section.
- **Gaps the page implies about itself**: a goal bullet with no mechanism described anywhere, a claim that something works "as version N did" while version N is undocumented, a subsection present for one version and absent for its siblings.
- **Unnamed or unlinked commands and dialogs** where sibling sections link theirs.

## Close

Re-run the link check and the hygiene greps. Then give a short summary of what changed, and separately list what the author declined, so those decisions are recorded rather than silently lost.
