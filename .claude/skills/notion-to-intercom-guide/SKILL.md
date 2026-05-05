name: Notion to Intercom Guide
description: |
  This skill takes a product one pager from a ProductHQ item in Notion and creates a user-facing Intercom Help Center article for the new feature. It reads the internal one pager, transforms it into clear, customer-friendly language, and publishes it (or saves it as a draft) in Intercom.

> Before starting, read `product-context/COMPANY.md` for internal Notion URLs (ProductHQ, Product Status database).

## Overview

Given either a Notion URL for a ProductHQ item or a feature name to search for, this skill will:

1. Find and read the One Pager from the item's Documentation database in Notion
2. Transform the internal product content into a customer-facing user guide
3. Authenticate with Intercom (if not already authenticated)
4. Create a Help Center article in Intercom

---

## Step 1 — Find the ProductHQ item

If the user has provided a Notion URL, fetch it directly. If they have provided a feature name, search Notion for it:

- Search query: `[feature name] One Pager`
- ProductHQ URL: see `product-context/COMPANY.md`
- Product Status database URL: see `product-context/COMPANY.md`

Fetch the ProductHQ item page. Note its properties (Name, Product Area, Team, Quarter, Launch Status) for context.

---

## Step 2 — Find and fetch the One Pager

Inside each ProductHQ item page there is an inline **Documentation** database. Its URL is listed in the page content as:

```
<database url="..." inline="true" data-source-url="collection://...">Documentation</database>
```

Fetch that database URL, then search within it for a page whose title contains "One Pager". Fetch that One Pager page to read its full content.

The One Pager typically contains:
- **Problem We Are Solving** — the internal framing of what pain point is addressed
- **Evidence** — signals and data that justified building this
- **Key User Stories** — what the user can now do
- **How Will We Measure Success** — internal success metrics
- **Out of Scope** — what is explicitly excluded from this release
- **Technical Specification** — internal implementation details
- **Launch Timeline** — milestones and dates

---

## Step 3 — Write the Intercom user guide

Transform the One Pager into a customer-facing Help Center article. Follow these guidelines:

### Tone and voice
- Write in clear, simple English as if explaining to a non-technical customer
- Use second person ("you", "your") throughout
- Be direct and action-oriented — focus on what the user can do, not how it was built
- Avoid internal jargon, engineering terminology, and references to competitors
- Do not mention internal metrics, team ownership, or discovery/prioritisation rationale

### Article structure

**Title**: Use the feature name, phrased as a benefit or action (e.g. "Getting started with [Feature]" or "How to use [Feature]")

**Introduction** (1–2 sentences): What is this feature and what does it help the user achieve?

**What's new / What changed** (if applicable): If this is a change to existing behaviour, briefly explain what has changed and why it's better for the user.

**How it works**: A short explanation of the feature mechanism in plain language.

**How to use it** (step-by-step if applicable):
- Number each step
- Use imperative verbs: "Click", "Select", "Enable", "Open"
- Include specific UI element names where known from the One Pager or design assets
- Keep each step to one action

**Tips and best practices** (optional): Derive these from the Key User Stories and any nuances noted in the One Pager (e.g. known limitations, recommended use cases).

**Known limitations** (optional): Surface anything from "Out of Scope" that is genuinely relevant to the user experience. Frame it as "currently" rather than "won't do". Only include items that a user might hit and wonder about — don't include internal engineering deferrals.

**What to do if something goes wrong** (optional): Include only if the One Pager mentions known edge cases or workarounds that affect users.

Do **not** include:
- Internal milestone dates or team names
- Evidence/signals used to justify the feature
- Success metrics or OKRs
- Anything from Technical Specification that isn't user-visible
- Open questions or unresolved decisions

---

## Step 4 — Get the Intercom API token

Ask the user for their Intercom API token. They can find it at: **Intercom Settings → Developers → Access Token** (or via an OAuth app token). Do not proceed without it.

---

## Step 5 — Create the Intercom article via REST API

Use the Intercom REST API directly via `curl`. Do **not** use the `mcp__claude_ai_Intercom__authenticate` MCP tools — these do not expose article creation endpoints.

### 5a — Get the author ID

First, fetch the current user to get their Intercom `id` (needed as `author_id` when creating an article):

```bash
curl -s https://api.intercom.io/me \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Accept: application/json"
```

Note the `id` field from the response.

### 5b — Build the article body as HTML

Convert the article written in Step 3 to clean HTML:
- Use `<h2>` for section headings
- Use `<p>` for paragraphs
- Use `<ol>` / `<li>` for numbered steps
- Use `<ul>` / `<li>` for bullet lists
- Use `<strong>` for bold emphasis

### 5c — Create the article

```bash
curl -s -X POST https://api.intercom.io/articles \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "title": "<article title>",
    "body": "<html body>",
    "author_id": <author_id>,
    "state": "draft"
  }'
```

- Set `state` to `"draft"` unless the user explicitly asks to publish immediately.
- If the user specifies a Help Center collection, include `"parent_id": <collection_id>` and `"parent_type": "collection"` in the request body.

The response will include an `id`, `content_id`, and `workspace_id`. Construct the Intercom admin link using `content_id` (not `id`):  
`https://app.intercom.com/a/apps/<workspace_id>/knowledge-hub/all-content?activeContentId=<content_id>&activeContentType=article&editorMode=view&native_content=true`  
and share it with the user so they can review and publish.

---

## Notes

- If the One Pager is marked as a template (i.e. it contains placeholder text like `[e.g. ...]` or `[User]`) rather than real content, stop and let the user know the One Pager has not yet been filled in.
- If there are multiple One Pagers inside the Documentation database, ask the user which one to use.
- If the user wants to update an existing Intercom article rather than create a new one, ask for the article URL and update it instead.
