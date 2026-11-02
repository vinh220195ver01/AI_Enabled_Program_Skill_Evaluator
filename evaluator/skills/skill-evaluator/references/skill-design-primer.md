# Skill Design & Evaluation Framework — Background

This is the conceptual framing behind the 8-dimension rubric in `agents/input-layer-judge.md`, plus the "Common Failure Patterns" catalog. It's background/teaching material, not part of the scoring mechanism itself — `input-layer-judge.md` doesn't need this file loaded to score a skill; it's here for whoever wants the reasoning behind the rubric, or a worked-example catalog of failure modes before writing a NEW skill (skill-creator's job) rather than grading an existing one.

**Do NOT load this file as part of scoring L0.** The rubric tables in `agents/input-layer-judge.md` are self-sufficient for grading; this file was split out specifically because it was dead weight on every scoring pass.

---

### The Value Equation

> **Effective Skill = Specialized Expertise − Model's Existing Knowledge**

A Skill's worth comes down to its **knowledge delta** — the distance between what it contributes and what the model can already figure out on its own. If a Skill spends tokens explaining "what is a PDF" or "how a for-loop works," it's rehashing what the model already carries. That's **wasted context** — and context is a shared, finite resource split between system prompts, conversation history, other Skills, and the user's actual request. This equation is what D1 ("Knowledge Payoff") is actually measuring — everything below operationalizes it.

### Three Categories of Skill Content

Every section in a Skill falls into one of these buckets:

| Category | What It Means | How to Handle It |
|---|---|---|
| **Expert** | Knowledge the model genuinely lacks | Preserve — this is the Skill's reason for existing |
| **Activation** | Knowledge the model has but might not surface unprompted | Keep sparingly — useful as a nudge, not a lecture |
| **Redundant** | Knowledge the model already reliably applies | Remove — it burns tokens for zero benefit |

Great Skill design means **maximizing Expert content**, using Activation as a light touch, and cutting Redundant material without mercy.

---

## Common Failure Patterns

### Pattern 1: The Tutorial Trap
```
Symptom:  Explains what a PDF is, how Python works, basic library usage
Root cause: Author assumes the Skill's job is to "teach" the model
Fix:      The model already knows this. Strip all basic explanations.
          Redirect focus to expert decisions, trade-offs, and anti-patterns.
```

### Pattern 2: The Info Dump
```
Symptom:  SKILL.md bloats past 800+ lines with everything thrown in
Root cause: No progressive disclosure strategy
Fix:      Core routing and decision trees in SKILL.md (<300 lines ideal).
          Move detailed content to references/, loaded on demand.
```

### Pattern 3: The Orphaned References
```
Symptom:  references/ directory exists but files are never actually loaded
Root cause: No explicit loading triggers in the workflow
Fix:      Add "MANDATORY — READ ENTIRE FILE" at workflow branch points.
          Add "Do NOT load" directives to prevent unnecessary loading.
```

### Pattern 4: The Checkbox Walkthrough
```
Symptom:  Step 1, Step 2, Step 3… mechanical procedures with no reasoning
Root cause: Author thinks in operations, not decision frameworks
Fix:      Reframe as "Before doing X, ask yourself…"
          Center on decision principles, not operation sequences.
```

### Pattern 5: The Vague Warning
```
Symptom:  "Be careful," "avoid errors," "consider edge cases"
Root cause: Author senses things can go wrong but hasn't pinpointed the specifics
Fix:      Replace with a concrete NEVER list — specific examples + non-obvious reasons.
          "NEVER use X because [problem that takes real experience to discover]"
```

### Pattern 6: The Invisible Skill
```
Symptom:  Stellar content but the Skill barely ever gets activated
Root cause: Description is vague, lacks keywords, or omits trigger scenarios
Fix:      Description must answer WHAT, WHEN, and include KEYWORDS.
          "Use when…" + specific scenarios + searchable terms

Example fix:
BAD:  "Helps with document tasks"
GOOD: "Create, edit, and analyze .docx files. Use when working with
       Word documents, tracked changes, or professional document formatting."
```

### Pattern 7: The Misplaced Trigger
```
Symptom:  "When to use this Skill" lives in the body, not the description
Root cause: Misunderstanding of the three-tier loading model
Fix:      Move all triggering information into the description field.
          The body is only loaded AFTER the activation decision is already made.
```

### Pattern 8: The Over-Engineered Package
```
Symptom:  README.md, CHANGELOG.md, INSTALLATION_GUIDE.md, CONTRIBUTING.md
Root cause: Treating the Skill like a software project
Fix:      Delete all auxiliary files. Include only what the Agent needs to do the job.
          No documentation about the Skill itself — only documentation for the task.
```

### Pattern 9: The Freedom Mismatch
```
Symptom:  Rigid scripts imposed on creative tasks, vague pointers given for fragile operations
Root cause: No consideration of task fragility
Fix:      High freedom for creative work (principles, not steps).
          Low freedom for fragile operations (exact scripts, locked parameters).
```
