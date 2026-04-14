# Project Report Source Notes (Public Version)

> Purpose: source-of-truth notes for drafting the public English report.
> Scope: technical facts only (environment, data, training, experiment protocol).

---

## 1. Project Baseline

| 项 | 内容 |
|----|------|
| Scope | ComfyUI + custom LoRA workflow |
| 底模 | **唯一** **FLUX.1 [dev]**（`black-forest-labs/FLUX.1-dev`），**勿与 Schnell 混用** |
| 训练工具 | **Ostris AI Toolkit**（仓库名 `ostris/ai-toolkit`），教授推荐 |
| 对照设计 | 教授确认**无需第二种 checkpoint**；对比：**无/有 LoRA**、**LoRA 强度**、**prompt 复杂度** |
| LoRA 主题 | **日系魔幻风格**（训练侧用触发词 **`jpfantasy_style`**） |
| Report form | English PDF main body + appendix images |

---

## 2. Paths and Environment

**勿提交大模型与 venv 到 GitHub；下列为本地事实路径。**

| 角色 | 路径 |
|------|------|
| 作业文档与精选产出 | `F:\Cursor_project\ComfyUI_Project\` |
| LoRA 工程（数据、说明、脚本） | `F:\Cursor_project\ComfyUI_Project\lora_model\` |
| ComfyUI 本体 | `F:\AI_tool\ComfyUI\`（venv：`F:\AI_tool\ComfyUI\venv`） |
| Ostris / AI Toolkit | `F:\AI_tool\ai-toolkit\`（venv：`F:\AI_tool\ai-toolkit\venv`） |
| Hugging Face 凭据缓存（本机） | `C:\Users\19613\.cache\huggingface\`（勿提交） |

**ComfyUI 启动（PowerShell）：**

```powershell
cd F:\AI_tool\ComfyUI
.\venv\Scripts\Activate.ps1
python main.py
```

浏览器：`http://127.0.0.1:8188`（若改端口以终端为准）。

---

## 3. Environment and Versions

### 3.1 ComfyUI 侧（推理）

- 曾记录：PyTorch **Nightly cu128** 以支持 **RTX 50 / sm_120**（见 `ASSIGNMENT_MEMORY.md` 变更日志）。
- 抽样检查（ComfyUI venv）：`torch` 曾为 `2.12.0.dev...+cu128`，`CUDA 12.8`，`torch.cuda.is_available() True`（以本机 `python -c "import torch; ..."` 为准写报告）。

### 3.2 Ostris 侧（训练）

- 安装方式：克隆 `F:\AI_tool\ai-toolkit`，独立 venv，按官方 README：先装 **torch 2.9.1 + cu128**，再 `pip install -r requirements.txt`。
- 曾遇问题：`requirements.txt` 中 `scipy==1.12.0` 在 **Python 3.13** 下易触发源码编译失败；处理：先装 **`scipy==1.17.1`**（wheel），再用 **`pip install -r requirements_base.txt --use-deprecated=legacy-resolver`**；并将 **`huggingface_hub` 固定为 `0.36.2`** 以匹配 `transformers 4.57.3`。
- 验证：`python run.py --help` 正常；`hf auth whoami` 显示已登录用户（见下）。

### 3.3 Hugging Face

- 登录状态：**已成功**（`hf auth whoami` 可返回有效账号信息）。
- 访问 **FLUX.1-dev** 前须在网页端接受模型许可；token 权限：**Repositories Read** 即可（无需 Billing/Collections 等）。

---

## 4. Dataset

### 4.1 来源

- 原始工程文件夹：  
  `F:\Cursor_project\ComfyUI_Project\USO style reference generated photo for training`
- **ComfyUI 生成管线名称：** **flux1 USO Style Reference**（用于各场景候选图与风格参考；与作业约定一致，底模为 **FLUX.1 [dev]** 族）。英文报告可写：*Candidate images were produced with the ComfyUI workflow **flux1 USO Style Reference** (FLUX.1-based).*
- 结构：每场景子文件夹含  
  - 根目录一张 **`ComfyUI_*.png`**（训练图）  
  - `seed and prompt.txt`（prompt + seed）  
  - `reference photo\` 内两张官图参考（**未纳入训练集**）

- **筛选流程（可写进 Method / Dataset）：** 每个场景会先通过生成管线得到 **二十张以上** 候选图，再经 **人工筛选** 保留 **一张** 作为该场景最终训练图（共 28 场景 → 28 张训练图）。英文报告可简述为：*For each scene, we generated over twenty candidates and manually selected one image for the training set.*

### 4.2 导入后规范

- 训练图目录：`lora_model\data\train\images\`
- Caption 目录：`lora_model\data\train\captions\`
- 数量：**28** 对（图 + `.txt`）
- 命名：`jpfantasy_style_0001` … `jpfantasy_style_0028`（扩展名均为 `.png`）
- 子文件夹排序：按文件夹名 **Unicode 排序** 编号（与脚本 `import_uso_dataset.py` 一致）

### 4.3 Caption 流程（可写进方法）

1. **首版**：从 `seed and prompt.txt` 提取 `prompt：` 与 `seed：` 之间正文，全文保留；若无 `jpfantasy_style` 则前缀 **`jpfantasy_style, `**；**seed 不写入 caption**。
2. **压缩版（当前）**：统一缩短为「触发词 + 主体/场景要点 + 少量画风词」，脚本：`lora_model\scripts\compress_captions.py`。

---

## 5. Training Configuration

### 5.1 Ostris 可执行配置（以 `run.py` 为准）

路径：`F:\AI_tool\ai-toolkit\config\`

| 阶段 | 文件 | 要点 |
|------|------|------|
| Stage A (main usable run) | `train_lora_jpfantasy_stageA.yaml` | `steps: 600`, `save_every: 20`, low-VRAM settings, trigger token `jpfantasy_style` |
| Stage B (optional extension) | `train_lora_jpfantasy_stageB.yaml` | higher-step extension config (optional, not required for baseline report) |

**笔记本若卡在 0/600、未到 step 1：** 多为 **首步训练显存/算力压力**（非采样）。本项目已用低显存组合并以 `resolution: [512]` 跑通 Stage A；若仍报错，可删除本次训练输出目录下 **latent 缓存** 后重跑。

- `model.name_or_path`: `black-forest-labs/FLUX.1-dev`
- `datasets[0].folder_path`: `F:/Cursor_project/ComfyUI_Project/lora_model/data/train/images`
- `training_folder`: `F:/Cursor_project/ComfyUI_Project/lora_model/outputs`
- 示例中常见项：`network linear 16 / linear_alpha 16`，`optimizer adamw8bit`，`lr` Stage A `1e-4`、Stage B `8e-5`，`noise_scheduler: flowmatch`，`dtype: bf16`，`quantize: true` 等（**以实际 yaml 为准抄表**）。

**启动命令（在 `ai-toolkit` venv 下）：**

```powershell
cd F:\AI_tool\ai-toolkit
.\venv\Scripts\Activate.ps1
python run.py config/train_lora_jpfantasy_stageA.yaml
```

### 5.2 项目内映射模板（通用 YAML，供文档说明）

- `lora_model\configs\dataset.yaml`、`train.stageA.yaml`、`train.stageB.yaml`：语义与上对齐，**实际训练以 `F:\AI_tool\ai-toolkit\config\` 下为准**。

### 5.3 流程说明文档

- 开训步骤与排错：`lora_model\RUNBOOK.md`
- 前置清单：`lora_model\LORA_PREP_CHECKLIST.md`

---

## 6. Inference and Comparison Experiments

### 6.0 Training Execution Summary

- **Stage A 已完整跑通**，训练日志：`lora_model\outputs\stageA_bg_run.log`（约 2 小时）。
- **报告主用 LoRA（默认）：** `lora_model\outputs\jpfantasy_style_stageA\jpfantasy_style_stageA.safetensors`。
- 目录中仍保留最近 step 盘（轮转后）：`_000000500`、`_000000520`、`_000000540`、`_000000560`、`_000000580`。
- `optimizer.pt` 仅用于续训；ComfyUI 推理不需要加载。
- Stage A is sufficient as the baseline experiment source under constrained hardware/time conditions.

**计划写入报告的对比：**

| 实验轴 | 设置 |
|--------|------|
| LoRA 开关 | 无 LoRA vs 有 LoRA |
| LoRA 强度 | `0 / 0.6 / 0.8 / 1.0`（ComfyUI Load LoRA） |
| Prompt 复杂度 | 3–4 档：极简 → 长文本（固定底模下） |

**实验记录与复现（已与出图同步，2026-04-14）：**

- [x] 选用 checkpoint 文件名 / step：`jpfantasy_style_stageA.safetensors`（最终盘；可与 `_000000580` 做补充对比）  
- [x] **固定评估 prompt 列表、clip_l/t5xxl、各子组 seed、强度档位与主观观察：** 以仓库内 **`ComfyUI_Project\outputs\compare\PROMPTS_COMPARE_LOG.md`** 为**唯一权威沟通稿**（A/B/C 各组、`A_lora_on_off`、`B_strength`、`C_prompt_complexity` 路径与命名规则均在该文件中维护）。撰写英文正文时从该 log 摘取 prompt 与参数，避免与聊天记录不一致。  
- [x] **固定 seed：** 同上，已按归档文件名写入 `PROMPTS_COMPARE_LOG.md`（A1–A4、B1–B3、C1–C2 等；**不再**以 Ostris `sample.prompts` 或旧备忘 `20260407` 为出图准绳，除非刻意复现实验）。  
- [ ] **附录图编号与正文引用对应表：** 留待 **PDF 排版定稿** 时编制（建议附录图注英文，编号与正文 `Figure A1` / `Appendix Fig. B` 等一致即可）；素材文件已齐，无需再跑图。  

---

## 7. Report Coverage Reminder

正文英文需覆盖作业硬性三点：

1. 生成图：风格、艺术性、美感、真实感、观感等维度对比。  
2. Prompt：简单到长文本多档对比。  
3. 不足与展望：工具/模型局限与近期期望。

附录：全部 Gen.AI 图；图注建议英文。

---

## 8. Reproducibility Scripts

| 脚本 | 作用 |
|------|------|
| `lora_model\scripts\import_uso_dataset.py` | 从 USO 文件夹导入 28 对图+caption |
| `lora_model\scripts\compress_captions.py` | 批量压缩 caption |

---

## 8.1 基线工作流资料（ComfyUI 对比图复现）

- 工作流截图（当前连接状态）：`outputs\compare\_workflow_baseline\workflow_baseline_connected.png`
- 参数快照（中文沟通稿）：`outputs\compare\_workflow_baseline\workflow_baseline_params.md`
- 用途：作为后续 `A_lora_on_off`、`B_strength`、`C_prompt_complexity` 三组实验的统一基线；最终定稿后再转英文表达。

---

## 9. Suggested Work Order

1. 若训练未跑：按 `RUNBOOK.md` 先 Stage A 再 Stage B。  
2. 用 ComfyUI 同一 FLUX.1 dev + LoRA 出对比图。  
3. **对比实验参数与 prompt：** 以 **`outputs\compare\PROMPTS_COMPARE_LOG.md`** 为准；§6 上表已同步勾选。  
4. 英文撰写时从 **§1–§6 与本节 log 指向** 摘事实；附录编号在排版 PDF 时完成。

---

*This public note is maintained as a technical source summary for report writing.*
