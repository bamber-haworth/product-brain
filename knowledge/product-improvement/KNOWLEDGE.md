# Knowledge — Product Improvement Methodology

A structured approach for identifying and prioritising product improvements. General pattern, applicable regardless of product or company.

---

## The Five-Step Product Improvement Sequence

### Step 1: Define the product precisely

Before diagnosing problems, establish a shared, explicit definition of what the product is and who it serves. Use the positioning statement template:

> "For [target customer] who [statement of need or opportunity], the [product name] is a [product category] that [statement of key benefit]. Unlike [competitor], our product [statement of primary differentiation]."

This forces four things to be explicit: who the customer is, what problem exists, what category the product belongs to, and what differentiates it from alternatives. Vague positioning produces vague improvement directions.

If the team cannot agree on the positioning statement, that disagreement is the first problem to solve. Improvement work without a settled "for whom and why" tends to drift toward whatever is loudest, not what matters most.

### Step 2: Segment users by behaviour, not by demographics

Segment users by how they actually use the product, derived from analytics. Behavioural segments reveal meaningfully different needs; demographic segments usually do not.

Sources for behavioural segmentation:
- Usage frequency (daily vs. weekly vs. churned)
- Feature adoption patterns (which capabilities they use, in what sequence)
- Workflow type (e.g., users who complete the full workflow vs. users who stop partway through)
- Output type or goal (e.g., what they are trying to produce)

Demographic segmentation (company size, role title, industry) can be layered on top but should not be the primary organising principle. Two users with identical job titles can have entirely different usage patterns and therefore entirely different needs.

The goal is to identify two to four segments that have internally coherent behaviour and externally different needs. More than four typically means the segments are too granular to act on.

### Step 3: Journey map each segment

Build a user journey map for each behavioural segment identified in Step 2. Each segment may have a materially different journey — do not assume one map covers all users.

Populate the map from research (interviews, session recordings, support transcripts), not from internal assumptions. Map the current actual journey, not the intended one.

At minimum, capture for each stage:
- What the user is trying to do
- What they actually do (actions and workarounds)
- Their emotional state
- Pain points and blockers

Do not add opportunity statements yet — that comes in the next step.

### Step 4: Identify friction points and improvement vectors

From the journey maps, surface the highest-friction moments: stages where users struggle, stop, use workarounds, or show negative emotional signals.

Distinguish between:
- **Friction points:** Specific moments in the journey where the experience breaks down (e.g., "users cannot find X," "users misunderstand what Y means," "users must leave the product to do Z").
- **Improvement vectors:** The directions in which improvements should move (e.g., reduce steps in onboarding, make the output preview faster, surface relevant templates earlier).

Improvement vectors should be derived from clusters of friction points, not generated independently. A vector without supporting friction evidence is a solution in search of a problem.

Frame vectors as "How might we..." statements to keep them in problem space rather than jumping to specific solutions prematurely.

### Step 5: Prioritise using a framework

Apply a prioritisation framework to decide which improvement vectors to tackle first. The choice of framework depends on the product stage and available data:

**RICE (Reach, Impact, Confidence, Effort):** Useful when you have enough usage data to estimate reach and confidence. Prevents HiPPO-driven prioritisation.

**ICE (Impact, Confidence, Ease):** Lighter version of RICE; appropriate for early-stage or data-sparse contexts.

**Opportunity scoring (Ulwick/JTBD):** Score each opportunity by importance to the user minus current satisfaction. High importance + low satisfaction = the highest-priority opportunities. Requires interview or survey data.

**Value vs. effort matrix:** A 2x2 for quick visual triage. Useful for stakeholder alignment conversations, less rigorous for actual decision-making.

Whichever framework is used, the output should be a ranked list of improvement vectors with a stated rationale for the ranking, not just a score. Scores without rationale are difficult to challenge and difficult to revisit when assumptions change.

---

## Principles Underlying This Approach

- Start with positioning because improvement without a clear "for whom and why" produces local optimisations that do not move the right needle.
- Segment by behaviour because different usage patterns reflect different underlying needs; treating all users as one produces improvements that are mediocre for everyone.
- Journey map before generating solutions to stay in the opportunity space (Torres) and avoid solving the wrong problem precisely.
- Derive improvement vectors from friction evidence, not from team intuition or stakeholder requests.
- Prioritise explicitly with a framework to make trade-offs visible and contestable, not implicit and political.
