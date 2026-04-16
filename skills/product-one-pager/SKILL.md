Product One-Pager Skill
You are helping a product manager or designer create a structured product one-pager in Notion. The one-pager follows a specific template and is grounded in real evidence drawn from connected tools — not made up.
Step 1: Clarify the topic
If the user hasn't already specified the feature or problem area, ask them:

What feature/problem area is this one-pager about?
Is there a specific angle or framing they want to lead with?
Is there a Notion parent page or section it should live under?

Keep this brief — one or two questions max. If the user has already given you a clear topic, skip ahead to research.
Step 2: Research in parallel
Search all available data sources simultaneously. Don't wait for one to finish before starting the next. Be thorough — surface anything that could inform the one-pager sections.
Notion
Use notion-search to find:

Existing product specs, PRDs, or briefs related to the topic
Research notes or discovery docs
Meeting notes or decision logs
Customer feedback summaries

Search with several different queries — the topic name, related feature names, synonyms. Fetch the most relevant pages in full using notion-fetch.
Figma
Use search_design_system or use_figma to find:

Design files or prototypes related to the topic
Past research artefacts (journey maps, wireframes, usability study outputs)
Any screens or flows relevant to the problem area

Note file names and URLs for any Figma assets found — these will go in the "Illustrative Design Assets" section.
Slack
Use slack_search_public_and_private (or slack_search_public if the former is unavailable) to find:

Discussions about the feature or problem area
Fathom call summaries or meeting notes mentioning the topic (search "fathom [topic]" or "call notes [topic]")
Customer quotes or pain points surfaced in team channels
Any previous decisions or debates about this area

Intercom
Use search_conversations to find customer conversations related to the topic. Look for:

Common complaints or requests related to the feature area
Language customers use to describe the problem
Frequency signals (how often this comes up)

Use search_articles to see if support docs exist, which can reveal scope boundaries.
PostHog (if connected)
If you have PostHog access, search for usage data or feature flag information related to the topic. If PostHog is not connected, note this gap — the user may want to add usage data manually.
Step 3: Synthesise your findings
Before writing, mentally organise what you found:

What is the core problem? What evidence supports it?
Who is affected and how do they describe it?
What has already been tried or considered?
What designs or research already exist?
What metrics could measure success?

Be honest about gaps — if evidence is thin, say so in the doc rather than padding it out.
Step 4: Write the one-pager
Now create the Notion page using notion-create-pages. The page title should be descriptive (e.g. "One-Pager: [Feature/Problem Name]").
Use this exact section structure, populated with your research findings:

Problem we are solving and why
A concise statement of the problem and its business/user importance. Why now? What's the cost of not solving it? Inline-link any Notion docs, Slack threads, or strategy pages that informed this framing (e.g. as noted in [Product Strategy 2025](notion-url)).
Evidence
Bullet points of concrete evidence, every item linked to its source:

Customer quotes from Intercom or Slack — include the actual quote in quotation marks, the customer name or channel, and a hyperlink to the Slack message or Intercom conversation (e.g. "The waveform is missing" — [#ux-feedback, Apr 2025](slack-link))
Quantitative signals (usage data, support ticket volume, NPS feedback) — link to the PostHog dashboard, Notion report, or data source
Research findings from Notion — link directly to the source page (e.g. Key finding from [Audio Player Technical Spike](notion-url))
Fathom call notes or meeting recordings — link to the Fathom summary or Notion meeting note

Every evidence bullet must have a link. If you cannot find a URL for something, note it as "⚠️ source not linkable" so the user knows to verify it manually. If evidence is thin overall, explicitly flag this so the user knows what to fill in.
Key User Stories
Format as: "As a [user type], I want to [do something] so that [outcome]."
Ground these in what you found — don't invent user stories that have no basis in the research. Aim for 3–5 stories covering the main use cases.
How will we measure success?
Specific, measurable outcomes:

What metric moves and by how much?
What user behaviour change indicates success?
What is the target timeline to see results?

If PostHog data was available, reference relevant metrics. If not, suggest what to measure.
Out of Scope
Be explicit about what this does NOT cover. Pull from:

Boundaries implied by the user stories
Scope decisions found in Notion docs
Related but separate problems surfaced in research

Illustrative Design Assets
List any Figma files found during research with their URLs. Format as:

File name — brief description of what it shows

If no relevant Figma files were found, note: "No existing design assets found — new designs needed."
Technical Specification
High-level technical notes from anything found in Notion or Slack. Link every item to its source:

Known technical constraints or dependencies — link to the Notion ADR, spike doc, or engineering spec (e.g. per [Bulk Download ADR](notion-url))
API or data model implications — link to relevant Notion technical docs
Engineering discussion threads — link directly to the Slack thread (e.g. [Discussion on backend vs frontend zipping](slack-link), Feb 2026)

If nothing was found, leave a placeholder: "To be completed with engineering input."
Proposed Launch timeline and distribution
Based on anything found about project status or roadmap in Notion/Slack:

Suggested phases (discovery → design → build → launch)
Distribution strategy (who gets it first — beta users, all users, specific segments?)
Known dependencies or blockers

If no timeline information was found, provide a sensible template the user can fill in.

Step 5: Report back
After creating the Notion page, share:

A link to the newly created page
A brief summary of the key sources you drew from
An honest note about any sections that need human input (thin evidence, missing PostHog data, no technical spec yet, etc.)

Don't over-explain. The user can see the doc — point them to it and flag what needs their attention.
Important principles
Ground everything in evidence. Don't invent problems or evidence. If a section is thin, leave a clear placeholder rather than fabricating plausible-sounding content.
Use the customer's language. When quoting customers from Intercom or Slack, use their actual words — this is more compelling than paraphrased summaries.
Be honest about gaps. A one-pager with honest gaps is more useful than a padded one that looks complete but isn't. Flag where the user needs to contribute.
Link every reference. This is non-negotiable. Every claim, quote, finding, and design asset must be hyperlinked back to its source — Notion page, Slack message, Figma file, or Intercom conversation. A reader should be able to click any reference and land on the original. If a source has no linkable URL, mark it ⚠️ source not linkable rather than leaving it bare. The one-pager is an entry point into deeper research, not a dead end — links are what make it useful rather than just another doc.