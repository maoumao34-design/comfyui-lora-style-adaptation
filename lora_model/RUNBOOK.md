# LoRA Training Runbook (Public Version)

> Goal: start training quickly once data is ready.
> Scope: generic FLUX.1-dev style LoRA workflow with Ostris + ComfyUI.

## 0）前提条件

- 已存在目录：`lora_model/data/train/images`、`lora_model/data/train/captions`、`lora_model/outputs/*`。
- 已存在配置：`lora_model/configs/dataset.yaml`、`lora_model/configs/train.stageA.yaml`、`lora_model/configs/train.stageB.yaml`。
- Keep training and inference within one model family (FLUX.1-dev).

## 1）放置数据（约 2 分钟）

将数据拷贝到以下目录：

- 图片：`lora_model/data/train/images`
- captions：`lora_model/data/train/captions`

必须满足：

- 同名配对：`jpfantasy_style_0001.png` ↔ `jpfantasy_style_0001.txt`
- 一图一 caption
- caption 编码为 UTF-8
- caption 中统一包含触发词：`jpfantasy_style`

## 2）开训前快速自检（约 2 分钟）

- [ ] 图片数量 = caption 数量
- [ ] 无空 caption 文件
- [ ] 无损坏图片
- [ ] 文件名完全一一对应（不多空格、不乱后缀）
- [ ] `dataset.yaml` 路径指向当前目录结构
- [ ] `train.stageA.yaml` 与 `train.stageB.yaml` 的 base 均为 `FLUX.1-dev`

## 3）Stage A（smoke test）

直接使用 `configs/train.stageA.yaml` 运行短程验证（已预设）：

- `total_steps: 600`
- `save_every_steps: 200`
- `sample.every_steps: 200`
- `seed: 20260407`

Goals:

- 验证训练流程可跑通
- Verify style shift appears in sample outputs
- Do not optimize final quality at this stage

## 4）检查冒烟结果（约 1 分钟）

查看：

- `outputs/checkpoints` 是否正常产出权重
- `outputs/samples` 是否正常产出样图
- 样图是否出现“日系魔幻风格”倾向

若失败，先修复数据/路径/配置，不要直接加步数。

## 5）Stage B（full training）

冒烟通过后，切换到 `configs/train.stageB.yaml` 进入正式训练：

- `total_steps: 3000`（可按数据规模再调到 2000~6000）
- 保持其余参数稳定，避免多变量同时变化
- 固定评估 prompt 与固定 seed

Goals:

- 产出多个可对比 checkpoint
- Select the best checkpoint for inference and report examples

## 6）选择最佳 LoRA（训练后）

固定同一评估 prompt + 同一 seed，对比各 checkpoint：

- 风格一致性
- 细节质量（线条、材质、伪影）
- 泛化能力（更换主体/场景是否仍保风格）

建议保留：

- 1 个主 checkpoint（用于报告主图）
- 1 个备选 checkpoint（用于兜底）

## 7）接入 ComfyUI 做对比图

- 使用同一 FLUX.1 dev 基座
- 加载 LoRA（主/备选）
- 进行强度对比：`0 / 0.6 / 0.8 / 1.0`
- 保存“无 LoRA vs 有 LoRA”的同 prompt 对照图

---

## 常见异常速查表（5 类）

### A. 训练直接报路径错误

可能原因：

- `dataset.yaml` / `train.yaml` 路径写错
- Windows 路径分隔符混用

处理：

- 统一使用当前项目绝对路径
- 先检查 `image_dir`、`caption_dir`、`output_root`

### B. 图片数量与 caption 数量不一致

可能原因：

- 漏了 `.txt` 或文件名不一致
- 图片后缀与配置不匹配

处理：

- 对齐同名 stem（不含后缀）
- 在 `dataset.yaml` 增加或确认对应后缀

### C. 样图几乎无风格变化

可能原因：

- steps 太少
- caption 触发词不统一
- 风格数据分布不稳定

处理：

- 先检查 token 一致性（`jpfantasy_style`）
- 保持参数不变，增加正式训练步数
- 清理离群样本

### D. 出现明显过拟合（只会复现固定构图）

可能原因：

- 数据重复度过高
- caption 过于具体（身份词过多）

处理：

- 降低具体身份描述，强化风格描述
- 增加场景与构图多样性
- 优先选择中间 checkpoint

### E. ComfyUI 推理效果与训练样图差异大

可能原因：

- 推理底模与训练底模不一致
- LoRA 强度过高或过低

处理：

- 确认推理端同为 FLUX.1 dev 权重族
- 从 `0.6 -> 0.8 -> 1.0` 逐档测试

---

Status: public runbook for reproducible LoRA training workflow.
