# AGENTS.md

## Project Overview

**AL-JEPA** is a two-stage framework for zero-shot music genre classification.

**Stage 1 — Audio Pretraining:** An audio encoder (ViT-based, mel-spectrogram input) is pretrained on large-scale unlabeled audio using LeJEPA. The objective is a prediction loss plus SIGReg (Sketched Isotropic Gaussian Regularization), which replaces the heuristics of standard JEPAs (EMA teacher, stop-gradient, asymmetric views) with a single principled collapse-prevention term. Output: a frozen audio encoder with strong general representations.

**Stage 2 — Language Grounding:** With the stage 1 encoder frozen, a predictor is trained to map audio embeddings into the Gemma text embedding space, conditioned on song captions and genre descriptions. Loss: cross-modal prediction loss + SIGReg on both the audio and text sides (collapse avoidance). Inspired by VL-JEPA — predicts continuous embeddings, not tokens.

**Evaluation:** Zero-shot genre classification via nearest-neighbour search between predicted audio embeddings and genre prompt embeddings. Accuracy measured on a held-out genre benchmark; a separate final holdout is never touched during development.

---

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.
