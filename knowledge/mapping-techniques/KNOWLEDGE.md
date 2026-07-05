# Knowledge — Mapping Techniques

Confirmed facts and patterns about Wardley Mapping, User Story Mapping, and User Journey Mapping. No company- or product-identifying detail.

---

## Wardley Mapping

Created by Simon Wardwell. A strategic tool for visualizing the components of a value chain and their competitive maturity.

### Structure

Two axes:
- **Y-axis (visibility):** How visible a component is to the user. Infrastructure sits at the bottom; user-facing components at the top.
- **X-axis (evolution):** How mature or commoditized a component is. Moves left to right through four stages: Genesis (novel, uncertain) → Custom (bespoke builds) → Product (packaged solutions) → Commodity (utility, near-invisible).

Components are connected by dependency arrows (A depends on B depends on C).

### How to build one

1. Identify the user need at the top.
2. List every component required to meet that need, directly or indirectly.
3. Map dependencies between components.
4. Position each component on the evolution axis based on current maturity, not aspirational state.
5. Look for misalignments: custom-built commodities, undifferentiated bets, gaps in the chain.

### Strategic uses

- Make/buy/partner decisions: never custom-build a commodity.
- Anticipating competitor moves: components always evolve left to right over time. If a competitor is commoditizing something you custom-built, a response is required.
- Surfacing strategic bets: what is currently in genesis that you could own before it matures?
- Exposing organisational inertia: where is the team resisting evolution because of past investment?

### Common mistakes

- Treating the map as a fixed artifact rather than a thinking tool. The value is in the conversation it generates.
- Mapping aspirational positions instead of current reality.
- Conflating evolution stage with quality or importance.

### Relation to product discovery

Wardley mapping operates at the strategy layer, before Cagan's product discovery. It answers "what is worth building at all?" before you ask "how do we build it right?"

---

## User Story Mapping

Created by Jeff Patton. A delivery-planning tool that organises user stories into a structured map to maintain the whole-product view while planning releases.

### Structure

A two-dimensional grid:
- **Horizontal axis (backbone):** User activities, left to right in the order a user would perform them. These are high-level tasks, not features (e.g., "Search for a track," "Preview it," "Add to project").
- **Vertical axis (depth):** User tasks and stories beneath each activity, ranked by priority or value from top to bottom.

Release lines are drawn horizontally across the map, cutting it into slices. Each slice represents a coherent release that delivers end-to-end value, even if incomplete.

### How to build one

1. Identify the user and the goal they are trying to achieve.
2. Walk through the activity flow from their perspective. Write each activity on a card.
3. For each activity, add the specific tasks and stories below it.
4. Prioritise vertically within each column.
5. Draw release slices horizontally to define what goes into each version.

### Why it matters

- Prevents the "flat backlog" problem, where individual stories lose their connection to the user journey.
- Forces teams to think in releases that deliver coherent experiences rather than isolated features.
- Makes scope decisions explicit: what is the minimum set of stories across all activities that creates a viable experience?

### Common mistakes

- Mapping features instead of activities. If the backbone reads like a feature list, the user perspective has been lost.
- Starting with delivery rather than user activities; this inverts the purpose.

### Relation to product discovery

Story mapping connects to Torres's opportunity space. Once an opportunity has been identified and solutions validated, story mapping is how you plan delivery without losing user context. It also reflects Cagan's principle that the product manager owns the "why" at the activity level, not just the story level.

---

## User Journey Mapping

A research synthesis and communication tool. Visualises the full experience a user has across all touchpoints with a product or service, from first awareness through ongoing use.

### Structure

A timeline of stages (columns), with rows for:
- **Actions:** What the user does at each stage.
- **Thoughts and questions:** What they are thinking or asking.
- **Emotions:** Their emotional state, often shown as a curve.
- **Touchpoints:** Where they interact with the product, team, or content.
- **Pain points:** What is frustrating or blocking them.
- **Opportunities:** Where the experience could be improved.

### How to build one

1. Define the user (persona or segment) and scope (which part of the journey: onboarding only, full lifecycle, a specific workflow).
2. Populate stages from research, not assumption. Interview transcripts, session recordings, and support tickets are primary sources.
3. Fill in actions, thoughts, and emotions from evidence.
4. Identify the highest-friction moments (the biggest dips in the emotion curve).
5. Add opportunity statements, framed as "How might we..." questions rather than solutions.

### Why it matters

- Makes the emotional and experiential reality of the user visible to teams who never directly observe customers.
- Identifies moments of friction that quantitative data alone cannot surface.
- Creates a shared artifact for cross-functional alignment (sales, support, product, marketing all see their role in the same map).
- Useful for adoption analysis: where does the experience break down between acquisition and habit?

### Common mistakes

- Building it from internal assumptions without user research. An assumed journey map is a communication artifact at best and a misleading document at worst.
- Mapping the ideal journey rather than the actual one.
- Stopping at pain point identification without generating opportunity statements.

### Relation to product discovery

Journey mapping is a discovery artifact, consistent with Torres's continuous discovery. It directly addresses Cagan's usability risk: it surfaces where the product fails the user experientially, not just functionally. For adoption work, it maps to the activation funnel and time-to-value analysis.

---

## Comparison: When to Use Each

| Technique | Primary use | Time horizon | Lens |
|---|---|---|---|
| Wardley Map | Strategic positioning and make/buy decisions | 2-5 years | Market and competitive |
| Story Map | Release planning while preserving user context | Quarters and sprints | Delivery |
| Journey Map | Experience diagnosis and opportunity identification | Current state | Customer experience |

### Sequencing

Wardley mapping at the strategy layer informs what is worth building. Journey mapping at the discovery layer reveals where users struggle. Story mapping at the delivery layer plans how to solve it in coherent releases.
