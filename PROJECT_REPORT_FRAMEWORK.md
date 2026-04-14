# Public Report Framework

> This file provides a portfolio-safe writing framework for the project report.

**用途：** 作为 PDF 报告的主干目录与要点清单。各节展开为完整英文正文。**所有生成图像放在文末附录**；附录页数**不计入**正文至少 6 页的要求。

---

## Title Page

- Project title, author, and date.
- Recommended title style:
  **"ComfyUI Advanced Workflow: Custom LoRA Training (FLUX.1-dev)"**

---

## Abstract / Executive Summary

- One concise paragraph: goal, method, key findings, and future direction.

---

## 1. 引言（Introduction）

- 动机：为何选用开源 ComfyUI、为何用 LoRA（可控性、可复现、相对全量微调更省资源等）。
- 报告范围：所用**底模**、LoRA 目标（画风 / 角色或物体）、你展示的高级内容（LoRA 训练 + 推理；若另有工作流需与老师确认后写入）。
- 后文结构：简要预告第 2–7 节与附录。

---

## 2. 背景与环境（Background and Setup）

### 2.1 软硬件环境

- GPU / 显存、操作系统；若有关键安装方式（便携版、虚拟环境等）可简述。
- ComfyUI 版本（或 commit）、实际用到的扩展 / 自定义节点（只写真实用过的）。

### 2.2 生成式图像底模（Base models）

- **本项目定案（见 `ASSIGNMENT_MEMORY.md`）：** 仅使用 **FLUX.1 [dev]** 作为唯一底模；**已与教授确认**无需像 Scenario 2 那样引入第二种 checkpoint 做对照。
- 写明：模型全名 / 变体（dev 与 schnell 勿混用）、权重来源（如 `black-forest-labs/FLUX.1-dev`）、ComfyUI 采用分包或 fp8 单文件、**非商业许可**等；强调 **Ostris 训练与 ComfyUI 推理为同一 FLUX.1 变体**。

### 2.3 LoRA 训练工具链

- 所用工具：**Ostris AI Toolkit**（教授推荐）及选用理由。
- 数据集：张数、裁剪方式、打标签 / 写 caption 策略、数据清洗（重复图、离群样本）。
- **超参数表**：network dim/rank、学习率、步数/epoch、batch size、分辨率、优化器、repeats 等。

### 2.4 ComfyUI 推理工作流

- 节点图简述：加载模型、LoRA、CLIP、KSampler、VAE 解码；若有高清修复、ControlNet 等一并说明。
- 可附一张简化流程图或导出工作流截图（若占正文篇幅可放附录）。

---

## 3. 训练过程与个人经验（Training Experience）

- 时间线与迭代：第一次失败跑通 → 你改了什么。
- 观察：过拟合/欠拟合迹象、对 caption 的敏感度、显存瓶颈。
- 可复现性：固定 seed、保存配置或 workflow JSON 的做法。

---

## 4. 生成图像 — 对比分析（作业要求：风格、艺术、美感、真实感、观感）

### 4.1 对比维度

正文用**表格**概括，用**成对图像**支撑（图放**附录**，正文用 Figure A1、A2…引用）。

| 维度     | 可写内容（示例） |
|----------|------------------|
| 风格     | 色板、线条/笔触、质感、类型片一致性 |
| 艺术性   | 构图、视觉焦点、新意（避免断言「客观艺术高低」） |
| 美感     | 和谐度、对比与留白、杂乱度、是否符合目标受众 |
| 真实感   | 解剖/比例、材质、光照合理性、违和与伪影 |
| 画面质量 | 清晰度、整体一致性、图中文字（若有）、手/脸等难点 |

### 4.2 底模 vs 加 LoRA

- 在**相同 prompt、尽量相同 seed** 下：**无 LoRA** vs **多档 LoRA 强度**（如 0.6、0.8、1.0）。
- 讨论取舍：身份/风格「锁死」程度与灵活度、风格污染、背景是否被带偏等。

### 4.3 其他对比（可选）

- **单底模路线下本节可省略**，或改为：**同一底模下不同 seed / 不同采样步数** 的稳定性讨论；**失败案例**（崩脸、糊细节、长 prompt 丢条件等）仍建议保留。

---

## 5. Prompt 复杂度研究（作业要求：从简单到长文本）

定义 **3–4 个 prompt 档位**，例如：

1. **档位 1 — 极简：** 主体 + 一个属性（例：「a red sports car, studio lighting」）。
2. **档位 2 — 中等：** 加环境、情绪、机位/镜头感。
3. **档位 3 — 丰富：** 材质、时段、镜头、调色等。
4. **档位 4 — 长 prompt：** 在档位 3 基础上加 negative prompt、构图约束、风格词等。

每一档建议说明：

- 各对比维度下**一张代表性出图**（附录引用）。
- 模型是否遵守**全部**子句？prompt 变长时**最先被忽略**的是哪类描述？
- 与 LoRA 的交互：长 prompt 是**压制**还是**加强** LoRA 效果？

---

## 6. Limitations and Future Work

### 6.1 当前欠缺什么

- ComfyUI：节点图复杂、文档分散、排错成本、环境迁移等。
- 模型：一致性、细部、图中文字、偏见与许可等。
- LoRA 训练：数据效率、评价指标、自动化质量门槛等。

### 6.2 希望近期出现的发展

- 写具体一点：例如更轻量的消费级显卡训练方案、界面内 LoRA 强度曲线、更顺滑的 inpaint + 重打光整合等。

---

## 7. 结论（Conclusion）

- 总结你会**继续沿用**哪套工具/流程及原因（与学习曲线、控制力、出图质量挂钩）。
- 三条要点：「若重做本项目我会如何改进」。

---

## 参考文献（References）

- 所用模型、LoRA 工具、论文（如 SD、LoRA 原文）、ComfyUI 文档、参考教程。按课程要求选用 **APA / IEEE** 等格式。

---

## 附录 A — 生成图像（作业要求：全部 Gen.AI 图放附录）

**要求：** 所有生成图像集中在此；**每张编号**。

单张图建议标注：

- **图 A#：** 简短英文说明（与 PDF 正文语言一致）
- **Prompt 档位：**（1–4）
- **底模名称**
- **LoRA：** 有/无；强度
- **Seed / 备注：**（可选）
- **图像**

可按实验分组，例如：

- A1–A4：底模 vs LoRA 强度扫描  
- A5–A12：各 **Prompt 档位**（单一 **FLUX.1 [dev]** 底模；可按需增减张数）  
- A13 起：失败案例与有趣离群样本  

---

## 附录 B — 补充材料（可选）

- 工作流导出（JSON）、额外训练曲线、完整 prompt 列表、扩展超参表等。

---

## Pre-submission Checklist

- [ ] PDF；正文 **≥ 6 页**（12 磅、A4），**不含附录**。
- [ ] 标题标明项目主题与具体题目（如 ComfyUI + custom LoRA）。
- [ ] 覆盖作业三点：**（1）** 视觉维度对比；**（2）** 简单到长 prompt；**（3）** 不足与未来展望。
- [ ] 所有生成图均在**附录**。
- [ ] Main body and appendix are complete and internally consistent.

---

*框架文档结束。*
