# ComfyUI LoRA 风格迁移实践项目

本仓库展示了一个基于 `FLUX.1-dev` 的 LoRA 风格迁移实践流程，覆盖数据准备、训练配置与可控对比实验，重点体现可复现性和工程落地过程。

## 项目目标

- 搭建可复现的 LoRA 训练与推理流程。
- 对比不同 Prompt 与强度参数下的生成表现。
- 记录真实硬件约束下的关键取舍与实践结论。

## 仓库结构

- `lora_model/data/train/images/`：训练图片（28 张）。
- `lora_model/data/train/captions/`：与训练图片一一对应的文本标注。
- `lora_model/configs/`：训练与数据集配置文件。
- `outputs/compare/`：对比实验输出与实验日志。
- `PROJECT_REPORT_DRAFT_EN.md`：英文项目报告草稿。
- `PROJECT_REPORT_DRAFT_CN.md`：中文项目报告草稿。
- `PROJECT_REPORT_SOURCE_NOTES.md`：报告撰写使用的事实与实验记录。
- `PROJECT_REPORT_FRAMEWORK.md`：报告结构框架（公开版）。
- `PROJECT_REQUIREMENTS_PUBLIC.md`：项目需求说明（公开版）。
- `PROJECT_MEMORY_PUBLIC.md`：项目记录与决策摘要（公开版）。

## 方法概览

1. 筛选规模适中且风格一致的数据集。
2. 准备压缩后的风格导向 captions。
3. 在有限硬件条件下完成 LoRA 训练。
4. 使用固定 seed 进行可控对比实验。
5. 分析不同强度下的风格收益与伪影风险。

## 复现说明

- 训练与推理统一使用基座模型：`FLUX.1-dev`。
- Prompt ID、seed 与 strength 参数记录在 `outputs/compare/PROMPTS_COMPARE_LOG.md`。
- 基线工作流参考见 `outputs/compare/_workflow_baseline/`。



