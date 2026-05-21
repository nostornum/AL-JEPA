# AL-JEPA — Audio-Language Joint Embedding Predictive Architecture

**AL-JEPA** is a two-stage framework for learning audio representations and applying them to zero-shot music genre prediction — without direct audio-label supervision.

---

## Motivation

Most audio classification systems require labeled data and cannot generalize to unseen categories. AL-JEPA takes a more foundational approach: first learn strong general-purpose audio representations through self-supervised pretraining, then teach the model to ground those representations in natural language — enabling zero-shot classification via text prompts.

---

## Training Stages

### Stage 1 — Audio Pretraining with LeJEPA

The audio encoder is pretrained on large-scale unlabeled audio using **LeJEPA** (Balestriero & LeCun, 2025), a principled self-supervised method that replaces the fragile heuristics of standard JEPAs (stop-gradient, EMA teacher, asymmetric views) with a single regularizer: **SIGReg** (Sketched Isotropic Gaussian Regularization).

SIGReg encourages the embedding distribution to match an isotropic Gaussian — the unique distribution proven to minimize downstream prediction risk for both linear and nonlinear probes. The full objective is:

$$\mathcal{L} = \mathcal{L}_{\text{pred}} + \lambda \cdot \mathcal{L}_{\text{SIGReg}}$$

This stage produces a frozen audio encoder with strong, collapse-free representations.

### Stage 2 — Grounding Audio in Language

With the stage 1 encoder frozen, a **predictor** is trained to map audio embeddings into the embedding space of a text encoder (Gemma). The predictor is conditioned on song captions and genre descriptions, learning to bridge the audio and language modalities without token-level generation.

The approach is inspired by **VL-JEPA** (Chen et al., 2026): rather than generating text autoregressively, the model predicts a continuous target embedding — making ill-posed tasks (many valid genre labels per song) tractable.

Training minimizes:

$$\mathcal{L} = \mathcal{L}_{\text{pred}} + \mathcal{L}^{\text{audio}}_{\text{SIGReg}} + \mathcal{L}^{\text{text}}_{\text{SIGReg}}$$

where the two SIGReg terms prevent collapse on each side of the embedding space independently.

---

## Inference — Zero-Shot Genre Classification

At inference time:

1. The audio encoder embeds the input song.
2. The predictor maps it into the text embedding space.
3. Genre prompts (e.g. *"a jazz song"*, *"a heavy metal track"*) are embedded by the text encoder.
4. The predicted embedding is compared against genre prompt embeddings via nearest-neighbour search.

No retraining or fine-tuning is required to classify new genres — only new text prompts.

---

## Evaluation

Genre classification accuracy is measured on a held-out split of a song genre benchmark dataset. A separate holdout set is reserved for final validation and is never used during development.

---

## Key References

- **LeJEPA**: Balestriero & LeCun (2025). *Provable and Scalable Self-Supervised Learning Without the Heuristics.* arXiv:2511.08544
- **VL-JEPA**: Chen et al. (2026). *Joint Embedding Predictive Architecture for Vision-Language.* arXiv:2512.10942
- **SLAP**: Mei et al. (2026). *Scalable Language-Audio Pretraining with Variable-Duration Audio and Multi-Objective Training.* arXiv:2601.12594

---

## Citation

```bibtex
@misc{aljepa2026,
  title   = {AL-JEPA: Audio-Language Joint Embedding Predictive Architecture for Zero-Shot Genre Prediction},
  author  = {},
  year    = {2026},
}
```

---

## License

[LICENSE](LICENSE)
