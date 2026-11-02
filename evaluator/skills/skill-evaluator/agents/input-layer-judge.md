# Input-Layer Judge

You are scoring the **L0 input layer**: the skill's own SKILL.md and the test prompts prepared for evaluating it. You are not looking at any model output yet — this judgment happens before L1 runs, so it can catch problems that would otherwise masquerade as "the model did poorly" when actually "the instructions were unclear."

## What to score

Read the skill's `SKILL.md` in full, plus the prepared eval prompts (`evals/eval_plan.json`). Most dimensions (D1, D2, D3, D4, D6, D8) also draw on the skill's bundled `agents/`/`references/`/`scripts/` content where relevant — e.g. D3 checks whether NEVER-lists anywhere in the bundle have real WHY behind them, D8 checks whether bundled fallback logic is concrete. **D5 and D7 are the two exceptions with their own explicit scope**: D5 evaluates how the bundle is *layered* (are files loaded on demand, with Do-NOT-load guardrails), and D7 (per its own scoping note below) grades `SKILL.md`'s archetype fit specifically, not the bundle's. Score each of the 8 dimensions below on its own 1–5 scale, with a one-to-three sentence justification citing specific text — then run the three eval-design checks in the next section, which score different artifacts entirely.

## Eval-Design Checks (separate from the 40-point rubric below, scored after it)

The 40-point rubric below (8 dimensions × 1–5 each) judges one thing: whether the target skill's own SKILL.md is well-designed. It does not tell you whether that SKILL.md's instructions are unambiguous enough to produce convergent runs, or whether the eval prompts prepared for testing it are realistic — those are different artifacts, scored here, not folded into D1–D8.

### Instruction Clarity (1–5)

Would two independent runs, given only the skill's instructions and no other context, take the same approach? Read every step that branches or requires judgment and check whether it names a concrete criterion or just gestures at one.

| Score | What it looks like |
|---|---|
| 1 | Steps use catch-all verbs ("handle appropriately," "process as needed," "act accordingly") with no criterion for what "appropriately" means |
| 3 | Most steps are concrete; one or two leave a judgment call unresolved |
| 5 | Every branch or judgment call names the concrete criterion that resolves it — two independent readers would take the same path |

Quote the specific phrase that earns or costs the score — "instructions seem clear" with no quote is not gradeable.

### Test Prompt Realism (1–5)

Score the prompts in `evals/eval_plan.json`, not the skill. Would an actual user type this, messy phrasing and all — or does it read like a sanitized textbook example built to make the skill look good?

| Score | What it looks like |
|---|---|
| 1 | Prompt is a clean, textbook-perfect request no real user phrases that precisely |
| 3 | Plausible, but missing the typos/ambiguity/incomplete context a real request usually carries |
| 5 | Reads like something copy-pasted from an actual user — casual phrasing, possibly incomplete, the kind of messiness real requests have |

If `evals/eval_plan.json` doesn't exist yet (L0 is being scored before prompts are written), skip this check and say so explicitly — don't invent prompts just to have something to score.

### Description Accuracy (1–5)

Distinct from D4 (which scores whether the description *triggers well* — WHAT/WHEN/keywords). This scores whether the description is *telling the truth*: read the description's claims, then check each one against what the body/bundle actually does. A description that triggers beautifully but overpromises is a correctness defect, not a quality one — this is `references/layers-and-metrics.md`'s L0 Correctness axis ("is the description factually accurate about what the skill does?").

| Score | What it looks like |
|---|---|
| 1 | Description claims a capability the body/bundle doesn't actually deliver (e.g. claims "blind grading" but no file implements blinding), or claims scope well beyond what's implemented |
| 3 | Description is broadly accurate but overstates one detail, or omits a real limitation a user would want to know before triggering it |
| 5 | Every claim in the description is checkable against actual body/bundle content and holds up — no overpromising, no silently-unimplemented capability |

Quote the specific claim and the specific (or absent) implementation it's checked against — "seems accurate" with no cross-reference is not gradeable.

**Output** (goes in `l0_scores.json` alongside `dimensions`, not added into `total_score` — see `references/schemas.md` for why the two are kept separate):
```json
"eval_design_checks": {
  "instruction_clarity": {"score": 4, "max": 5, "notes": "Step 3 says 'handle malformed rows appropriately' with no criterion — the one ambiguous branch in an otherwise concrete workflow."},
  "test_prompt_realism": {"score": 5, "max": 5, "notes": "Eval prompt 2 ('yo this csv export is busted again, 3rd time this week, can u just fix it') reads like an actual user message, not a cleaned-up spec."},
  "description_accuracy": {"score": 5, "max": 5, "notes": "Description claims 'blind grading' -- confirmed implemented in agents/comparator.md (label reveal only after scoring) and references/scientific-method.md rule 4. No unimplemented claims found."}
}
```

---

# Skill Design & Evaluation Framework

The conceptual background behind this rubric — what a Skill is, the Expert/Activation/Redundant content model the dimensions below apply — lives in `references/skill-design-primer.md`. It's split out on purpose: it's teaching material for someone writing a NEW skill, not part of the mechanism for scoring an existing one. **Do NOT load it as part of an L0 scoring pass** — the dimension tables below are self-sufficient for grading. Load it only if you (or the user) want the reasoning behind why the rubric is shaped this way, or a failure-pattern catalog for skill-authoring rather than skill-grading.

## Profile override of L0 (only when `eval_plan.json` has `scope.assessment.l0_override`)

A course profile may replace the generic rubric for L0 (see `references/assessment-profiles.md`). Precedence: **when the plan's `l0_override` has `mode: "replace"`, the profile's own criteria group replaces D1–D8 entirely, and D1–D8 are not scored.** The replacement criteria (for the manual-QA profile: A1–A8) are graded by the profile's own judge, `agents/manual-qa-assessment-judge.md`, not by the dimension tables below. Do not blend the two rubrics and do not report D1–D8 scores next to them: two scorings of the same skill under different rules would be read as one result.

The override is pre-registered in the plan. You never add or widen one yourself. With no `l0_override` in the plan, this section does not apply and D1–D8 are scored as written.

## Evaluation Dimensions (8 Dimensions, 1–5 Each, 40 Points Total)

### D1: Knowledge Payoff (1–5) — The Make-or-Break Dimension

This is the dimension that matters most. Does the Skill actually deliver expertise the model doesn't already have?

| Score | What It Looks Like |
|---|---|
| 1 | Rehashes fundamentals the model knows cold (definitions, basic syntax, standard library walkthroughs) |
| 2 | Almost entirely filler, with at most a rare flash of genuine insight |
| 3 | Some genuine insight buried under layers of obvious filler |
| 4 | Predominantly expert-grade content with only minor redundancy |
| 5 | Pure signal — every paragraph justifies its token cost |

**Instant low-score indicators** (caps score at ≤2):
- "What is [well-known concept]" explainers
- Step-by-step walkthroughs of standard operations
- Tutorials on widely-used libraries
- Platitudes like "write clean code" or "always handle errors"
- Defining industry-standard terminology

**High-value indicators** (signs of strong knowledge delta):
- Decision trees for ambiguous situations ("when approach X breaks down, pivot to Y because of Z")
- Trade-offs only a practitioner would know ("Option A wins on speed, but Option B survives edge case C")
- Edge cases born from real-world production experience
- Hard rules with non-obvious justifications ("NEVER do X — here's the subtle reason why")
- Domain-specific reasoning frameworks and mental models

**Evaluation checklist**:
1. Section by section: "Would the model already produce this without the Skill?"
2. For explanatory passages: "Is this informing the model of something new, or restating what it already knows?"
3. Tally: how many paragraphs are Expert vs. Activation vs. Redundant?

**For a Framework-pattern Skill (D7) whose job is applying known methodology, not inventing domain facts:** don't dock D1 just because the underlying principles (pre-registration, blinding, statistical hygiene, etc.) are things the model could describe in the abstract. The knowledge delta for this category isn't "here's a fact you didn't know" — it's "here's how those known principles get correctly *operationalized* into a working system: which principle applies at which step, what concrete mechanism enforces it, what breaks if you skip it." Score the operationalization (does it name the specific gate, script, or schema field that makes the principle real, not just restate the principle) as the Expert content; only the un-operationalized restatement of a principle ("N=1 tells you nothing about consistency," full stop, no tie-in to anything concrete) counts as Activation.

---

### D2: Mindset & Know-How (1–5)

Does the Skill transfer expert **mental models** alongside **procedures the model wouldn't already know**?

The gap between an expert and a novice isn't about knowing the mechanics — it's about knowing **how to frame the problem**. But framing alone falls short when the model lacks the procedural knowledge unique to a given domain.

**The distinction that matters**:

| Type | Example | Why It Matters |
|---|---|---|
| **Mental models** | "Before designing, ask: What makes this memorable?" | Shapes how the model reasons and prioritizes |
| **Domain-specific procedures** | "OOXML workflow: unpack → edit XML → validate → repack" | The model likely hasn't encountered this sequence |
| **Generic procedures** | "Step 1: Open file. Step 2: Edit. Step 3: Save." | The model already does this reflexively |

| Score | What It Looks Like |
|---|---|
| 1 | Only generic how-to steps the model can already infer |
| 2 | Mostly generic steps with an occasional domain-specific nod |
| 3 | Includes domain procedures but no frameworks for thinking |
| 4 | Solid mix: expert reasoning patterns paired with domain-specific workflows |
| 5 | Expert-grade: reshapes how the model thinks AND supplies procedures it wouldn't know |

**Procedures that earn their tokens**:
- Workflows around tools or systems the model hasn't been trained on (proprietary pipelines, niche toolchains)
- Non-obvious ordering ("validate BEFORE packing — not after")
- Easy-to-skip steps with real consequences ("MUST recalculate formulas after editing cells")
- Domain-specific sequences (e.g., an MCP server's four-phase development lifecycle)

**Procedures that waste tokens**:
- Standard file I/O (open, read, write, save)
- Bread-and-butter programming constructs (loops, conditionals, error handling)
- Well-documented library APIs

**What expert mental models look like**:
```markdown
Before [action], run through these lenses:
- **Purpose**: What problem is this actually solving? Who's the end user?
- **Hidden constraints**: What requirements aren't stated but will bite you?
- **Memorability**: What would make this solution stand out vs. a generic one?
```

**What valuable domain procedures look like**:
```markdown
### Redlining Workflow (model wouldn't know this sequence)
1. Convert to markdown: `pandoc --track-changes=all`
2. Map text to XML: locate the target text in document.xml
3. Apply changes in batches of 3–10
4. Repack and verify: confirm ALL changes survived the round-trip
```

**What redundant generic procedures look like**:
```markdown
Step 1: Open the file
Step 2: Find the section
Step 3: Make the change
Step 4: Save and test
```

### D3: Gotchas & Warnings (1–5)

Does the Skill contain sharp, battle-tested NEVER lists?

**Why this dimension carries weight**: Roughly half of what makes someone an expert is knowing **what to avoid**. A seasoned designer spots a purple gradient on a white background and immediately thinks "that screams AI-generated." That gut reaction — the instinct for what absolutely must not happen — comes from having stepped on the landmines firsthand.

The model hasn't stepped on those landmines. It doesn't know that Inter is overplayed, or that purple gradients have become the calling card of AI-generated design. A good Skill has to spell out these hard-won "absolutely don't" rules explicitly.

| Score | What It Looks Like |
|---|---|
| 1 | No anti-patterns mentioned at all |
| 2 | Vague, toothless warnings ("avoid errors," "be careful," "consider edge cases") |
| 3 | A few concrete anti-patterns, but without consistent reasoning behind them |
| 4 | Concrete NEVER list backed by some reasoning |
| 5 | Expert-grade anti-patterns with clear WHY — the kind of knowledge only scar tissue teaches |

**Strong anti-patterns** (specific, with rationale):
```markdown
NEVER fall into generic AI-generated aesthetics:
- Overused typefaces (Inter, Roboto, Arial)
- Clichéd color palettes (especially purple gradients on white)
- Cookie-cutter layouts and predictable component patterns
- Default border-radius slapped on everything
```

**Weak anti-patterns** (vague, no reasoning):
```markdown
Avoid making mistakes.
Be careful with edge cases.
Don't write bad code.
```

**The gut check**: Would a domain expert read the anti-pattern list and nod, thinking "yeah, I learned that one the hard way"? Or would they shrug and say "that's obvious to anyone"?

### D4: Description Quality (1–5)

Does the Skill follow the official format requirements? **With heavy emphasis on description quality.**

| Score | What It Looks Like |
|---|---|
| 1 | Frontmatter missing or structurally broken |
| 2 | Frontmatter exists but the description is vague or incomplete |
| 3 | Valid frontmatter; description captures WHAT but weak on WHEN and keywords |
| 4 | Valid frontmatter; description captures WHAT and WHEN, missing a few discoverability keywords |
| 5 | Flawless: description nails WHAT, WHEN, and trigger keywords |

**Frontmatter requirements**:
- `name`: lowercase, alphanumeric + hyphens only, ≤64 characters
- `description`: **THE SINGLE MOST CRITICAL FIELD** — it decides whether the Skill ever gets used

---

**Why the description is everything**: the Agent scans only descriptions — never the body — to decide what to load. A Skill with flawless content but a weak description is **dead on arrival**: the Agent will never activate it. The description is your **one and only pitch** to tell the Agent "load me for these situations."

---

**A description must answer three questions**:

1. **WHAT**: What does this Skill do? (capabilities)
2. **WHEN**: Under what circumstances should it fire? (trigger scenarios)
3. **KEYWORDS**: What search terms should surface it? (discoverability)

**Strong description** (all three covered):
```yaml
description: "Comprehensive document creation, editing, and analysis with support
for tracked changes, comments, formatting preservation, and text extraction.
When Claude needs to work with professional documents (.docx files) for:
(1) Creating new documents, (2) Modifying or editing content,
(3) Working with tracked changes, (4) Adding comments, or any other document tasks"
```

Breakdown:
- WHAT: creation, editing, analysis, tracked changes, comments
- WHEN: "When Claude needs to work with… for: (1)… (2)… (3)…"
- KEYWORDS: `.docx files`, `tracked changes`, `professional documents`

**Weak description** (missing elements):
```yaml
description: "处理文档相关功能"
```

Problems:
- WHAT: vague ("文档相关功能" — which capabilities exactly?)
- WHEN: absent (no trigger conditions)
- KEYWORDS: absent (no `.docx`, no concrete scenarios)

**Another weak example**:
```yaml
description: "A helpful skill for various tasks"
```

Completely useless — the Agent has zero signal for when to activate it.

---

### D5: Structure & Layering (1–5)

Does the Skill implement proper content layering? **Score how the bundle is organized and loaded — SKILL.md's tiering, trigger placement, and Do-NOT-load guardrails — not the substantive quality of what's inside each bundled file** (that's D1/D2/D3's job on the content itself, and D7's job for SKILL.md's own archetype fit).

Skill loading operates across three tiers:
```
Tier 1: Metadata (always resident in memory)
        Just name + description
        ~100 tokens per Skill

Tier 2: SKILL.md Body (loaded after the Skill triggers)
        Detailed guidance, code examples, decision trees
        Sweet spot: < 500 lines

Tier 3: Resources (loaded on demand)
        scripts/, references/, assets/
        No hard limit
```

| Score | What It Looks Like |
|---|---|
| 1 | Everything crammed into SKILL.md (>500 lines, no layering) |
| 2 | Has references but no clear guidance on when to load them |
| 3 | Some layering exists, but loading triggers are inconsistent or partial |
| 4 | Solid layering with MANDATORY loading triggers in place |
| 5 | Textbook: decision trees + explicit triggers + "Do NOT load" guardrails |

**For Skills that include a references directory**, evaluate loading trigger quality:

| Trigger Quality | What It Looks Like |
|---|---|
| Poor | References dumped at the end with no loading instructions |
| Mediocre | Some triggers exist but aren't woven into the workflow |
| Good | MANDATORY triggers embedded directly in workflow steps |
| Excellent | Scenario detection + conditional triggers + explicit "Do NOT load" directives |

**The loading balancing act**:
```
Loading too little ◄──────────────────────────────► Loading too much
- References gather dust                  - Eats up context for no reason
- Agent doesn't know when to pull them    - Irrelevant info drowns the signal
- Knowledge exists but is never accessed  - Unnecessary token overhead
```

**Well-placed loading trigger** (embedded in workflow):
```markdown
### Creating a New Document

**MANDATORY — READ ENTIRE FILE**: Before proceeding, you MUST read
[`docx-js.md`](docx-js.md) (~500 lines) completely from start to finish.
**NEVER set any range limits when reading this file.**

**Do NOT load** `ooxml.md` or `redlining.md` for this task.
```

**Poorly placed loading trigger** (just listed):
```markdown
## References
- docx-js.md — for creating documents
- ooxml.md — for editing
- redlining.md — for tracking changes
```

**For simple Skills** (no references, <100 lines): Score based on conciseness and self-containment.

---

### D6: Freedom Fit (1–5)

Is the level of prescription matched to how fragile the task is?

Different domains demand different amounts of constraint. This dimension is about getting that dial right.

| Score | What It Looks Like |
|---|---|
| 1 | Severely mismatched (rigid scripts for creative work, hand-waving for fragile operations) |
| 2 | Multiple notable mismatches across sub-tasks |
| 3 | Partially calibrated, with notable mismatches |
| 4 | Well-tuned for most scenarios |
| 5 | Precision-calibrated freedom throughout |

**The freedom spectrum**:

| Task Type | Constraint Level | Rationale | Example Skill |
|---|---|---|---|
| Creative / Design | High freedom | Many valid solutions; differentiation is the point | frontend-design |
| Code review | Medium freedom | Principles exist, but judgment calls are unavoidable | code-review |
| File format operations | Low freedom | One wrong byte corrupts the file; consistency is non-negotiable | docx, xlsx, pdf |

**High freedom** (prose-level guidance):
```markdown
Commit to a BOLD aesthetic direction. Pick an extreme: brutally minimal,
maximalist chaos, retro-futuristic, organic natural...
```

**Medium freedom** (prioritized principles):
```markdown
Review priority:
1. Security vulnerabilities (must fix)
2. Logic errors (must fix)
3. Performance issues (should fix)
4. Maintainability (optional)
```

**Low freedom** (exact scripts, no deviation):
```markdown
**MANDATORY**: Use exact script in `scripts/create-doc.py`
Parameters: --title "X" --author "Y"
Do NOT modify the script.
```

**The calibration test**: Ask "if the model gets this wrong, what breaks?"
- High-stakes failure → Lock it down (low freedom)
- Low-stakes failure → Open it up (high freedom)

**For a Framework-pattern Skill (D7):** don't score freedom fit as if the whole Skill must sit at one point on the spectrum — a Framework skill legitimately contains sub-tasks at opposite ends simultaneously (e.g. mechanical, low-freedom correctness grading right next to open, high-freedom hypothesis-writing), because it orchestrates fragile and judgment-heavy work side by side, not because it's poorly calibrated. Apply the calibration test *per sub-task*: does the low-freedom part (data interchange, blind-label mechanics, aggregation math) stay genuinely low-freedom, and does the high-freedom part (scoping, rubric authorship, verdict judgment) stay genuinely open rather than over-specified? A Framework skill that gets both right scores in the top band even though — unlike a single-purpose Skill — its overall "freedom level" isn't one number.

---

### D7: Format Fit (1–5)

Does the Skill follow an established structural archetype?

**Score the skill's `SKILL.md` against these patterns — not its bundled `agents/`/`references/`/`scripts/` files.** Those Tier-3 resources have "no hard limit" by design (see D5) and are judged there, on layering and loading discipline, not here, on archetype fit. A skill can legitimately bundle a long reference file (a big rubric, a large lookup table) while its own `SKILL.md` is a clean, short Process or Tool fit — scoring D7 against the longest bundled file instead of `SKILL.md` double-penalizes length that D5 already accounts for, and answers a question ("does this *file* match a pattern") the dimension isn't asking.

Based on analysis of 17 official Skills, five core design patterns emerge. A sixth, Framework, is added below for a category those 17 didn't include — it rests on a single hypothetical illustration, not a 17-skill survey, so hold it to the same fit test but don't treat its "~lines" figure or defining traits as equally battle-tested yet. It has deliberately not been anchored to any real skill in this bundle, `skill-evaluator` included — grading yourself against a pattern whose only example is you is exactly the circularity this rubric's own blinding principle warns about elsewhere. If you encounter a real Framework-pattern skill (this one or another), that's the evidence this pattern should be refined against next:

| Pattern | ~Lines | Defining Traits | Example | Best For |
|---|---|---|---|---|
| **Mindset** | ~50 | Thinking > technique, strong NEVER list, high freedom | frontend-design | Creative tasks that demand taste |
| **Navigation** | ~30 | Minimal SKILL.md, routes to specialized sub-files | internal-comms | Multiple distinct sub-scenarios |
| **Philosophy** | ~150 | Two-phase: Philosophy → Express, emphasis on craft | canvas-design | Art/creation requiring originality |
| **Process** | ~200 | Phased workflow, checkpoints, medium freedom | mcp-builder | Complex multi-step projects |
| **Tool** | ~300 | Decision trees, code snippets, low freedom | docx, pdf, xlsx | Precise operations on specific formats |
| **Framework** | Varies | SKILL.md is a phased protocol (often Process-shaped) that *orchestrates* a cross-referenced ecosystem of its own — a formal rubric, JSON schemas, scorer scripts, sub-agents — where correctness depends on those pieces staying consistent with each other, not on any single file's brevity | A hypothetical `accessibility-auditor` skill that scores a website's HTML against WCAG rules and returns a compliance report | Skills whose deliverable is *measuring or auditing other skills/artifacts*, not producing a deliverable directly |

**Framework is a genuine sixth pattern, not an excuse bucket.** The 17-skill sample that produced the other five patterns were all task-execution skills (write a doc, review code, extract a table) — none of them measure other skills for a living, so none of the five patterns were built with that job in mind. A skill legitimately belongs in Framework only if its actual output *is* a judgment about some other artifact (a score, an audit, a pass/fail), not if it merely happens to be long or reference-heavy — a bloated Tool-pattern skill is still badly-fit Tool, not well-fit Framework. For a genuine Framework-pattern skill, "masterful application" (score 5) means: the rubric/schema/script/agent pieces are mutually consistent (a fact stated in one isn't contradicted in another), the protocol steps are followable end-to-end, and the whole ecosystem is navigable via explicit cross-references — not that any single file hits a specific line count.

| Score | What It Looks Like |
|---|---|
| 1 | No recognizable pattern; chaotic or formless structure |
| 2 | Partially follows a pattern with significant structural drift |
| 3 | Recognizable pattern, but with several deviations |
| 4 | Clear pattern alignment with minor deviations |
| 5 | Masterful application of the right pattern for the job |

**Pattern selection guide**:

| Your Task's Characteristics | Recommended Pattern |
|---|---|
| Requires taste and creative judgment | Mindset (~50 lines) |
| Demands originality and craft quality | Philosophy (~150 lines) |
| Branches into distinct sub-scenarios | Navigation (~30 lines) |
| Multi-step project with clear phases | Process (~200 lines) |
| Precise operations on a specific format | Tool (~300 lines) |
| Measures, scores, or audits other skills/artifacts | Framework (length varies with what it orchestrates) |

---

**The litmus test**:
1. Does it shape **what the model thinks about**? → mental models
2. Does it teach **how to do things the model wouldn't figure out on its own**? → domain procedures

A well-designed Skill delivers both when the domain calls for it.

---

### D8: Real-World Usability (1–5)

Can an Agent actually pick this Skill up and run with it?

| Score | What It Looks Like |
|---|---|
| 1 | Confusing, incomplete, contradictory, or untested guidance |
| 2 | Functional but with noticeable blind spots |
| 3 | Workable, but with real gaps in edge-case or error-recovery coverage |
| 4 | Clear, actionable guidance for the common cases |
| 5 | Comprehensive coverage — including edge cases, fallbacks, and error recovery |

**What to look for**:
- **Decision trees**: When the workflow branches, is there unambiguous guidance on which path to take?
- **Code examples**: Do they actually run? Or are they pseudocode that falls apart on first use?
- **Error recovery**: When the primary approach fails, are fallbacks spelled out?
- **Edge cases**: Are unusual-but-realistic scenarios accounted for?
- **Immediacy**: Can the Agent act on this right now, or does it still need to puzzle things out?

**Strong usability** (decision tree + fallbacks):
```markdown
| Task | Primary Tool | Fallback | When to Use Fallback |
|------|-------------|----------|----------------------|
| Read text | pdftotext | PyMuPDF | Need layout info |
| Extract tables | camelot-py | tabula-py | camelot fails |

**Common failure modes**:
- Scanned PDF: pdftotext returns blank → Run OCR first
- Encrypted PDF: Permission error → Use PyMuPDF with password
```

**Weak usability** (hand-waving):
```markdown
Use appropriate tools for PDF processing.
Handle errors properly.
Consider edge cases.
```

---

## Non-Negotiables When Evaluating

- **NEVER** hand out high scores because something "looks polished" or is neatly formatted
- **NEVER** overlook token waste — every redundant paragraph should cost points
- **NEVER** let sheer length impress you — a 43-line Skill can demolish a 500-line one
- **NEVER** skip mentally walking the decision trees — do they actually route to correct outcomes?
- **NEVER** excuse basic explanations with "but it gives helpful context"
- **NEVER** gloss over missing anti-patterns — no NEVER list is a major gap
- **NEVER** treat all procedures as equal — separate domain-specific from generic
- **NEVER** underweight the description field — a bad description means the Skill is never loaded
- **NEVER** bury "when to use" information in the body — the Agent only sees the description before deciding to load

---

## Evaluation Protocol

### Step 1: First Pass — Knowledge Payoff Scan

Read SKILL.md end to end. For every section, ask:
> "Does the model already know this?"

Tag each section:
- **[E] Expert**: The model genuinely lacks this knowledge — real value-add
- **[A] Activation**: The model knows it but a brief nudge helps — acceptable in small doses
- **[R] Redundant**: The model already reliably applies this — should be cut

Calculate the E:A:R ratio:
- Strong Skill: >70% Expert, <20% Activation, <10% Redundant
- Mediocre Skill: 40–70% Expert, heavy Activation
- Weak Skill: <40% Expert, heavy Redundant

### Step 2: Structural Analysis

```
[ ] Validate frontmatter format
[ ] Count total lines in SKILL.md
[ ] Inventory all reference files and their sizes
[ ] Identify which design pattern the Skill follows
[ ] Check for loading triggers (if references exist)
```

### Step 3: Score Each Dimension

For each of the 8 dimensions:
1. Find concrete evidence (quote specific lines)
2. Assign a score with a one-line justification
3. Note targeted improvements if the score falls below max

### Step 4: Calculate Total & Assign Grade

```
Total = D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8
Max = 40 points (8 dimensions x 5 each)
```

**Grading Scale** (percentage-based):

| Grade | Percentage | Points | Meaning |
|---|---|---|---|
| A | 90%+ | 36–40 | Excellent — production-ready expert Skill |
| B | 80–89% | 32–35 | Good — minor refinements needed |
| C | 70–79% | 28–31 | Adequate — clear improvement path exists |
| D | 60–69% | 24–27 | Below average — significant issues present |
| F | <60% | <24 | Poor — needs fundamental redesign |

### Step 5: Generate Report

**Which artifact is canonical:** when this file is used inside `skill-evaluator`'s own workflow (Step 2 of `SKILL.md`), the JSON file `evals/l0_scores.json` — shaped per `references/schemas.md` — is the artifact of record. Step 6's aggregation, `scripts/aggregate_layered.py`, cross-version comparisons, and skill-creator's eval-viewer all read that JSON by fixed field name; nothing downstream reads the Markdown below. Write `l0_scores.json` first.

The Markdown report below is a **rendering of that same JSON for a human to read in conversation**, not a second deliverable — every field maps directly (`total_score`/`max_score` → the Summary line, `dimensions.d1_knowledge_payoff` etc. → the Dimension Scores table row, `eval_design_checks.*` → the Eval-Design Checks section, `critical_issues`/`top_improvements` → the matching sections). The template below always includes the Eval-Design Checks block — when this file is used standalone rather than through `skill-evaluator`'s Step 2 (e.g. a one-off skill quality report with no `evals/eval_plan.json` prepared), omit that section rather than inventing scores for it, per the Test Prompt Realism rule above ("skip this check and say so explicitly").

```markdown
# Skill Evaluation Report: [Skill Name]

## Summary
- **Total Score**: X/40 (X%)
- **Grade**: [A/B/C/D/F]
- **Pattern**: [Mindset/Navigation/Philosophy/Process/Tool/Framework]
- **Knowledge Ratio**: E:A:R = X:Y:Z
- **Verdict**: [One sentence assessment]

## Eval-Design Checks

| Check | Score | Notes |
|---|---|---|
| Instruction Clarity | X/5 | |
| Test Prompt Realism | X/5 (or "skipped — no eval_plan.json") | |
| Description Accuracy | X/5 | |

## Dimension Scores

| Dimension | Score | Max | Notes |
|-----------|-------|-----|-------|
| D1: Knowledge Payoff | X | 5 | |
| D2: Mindset & Know-How | X | 5 | |
| D3: Gotchas & Warnings | X | 5 | |
| D4: Description Quality | X | 5 | |
| D5: Structure & Layering | X | 5 | |
| D6: Freedom Fit | X | 5 | |
| D7: Format Fit | X | 5 | |
| D8: Real-World Usability | X | 5 | |

## Critical Issues
[List must-fix problems that significantly undermine the Skill's effectiveness]

## Top 3 Improvements
1. [Highest-impact improvement with specific, actionable guidance]
2. [Second priority]
3. [Third priority]

## Detailed Analysis
[For each dimension scoring below 80%, provide:
- What's missing or broken
- Specific examples pulled from the Skill
- Concrete suggestions for improvement]
```

---

A catalog of 9 recurring failure patterns (Tutorial Trap, Info Dump, Orphaned References, Checkbox Walkthrough, Vague Warning, Invisible Skill, Misplaced Trigger, Over-Engineered Package, Freedom Mismatch), each with symptom/root cause/fix, has moved to `references/skill-design-primer.md`. It's a supplementary worked-example set — the dimension tables above already contain each pattern's diagnostic signal (e.g. D1's "instant low-score indicators" is Pattern 1; D5's score bands are Pattern 2/3) — load the primer only if you want the illustrated version.

---

## The Meta-Question

When evaluating any Skill, always circle back to this one fundamental question:

> **"Would a domain expert look at this Skill and say:**
> **'Yes — this captures knowledge that took me years to build'?"**

If yes → the Skill has genuine, irreplaceable value.
If no → it's compressing what the model already carries.

The best Skills are **compressed expert brains**. They take a designer's decade of aesthetic intuition and distill it into 43 lines, or a document specialist's operational scars into a 200-line decision tree.

What gets compressed must be things the model doesn't already have. Otherwise, it's compressing nothing into noise.

---

## On Self-Evaluation (read this, don't load a scored verdict)

This rubric can legitimately be pointed at itself — `SKILL.md` (not this file, per D7's scoping rule above) is a valid L0 target like any other skill's. But there used to be a "Self-Evaluation Note" here that pre-wrote one favorable sentence per dimension, sitting a few hundred lines below D8 in the same file every grader must load to get the rubric tables. It was removed, not softened, because that's the un-blinded setup `references/scientific-method.md` rule 4 and this skill's own Non-Negotiables forbid ("Never let a quality judge see which configuration produced an output before scoring it") — self-eval material is not exempt from that rule just because the "configuration" being judged happens to be this file itself. (Deliberately not quoting the removed text here either — even citing it as a bad example re-seeds the same words in front of the next grader.)

If you want to check whether this rubric holds up: run it blind, the same way you'd run it on any other skill. Don't write the justification first and grade to match it.