name: Harvestr Weekly Summary
description: Summarises the last 7 days of activity in the team's Harvestr workspace — feedback received, items shipped, items in progress, and new discoveries added — broken down per component and in aggregate.

## What This Skill Produces

A structured summary covering:
- **Total feedback received** in the last 7 days (overall only)
- **Shipped items** — discoveries moved to "Shipped" state in the last 7 days (per component + total)
- **In-progress items** — discoveries currently in "In progress" state (per component + total)
- **New discoveries added** in the last 7 days (per component + total)

---

## Known Harvestr Structure

Component names and IDs are in `product-context/HARVESTR.md` (gitignored). Read that file to get the current list before making any calls.

---

## Step-by-Step Instructions

### Step 1 — Calculate the date window

Compute `week_ago` = today's date minus 7 days, formatted as ISO 8601 (e.g. `2026-04-28T00:00:00Z`). Use this in all date filters below.

### Step 2 — Fetch all data

Run everything in parallel where there are no dependencies.

---

#### 2A. Total feedback received (last 7 days)

- Tool: `list_harvestr_feedback`
- Parameters: `created_at.gte = week_ago`, `take = 50`, `source = "all"`
- **Paginate**: if `nextCursor` is present, keep fetching until exhausted.
- Count = total number of feedback items across all pages.

---

#### 2B. Shipped discoveries

Use `discoverystate_name = "Shipped"` as the state filter throughout. Do NOT use `discoverystate_ids` — use the name filter.

To find items that were **shipped in the last 7 days**, filter by `last_discoverystate_type_updated_at.gte = week_ago`. This captures when a discovery transitioned into the FINISHED state type.

**Overall (one call):**
- Tool: `list_harvestr_discoveries`
- Parameters: `discoverystate_name = "Shipped"`, `last_discoverystate_type_updated_at.gte = week_ago`, `take = 100`, `include = ["feedback_count"]`
- Paginate if `nextCursor` is present.

**Per component (4 calls in parallel):**
- Same parameters as above, but add `nested_parent_ids = [<component_id>]` for each component.

---

#### 2C. In-progress discoveries

Use `discoverystate_name = "In progress"` as the state filter. This reflects current state — no date filter needed.

**Overall (one call):**
- Tool: `list_harvestr_discoveries`
- Parameters: `discoverystate_name = "In progress"`, `take = 100`, `include = ["feedback_count"]`
- Paginate if `nextCursor` is present.

**Per component (4 calls in parallel):**
- Same parameters, add `nested_parent_ids = [<component_id>]` for each component.

---

#### 2D. New discoveries added (last 7 days)

**Overall (one call):**
- Tool: `list_harvestr_discoveries`
- Parameters: `created_at.gte = week_ago`, `take = 100`
- Paginate if `nextCursor` is present.

**Per component (4 calls in parallel):**
- Same parameters, add `nested_parent_ids = [<component_id>]` for each component.

---

### Step 3 — Identify unattached discoveries

For each category (Shipped, In progress, New), compare the overall list against the per-component lists. Any discovery that does not appear in any component's results is "unattached to a component".

---

### Step 4 — Format the output

Write a plain text summary. No commentary or analysis unless the user asks. Use the writing style from CLAUDE.md (precise, no flourishes, no em dashes).

```
## Harvestr Weekly Summary — [date range, e.g. 28 Apr – 5 May 2026]

### Overview
- Feedback received this week: [N]
- Shipped this week: [N] total ([N] Audio Intelligence / [N] InstantCreative / [N] DynamicCreative / [N] New product areas)
- Currently in progress: [N] total ([N] Audio Intelligence / [N] InstantCreative / [N] DynamicCreative / [N] New product areas)
- New discoveries added: [N] total ([N] Audio Intelligence / [N] InstantCreative / [N] DynamicCreative / [N] New product areas)

---

### Shipped this week ([N] total)

**Audio Intelligence ([N])**
- [Discovery title] — [N] feedback items
- ...

**InstantCreative ([N])**
- ...

**DynamicCreative ([N])**
- ...

**New product areas ([N])**
- ...

**Unattached to a component ([N])**  ← omit this section if empty
- ...

---

### In progress ([N] total)

[Same structure as Shipped, including feedback count per item]

---

### New discoveries added this week ([N] total)

[Same structure, titles only — no feedback count needed]

---

### Feedback
Total feedback items received in the last 7 days: [N]
```

**Formatting rules:**
- Omit a component section entirely if it has 0 items for that category.
- Omit the "Unattached to a component" section if it is empty.
- In the Overview line, omit components with 0 from the per-component breakdown in parentheses.
