# 《AI for Astronomers》Part I/II 编辑规格书 V2

> 适用范围：`AIforAstronomers-Project` 教材 Part I / Part II。  
> 文件性质：从“评审意见”升级为“可执行编辑规格书”；本文件是 Part I/II 后续正文、notebook、模板和评分标准修改的 authoritative spec。  
> 核心目标：把 Part I/II 改造成进入 Part III 机器学习之前的**工作流与数据契约闸门**，而不是补全成 Linux、Git、Python、FITS 或天文数据处理百科。

---

## 0. V2 总原则

### 0.1 一句话编辑准则

> **Part I/II 的修改不以增加知识点为目标，而以降低复查成本为目标。每章只保留足够学生完成一个 Evidence Record 的概念、操作和判断标准。**

这句话应作为后续改稿的约束。看到一个知识点“有用”，不等于它应该进入正文主线。只有当它直接帮助学生完成以下任务时，才应进入主线：

1. 找到输入；
2. 重跑操作；
3. 找到输出；
4. 解释检查；
5. 写清限制；
6. 安全交接到 Part III。

后续改稿时应先问：它是否帮助学生完成 Evidence Record / Data Card / Dataset Contract？如果不能，就放到提示框、附录或 notebook 注释里，而不是进入正文主线。

### 0.2 Part I/II 的功能定位

Part I/II 不应被写成“基础知识大全”。它们在整本教材中的功能是：

- **Part I：把学生从会写代码/会敲命令，带到能组织一个可复查的小型科研项目。**
- **Part II：把学生从能打开数据文件，带到能把天文/物理数据组织成可复查、可建模、可解释的科研对象。**

因此，Part I/II 可以快速读，但不能随意跳过。它们是 Part III 机器学习之前的最低工作流和数据契约训练。

### 0.3 三层文件体系：不要混用

V2 的核心架构是三层文件体系：

| 层级 | 文件 | 回答的问题 | 使用时机 |
|---|---|---|---|
| 操作层 | Evidence Record | 我做了什么？ | 每次关键操作、图表、分析结果之后 |
| 数据层 | Data Card v0.1 | 这个数据集是什么？ | 一个数据集/样本集合形成之后 |
| 建模交接层 | Part III Dataset Contract | 这个数据集如何安全进入模型？ | 进入机器学习训练/评估之前 |

一句话定义：

> **Evidence Record 记录“我做了什么”；Data Card 记录“这个数据集是什么”；Dataset Contract 记录“这个数据集如何安全进入模型”。**

这三者不能混在一起。否则学生会不知道什么时候写操作记录，什么时候写数据说明，什么时候写机器学习交接文件。

---

## 1. 全局模板规范

## 1.1 Evidence Record 母模板

所有章节共用一个 Evidence Record 母模板。每章只增加少量 chapter-specific fields，通常 3–5 项；复杂数据章可到 6–9 项，但不得形成独立新模板，避免 record 过载。

```markdown
# Evidence Record

## 1. Input
本次使用了什么数据、文件、代码或环境？

必须能定位：
- 相对路径或文件名；
- 数据来源或生成方式；
- 关键脚本/notebook 名称；
- 必要时包含 commit/tag 或版本信息。

## 2. Operation
做了什么处理、运行了什么命令或脚本？

必须能重跑：
- 命令或运行入口；
- 关键参数；
- 随机种子；
- 输出目录。

## 3. Output
生成了什么结果、图表、表格、日志或中间文件？

必须能找到：
- 输出文件路径；
- 图表/表格文件名；
- 结果摘要；
- 生成时间或版本。

## 4. Check
如何检查结果不是路径错误、代码错误、单位错误或偶然结果？

至少写出一种检查：
- 文件大小/行数/header 检查；
- 单位或数量级检查；
- 图表自审；
- 残差/误差/质量标记检查；
- 与 baseline 或已知结果比较。

## 5. Limit
当前结果不能支持什么解释？

必须写清：
- 样本限制；
- 选择效应；
- 误差或质量限制；
- 外推风险；
- 不能得出的科学结论。

## 6. Reuse in ML
如果进入 Part III，它会成为：
- 样本？
- 特征？
- 标签？
- 误差/质量标记？
- 预处理记录？
- 复现证据？
```

### 使用原则

- 每章不再设计完全独立的新 record 模板。
- 每章只在母模板后补 3–5 个专属字段。
- Evidence Record 不是作文，而是最小复查凭据。
- 记录越短越好，但路径、脚本、输出、检查和限制不能缺。

---

## 1.2 Evidence Record Rubric

建议全书 Part I/II 使用统一的轻量评分口径。

```markdown
# Evidence Record Rubric

## Pass
满足以下五点：

1. 输入可定位：别人能找到原始文件、代码或环境入口。
2. 操作可重跑：别人知道运行什么命令、脚本或 notebook。
3. 输出可找到：别人能找到生成的图、表、日志或结果文件。
4. 检查可解释：学生说明了至少一种质量检查或合理性检查。
5. 限制写清楚：学生明确说明当前结果不能支持什么结论。

## Revise
有结果，但缺少以下一项或多项：

- 输入路径不清楚；
- 脚本名或运行命令不清楚；
- 输出文件不可定位；
- 缺少版本/commit/tag/环境信息；
- 检查只写“看起来正常”，没有具体依据；
- 限制写得过泛。

## Fail
只给图、截图、口头解释或 notebook，无法判断：

- 数据从哪里来；
- 代码如何运行；
- 图表如何生成；
- 结果是否经过检查；
- 当前结论有什么边界。
```

### Rubric 的硬判断点

> **路径和版本是否可定位，是 Pass 的硬条件。**

很多学生的记录看似完整，但没有相对路径、脚本名、commit、输出文件名，仍然无法复查。这类记录应判为 Revise，而不是 Pass。

---

## 1.3 Data Card v0.1 模板

Data Card 面向的是一个数据集或样本集合，不是一次操作。

```markdown
# Data Card v0.1

## Dataset
- 名称：
- 来源：
- 许可证/使用限制：
- 版本或获取日期：

## Sample Definition
一行、一个 cutout、一条光谱或一条时间序列代表什么？

## Data Structure
- 表格 / 图像 / 光谱 / 时间序列 / 模拟数据：
- 样本数：
- 主要字段或数组：
- 单位：

## Measurement and Uncertainty
- 主要测量值：
- 不确定度：
- 质量标记：
- 缺失值：

## Selection
- 样本如何筛选？
- 哪些对象被排除？
- 可能有什么选择效应？

## Preprocessing
- 派生量：
- 归一化：
- 重采样：
- 背景扣除：
- mask 或 quality cut：

## Known Limits
这个数据集不能支持什么科学结论？
```

### 使用时机

- 一个微型项目完成后；
- 一个样本集合准备好后；
- Part II synthesis 中；
- 进入 Part III Dataset Contract 之前。

---

## 1.4 Part III Dataset Contract 模板

Dataset Contract 是进入机器学习之前的正式交接文件。

```markdown
# Part III Dataset Contract

## 1. Sample Definition
一行、一个 cutout、一条光谱或一条时间序列代表什么？

## 2. Sample ID
每个样本如何唯一识别？

要求：
- sample_id 不应在预处理中丢失；
- 图像、光谱、时间序列也要有唯一 ID；
- 后续 train/validation/test split 必须能追踪回原始样本。

## 3. Input Features
哪些变量或数组会进入模型？

要求：
- 字段名；
- 单位；
- 派生方式；
- 是否标准化/归一化；
- 是否包含质量标记。

## 4. Target / Label
预测目标或标签从哪里来？

要求：
- 标签来源；
- 标签规则；
- 是否人工标注、目录匹配、物理公式派生或模拟真值；
- 边界样本如何处理。

## 5. Uncertainty / Quality
误差、质量标记、缺失值如何保留？

要求：
- 哪些误差进入模型；
- 哪些只用于筛选；
- 缺失值如何处理；
- 质量差样本是否删除或单独标记。

## 6. Selection
样本经过了哪些筛选？

要求：
- selection cut；
- 排除条件；
- 选择效应；
- 训练集是否代表未来应用数据。

## 7. Preprocessing
做了哪些归一化、重采样、背景扣除或派生变量计算？

要求：
- 预处理顺序；
- 参数；
- 是否只在训练集上 fit scaler；
- 是否存在数据泄漏风险。

## 8. Split Readiness
是否可以安全划分 train / validation / test？

要求：
- 是否有重复对象；
- 是否有同一对象的多次观测；
- 是否有空间、时间、目标类别上的泄漏风险；
- split 单位是样本、对象还是观测。

## 9. Baseline Readiness
是否可以建立非机器学习或简单机器学习 baseline？

要求：
- 规则 baseline；
- 常数/均值 baseline；
- 线性模型 baseline；
- 简单物理模型 baseline。

## 10. Known Limits
这个数据集不能支持什么科学结论？

## Provenance Links
- Data Card:
- Key Evidence Records:
- Code version / tag:
```

### Dataset Contract 的判定标准

如果 Dataset Contract 不能回答以下问题，就不应进入 Part III：

1. 样本是什么？
2. 特征是什么？
3. 标签是什么？
4. 误差/质量信息是否还在？
5. 选择效应是什么？
6. 预处理是否会造成泄漏？
7. 训练/验证/测试如何安全划分？

---

## 2. 每章统一编辑格式

每章只新增两块短内容：章首短卡和章末 Exit Gate。

## 2.1 章首短卡

```markdown
### 本章阅读方式

- 阅读层级：快读 / 必做 / 方向精做
- 最低交付：一个 Evidence Record + 一个可复查 artifact
- 进入 Part III 的作用：说明本章如何影响样本、特征、标签、误差、质量标记、选择效应或复现
```

要求：

- 控制在 100–150 字；
- 不写成新导论；
- 直接告诉学生怎么读、做什么、为什么对后续有用。

## 2.2 章末 Exit Gate

```markdown
### Exit Gate

回答 4 个问题：

1. 输入是什么？
2. 处理过程能不能重跑？
3. 输出支持什么 claim？
4. 当前限制是什么？

最低交付：
- 一个 Evidence Record；
- 一个可复查 artifact，例如脚本、图、表、日志或 notebook。
```

要求：

- Exit Gate 不是新正文；
- 不展开讲道理；
- 不超过 150 字；
- 每章只增加 1 个 special requirement。

---

## 3. Part I 编辑规格

## 3.1 Part I 总定位

Part I 的关键词是：

> **路径、版本、脚本、数据入口、图表证据。**

Part I 不应成为 Linux/Git/Python/FITS/Matplotlib 工具课。它的目标是让学生能够组织一个最小可复查科研项目。

---

## 3.2 Part I 导读

### 章首定位

```markdown
### Part I 阅读方式

Part I 可以快速读，但每章都必须完成最低交付。重点不是掌握最多工具命令，而是让别人能复查你的项目：数据在哪里、代码怎么跑、输出在哪里、结果如何检查、限制是什么。
```

### 需要加入的总说明

```markdown
Part I 的所有章节共用 Evidence Record 母模板。每章只增加少量专属字段。最终这些记录会汇入 Part II 的 Data Card 和 Part III 的 Dataset Contract。
```

### Part I Exit Gate

```markdown
进入 Part II 前，学生必须能够：

1. 用相对路径说明项目结构；
2. 用 Git 定位一次可评分版本；
3. 从命令行重跑一个脚本；
4. 读入一个数据文件并说明字段/header；
5. 生成一张带有 claim 和 limit 的图表。
```

---

## 3.3 Ch01 Unix/Linux 与科研计算环境

### 核心判断

Ch01 当前不需要继续堆命令。它需要的是：

1. 命令分层；
2. 写操作前的安全习惯；
3. 最小脚本运行；
4. 路径、日志、输出文件可定位；
5. 为 Ch04 的 reproducible workflow 铺路。

### 命令深度判断

当前 Linux 内容若已经覆盖路径、目录、查看文件、通配符、重定向、管道、日志、权限、远程、长任务、脚本和归档，则覆盖面已经足够。后续不应加入 `awk` 深度教程、复杂 Bash、HPC 作业系统或服务器管理细节。

### Ch01 分层标准

#### 必须掌握

```text
路径：pwd, ls, cd, mkdir
只读检查：ls -lh, head, tail, cat, wc -l
查找与筛选：grep, find
安全操作：cp, mv，以及理解 rm 风险与预览/备份习惯
重定向：>, >>, 2>, > file 2>&1；&> 作为常见简写了解
管道：|
日志：tee + log file；script 作为可选补充
最小脚本运行：bash run.sh, python script.py
环境入口检查：which python, python --version
```

#### 科研高频补充

```text
du -sh      # 检查目录大小
df -h       # 检查磁盘空间
file        # 检查文件类型
sha256sum   # 检查文件完整性
tar         # 打包结果或小型项目包
tree/find   # 查看项目结构
history     # 回查命令历史
```

#### 只做了解

```text
权限细节：chmod/chown 的深入机制
远程服务器：ssh/scp/rsync 的系统展开
长任务管理：nohup/tmux/screen 的复杂用法
复杂 shell：变量、循环、条件判断、函数
环境变量深入机制：PATH/PYTHONPATH/LD_LIBRARY_PATH 的系统细节
HPC 调度：Slurm/PBS 等
```

注意：复杂 shell 可以了解，但**最小可运行脚本**、`which python`、`python --version`、路径环境检查必须保留为必做，因为它们直接连接 Ch04。

### Ch01 章首短卡

```markdown
### 本章阅读方式

本章快读命令说明，重点完成一次可复查的命令行操作记录。你不需要成为 Linux 专家，但必须能定位项目路径、预览写操作、保存日志、运行最小脚本，并说明输入和输出文件在哪里。
```

### Chapter-specific fields

在 Evidence Record 后补充：

```markdown
## Ch01 Fields
- project root:
- key read-only checks:
- preview before write:
- log file:
- script or command entry:
- python path/version check:
```

### Special requirement

```markdown
Pass 必须包含一次写操作前的 preview，或明确说明本章操作全部为只读。
```

### Ch01 Exit Gate

```markdown
### Exit Gate

1. 我能否从项目根目录定位输入和输出？
2. 我是否在写操作前做了 preview？
3. 我是否保存了关键命令或日志？
4. 我是否能运行一个最小脚本并检查 Python 路径/版本？

最低交付：Evidence Record + 命令日志或最小脚本。
```

---

## 3.4 Ch02 Git 与可复现科研

### 核心判断

Ch02 的目标不是完整 Git 协作，而是让学生能冻结一次可评分科研状态。

### 必须掌握

```text
git status
git diff
git add
git commit
git log
.gitignore
git tag
```

### 课堂了解

```text
branch
merge
remote
conflict
```

### 不宜深入

```text
复杂多人协作流程
pull request 规范
rebase
submodule
CI/CD
```

### Ch02 章首短卡

```markdown
### 本章阅读方式

本章快读 Git 概念，重点学会把一次科研结果冻结到可定位版本。评分重点不是 commit 数量，而是别人能否知道哪个版本生成了哪个图、表或 record。
```

### Chapter-specific fields

```markdown
## Ch02 Fields
- repository root:
- relevant commit:
- tag/checkpoint:
- tracked files:
- ignored files:
- output linked to commit:
```

### Special requirement

```markdown
Pass 必须能指出：哪个 commit 或 tag 生成了哪个输出文件。
```

### Ch02 Exit Gate

```markdown
### Exit Gate

1. 仓库当前状态是否干净？
2. 关键代码和 record 是否已 commit？
3. 是否有可评分 tag 或 commit？
4. 输出文件能否追踪到版本？

最低交付：Evidence Record + git log/status/tag 记录。
```

---

## 3.5 Ch04 库、脚本与 Jupyter

### 核心判断

Ch04 是 Part I 的主桥。它把探索式 notebook 转成可重跑 workflow，直接决定 Part III 的实验是否可复现。

### 必须强调

1. notebook、script、module 的分工；
2. 从 notebook 到 script 的转换；
3. 环境和依赖记录；
4. 参数、随机种子、输出路径；
5. 一键或单命令重跑。

### Ch04 章首短卡

```markdown
### 本章阅读方式

本章需要精读并动手。目标不是多写 Python，而是把探索代码整理成可重跑入口：别人知道用哪个环境、运行哪个脚本、输入在哪里、输出到哪里、随机种子和参数是什么。
```

### Chapter-specific fields

```markdown
## Ch04 Fields
- notebook:
- script entry:
- command to run:
- python version:
- key package versions:
- random seed:
- output directory:
```

### Special requirement

```markdown
Pass 必须包含一个能从命令行运行的脚本入口，而不仅是 notebook。
```

### Ch04 Exit Gate

```markdown
### Exit Gate

1. notebook 和 script 的分工是否清楚？
2. 脚本能否从命令行重跑？
3. 环境、参数、随机种子是否记录？
4. 输出目录是否固定且可定位？

最低交付：Evidence Record + 可运行脚本 + 运行日志。
```

---

## 3.6 Ch06 文件 I/O、FITS 与科学数据入口

### 核心判断

Ch06 只负责“数据入口协议”，不应提前承担完整 FITS/WCS/图像处理任务。WCS、背景、孔径测光应留给 Ch12。

### 必须强调

1. 文件从哪里来；
2. 文件格式是什么；
3. 字段/header 表示什么；
4. 单位是什么；
5. 缺失值和质量标记在哪里；
6. 后续哪些列或数组会被使用。

### Ch06 章首短卡

```markdown
### 本章阅读方式

本章需要精读并动手。目标不是学完所有文件格式，而是建立数据入口契约：一个文件被读入之前，必须知道来源、格式、字段/header、单位、缺失值、质量标记和后续用途。
```

### Chapter-specific fields

```markdown
## Ch06 Fields
- file path:
- data source:
- file format:
- fields/header checked:
- units:
- missing values:
- quality flags:
- columns/arrays used later:
```

### Special requirement

```markdown
Pass 必须说明字段/header、单位、缺失值或质量标记；不能只说“文件可以打开”。
```

### Ch06 Exit Gate

```markdown
### Exit Gate

1. 数据文件来源和路径是否清楚？
2. 字段/header 和单位是否说明？
3. 缺失值或质量标记是否记录？
4. 哪些列/数组会进入后续分析是否明确？

最低交付：Evidence Record + 数据入口检查输出。
```

---

## 3.7 Ch08 可视化与科研图表

### 核心判断

Ch08 不应变成 Matplotlib 技巧章。它应训练学生把图表作为证据：图支持什么 claim、不能支持什么 claim。

### 必须强调

1. 图表类型选择；
2. 坐标、单位、尺度；
3. 样本筛选；
4. 误差或质量标记；
5. claim--evidence--limit。

### Ch08 章首短卡

```markdown
### 本章阅读方式

本章需要精读图表判断部分，绘图 API 可查读。目标是生成一张可作为科学证据的图：变量、单位、样本筛选、尺度、claim 和 limit 都要清楚。
```

### Chapter-specific fields

```markdown
## Ch08 Fields
- figure file:
- plotting script:
- input data:
- axis variables and units:
- sample selection:
- visual encoding:
- claim supported:
- claim not supported:
```

### Special requirement

```markdown
Pass 必须写清图表支持的 claim 和不能支持的 limit。
```

### Ch08 Exit Gate

```markdown
### Exit Gate

1. 图的输入数据和脚本是否可定位？
2. 变量、单位、尺度是否清楚？
3. 图支持的 claim 是否明确？
4. 图不能支持的解释是否写清？

最低交付：Evidence Record + 图文件 + 生成脚本。
```

---

## 4. Part II 编辑规格

## 4.1 Part II 总定位

Part II 的关键词是：

> **对象、单位、误差、处理、选择效应、可建模样本。**

Part II 不应成为完整天文数据处理课。它的任务是让学生知道不同数据类型如何变成机器学习可用、也可科学复查的样本。

---

## 4.2 Part II 选学路径

### 必修

```text
Ch10 科学数据、误差与单位
Ch11 表格数据、星表与 HR 图
Part II synthesis
```

### 所有学生快读

```text
Ch12 天文图像、FITS 与 WCS
Ch13 光谱数据、谱线与红移
Ch14 时间序列、采样与周期信号
Ch15 物理实验、模型拟合与模拟数据
```

### 每位学生至少精做一章

```text
图像/星系/目标检测方向：Ch12
光谱方向：Ch13
时域方向：Ch14
物理实验/模拟方向：Ch15
```

### 选学原则

> **Ch12–15 不是完全选读，而是共同框架快读 + 至少一章方向精做。**

这样可以避免学生只懂自己项目方向，而完全缺乏对其他数据类型进入 ML 前的横向认识。

---

## 4.3 Part II 导读

### 需要加入的说明

```markdown
Part II 的核心任务不是处理完所有天文数据类型，而是学会对任何数据类型追问同一组问题：对象是什么、单位是什么、误差是什么、选择条件是什么、预处理做了什么、进入机器学习时哪些信息不能丢。
```

### Part II 到 Part III 的接口

```markdown
进入 Part III 前，每个数据集必须至少能说明：

- sample_id；
- input features；
- target / label；
- uncertainty / quality flag；
- selection rule；
- preprocessing history；
- excluded cases；
- split readiness。
```

---

## 4.4 Ch10 科学数据、误差与单位

### 核心判断

Ch10 是 Part II 必修核心。它应比其他 Part II 章节更理论化一点，因为它为所有后续数据类型提供共同语言。

### 必须强调

1. 测量值、派生量、模型量的区别；
2. 随机误差和系统误差；
3. 单位检查；
4. 误差传播；
5. 数量级检查；
6. 低信噪比或低质量数据下公式反演的风险。

### Ch10 章首短卡

```markdown
### 本章阅读方式

本章必须精读。后续所有数据处理和机器学习任务都依赖本章：一个数字只有同时带有单位、误差、来源、适用条件和限制，才是科学数据。
```

### Chapter-specific fields

```markdown
## Ch10 Fields
- measured quantity:
- unit:
- uncertainty:
- derived quantity:
- formula used:
- error propagation:
- order-of-magnitude check:
- systematic risk:
```

### Special requirement

```markdown
Pass 必须包含单位检查和至少一种误差/数量级检查。
```

### Ch10 Exit Gate

```markdown
### Exit Gate

1. 原始测量值、单位和误差是否清楚？
2. 派生量公式和适用条件是否写明？
3. 单位或数量级是否检查？
4. 系统误差或公式反演风险是否说明？

最低交付：Evidence Record + 一个测量/派生量检查。
```

---

## 4.5 Ch11 表格数据、星表与 HR 图

### 核心判断

Ch11 是 Part II 的样板章。它最适合展示从原始表格列到派生物理量、再到图表解释和 ML 特征的完整链条。

### 必须强调

1. 星表字段契约；
2. 视差、距离、绝对星等、颜色指数；
3. 筛选条件和选择效应；
4. HR 图结构解释；
5. HR 图不是标签本身；
6. 可进入 ML 的特征来源。

### Ch11 章首短卡

```markdown
### 本章阅读方式

本章必须精读并完成样板项目。目标是从星表字段出发，经过单位、筛选、派生量和图表解释，形成一个可进入机器学习的数据样本说明。
```

### Chapter-specific fields

```markdown
## Ch11 Fields
- catalog/table path:
- source columns:
- units:
- quality cuts:
- derived quantities:
- HR diagram file:
- structures identified:
- selection effects:
- possible ML features:
```

### Special requirement

```markdown
Pass 必须说明筛选条件和选择效应；不能只给 HR 图。
```

### Ch11 Exit Gate

```markdown
### Exit Gate

1. 星表字段、单位和质量筛选是否清楚？
2. 派生量公式是否可复查？
3. HR 图解释是否区分 claim 和 limit？
4. 可进入 ML 的特征和风险是否说明？

最低交付：Evidence Record + HR 图 + Data Card 草稿。
```

---

## 4.6 Ch12 天文图像、FITS 与 WCS

### 核心判断

Ch12 是方向精做章之一。所有学生应快读共同框架，图像/目标检测/星系方向学生应精做。

### 必须强调

1. 显示图像不等于测量图像；
2. FITS header/data/WCS 最小检查；
3. 背景估计；
4. 孔径或 cutout 选择；
5. 图像进入 ML 前的记录。

### Ch12 章首短卡

```markdown
### 本章阅读方式

所有学生快读图像数据共同框架；图像、星系或目标检测方向学生精做。目标不是完整图像处理，而是理解像素如何在 header、WCS、背景、单位和预处理后变成可建模输入。
```

### Chapter-specific fields

```markdown
## Ch12 Fields
- FITS file:
- HDU/header checked:
- image shape:
- pixel scale / WCS:
- background method:
- aperture or cutout setting:
- normalization:
- mask / bad pixels:
- possible ML input shape:
```

### Special requirement

```markdown
Pass 必须说明背景/归一化/cutout 或 aperture 设置中的至少一项；不能只给 imshow 图。
```

### Ch12 Exit Gate

```markdown
### Exit Gate

1. FITS header/data 和图像形状是否检查？
2. 坐标、像素尺度或 WCS 风险是否说明？
3. 背景、cutout、aperture 或归一化是否记录？
4. 图像进入 ML 前会丢失什么信息是否说明？

最低交付：Evidence Record + 图像检查结果或 photometry/cutout 结果。
```

---

## 4.7 Ch13 光谱数据、谱线与红移

### 核心判断

Ch13 是方向精做章之一。所有学生应快读光谱共同框架，光谱方向学生精做。

### 必须强调

1. 波长轴和流量轴的契约；
2. 连续谱处理；
3. 谱线识别；
4. 红移不能只靠一条线；
5. 重采样/归一化/mask 对 ML 的影响。

### Ch13 章首短卡

```markdown
### 本章阅读方式

所有学生快读光谱共同框架；光谱方向学生精做。目标是理解一维数组背后的波长、流量、校准、连续谱、谱线和红移假设，并记录其进入机器学习前的预处理历史。
```

### Chapter-specific fields

```markdown
## Ch13 Fields
- spectrum file:
- wavelength unit/grid:
- flux unit:
- calibration status:
- continuum treatment:
- line candidates:
- redshift estimate:
- S/N or quality flag:
- resampling/normalization:
```

### Special requirement

```markdown
Pass 必须说明红移或谱线判断的质量依据；不能只标出一个峰。
```

### Ch13 Exit Gate

```markdown
### Exit Gate

1. 波长和流量单位是否清楚？
2. 连续谱、归一化或重采样是否记录？
3. 谱线/红移判断是否有质量依据？
4. 光谱进入 ML 前的预处理风险是否说明？

最低交付：Evidence Record + 光谱图或红移/谱线记录。
```

---

## 4.8 Ch14 时间序列、采样与周期信号

### 核心判断

Ch14 是方向精做章之一。所有学生应快读时间序列共同框架，时域方向学生精做。

### 必须强调

1. 时间戳是数据的一部分；
2. 采样窗口和 alias；
3. 周期不是最高峰，而是假设；
4. 不能只报告 best period；
5. 时间序列进入 ML 前的特征和缺失模式。

### Ch14 章首短卡

```markdown
### 本章阅读方式

所有学生快读时间序列共同框架；时域方向学生精做。目标是理解时间、采样、噪声和窗口函数如何影响周期判断，以及这些信息如何进入机器学习特征或质量记录。
```

### Chapter-specific fields

```markdown
## Ch14 Fields
- time series file:
- time unit/system:
- cadence:
- duration:
- missing pattern:
- period search range:
- best period:
- second-best period:
- phase-folded plot:
- alias risk:
```

### Special requirement

```markdown
Pass 不能只报告 best period；必须说明 second-best period 或 alias 风险。
```

### Ch14 Exit Gate

```markdown
### Exit Gate

1. 时间戳、时间跨度和采样是否说明？
2. 周期搜索范围是否合理？
3. 是否报告 best period 之外的候选或 alias 风险？
4. 时间序列进入 ML 前的缺失/采样风险是否说明？

最低交付：Evidence Record + period search/phase-folding 结果。
```

---

## 4.9 Ch15 物理实验、模型拟合与模拟数据

### 核心判断

Ch15 是 Part II 到 Part III 的桥梁章。它自然引出“物理模型 vs 数据驱动模型”。所有学生应快读，物理实验/模拟方向学生精做。

### 必须强调

1. 前向模型；
2. 参数含义和单位；
3. 残差图比拟合曲线更重要；
4. chi-square 或误差指标；
5. Monte Carlo 不确定度；
6. 物理模型与 ML baseline 的关系。

### Ch15 章首短卡

```markdown
### 本章阅读方式

所有学生快读模型拟合共同框架；物理实验和模拟方向学生精做。目标不是找到最低误差曲线，而是说明模型、参数、残差、不确定度和解释边界，并理解它如何成为机器学习 baseline。
```

### Chapter-specific fields

```markdown
## Ch15 Fields
- model formula:
- parameter meanings:
- parameter units:
- fitting method:
- residual plot:
- error metric / chi-square:
- uncertainty estimate:
- baseline comparison:
- physical interpretation limit:
```

### Special requirement

```markdown
Pass 必须包含残差或误差诊断；不能只给拟合曲线。
```

### Ch15 Exit Gate

```markdown
### Exit Gate

1. 模型公式、参数和单位是否清楚？
2. 拟合方法和误差指标是否说明？
3. 是否查看残差或不确定度？
4. 物理模型和 ML baseline 的关系是否说明？

最低交付：Evidence Record + 拟合结果 + 残差/不确定度检查。
```

---

## 4.10 Part II Synthesis

### 核心判断

Part II synthesis 是进入 Part III 的正式闸门。它不应只是总结，而应产出 Data Card v0.1 和 Dataset Contract 草稿。

### 必须加入

```markdown
### Part II Exit Gate

进入 Part III 前，学生必须完成：

1. 至少一个 Data Card v0.1；
2. 至少一个 Part III Dataset Contract 草稿；
3. 至少一个方向精做章节的 Evidence Record；
4. 一个说明样本、特征、标签、误差、质量标记、选择效应和预处理历史的摘要。
```

### Part II synthesis special requirement

```markdown
Pass 必须能回答：这个数据集如何安全进入机器学习？
```

---

## 5. 建议后的 Part I/II 运行方式

## 5.1 Part I 运行方式

```text
Part I 导读
  ↓
Ch01：路径、日志、最小脚本
  ↓
Ch02：版本和 checkpoint
  ↓
Ch04：notebook 到 script
  ↓
Ch06：数据入口契约
  ↓
Ch08：图表证据
  ↓
Part I workflow packet
```

Part I 的最终产物不是很多工具知识，而是一个 workflow packet：

```markdown
# Part I Workflow Packet

- project root
- environment check
- command log
- git checkpoint
- runnable script
- data intake Evidence Record
- figure Evidence Record
```

## 5.2 Part II 运行方式

```text
Ch10：误差与单位，必修
  ↓
Ch11：星表与 HR 图，样板章，必修
  ↓
Ch12–15：共同框架快读 + 至少一章精做
  ↓
Part II synthesis
  ↓
Data Card v0.1
  ↓
Part III Dataset Contract
```

Part II 的最终产物不是“处理过一些数据”，而是一个 Part III-ready dataset package：

```markdown
# Part III-ready Dataset Package

- Evidence Record(s)
- Data Card v0.1
- Dataset Contract
- sample table or sample collection
- feature/label/quality/selection summary
- known limits
```

---

## 6. 实施优先级

## Phase 1：先做四个全局资产

最高优先级。

```text
1. Evidence Record 母模板
2. Data Card v0.1
3. Part III Dataset Contract
4. Evidence Record Rubric
```

交付位置建议：

```text
templates/evidence_record_template.md
templates/data_card_v0_1.md
templates/part3_dataset_contract.md
templates/evidence_record_rubric.md
```

## Phase 2：给每章加短卡和 Exit Gate

不要大改正文。

每章只加：

```text
章首：本章阅读方式
章末：Exit Gate
母模板后：chapter-specific fields
```

## Phase 3：优先精修四座主桥

优先级最高的四章：

| 章节 | 桥梁作用 |
|---|---|
| Ch04 | 从探索代码到可重跑 workflow |
| Ch06 | 从文件到数据入口契约 |
| Ch10 | 从数字到科学测量 |
| Ch11 | 从星表到可解释、可建模样本 |

这四章修好后，Part I/II 到 Part III 的接口基本成立。

## Phase 4：处理 Ch01 分层和 Ch12–15 方向选读化

Ch01：

- 不再堆命令；
- 按必须掌握、科研高频、了解三层重排；
- 保留最小脚本和 Python 路径/版本检查为必做。

Ch12–15：

- 共同框架快读；
- 每位学生至少精做一章；
- 每章明确“这种数据进入 ML 前最容易丢失什么信息”。

## Phase 5：notebook 与模板对齐

检查每个 notebook 是否能产出相应 Evidence Record 所需信息：

```text
输入路径是否明确？
运行入口是否明确？
输出文件是否固定？
是否有检查？
是否有限制？
是否能汇入 Data Card 或 Dataset Contract？
```

---

## 7. 需要避免的改稿倾向

## 7.1 避免工具百科化

不要因为某个命令、格式、算法“有用”就加入正文主线。只有当它服务于 Evidence Record、Data Card 或 Dataset Contract 时，才进入主线。

## 7.2 避免 record 过载

不要给每章设计完全不同的表格。统一母模板 + 少量专属字段即可。

## 7.3 避免 Exit Gate 正文化

Exit Gate 只做收束，不再讲新内容。

## 7.4 避免选读路径割裂

Ch12–15 不能被完全跳过。所有学生至少快读共同框架，再按方向精做一章。

## 7.5 避免把可复现写成形式主义

可复现不是“写了很多说明”，而是别人可以定位输入、重跑操作、找到输出、理解检查和限制。

---

## 8. 最终版核心判断

Part I/II 的核心架构可以定为：

```text
Evidence Record：我做了什么。
Data Card v0.1：这个数据集是什么。
Part III Dataset Contract：这个数据集如何安全进入模型。
```

Part I 负责让学生能组织可复查 workflow。  
Part II 负责让学生能构造可解释、可建模的数据对象。  
Part III 才开始系统进入机器学习。

因此，后续改稿的重点不是继续增加基础知识，而是：

1. 统一记录格式；
2. 降低学生填表负担；
3. 强化路径和版本可定位；
4. 设置短而硬的 Exit Gate；
5. 建立明确的 Dataset Contract；
6. 把每章都导向最终 capstone portfolio。

一句话总结：

> **证据链训练的目标不是制造更多表格，而是让学生用最小记录成本保留最大科研可复查性。**
