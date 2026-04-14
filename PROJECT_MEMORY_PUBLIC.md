# Project Memory (Public Version)

This file keeps stable, public-facing project decisions for portfolio use.

## 1) Project Scope

- Project type: custom style LoRA workflow
- Inference stack: ComfyUI
- Training stack: Ostris AI Toolkit
- Base model family: FLUX.1-dev only (no mixing with Schnell)
- Main comparison axes:
  - LoRA on/off
  - LoRA strength (`0.0 / 0.6 / 0.8 / 1.0`)
  - Prompt complexity (short -> medium -> long)

## 2) Data and Artifact Policy

- Training data layout:
  - `lora_model/data/train/images`
  - `lora_model/data/train/captions`
- Public repo should keep reproducible configs, scripts, and selected outputs.
- Large local runtime assets (venv, full checkpoints, caches, temporary logs) should remain outside GitHub.

## 3) Reporting Structure

Public report/documentation should include:

1. Visual comparison across style, aesthetics, realism, and perception
2. Prompt complexity analysis from short to long prompts
3. Limitations and future work based on observed failure patterns

## 4) Execution Baseline

- Train with Stage A as the primary usable checkpoint source.
- Keep experiment settings traceable via prompt IDs, seeds, and output filenames.
- Use a fixed baseline workflow for fair comparison across A/B/C groups.

## 5) Change Log (Public)

Use this section to track major technical changes without course-specific metadata.

| Date | Summary |
|------|---------|
| 2026-04-04 | Initial local setup for ComfyUI + training toolchain |
| 2026-04-13 | Stage A training completed with usable checkpoint |
| 2026-04-14 | Comparison protocol finalized (A/B/C groups + fixed seeds) |
