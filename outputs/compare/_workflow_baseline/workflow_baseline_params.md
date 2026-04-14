# ComfyUI 基线工作流（报告参考快照）

> 记录日期：2026-04-13  
> 用途：作为后续对比图实验与报告复现的基线配置快照（中文沟通稿）。

## 1) 工作流截图

- 文件：`outputs/compare/_workflow_baseline/workflow_baseline_connected.png`
- 说明：该截图为当前可运行的 FLUX.1-dev + LoRA 节点连接状态。

## 2) 主要模型与节点连接

- 底模（UNet）：`flux1-dev.safetensors`
- 文本编码：`clip_l.safetensors` + `t5xxl_fp16.safetensors`（flux 双编码）
- VAE：`ae.safetensors`
- LoRA：`jpfantasy_style_stageA.safetensors`

LoRA 连接约定（保持不变）：

- `UNet加载器(model) -> 加载LoRA(model in)`
- `双CLIP加载器(clip) -> 加载LoRA(clip in)`
- `加载LoRA(model out) -> K采样器(model)`
- `加载LoRA(clip out) -> CLIP文本编码(Flux)(clip)`

## 3) 当前基线参数（截图对应）

- 分辨率：`1024 x 1024`
- 批量：`1`
- 采样步数（steps）：`20`
- CFG：`1.0`
- Sampler：`euler`
- Scheduler：`simple`
- Denoise：`1.00`
- Seed：截图时为随机模式（`randomize`）

## 4) 对比实验执行约定

为保证报告可复现，正式出对比图时：

- 固定 seed（建议统一 `20260407`）
- 固定采样参数（steps/cfg/sampler/scheduler/分辨率）
- 单次实验只改一个变量（LoRA 开关、LoRA 强度、prompt 长度）

## 5) 备注

- 本文件是“基线工作流快照”，不是最终英文报告正文。
- 最终定稿后再统一转英文写入报告。
