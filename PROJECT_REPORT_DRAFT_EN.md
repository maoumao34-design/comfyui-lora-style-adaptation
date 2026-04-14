# Title

**An Experimental Study of Custom LoRA Training in ComfyUI (FLUX.1-dev)**

---

## Abstract

This report presents a completed end-to-end project on training and evaluating a custom LoRA style model using `ComfyUI + Ostris AI Toolkit`. The entire pipeline uses a single base model, `FLUX.1-dev`, and keeps training and inference within the same model family (without mixing Schnell). The training set contains 28 Japanese-fantasy themed images with matched captions, using `jpfantasy_style` as the trigger token. The Stage A output, `jpfantasy_style_stageA.safetensors`, is used as the core artifact for method and result analysis.

To address the core evaluation dimensions, I completed three experiment groups: Group A compares LoRA on/off and strength levels, Group B compares short-to-long prompts, and Group C focuses on difficult failure cases (multi-character dynamics and text readability). Under fixed-seed, single-run settings, LoRA strength clearly affects style intensity and scene atmosphere, while longer prompts generally improve intra-group consistency. At the same time, hand structure, multi-character interaction, and complex text rendering remain major limitations. Due to hardware and time constraints, the project was finalized with Stage A, and Stage B was cancelled after the Stage A pipeline had produced usable and reproducible results.

---

## 1. Introduction

I selected this advanced workflow project to complete a full ComfyUI pipeline with custom LoRA training, rather than only testing online tools. This direction was chosen for three reasons. First, the open-source workflow offers stronger controllability through explicit model, node, and parameter management. Second, LoRA training is more resource-efficient than full fine-tuning, which makes it feasible within the assignment timeline. Third, the advanced workflow scope emphasizes hands-on practice; using a Japanese-fantasy LoRA theme provides a complete and explainable train-infer-compare loop.

This report follows a single-base-model setup: both training and inference use `FLUX.1-dev`, with no second checkpoint introduced for model-to-model comparison. This keeps the variables focused on LoRA strength and prompt complexity. The report is organized as follows: Section 2 describes setup and environment, Section 3 explains the method and experiment protocol, Sections 4 and 5 address the first two required assignment components, Section 6 discusses limitations and future directions, and Section 7 concludes the project.

From a practical standpoint, the most important decision in this project was to prioritize a reproducible end-to-end workflow before scaling up. Under hardware constraints, I first validated the training chain with a 5-step test run, then proceeded to Stage A training. Once Stage A met the experiment needs, I focused on completing the A/B/C comparisons and result analysis instead of extending training scope.

---

## 2. Background and Setup

### 2.1 Toolchain and Runtime Environment

This project uses two local tools:
- Inference tool: `ComfyUI` (`F:\AI_tool\ComfyUI`)
- Training tool: `Ostris AI Toolkit` (`F:\AI_tool\ai-toolkit`)

They run in separate virtual environments to avoid dependency conflicts. ComfyUI is used for all A/B/C image generation, and Ostris is used for LoRA training. Hugging Face authentication was completed with access to `FLUX.1-dev`. The overall workflow is: data preparation -> caption preparation -> Stage A training -> ComfyUI LoRA inference for comparison.

Because of hardware and time limits, I used a staged risk-control strategy: a 5-step test was run first to verify configuration, paths, and training flow, then Stage A formal training was started. The save policy and scope-control decision are explained in Section 2.4.

### 2.2 Model Route and Consistency Constraint

The only base model in this project is `black-forest-labs/FLUX.1-dev`. Training and inference were kept in the same model family to avoid dev/schnell mismatch and uncontrolled behavior drift. This consistency is critical for interpretation: if different base families are mixed, LoRA effects become entangled with base-model differences.

### 2.3 Dataset and Caption Strategy

The training set contains 28 image-caption pairs:
- Images: `lora_model\data\train\images`
- Captions: `lora_model\data\train\captions`

Files are named from `jpfantasy_style_0001` to `jpfantasy_style_0028`. Captions use a compact format (trigger token + subject/scene keywords + a few style cues), with `jpfantasy_style` fixed as the trigger token. This compact format helps maintain learning focus and reduces noise from overly long prompt text.

Dataset construction followed a two-stage process: for each scene, more than 20 candidates were generated first, then one image was manually selected into the final training set. Reference images in scene folders were used only for visual guidance and were not included in training.

### 2.4 Training Configuration and Outputs

The core model used in this report comes from Stage A:
`lora_model\outputs\jpfantasy_style_stageA\jpfantasy_style_stageA.safetensors`.

Stage A was fully completed with training logs preserved, and all analyses in this report are based on Stage A outputs. Stage B was cancelled due to hardware and time constraints: even with low-VRAM and reduced settings, Stage A still required around two hours per run. Therefore, Stage B was not continued.

The training weights, configs, and logs are included as process evidence in the report but are not part of the submitted attachments. This scope decision prioritizes reproducibility and interpretability within the assignment timeline.

In practice, I first validated the pipeline with a 5-step test, then entered Stage A. To improve robustness, Stage A was configured to save every 20 steps. This strategy produced a usable model (`jpfantasy_style_stageA.safetensors`) and directly supported the final experiment scope.

## 3. Method and Comparison Protocol

### 3.1 Unified Baseline

All experiments use one unified ComfyUI baseline workflow (parameters recorded in the baseline notes), with fixed sampling settings: `1024x1024`, `steps=20`, `sampler=euler`, `scheduler=simple`, `cfg=1.0`.
LoRA clip strength is fixed at `1.0`. Model strength settings are `0.0 / 0.6 / 0.8 / 1.0` for Groups A/B, and `0.0 / 1.0` for Group C.

### 3.2 Three Experiment Groups

- **Group A (`A_lora_on_off`)**: multi-theme comparisons to evaluate visual/style changes across LoRA strengths.
- **Group B (`B_strength`)**: short/medium/long prompt comparisons under one seed to study prompt-length and LoRA interaction.
- **Group C (`C_prompt_complexity`)**: difficult cases (multi-character combat, dense signboards) for limitation analysis rather than best-looking outputs.

### 3.3 Experiment Protocol and Index Table (Aligned with `PROMPTS_COMPARE_LOG.md`)

| Group | Subgroup | Prompt ID | Seed | Model strength | Clip strength |
|------|------|-----------|------|----------------|---------------|
| A | A1 | `A1_prompt_hero` | `781069391428044` | `0.0 / 0.6 / 0.8 / 1.0` | `1.0` |
| A | A2 | `A2_prompt_city` | `558036329660600` | `0.0 / 0.6 / 0.8 / 1.0` | `1.0` |
| A | A3 | `A3_prompt_mage_harbor` | `506744058271183` | `0.0 / 0.6 / 0.8 / 1.0` | `1.0` |
| A | A4 | `A4_prompt_miko_gouache` | `298084320241887` | `0.0 / 0.6 / 0.8 / 1.0` | `1.0` |
| B | B1 | `B1_prompt_short_heroine` | `971947498959982` | `0.0 / 0.6 / 0.8 / 1.0` | `1.0` |
| B | B2 | `B2_prompt_medium_heroine` | `971947498959982` | `0.0 / 0.6 / 0.8 / 1.0` | `1.0` |
| B | B3 | `B3_prompt_long_heroine` | `971947498959982` | `0.0 / 0.6 / 0.8 / 1.0` | `1.0` |
| C | C1 | `C1_prompt_combat_multi` | `572738612206139` | `0.0 / 1.0` | `1.0` |
| C | C2 | `C2_prompt_sign_night_market` | `1082998128340460` | `0.0 / 1.0` | `1.0` |

Note: full `clip_l` and `t5xxl` texts are taken from `outputs\compare\PROMPTS_COMPARE_LOG.md` as the single source of truth.

### 3.4 Interpretation Boundary

All findings in this report come from fixed-seed, single-run, one-image-per-setting comparisons. This is an engineering-level comparison, not a statistically significant study. Therefore, conclusions are strictly limited to what is observed in this specific run.

In addition, all image references in the report and appendix use original filenames in `outputs\compare\` as the only index key. Filenames are not renamed, and no secondary mapping is introduced.

---

## 4. Results I: Visual Comparison (Requirement 1)

### 4.1 Style and Atmosphere Changes in A1/A2

In A1 (`A1_prompt_hero`, seed `781069391428044`), the `0.0` setting remains closer to base-model appearance. Style changes become clear at `0.6`. `0.8` and `1.0` are similar overall, but `1.0` is often brighter with stronger volume impression.

In A2 (`A2_prompt_city`, seed `558036329660600`), the contrast is more obvious. In this run, `0.0` looks more photographic, with sharper structural edges and cleaner street order. `1.0` appears more fantasy-illustrative, with denser distant layers and brighter atmosphere. `0.6` and `0.8` show transitional behavior between both ends.

### 4.2 Trade-off Between Aesthetic Cohesion and Structural Reliability

Higher LoRA strength often improves style cohesion, but structural stability does not improve monotonically with strength. Hand/foot artifacts observed in A3/A4 and Group B show that stronger style control does not automatically mean better anatomy reliability.

For stable generation, a mid-range strength (`0.6`-`0.8`) is generally safer in this project setup. For stronger style impact, `1.0` is usable, but manual selection and local correction become more important.

### 4.3 Section Summary

Group A demonstrates clear LoRA impact on style shaping, while also exposing a balance issue between style strength and structure stability. This provides a consistent explanation for Groups B and C: output quality is jointly affected by prompt information density, LoRA strength, and scene difficulty.

---

## 5. Results II: Prompt Complexity from Short to Long (Requirement 2)

### 5.1 Group B Design

B1/B2/B3 correspond to short/medium/long prompts (`B1_prompt_short_heroine`, `B2_prompt_medium_heroine`, `B3_prompt_long_heroine`), all under seed `971947498959982`, with four model strengths (`0.0 / 0.6 / 0.8 / 1.0`). This design isolates prompt complexity as the primary variable.

### 5.2 Main Observations

In this run, as prompt length increases, outputs across the four strength levels within the same subgroup become more similar in composition and overall character impression. Under short prompts, cross-strength variation is larger. A practical reading is that sparse language constraints leave more room for strength-driven drift, while richer constraints narrow that drift.

Also, several hand artifacts appear in higher-strength B1/B2 samples, while B3 does not show the same level of obvious hand issues in this run. This may be related to stronger structural guidance from longer prompts, but the evidence is still single-run and should not be generalized.

### 5.3 Section Summary

Group B satisfies the assignment requirement of short-to-long prompt comparison. The key engineering takeaway is that longer prompts are not automatically better, but in this setup they can improve consistency and controllability. In practice, the benefit should be balanced against prompt-writing complexity.

---

## 6. Limitations and Future Work (Requirement 3)

### 6.1 Failure Types and Representative Cases

The major issues in this project fall into three categories:
1) **Hand/foot structural artifacts** (A3, A4, B1, B2, C1)
2) **Unstable multi-character interaction** (C1 combat case)
3) **Text readability vs stylization conflict** (C2 signboard case)

To keep appendix references traceable, representative problematic samples are listed by original filenames (single-run, not replicated):

| Subgroup | Issue Type | Filename |
|------|----------|--------|
| B1 (`0.6`) | Fingers | `B1, 971947498959982, 0.6, 1.0.png` |
| B1 (`1.0`) | Fingers | `B1, 971947498959982, 1.0, 1.0.png` |
| B2 (`0.6`) | Fingers | `B2, 971947498959982, 0.6, 1.0.png` |
| B2 (`0.8`) | Fingers | `B2, 971947498959982, 0.8, 1.0.png` |
| B2 (`1.0`) | Fingers | `B2, 971947498959982, 1.0, 1.0.png` |
| A3 (`0.6`) | Hands | `A3, 506744058271183, 0.6, 1.0.png` |
| A4 (`0.8`) | Feet | `A4, 298084320241887, 0.8, 1.0.png` |
| C1 (`1.0`) | Hand structure/count | `C1, 572738612206139, 1.0, 1.0.png` |
| C2 (`1.0`) | Letterform distortion | `C2, 1082998128340460, 1.0, 1.0.png` |

For C1, the limitation is consistent with data coverage: the training set is mainly single-subject style data, so multi-character dynamic combat is out-of-distribution. For C2, stronger style improves fantasy mood, but standard text fidelity becomes less reliable.

### 6.2 Toolchain-Level Limitations

- ComfyUI offers high flexibility, but also a steeper learning and debugging cost.
- Training setup remains sensitive to environment and configuration details.
- Under assignment constraints, evaluation is mainly qualitative, with limited statistical support.

These issues do not negate the value of the toolchain; they show that high controllability and engineering complexity coexist and must be managed through careful workflow design.

### 6.3 Future Directions

If this project is extended in the future, the priorities are:
- **Replication strengthening**: multi-seed, multi-run evaluations for each subgroup.
- **Data coverage expansion**: more samples for multi-character interaction, difficult hand poses, and text-heavy scenes.
- **Process optimization**: better semi-automatic filtering plus manual review.

---

## 7. Conclusion

This project successfully completes its core targets: custom LoRA training in a ComfyUI workflow, plus structured analysis of visual comparison, prompt complexity, and limitations.

Under the current experimental setup, I confirm that LoRA strength strongly shapes Japanese-fantasy style appearance, and longer prompts can improve consistency in this run. At the same time, hand structure, multi-character dynamics, and text readability remain key weak points.

Given the balance between controllability, reproducibility, and extensibility, I will continue using the `ComfyUI + Ostris + FLUX.1-dev` route. The next improvements should focus on multi-seed validation and broader data coverage to improve reliability and generalization.

---

## Submission Scope and File Roles

To avoid confusion between process files and submission attachments, this project follows the scope below:

- **Submitted files**
  - `train` folder: `lora_model\data\train\` (`images` contains the 28 training images; `captions` contains the matching text labels).
  - `compare` folder: `outputs\compare\` (includes A/B/C comparison outputs and `workflow_baseline_connected.png` for baseline workflow reference).
  - Final report file (PDF body + appendix layout).

- **Used in workflow but not submitted**
  - Stage A / Stage B training configs and runtime process files.
  - LoRA weight files (e.g., `jpfantasy_style_stageA.safetensors`) and training logs.
  - Local environment/cache files and tool runtime dependencies.

- **Why these are excluded from attachments**
  - The project evaluation focus is experiment design, visual comparison, and reflective analysis; image evidence directly supports these components.
  - Training weights and process files are used for methodological traceability and are documented in the report text.
  - Stage B was cancelled due to hardware/time constraints after Stage A had already met the experiment requirements.
