# LoRA Prep Checklist (Public Version)

> Scope: pre-training checklist for a reusable style-LoRA workflow.
> Goal: move from prepared data to stable training quickly.

## 0）Scope Lock

- [ ] Task type is **style LoRA**, not identity LoRA.
- [ ] 训练与推理统一使用 **FLUX.1 [dev]**。
- [ ] 全流程不混用 **FLUX.1 schnell**。
- [ ] Comparison strengths are fixed: `0 / 0.6 / 0.8 / 1.0`.

## 1）工作目录结构

- [x] 已创建 `lora_model/data/train/images`。
- [x] 已创建 `lora_model/data/train/captions`。
- [x] 已创建 `lora_model/configs`。
- [x] 已创建 `lora_model/outputs/checkpoints`。
- [x] 已创建 `lora_model/outputs/samples`。
- [x] 已创建 `lora_model/outputs/logs`。
- [x] 已创建 `lora_model/scripts`。

## 2）数据命名规则（必须保持）

- [ ] 图片命名固定：`jpfantasy_style_0001.png` ... `jpfantasy_style_NNNN.png`。
- [ ] caption 命名 1:1 对齐：`jpfantasy_style_0001.txt` ... `jpfantasy_style_NNNN.txt`。
- [ ] 每张图片严格对应 1 个 caption 文件。
- [ ] caption 文件统一为 UTF-8 纯文本。

## 3）Caption Strategy

- [ ] 固定触发词（trigger token）：`jpfantasy_style`。
- [ ] caption 长度控制在短到中等，避免过长叙事文本。
- [ ] 保留可复用视觉信息：构图、光照、材质、氛围等。
- [ ] 避免过度具体的身份词，防止模型记忆成角色 LoRA。
- [ ] 全数据集 caption 语气与写法保持一致。

示例 caption 模板：

`jpfantasy_style, anime illustration, soft cel shading, clean lineart, pastel palette, fantasy atmosphere`

## 4）Two-Stage Training Plan

### Stage A - Smoke Test

- [ ] 先进行短程训练（例如 300-800 steps）验证流程。
- [ ] 确认输出出现可见风格偏移。
- [ ] 确认无路径、配置、运行时错误。

### Stage B - Full Training

- [ ] 进行完整训练，产出可用于报告的 checkpoints。
- [ ] 周期性保存 checkpoint（例如每 200-500 steps）。
- [ ] 固定评估 prompt 与固定 seed 做公平比较。

## 5）起始超参数建议范围

> 最终值可在 Ostris 中再微调，先从保守稳定范围起步。

- [ ] LoRA rank/dim：从 `16` 起步（必要时升到 `32`）。
- [ ] Alpha：与 rank 相同，或设为 rank 的一半。
- [ ] Learning rate：`1e-4` 到 `5e-5`（风格任务优先稳）。
- [ ] Resolution：与数据集保持一致（可行时优先 1024 体系）。
- [ ] Batch size：按显存上限取稳定值。
- [ ] Optimizer：AdamW（或 Ostris 默认稳定选项）。

## 6）开训前校验（按下 Train 前）

- [ ] Ostris 训练 base 已确认是 FLUX.1 dev。
- [ ] ComfyUI 推理端已准备同一 FLUX.1 dev 权重族。
- [ ] 图片数量与 caption 数量一致。
- [ ] 图片与 caption 文件名映射正确。
- [ ] 触发词 `jpfantasy_style` 在数据集中使用一致。
- [ ] 无损坏图片、空 caption、乱码文件。
- [ ] 输出目录可写且磁盘剩余空间充足。
- [ ] checkpoint 保存间隔已设置。
- [ ] 评估 prompts 已提前准备并固定。
- [ ] 训练配置快照已保存（保证报告可复现）。

## 7）Minimal Handover Flow

1. 将训练图复制到 `data/train/images`。
2. 将同名 captions 复制到 `data/train/captions`。
3. 在 Ostris 载入预设训练配置。
4. 先跑 Stage A 冒烟测试。
5. 再跑 Stage B 正式训练。
6. 用固定 prompt/seed 对比 checkpoints，选出最佳 LoRA。

---

Status: public checklist for reproducible LoRA preparation.
