# 对比图 Prompt 记录（中文沟通稿）

> 路径：`F:\Cursor_project\ComfyUI_Project\outputs\compare\`  
> 用途：统一记录 A/B/C 各组生成图所用 prompt 与关键参数，便于后续写报告引用。  
> 约定：最终英文报告定稿前，记录与沟通保持中文。

---

## 0. 全局固定参数（当前）

- 底模：`FLUX.1-dev`（ComfyUI 预设工作流）
- LoRA：`jpfantasy_style_stageA.safetensors`
- LoRA clip strength：`1.0`（A/B 与 C 若未另注则沿用）
- LoRA model strength：**A 组**与 **B 组（当前归档）**对比档位均为 `0.0 / 0.6 / 0.8 / 1.0`；**C 组（当前归档）**为 `0.0 / 1.0`（见 §3）
- 分辨率：`1024 x 1024`
- 采样参数：`steps=20`, `sampler=euler`, `scheduler=simple`, `cfg=1.0`, `denoise=1.00`
- seed：每个实验子组内固定（具体值写在该子组记录中）
- 说明：**A 组**为「多题材 × 多档 model strength」；**B 组**以「短 / 中 / 长 prompt」为主对照，**实际归档**见 `B_strength` 文件名（含多档 model strength，与初稿「仅 0.8」可同时保留：报告可侧重 `0.8` 或全四档）；**C 组**为难例与局限讨论（强度见 C 节）。各组以对应小节为准。
- **跨组现象（供报告谨慎引用）：**仅为 **各子组固定 seed、单轮出图、每档各 1 张** 下的**主观对照**，**不作普适或统计结论**。在本轮归档印象里：**`0.0`** 较少出现整体崩坏；**`1.0`** 风格强化后多数仍可用；**`0.6` / `0.8`** 在部分子组出现手足等问题（见下表）。**未**做多样 seed / 多样本复现，外推须谨慎。单人体结构类可引用下表及 **B3**；**多人体 / 强动态**见 **C1**；**多招牌字形与反射**见 **C2**（§3 加难版）。

### 明显问题样张索引（本轮归档 · 用户主观标注 · 附录引用）

以下文件位于 `outputs\compare\A_lora_on_off\`、`B_strength\` 或 `C_prompt_complexity\`，命名形如 `A3, <seed>, <model>, <clip>.png`。

> **范围：**每档 **仅 1 张**、**未复现**；表中为单次结果后的主观判定，报告宜写为「在本次实验中观察到……」。

| 子组 | model strength | 明显问题 | 文件名 |
|------|----------------|----------|--------|
| B1 | `0.6` | 手指 | `B1, 971947498959982, 0.6, 1.0.png` |
| B1 | `1.0` | 手指 | `B1, 971947498959982, 1.0, 1.0.png` |
| B2 | `0.6` | 手指 | `B2, 971947498959982, 0.6, 1.0.png` |
| B2 | `0.8` | 手指 | `B2, 971947498959982, 0.8, 1.0.png` |
| B2 | `1.0` | 手指 | `B2, 971947498959982, 1.0, 1.0.png` |
| A3 | `0.6` | 手部 | `A3, 506744058271183, 0.6, 1.0.png` |
| A4 | `0.8` | 足部 | `A4, 298084320241887, 0.8, 1.0.png` |
| C1 | `1.0` | 手部明显结构/数量问题 | `C1, 572738612206139, 1.0, 1.0.png` |
| C2 | `1.0` | 字形变形；观感近似「奇幻美术字」而非标准可读英文 | `C2, 1082998128340460, 1.0, 1.0.png` |

> **注（C2）：**上表**不**等同于「拼写失败」：变形在视觉上**可能反而贴合 fantasy 装饰字**；报告可写 **「忠实拼写 ↔ 风格化字形」的取舍**，与「乱码不可读」区分。  
> **注：** **B3（长 prompt）** 未列入上表——在 **同一 seed、本轮各档各 1 张** 的主观检查中**未**与上表同等级的明显问题；与 B1/B2 的差异**仅限本次短/中/长对照**，详见 **B3** 小节观察。

---

## 1. A组（风格/观感对比）

### A1（角色主图）

- Prompt ID：`A1_prompt_hero`
- clip_l：
  - `jpfantasy_style, fantasy heroine, ornate armor, sunset rim light, cinematic, clean lineart`
- t5xxl：
  - `A full-body fantasy heroine standing on an ancient stone bridge at sunset. She wears intricate silver-blue armor with layered fabric and elegant ornaments. Warm rim light outlines her silhouette, while a soft magical atmosphere fills the background with distant towers and floating particles. The composition is cinematic, visually balanced, and highly detailed, with clean linework and coherent anatomy.`
- 对比档位：
  - model strength：`0.0 / 0.6 / 0.8 / 1.0`
  - clip strength：`1.0`（固定）
- 本轮 seed（用户实测）：`781069391428044`
- 当前观察（中文）：
  - `0.0` 相比 LoRA 档位更偏底模观感；
  - `0.6` 起风格变化明显；
  - `0.8` 与 `1.0` 在风格上接近，但并排对比可见 `1.0` 更亮、体积感更强。

### A2（场景主图）

- Prompt ID：`A2_prompt_city`
- clip_l：
  - `jpfantasy_style, fantasy city street, dusk, lanterns, atmospheric fog, cinematic composition`
- t5xxl：
  - `A magical fantasy city street at dusk, illuminated by floating lanterns and soft ambient light. Gothic architecture, layered depth, and subtle fog create a rich atmosphere. The scene should feel artistic and visually coherent, with strong composition, clear subject-background separation, and refined details in buildings, paving stones, and lighting transitions.`
- 对比档位（建议与 A1 一致）：
  - model strength：`0.0 / 0.6 / 0.8 / 1.0`
  - clip strength：`1.0`（固定）
- 本轮 seed（来自归档文件名）：`558036329660600`
- 观察（中文）：在本轮 **同 seed、各档各 1 张** 的主观对比中，**`0.0`** 整体更偏 **写实摄影感**：建筑与街面 **棱角更分明**，灯笼/灯带的 **排布更整齐**、秩序感强。**`1.0`** 整体更偏 **奇幻插画氛围**：远景常呈现 **层层叠叠、数量感更多的屋宇与光点**，街景 **更灯火通明、更「热闹奇幻」**；**`0.6`～`0.8`** 介于两者之间，远景层次与灯光密度随强度递增而渐强。**未复现**，报告宜写为「在本次 A2 归档中的观感」。

### A3（港口法师 / 月下二次元）

- Prompt ID：`A3_prompt_mage_harbor`
- clip_l：
  - `jpfantasy_style, anime fantasy mage, moonlit harbor, ornate robe, glowing magic circle, clean lineart, cinematic`
- t5xxl：
  - `A full-body anime fantasy mage standing on an ancient stone pier in a moonlit harbor, wearing an ornate layered robe with silver-blue details and subtle armor ornaments. A glowing magic circle forms near her hand, casting soft blue light on her sleeves and the wet stones. The background shows fantasy ships, distant towers, and mist over the water. The image should emphasize stylized anime-fantasy aesthetics, clean linework, coherent anatomy, and a cinematic composition with clear subject focus.`
- 对比档位：
  - model strength：`0.0 / 0.6 / 0.8 / 1.0`
  - clip strength：`1.0`（固定）
- 本轮 seed（来自归档文件名）：`506744058271183`
- 当前观察（中文）：
  - **`0.6`**（该档本轮 1 张）：手部主观判定为明显结构/形态问题（见 §0「明显问题样张索引」；未复现）。

### A4（祭典台阶巫女 · 水粉水彩插画向）

- Prompt ID：`A4_prompt_miko_gouache`
- clip_l：
  - `jpfantasy_style, shrine maiden on festival stone steps, lanterns and torii, golden bokeh, cherry petals with snow, slice-of-life fantasy atmosphere, gouache and watercolor fantasy illustration, soft brush texture, poetic muted palette, gentle diffused light`
- t5xxl：
  - `jpfantasy_style. A shrine maiden kneeling in prayer on wide festival stone steps at dusk, hands pressed together, red-white miko outfit with long detached sleeves. Paper lanterns overhead, a torii softly blurred in the background, warm golden bokeh, cherry petals drifting with light snow on the steps. Gouache-and-watercolor fantasy illustration with visible soft brush texture, matte pigment layering, and subtle paper grain; gentle diffused lantern light and a poetic muted palette. Painterly illustrated look. Slice-of-life fantasy atmosphere, coherent anatomy, delicate fabric folds.`
- 对比档位：
  - model strength：`0.0 / 0.6 / 0.8 / 1.0`
  - clip strength：`1.0`（固定）
- 本轮 seed（来自归档文件名）：`298084320241887`
- 当前观察（中文）：四档图片已生成并保存；`0.0` 侧刻意用水彩水粉插画词与 A3 的二次元奥术风区分；`1.0` 上观察 LoRA 与训练分布对齐程度（caption 近 `jpfantasy_style_0008`）。**`0.8`**（该档本轮 1 张）：足部主观判定为明显异常（见 §0「明显问题样张索引」；未复现）。

---

## 2. B组（Prompt 长度：短 → 中 → 长）

> **目的：**满足作业「从简单到长文本 prompt」的对照；**主变量**为 prompt 信息量（B1 短 / B2 中 / B3 长）。  
> **实际归档（`B_strength`）命名：**`B#, <seed>, <model_strength>, <clip_strength>.png`。当前 **B1 / B2 / B3 共用 seed `971947498959982`**，且 **各自均含** model strength **`0.0 / 0.6 / 0.8 / 1.0`**、clip **`1.0`** 四张（与 A 组命名习惯一致）。若报告正文只想强调「仅变 prompt 长度」，可选用每行 **`…, 0.8, 1.0.png`** 作主图，其余三档作补充对照。  
> **clip_l 字符量：**刻意满足 **B1 < B2 < B3**（与「短→中→长」一致）。若 CLIP-L 截断，溢出句可挪到 `t5xxl`。  
> **本轮跨 B1–B3 的主观印象（谨慎表述）：**在 **同 seed**、仅变 prompt 长度时，**prompt 越长，同一子组内**（`0.0`～`1.0` 四档）**四张图整体越「像彼此」**（构图与角色气质更接近）；**短 prompt** 下四档之间的观感跨度相对更大。可为报告讨论点之一；**未**做量化指标或多样 seed 复现，**不宜**外推为普遍规律。

### B1（短）

- Prompt ID：`B1_prompt_short_heroine`
- clip_l：
  - `jpfantasy_style, anime fantasy heroine`
- t5xxl（刻意保持短，与 B2/B3 拉开差距；若工作流允许更空可再缩短）：
  - `An anime fantasy heroine, full-body.`
- 对比档位（与文件名一致）：model `0.0 / 0.6 / 0.8 / 1.0`，clip `1.0`
- 本轮 seed（来自 `B_strength` 文件名）：`971947498959982`（B2、B3 同）
- 观察（中文）：**`0.6`、`1.0`**（各该档本轮 1 张）手指主观判定为明显问题（见 §0「明显问题样张索引」；未复现）。

### B2（中）

- Prompt ID：`B2_prompt_medium_heroine`
- clip_l：
  - `jpfantasy_style, anime fantasy heroine, detailed costume, soft rim light, fantasy city background, clean lineart, high quality`
- t5xxl（与 clip_l 同档信息量的中等扩写，可按听感微调）：
  - `A full-body anime fantasy heroine with detailed costume, soft rim light, fantasy city background, clean lineart, high image quality.`
- 对比档位（与文件名一致）：model `0.0 / 0.6 / 0.8 / 1.0`，clip `1.0`
- 本轮 seed（来自 `B_strength` 文件名）：`971947498959982`（同 B1）
- 观察（中文）：**`0.6`、`0.8`、`1.0`**（各该档本轮 1 张）手指主观判定为明显问题（见 §0「明显问题样张索引」；未复现）。

### B3（长）

- Prompt ID：`B3_prompt_long_heroine`
- clip_l（**完整长稿**，信息量明显长于 B2 的 `clip_l`）：
  - `jpfantasy_style, a full-body anime fantasy heroine standing in a medieval magic city at dusk, intricate layered costume with metallic ornaments and fabric folds, glowing lanterns and atmospheric fog in the background, cinematic wide shot, balanced warm and cool lighting, clean lineart, coherent anatomy, rich texture details, visually appealing composition, high image quality`
- t5xxl（与 `clip_l` **同句**，便于 FLUX 双编码器一致理解；若你习惯长句只写 t5、clip 略短，以实际出图栏为准，但本 log 以「B3 两栏均承载长稿」记录）：
  - `jpfantasy_style, a full-body anime fantasy heroine standing in a medieval magic city at dusk, intricate layered costume with metallic ornaments and fabric folds, glowing lanterns and atmospheric fog in the background, cinematic wide shot, balanced warm and cool lighting, clean lineart, coherent anatomy, rich texture details, visually appealing composition, high image quality`
- 对比档位（与文件名一致）：model `0.0 / 0.6 / 0.8 / 1.0`，clip `1.0`
- 本轮 seed（来自 `B_strength` 文件名）：`971947498959982`（同 B1）
- 观察（中文）：在 **本轮同一 seed、每档各 1 张** 的主观对比中，**B3** 四档**未**出现与 B1/B2 相当的明显手指等硬伤。**可能**与长 prompt 约束更细有关，**仅为推测**。另见 B 组总述：**长 prompt 下四档彼此更相似**（与 B1/B2 相比），或为「条件写满后、强度带来的构图漂移变小」的**单次观察**。**未**做多 seed 或重复生成，**不宜**表述为普遍规律；报告建议限定为「在本次 B1/B2/B3 短中长对照中」并说明**仅一版对比**。

---

## 3. C组（「不足与展望」用失败 / 难例样本）

> **目的：**不是为了好看，而是为报告 **3. 不足与展望** 提供可分析素材（多体交互、可读文字等）。  
> **与 A/B 的分工：**A/B 以单主体或常规场景为主；**C1** 补 **多人 / 强动态**；**C2** 补 **招牌文字与徽章**；与单人体手指问题等**维度不同**。  
> **训练数据预期：**28 张训练图**无「多人同框」**，C1 对 LoRA 为 **OOD**——失败样张仍可支撑「数据覆盖不足 → 泛化局限」；**不必苛求**一次出图成功。  
> **实际归档（`C_prompt_complexity`）命名：**`C#, <seed>, <model_strength>, <clip_strength>.png`。当前 **C1、C2 各含** model **`0.0` 与 `1.0`** 两档、clip **`1.0`**（与文件名一致）。**出图策略：**仍可用**换 seed** 补跑更多候选，但 log 以**已落盘文件名**为准。  
> **保守表述：**未多样 seed 系统复现则勿外推为统计结论。  
> **归档建议：**`outputs\compare\C_prompt_complexity\` 或 `C_failure_samples\`，附录标注「难例 / 局限讨论」。  
> **C2 修订说明：**初版「单块招牌 + 泛化可读字」易过稳；下表 **C2** 已改为 **夜市多招牌重叠 + 浅景深 + 地面积水倒影 + 蒸汽与人群**，在不逐字锁死拼写的前提下**提高字形/层次/反射**难度，仍可用 **换 seed** 挑典型失败入附录。

### C1（复杂动作 + 多对象）

- Prompt ID：`C1_prompt_combat_multi`
- clip_l：
  - `jpfantasy_style, two fantasy characters in dynamic combat, crossing swords mid-air, complex poses, motion blur, detailed armor, dramatic lighting, crowded background, ultra detailed`
- t5xxl：
  - `Two fantasy characters in dynamic combat, crossing swords mid-air, complex poses, motion blur, detailed armor, dramatic lighting, crowded background, ultra detailed.`
- 对比档位（与 `C_prompt_complexity` 文件名一致）：model `0.0 / 1.0`，clip `1.0`
- 本轮 seed（来自归档文件名）：`572738612206139`（**与 C2 不同**）
- 归档示例：`C1, 572738612206139, 0.0, 1.0.png`；`C1, 572738612206139, 1.0, 1.0.png`
- 预期问题（写报告用）：人数/身份混淆、肢体交接与手部、运动模糊与结构清晰度冲突、遮挡与构图糊等。
- 观察（中文）：在本轮 **同 seed、各档各 1 张** 的主观对比中，**`1.0`** 档**手部**主观判定为**明显**结构/数量问题（见 §0 表及 `C1, 572738612206139, 1.0, 1.0.png`）；**`0.0`** 未单独列入表，可附录并排作对照。**未复现。**
- **说明：**训练集无多人样本时，高 LoRA 权重**不一定**改善多体结构；**换 seed 挑典型失败或相对可看图** 即可支撑局限讨论，不苛求「完美双人打斗」。

### C2（文字与徽章 · 夜市多招牌加难版）

- Prompt ID：`C2_prompt_sign_night_market`（由初版 `C2_prompt_sign_text` **加难**；初版单招牌易过稳。）
- clip_l：
  - `jpfantasy_style, cramped fantasy night market alley, three overlapping hanging shop signs different depths, painted long fantasy shop titles, brass crests filigree, steam lantern bokeh, wet cobblestones mirror brightest glyphs, shallow depth of field, crowded silhouettes, ultra detailed`
- t5xxl：
  - `jpfantasy_style. A steep upward camera in a cramped fantasy night-market alley: three overlapping carved wooden hanging signs at different depths, each with a long invented English-style painted title and small brass emblem with fine filigree, signs partly occluding each other. Warm food-cart steam, orange lantern bokeh and cool moonlight mix, wet cobblestones mirror the brightest lettering layer, shallow depth of field so not all boards stay sharp at once, busy crowd silhouettes below, rainy haze, ultra detailed. Prefer legible letter shapes where in focus, but do not require a specific real-world spelling.`
- 对比档位（与 `C_prompt_complexity` 文件名一致）：model `0.0 / 1.0`，clip `1.0`
- 本轮 seed（来自归档文件名）：`1082998128340460`（**与 C1 不同**）
- 归档示例：`C2, 1082998128340460, 0.0, 1.0.png`；`C2, 1082998128340460, 1.0, 1.0.png`
- 预期问题（写报告用）：多块招牌**互相遮挡**、景深外文字发糊、**倒影与实体字形不一致**、细金线与雨雾糊、人群与招牌抢视觉焦点、LoRA 线描**切碎**笔画等。
- 观察（中文）：**`1.0`** 档招牌上的字主观上**有变形**，但观感**更接近奇幻设定里的装饰美术字**，而非完全不可辨的乱码；与「严格可读英文拼写」仍有差距，报告可讨论 **LoRA 强化风格时对字形忠实度的影响**（与 C1 手部类「硬伤」语气区分）。见 `C2, 1082998128340460, 1.0, 1.0.png`；**`0.0`** 可附录对照。**未复现。**
- **说明：**加难后仍**不**锁死每个字母，避免回到「过细 prompt」；若仍偏稳，可再略增「第四块竖窄条幅」或略加强 `crowded` / `steam`（自行小改并记入本行）。

---

## 4. 追加规则（后续扩展）

- 若新增任意 A/B/C 子组，按现有最大编号顺延（如 `A5`、`B4`、`C3`）。
- 每新增一组至少记录：`Prompt ID`、`clip_l`、`t5xxl`、`seed`、`强度设置`、`一句观察`。
- 若实验中调整固定参数（如 cfg/steps/sampler），必须在该组下单独注明。
