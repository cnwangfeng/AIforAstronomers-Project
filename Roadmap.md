# Roadmap: 面向天文与物理本科生的 AI 实战教材

版本日期：2026-05-04

## 0. 当前进展快照（2026-05-04）

本节用于会话切换、阶段交接和快速恢复工作状态；后续如需继续编写，请优先阅读本节。

### 0.1 仓库与同步状态

当前项目采用双仓库架构：

- `AIforAstronomers-Project/`：完整项目仓库，保存教材正文、notebooks、data、scripts、环境文件和课程资源。
- `AIforAstronomers/`：Overleaf 同步书稿仓库，只保存 LaTeX 书稿和编译所需资源。

截至本节编写前，最近已经推送的主题提交包括：

- 完整项目仓库：`889ac1a`，提交信息 `Complete textbook refresh and capstone expansion`
- Overleaf 书稿仓库：`4da027b`，提交信息 `Sync textbook refresh and capstone chapters`

`Part II` 第二轮教材化检查已经完成，并已在完整项目仓库形成本地提交：

- 完整项目仓库本地提交：`0d5dcf1`，提交信息 `Refine Part II textbook bridge material`
- 当前 `main` 分支相对 `origin/main` 至少领先 `1` 个提交；尚未把 `0d5dcf1` 推送到远端。
- Overleaf 书稿仓库当前仍停在 `4da027b`，尚未同步这组新的 `Part II` 改动。

在上述 checkpoint 之后，完整项目仓库又新增了多轮本地 checkpoint：

- `7ec2a1d`，提交信息 `Strengthen Part 0 prerequisites and bridges`
- `813ec30`，提交信息 `Update roadmap with latest checkpoint`
- 当前 `main` 分支相对 `origin/main` 已领先多个本地提交；具体数量以 `git status -sb` 为准。
- 这一轮把 `Part 0` 的先修底线、`Part I/II` 的前置桥接，以及若干入口说明同步到了当前状态。

本轮已经完成验证、准备作为 checkpoint 保留的是 `Part I` 轻量二轮补强，涉及文件为：

- `Roadmap.md`
- `book/chapters/part1/README.md`
- `book/chapters/part1/ch01_unix_linux_scientific_computing.tex`
- `book/chapters/part1/ch02_git_reproducible_research.tex`
- `book/chapters/part1/ch04_libraries_scripts_jupyter.tex`
- `book/chapters/part1/ch06_data_io_fits.tex`
- `book/chapters/part1/ch08_plotting_scientific_figures.tex`
- `notebooks/part1_scientific_computing/README.md`

这组 `Part I` 轻量二轮改动的核心目标，是在不重新大改章节结构的前提下，为 Linux/Git/脚本/I/O/绘图补上更明确的科研工作流检查点。本轮已经补入：

- `ch01`：破坏性 Linux 命令前的三步安全确认。
- `ch02`：一次好 Git 提交的边界、证据和说明标准。
- `ch04`：最小可复现脚本交付件标准。
- `ch06`：数据读入后的 I/O 检查记录模板。
- `ch08`：科研图表交付前的自审清单。
- `Part I` 正文和 notebook README：从“draft/future”语气调整为当前正式章节状态。

在这个基础上，后续又开始了更深一层的教材化加厚，重点放在：

- `ch01`：shell 展开顺序、重定向覆盖风险、`tee` 记录、长任务运行证据和 `set -euo pipefail` 脚本安全习惯。
- `ch01`：命令查找与 `PATH`、环境变量与 alias 边界、`sort/uniq/cut/xargs` 的最小统计与批处理。
- `ch02`：把结果、数据版本和 commit 线索连起来，形成可复查的科学记录。
- `ch04`：明确 notebook、script 和 module 的三层分工，防止把探索代码误当作可维护工作流。
- `ch06`：把 CSV 字段契约与 FITS header 契约统一为“先理解数据契约，再解释数值”的数据入口原则。
- `ch08`：补上视觉编码的解释风险，强调颜色、线型、坐标范围和图例并非纯装饰。
- `ch01/ch02/ch04/ch08`：补齐“配套 notebook 做了什么”小节，使 Part I 每章都明确正文概念如何落到可运行 notebook。
- 全书中文入口已补入六大 Part 显式分隔；Part I--VI 均新增或接入导读/收束层，用于说明每一部分的学习主线、能力边界和前后衔接。

当前恢复判断：

- 用户正在阅读 `Part I`；这轮轻量补强只是把明显缺口先补齐，后续仍应根据用户反馈决定是否逐章深改，尤其是 `ch01` Linux 操作深度。
- `Part II` 已完成一轮全章检查并提交；下一步若继续处理，应优先做局部微调、交叉引用、图表说明和练习分层。
- 近期如果要发布或备份，需先决定是否推送完整项目仓库的本地提交，并是否把 `book/` 同步到 Overleaf 书稿仓库。
- 历史约束仍需保留：涉及网络/API 请求时控制 `RPM <= 6`；遇到 `400`、`429` 等短暂错误时可以等待 `3` 到 `5` 秒后重试，不必因此停止。

最近一次验证状态：

- `bash scripts/build_book_local.sh zh`：通过，中文 PDF 输出为 `/tmp/aifor_book_main_zh/main_zh.pdf`，页数 `476`。
- `python scripts/smoke_test_notebooks.py`：通过，`59` 个 notebook。
- `git diff --check -- book/chapters/part1 notebooks/part1_scientific_computing/README.md`：通过。
- 仍有非阻塞提示：既有 `Underfull` 和 FontAwesome `ToUnicode` warning；`ch14` Nyquist 附近的小幅 `Overfull \hbox` 已处理。

书稿同步方式：

- 在完整项目仓库中维护 `book/` 目录。
- 使用 `bash scripts/sync_book_to_overleaf.sh` 先做 dry-run 预览。
- 使用 `bash scripts/sync_book_to_overleaf.sh --apply` 将 `book/` 同步到 `../AIforAstronomers/`。
- 然后在 Overleaf 书稿仓库单独提交并推送。

### 0.2 当前已完成的内容

截至 2026-05-04，项目已经从“路线图”推进到“可持续扩展的教材原型”，并完成以下内容：

- 中文教材正式题目已确定为《面向天文与物理本科生的 AI 科研实战》。
- 英文副标题已确定为 `Practical AI for Astronomy and Physics`。
- `Part 0` 已从正文主线中独立出来，作为 Python 先修模块。
- `Part I` 到 `Part III` 已建立连续正文和 notebook 主线。
- `Part IV` 已经启动，并完成多个连续案例章节。
- `Part V` 已经启动，并形成连续九章的深度学习与现代 AI 入口。
- `Part VI` 已经启动，并完成前二十一章 capstone workflow / project-integration / rubric / trial-teaching / course-calendar / release package / revision-archive / instructor-handoff / public-release-maintenance / launch-QA-adoption / adoption-feedback-maintenance / final-package-closure / package-directory-release-notes / semester-reboot-preflight / failure-mode-escalation / substitute-handoff-contingency / shutdown-warmstart / alumni-mentor-relay / community-memory-ledger / guest-intake-boundary 入口。
- 中文主书稿已经有六大 Part 分隔，并为 Part I--VI 补入导读、收束或全书收束层，避免正文变成孤立章节堆叠。
- 中文主书稿入口 `book/main_zh.tex` 已建立并保持可编译。
- 本地 LaTeX 编译、notebook smoke test、data manifest 校验已接入日常工作流。

当前资源规模：

- 已通过 smoke test 的 notebook：`59` 个
- 已登记并通过校验的教学数据集：`52` 个
- 中文书稿当前页数：约 `476` 页

### 0.3 各部分完成度

`Part 0. Python 先修模块`

- 已建立 notebook-first 结构。
- 已形成四个先修 notebook，分别覆盖 Python 入门、条件与循环、函数与模块、轻量 OOP。
- 先修底线已明确覆盖 notebook 执行顺序、变量与容器、`Path` / `csv`、`if` / `for` / `while`、函数与模块、随机种子、对象与方法接口。
- 角色定位已经明确：只承担正文外先修，不再占用正文主线篇幅，也不继续扩成第二本 Python 教材。
- `book/main_zh.tex` 的“读者准备”已经加入跳过/补修诊断清单。

`Part I. 科研计算基础`

- 已有 Linux、Git、脚本/Jupyter、数据 I/O、科学绘图等内容。
- `ch01`、`ch02`、`ch04`、`ch06`、`ch08` 已接回 `book/main_zh.tex`，并完成首轮教材化重写。
- 配套 notebook 已同步到当前正文主线，并通过完整 smoke test。
- 轻量二轮补强已加入 Linux 安全操作、好提交标准、最小脚本交付、I/O 检查记录和图表自审清单。
- 深读补强已经开始，当前新增重点是 Linux/shell 执行模型、Git 结果版本线索、notebook/script/module 分工、数据契约、科研图表视觉编码风险，以及每章正文到 notebook 的桥接说明。
- 章节入口已明确标出 Part 0 前置能力：`Path` / `csv.DictReader`、基础控制流、函数封装和对象方法调用。
- `ch08` 已补入 claim--evidence--limit 读图框架，强调图表如何从视觉输出进入科学论断。
- `ch01` 已补入命令查找与 `PATH`、环境变量边界，以及 `sort/uniq/cut/xargs` 的最小统计与批处理。
- `book/main_zh.tex` 已补入显式六大 Part 分隔；`Part I` 已新增导读，把 Linux/Git/脚本/I/O/绘图组织成一条可复现科研工作流。
- 后续重点从“大面积补写”转为逐章细读：统一术语、补交叉引用、补图表说明、补习题层次，并检查每章是否真正从概念引入走到可复现实操。

`Part II. 天文/物理数据处理`

- `ch10` 到 `ch15` 已接入 `book/main_zh.tex`，覆盖误差与不确定度、Gaia HR 图、FITS/WCS、光谱、时间序列与物理实验数据。
- 配套小数据和 notebook 已建立，并通过完整 smoke test。
- 第二轮教材化校订已经完成一轮全章检查，并补入多处“公式到算法到代码”的桥接段；下一步应先阅读、同步或根据反馈微调，而不是继续无限扩写。
- 章节入口已明确标出 Part 0 前置能力：表格读取、循环筛选、函数封装、对象方法调用与随机种子意识。
- 已新增 `Part II` 导读与收束综合，明确把星表、图像、光谱、时间序列、实验/模拟数据统一到“数据契约、单位误差、类型算法、诊断图表、可建模样本”的共同框架。

`Part III. 机器学习实战主线`

- 已形成连续章节链条，包括：
  - AI、机器学习与科学推断
  - 最小分类 workflow
  - 回归
  - 分类
  - 模型评估与诊断
  - 特征工程与数据预处理
  - 模型选择与超参数
  - 无监督学习
  - 异常检测
  - 不确定度、解释性与科学可信度
- 这一部分目前是全书最完整、最成体系的主干。
- 已新增 Part III 导读与收束综合，强调机器学习作为科学推断工具，而不是单纯模型调用。

`Part IV. 天文与物理案例`

当前状态如下：

- 第 26 章：Gaia HR 图与恒星分类
  - 正文：已完成
  - notebook：已完成
  - data：已完成
- 第 27 章：光度红移估计案例
  - 正文：已完成
  - notebook：已完成
  - data：已完成
- 第 28 章：光谱分类案例
  - 正文：已完成
  - notebook：已完成
  - data：已完成
- 第 29 章：星系形态分类案例
  - 正文：已扩写并补充图表、练习与 notebook 指引
  - notebook：已完成（传统形态特征 baseline 版本）
  - data：已完成（教学用 morphology demo 数据）
- 已新增 Part IV 导读与收束综合，把四个案例明确组织为从数据处理、机器学习 workflow 到完整项目意识的装配训练。

`Part V. 深度学习与现代 AI`

- 已启动，并形成连续的前九章入口。
- 第 30 章：神经网络基础
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成
- 第 31 章：卷积神经网络与图像局部特征
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成
- 第 32 章：一维卷积与光谱局部模式
  - 正文：已完成教学版扩展稿
  - notebook：已完成，并补上第二组 workflow 对照与 tiny trainable `Conv1d` learner
  - data：已完成，并新增 workflow demo 数据
- 第 33 章：表示学习、自编码器与重构误差
  - 正文：已完成教学版扩展稿
  - notebook：已完成，并补上 validation-calibrated anomaly workflow、latent retrieval / anomaly triage、shared-patch conv-style extension 与 end-to-end Conv1d autoencoder
  - data：已完成
- 第 34 章：Transformer、注意力与科学基础模型概念
  - 正文：已完成教学版扩展稿
  - notebook：已完成，并补上 patch-token baseline、masked-token workflow、two-head attention extension 与 masked-patch pretraining objective
  - data：已完成，并新增 masked-token / masked-patch workflow demo 数据
- 第 35 章：LLM 辅助科研编程、代码验证与 notebook 工作流
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成
- 第 36 章：agentic research assistants、工具调用与科研工作流
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成
- 第 37 章：LLM 辅助文献阅读与报告写作
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成
- 第 38 章：AI 伦理、版权与科研规范
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成
- 已新增 Part V 导读与收束综合，强调 baseline-first deep learning、现代 AI 工具的验证边界，以及进入 capstone 前的复杂度选择原则。

`Part VI. Capstone 项目`

- 已启动。
- 第 39 章：Capstone 项目工作流、项目模板与可信交付
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（project-board workflow demo 数据）
- 第 40 章：Capstone 项目选题、范围控制与可执行性
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（proposal-scoping workflow demo 数据）
- 第 41 章：Capstone 报告、展示与最终签字
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（final-delivery review demo 数据）
- 第 42 章：Capstone 案例模板与评分 Rubric
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（rubric case-template demo 数据）
- 第 43 章：Capstone 试教材料与课程运行包
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（trial-teaching feedback demo 数据）
- 第 44 章：Capstone 课程日历与里程碑
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（course-calendar demo 数据）
- 第 45 章：Capstone 学生 Handout 与助教评分指南
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（student-handout / TA-guide release demo 数据）
- 第 46 章：Capstone 修订闭环、公开归档与课程反馈
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（revision / archive feedback demo 数据）
- 第 47 章：Capstone 教师交接包
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（instructor-handoff demo 数据）
- 第 48 章：Capstone 公开发布索引与课程维护清单
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（public-release / maintenance demo 数据）
- 第 49 章：Capstone 公开发布 QA 与课程采用说明
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（launch-QA / adoption-note demo 数据）
- 第 50 章：Capstone 采用反馈与维护节奏
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（adoption-feedback / maintenance-cadence demo 数据）
- 第 51 章：Capstone 最终课程包索引与 Part VI 收束清单
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（final-package / closure checklist demo 数据）
- 第 52 章：Capstone 课程包目录页与发布版本说明
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（course-package directory / release-notes demo 数据）
- 第 53 章：Capstone 开课前预检与学期重启清单
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（semester-reboot / preflight demo 数据）
- 第 54 章：Capstone 故障模式与升级处理手册
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（failure-mode / escalation demo 数据）
- 第 55 章：Capstone 应急演练与替班教师接管手册
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（contingency / substitute-handoff demo 数据）
- 第 56 章：Capstone 学期收尾与下一届 Warm Start
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（shutdown / warm-start demo 数据）
- 第 57 章：Capstone 校友案例与导师接力
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（alumni / mentor-relay demo 数据）
- 第 58 章：Capstone 社群记忆与长期维护账本
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（community-memory / maintenance-ledger demo 数据）
- 第 59 章：Capstone 外部合作边界与客座项目准入
  - 正文：已完成教学版首稿
  - notebook：已完成
  - data：已完成（external-collaboration / guest-intake demo 数据）
- `Part VI` 的课程包闭环、读者入口层、跨学期重启入口、运行期故障升级层、替班接管层、跨届收尾层、长期导师接力层、长期记忆层和外部合作准入层已经形成；下一步可以从头回到前半本。
- 已新增 Part VI 导读和全书收束章，把 capstone 明确定位为可信交付，并把全书主线收束到“从会运行到会负责”。

### 0.4 已验证的本地环境与工作流

当前本地环境已确认可支持后续持续编写：

- 操作系统环境：macOS 本地开发环境
- LaTeX：已安装 MacTeX，可用 `latexmk`
- 中文编译：`XeLaTeX` 路径已跑通
- Python 环境定义：`environments/environment.yml`

当前 `environment.yml` 的核心依赖包括：

- `python=3.12`
- `jupyterlab`, `notebook`
- `numpy`, `scipy`, `pandas`
- `matplotlib`, `seaborn`
- `scikit-learn`
- `astropy`, `astroquery`, `photutils`, `specutils`, `lightkurve`
- `tqdm`, `joblib`, `pooch`, `requests`, `pyyaml`
- `jupytext`（通过 `pip`）

工作流补充：

- `scripts/build_book_local.sh` 现在会在需要时自动把 `/Library/TeX/texbin` 加入 `PATH`，减少 shell 环境差异带来的编译失败。

已验证可用的本地命令：

```bash
python scripts/smoke_test_notebooks.py
python scripts/validate_data_manifest.py
bash scripts/build_book_local.sh main
bash scripts/build_book_local.sh zh
```

默认输出位置：

- `main.tex` PDF：`/tmp/aifor_book_main/main.pdf`
- `main_zh.tex` PDF：`/tmp/aifor_book_main_zh/main_zh.pdf`

截至 2026-05-04 的最近一次、与当前 `Part I` 轻量补强直接相关的验证结果：

- `python scripts/smoke_test_notebooks.py`：通过（`59` 个 notebook）
- `bash scripts/build_book_local.sh zh`：通过（当前中文书稿 `476` 页）
- `git diff --check -- book/chapters/part1 notebooks/part1_scientific_computing/README.md`：通过（当前 `Part I` 改动无空白格式问题）

上一轮完整发布检查中，`python scripts/validate_data_manifest.py`、`bash scripts/build_book_local.sh main` 和 `bash scripts/sync_book_to_overleaf.sh` dry-run 也已经通过；当前 `Part I` 改动主要是 LaTeX 正文与 README，不涉及数据 manifest 或 notebook 代码。

当前编译中仍存在但不阻塞工作的提示：

- 目录页与个别页面附近偶发 `Underfull \vbox`
- FontAwesome 相关 `ToUnicode CMap` warning

这些提示目前不影响 PDF 生成，也不阻塞继续写作。

### 0.5 当前主入口与关键文件

当前最关键的工作入口：

- 路线图与交接文档：`Roadmap.md`
- 中文主书稿入口：`book/main_zh.tex`
- 英文稳定入口：`book/main.tex`
- 书稿目录说明：`book/README.md`
- 项目总说明：`README.md`
- 当前课程包发布说明：`COURSE_PACKAGE_RELEASE_NOTES.md`
- 同步与发布检查清单：`RELEASE_SYNC_CHECKLIST.md`
- 同步脚本：`scripts/sync_book_to_overleaf.sh`
- 本地编译脚本：`scripts/build_book_local.sh`
- notebook smoke test：`scripts/smoke_test_notebooks.py`
- data manifest 校验：`scripts/validate_data_manifest.py`

### 0.6 下一阶段建议优先级

如果后续切换会话后继续推进，建议按以下顺序展开：

1. 若尚未提交，先提交当前 `Part I` 轻量二轮补强 checkpoint。
2. 用户正在阅读 `Part I`；等用户反馈后再回到 `Part I` 做逐章细读校订，重点检查 Linux/Git/脚本/I/O/绘图是否真正达到教材深度。
3. 视需要将已经提交的 `Part II` 书稿变化同步到 Overleaf 书稿仓库，并在 `../AIforAstronomers/` 单独提交。
4. 若继续处理 `Part II`，优先做局部微调、交叉引用、图表说明和练习分层，不再默认大面积扩写。
5. 系统整理 `Part I` 和 `Part II` 的旧书稿资产，确认是否还有值得迁入的例题、图表、习题或参考资料。

## 1. 教材定位

暂定书名：

- 中文：面向天文与物理本科生的 AI 科研实战
- 英文：Practical AI for Astronomy and Physics
- 仓库名沿用：AIforAstronomers

核心定位：

本教材不是泛泛的人工智能概论，也不是只讲 Python 语法的科学计算手册，而是一本面向天文与物理本科生的实战教材。学生应通过真实或接近真实的数据项目，学会用 Python、现代机器学习和生成式 AI 工具完成可复现的科研数据分析。

目标读者：

- 天文、物理、空间科学、应用物理等专业本科生。
- 大二到大四为主，也可供低年级研究生补基础。
- 默认具备大学物理、微积分、线性代数和基础概率统计背景。
- 建议在进入正文前先完成 Part 0 的 Python 先修模块；进入正文后，学生应能独立阅读和修改基础 notebook。

学习产出：

完成本教材后，学生应能够：

- 在 Linux/macOS/远程服务器环境中组织科研代码和数据。
- 使用 Git 管理课程作业、科研小项目和协作代码。
- 使用 NumPy、SciPy、Pandas、Matplotlib、Astropy 处理常见天文/物理数据。
- 读取、清洗、可视化和解释表格、光谱、图像、时间序列等数据。
- 建立监督学习、无监督学习和深度学习模型，并理解训练、验证、测试的差别。
- 正确评估模型，识别过拟合、数据泄漏、类别不平衡、选择效应等问题。
- 在科研工作流中合理使用 LLM/生成式 AI 辅助编程、文献阅读和报告写作，同时保留验证、引用和可复现记录。
- 完成一个从数据获取到报告撰写的 capstone 项目。

## 2. 项目硬性要求

本项目最终交付物必须同时包含三类内容：

1. **中文教材正文**
   - 教材主体必须采用中文编写。
   - 教材内容必须覆盖本路线图提出的六个正文部分：科研计算基础、天文/物理数据处理、机器学习实战主线、天文与物理案例、深度学习与现代 AI、Capstone 项目；并额外提供 Part 0 Python 先修模块。
   - 教材应具有足够深度：不能停留在工具调用层面，必须解释核心概念、适用条件、失效场景、科学解释和误差/不确定度。
   - 教材应具有足够广度：覆盖表格、图像、光谱、时间序列、物理实验/模拟数据，以及监督学习、无监督学习、深度学习和生成式 AI 辅助科研。
   - 教材必须图文并茂。每个核心章节原则上至少包含 2 到 4 张高质量图表、流程图或数据可视化；案例章节应包含真实数据图、模型诊断图和结果解释图。
   - 图表必须有编号、标题、单位、来源说明和正文解读，不能只作为装饰。

2. **配套 notebooks**
   - 每章至少配套 1 个可运行 notebook。
   - notebook 不只是代码附录，而应承担“从数据到结果”的实战教学功能。
   - notebook 必须和教材正文相互引用：正文解释思想，notebook 展示可执行流程。
   - notebook 必须能在干净环境中运行，并尽量控制在本科课堂可接受的运行时间内。

3. **配套 data 目录**
   - `data/` 目录用于保存小型教学数据、数据说明、下载脚本和外部数据缓存说明。
   - 小数据可以直接进入仓库；大数据不直接提交，只提供下载脚本、来源链接、校验方式和预处理说明。
   - 每个数据集必须说明来源、许可证、字段含义、单位、处理流程和推荐使用章节。

因此，本项目不是单一 PDF，也不是一组零散 notebook，而是一套完整的本科教学资源包：中文教材正文负责体系化讲解，notebook 负责可执行实践，data 负责可复现练习。

## 3. 项目启动时仓库基线

当前仓库已经具备科学计算入门教材雏形：

- `UnixLinux.tex`：Unix/Linux 科研计算基础。
- `VersionControl/VersionControl.tex`：Git 版本控制。
- `Chapter2.tex` 到 `Chapter8.tex`：Python 基础、库、条件循环、I/O、FITS、函数、绘图、OOP。
- `Glossary.tex`：术语表。
- `main.tex`：LaTeX 主文件。

需要优先处理的问题：

- `main.tex` 中 `\include{Grossary.tex}` 拼写错误，应改为 `\include{Glossary}`。
- `\include{UnixLinux.tex}` 这类写法应统一为不带 `.tex` 后缀。
- 当前章节编号和正文中手写的 `Definition 2.0.1` 等编号会错位，应改用已有的 `defbox`、`examplebox`、`exercisebox` 自动编号环境。
- 目前没有 README、LICENSE、参考文献、notebook、数据目录、环境文件和测试脚本。
- 部分 Python 基础文字与 Python for Astronomers 高度接近。后续发布前必须完成授权检查、署名、改写和引用。

保留策略：

- 保留现有 Linux、Git、Jupyter、数据 I/O、绘图等内容作为 Part I 的核心资产。
- 将更通用的 Python 基础语法、条件循环、函数组织和轻量 OOP 逐步下沉到 Part 0 先修模块。
- 新增 AI/ML 内容时采用 notebook-first：每章书稿配一个或多个可运行 notebook。
- LaTeX 继续作为正式书稿格式；中长期可评估是否并行生成 Jupyter Book 或 Quarto 网站。

## 4. 教学结构

整本书采用“Part 0 先修 + 六部分正文”结构：

0. Python 先修模块（正文外）

1. 科研计算基础
2. 天文/物理数据处理
3. 机器学习实战主线
4. 天文与物理案例
5. 深度学习与现代 AI
6. Capstone 项目

每章建议固定模板：

- 学习目标：学生完成本章后能做什么。
- 科学问题：用一个天文或物理问题引入。
- 数据说明：数据来源、字段、单位、误差、选择效应。
- 核心概念：只讲完成任务必需的数学和算法。
- 动手实验：一个完整 notebook，能从头运行。
- 常见错误：数据泄漏、单位错误、坐标错误、过拟合等。
- AI 助手使用：给出可以问 AI 的问题、不能直接相信的部分、验证清单。
- 练习：基础题、进阶题、开放题。
- 小结：本章方法适合什么问题，不适合什么问题。

评估方式建议：

- 每章 1 个 notebook 作业。
- 每 3 到 4 章一个综合小项目。
- 期末 capstone：数据分析报告 + notebook + Git 提交记录 + 5 到 10 分钟展示。
- 明确区分 AI-encouraged 作业和 AI-discouraged 作业。

## 5. 建议仓库结构

本项目采用双仓库架构：

```text
AIforAstronomers-Project/   # 完整项目仓库：教材、notebooks、data、scripts、环境和课程资源
AIforAstronomers/           # Overleaf 同步书稿仓库：只保存 LaTeX 书稿和编译所需图片
```

这样做的原因：

- Overleaf 只适合编译轻量书稿，不适合保存大数据、notebooks 输出、模型文件和批处理脚本。
- 完整项目需要有 notebooks、data、scripts 和环境文件，后期体积会明显超过普通 Overleaf 项目的舒适范围。
- 通过 `scripts/sync_book_to_overleaf.sh` 将 `book/` 中的书稿同步到 Overleaf 仓库，可以保持两个仓库职责清晰。

完整项目仓库结构：

```text
AIforAstronomers-Project/
  Roadmap.md
  README.md
  book/
    main.tex
    references.bib
    UnixLinux.tex
    Chapter2.tex
    ...
    VersionControl/
  notebooks/
    part0_python_prereq/
    part1_scientific_computing/
    part2_data_processing/
    part3_machine_learning/
    part4_cases/
    part5_deep_learning_ai/
    part6_capstone/
  data/
    README.md
    manifest.yml
    small/
    external/
  figures/
  scripts/
    sync_book_to_overleaf.sh
    clean_notebooks.py
  environments/
    environment.yml
  requirements.txt
```

Overleaf 书稿仓库结构：

```text
AIforAstronomers/
  main.tex
  UnixLinux.tex
  Chapter2.tex
  ...
  VersionControl/
  Glossary.tex
```

原则：

- 小数据可以随仓库发布。
- 大型数据只放下载脚本、说明和校验信息，不直接提交。
- 所有 notebook 必须能从干净环境运行。
- 每个数据集需要 `README` 说明来源、许可证、字段、单位和预处理步骤。
- 教材正文、notebook 和数据说明必须保持同步。新增章节时，同时创建对应 notebook 入口和数据说明。
- Overleaf 仓库不保存 notebooks、data、环境文件和运行脚本。

## 6. 完整内容规划

### Part 0. Python 先修模块（正文外）

目标：用尽可能短的路径补齐进入本书所需的 Python 基础，不让正文主线被通用编程入门吞没。

组织原则：

- 以 notebook-first 为主。
- 只覆盖进入正文所需的最低限度语法与代码组织能力，但这部分必须足以支撑后续 Part I/II 的阅读与练习。
- 完成后应能读懂并修改基础 notebook，而不是成为一门独立的 Python 课程。
- `book/chapters/part0/` 只保留可选 LaTeX 支持材料；主教材不 include Part 0。

预备单元 A：Python 入门

- 主题：变量、数据类型、容器、索引、基础数学。
- 实验：用 Python 计算开普勒第三定律、黑体辐射或简单误差传播。
- 当前资源：`notebooks/part0_python_prereq/ch03_basic_python_prereq.ipynb`

预备单元 B：条件、循环与批处理

- 主题：if、for、while、列表推导、批量处理。
- 实验：批量筛选一组恒星或实验测量数据。
- 当前资源：`notebooks/part0_python_prereq/ch05_conditionals_loops_batch_processing.ipynb`

预备单元 C：函数、模块与最小代码组织

- 主题：函数、参数、返回值、模块、最小复用结构。
- 实验：把重复的数据清洗流程封装成函数。
- 当前资源：`notebooks/part0_python_prereq/ch07_functions_modules.ipynb`

预备单元 D：轻量 OOP 与读懂库接口

- 主题：类、对象、方法，以及如何读懂科学库中的对象接口。
- 实验：构造一个最小类，并理解为何真实项目中常见对象方法调用。
- 当前资源：`notebooks/part0_python_prereq/ch09_object_oriented_programming.ipynb`

### Part I. 科研计算基础

目标：默认学生已经具备基础 Python 阅读能力，继续把他们带到可以独立运行 notebook、管理代码、读取数据、画图并保持可复现的水平。

第 1 章：Unix/Linux 与科研计算环境

- 现有基础：`UnixLinux.tex`
- 主题：命令行、文件系统、远程登录、进程、压缩、HPC 基础。
- 实验：整理一个天文项目目录，下载数据，统计文件大小，批量重命名。
- 交付：一个结构清晰的项目文件夹。

第 2 章：Git 与可复现科研

- 现有基础：`VersionControl/VersionControl.tex`
- 主题：commit、branch、merge、remote、`.gitignore`、冲突处理。
- 实验：把一个 notebook 项目纳入版本控制，模拟协作冲突。
- 交付：一次规范 Git 提交历史。

第 4 章：库、脚本与 Jupyter

- 现有基础：`Chapter3.tex`
- 主题：import、脚本、notebook、环境管理、包安装。
- 新增重点：Jupyter cell 执行顺序、随机种子、环境记录。
- 实验：把交互式代码整理为可重复运行 notebook 和脚本。

第 6 章：文件 I/O、FITS 与数据格式

- 现有基础：`Chapter5.tex`
- 主题：文本、CSV、FITS、HDF5 简介、元数据。
- 实验：读取 FITS 图像和表格，检查 header，提取观测信息。

第 8 章：可视化与科研图表

- 现有基础：`Chapter7.tex`
- 主题：Matplotlib、误差棒、直方图、二维图像、颜色映射。
- 实验：制作一张接近论文质量的图。

### Part II. 天文/物理数据处理

目标：让学生理解真实科学数据的形态、误差、单位、选择效应和前处理。

第 10 章：科学数据、误差与单位

- 主题：测量误差、系统误差、单位、量纲、误差传播、`astropy.units`。
- 实验：用带误差的测量值估计物理量，并比较错误单位带来的后果。

第 11 章：表格数据、星表与坐标

- 主题：Pandas、Astropy Table、SkyCoord、交叉匹配。
- 数据候选：Gaia、Hipparcos、小型模拟星表。
- 实验：构建附近恒星样本，画 HR 图。

第 12 章：天文图像与 FITS/WCS

- 主题：FITS image、WCS、背景估计、源检测、孔径测光基础。
- 数据候选：SDSS cutout、HST/JWST public image、教材自带小 FITS。
- 实验：测量星源或星系的简单光度。

第 13 章：光谱数据

- 主题：波长、流量、红移、归一化、重采样、谱线特征。
- 数据候选：SDSS/LAMOST 小样本、模拟光谱。
- 实验：估计红移或识别谱线。

第 14 章：时间序列与周期信号

- 主题：采样、噪声、周期搜索、Lomb-Scargle、相位折叠。
- 数据候选：变星、TESS light curve、模拟摆实验。
- 实验：从光变曲线中恢复周期。

第 15 章：物理实验与模拟数据

- 主题：拟合、残差、卡方、Monte Carlo、简单数值模拟。
- 数据候选：摆、RC 电路、放射性衰变、Ising 模型、小型 N-body。
- 实验：比较物理模型拟合与数据驱动模型。

### Part III. 机器学习实战主线

目标：建立本科生可操作、可诊断、可解释的机器学习工作流。

第 16 章：什么是 AI、机器学习与科学推断

- 主题：AI/ML/DL/LLM 的边界；监督/无监督/强化学习；预测与科学解释的差异。
- 实验：同一数据集上比较规则方法、物理模型和机器学习模型。

第 17 章：机器学习项目流程

- 主题：问题定义、标签、特征、训练/验证/测试、baseline、数据泄漏。
- 实验：建立一个最小可用分类或回归 pipeline。

第 18 章：回归

- 主题：线性回归、多项式回归、正则化、随机森林回归、指标。
- 案例：光度红移、恒星参数估计、物理实验参数拟合。

第 19 章：分类

- 主题：kNN、逻辑回归、SVM、决策树、随机森林。
- 案例：恒星/星系/类星体分类，或信号/背景分类。

第 20 章：模型评估与诊断

- 主题：混淆矩阵、precision、recall、F1、ROC、PR 曲线、交叉验证、校准。
- 重点：类别不平衡和科学代价函数。

第 21 章：特征工程与数据预处理

- 主题：缺失值、缩放、编码、特征构造、pipeline、ColumnTransformer。
- 案例：从颜色、谱线等物理特征构建模型。

第 22 章：模型选择与超参数优化

- 主题：GridSearchCV、RandomizedSearchCV、validation curve、learning curve。
- 重点：避免在测试集上调参。

第 23 章：无监督学习与降维

- 主题：PCA、t-SNE/UMAP 概念、k-means、DBSCAN、Gaussian mixture。
- 案例：光谱聚类、HR 图结构、异常样本初筛。

第 24 章：异常检测与新奇发现

- 主题：Isolation Forest、LOF、autoencoder 概念、人工复核。
- 案例：特殊光谱、离群天体、实验异常读数。

第 25 章：不确定度、解释性与科学可信度

- 主题：bootstrap、预测区间、特征重要性、SHAP 概念、模型失效边界。
- 重点：机器学习输出不是物理真理，必须连接误差和选择效应。

### Part IV. 天文与物理案例

目标：把 Part III 的算法放回真实科学问题，训练完整项目意识。

案例 1：Gaia HR 图与恒星分类

- 数据：Gaia 小样本或预处理 CSV。
- 方法：数据清洗、颜色-星等图、聚类/分类。
- 产出：解释主序、巨星分支、白矮星区域。

案例 2：光度红移估计

- 数据：SDSS 星系测光 + 光谱红移小样本。
- 方法：回归、随机森林/梯度提升、误差分析。
- 产出：红移预测模型和残差图。

案例 3：光谱分类

- 数据：SDSS/LAMOST 小样本或模拟光谱。
- 方法：预处理、PCA、SVM/随机森林/CNN 入门。
- 产出：分类报告、错误案例复查。

案例 4：天文图像中的星系形态分类

- 数据：Galaxy Zoo 小样本或公开缩略图。
- 方法：传统特征 + CNN 迁移学习。
- 产出：比较手工特征与深度学习。

案例 5：时间域信号搜索

- 数据：TESS/变星/模拟光变曲线。
- 方法：周期搜索、特征提取、分类。
- 产出：可复现的 light curve 分析流程。

案例 6：物理实验数据的模型拟合与 ML 比较

- 数据：摆、衰变、热扩散或电路实验数据。
- 方法：物理模型拟合 vs 数据驱动回归。
- 产出：说明何时应优先使用物理模型，何时 ML 有帮助。

案例 7：粒子物理或引力波入门数据

- 数据：小型 HEP benchmark、GWOSC 教学数据或模拟数据。
- 方法：信号/背景分类、matched filtering 概念或 ML baseline。
- 产出：跨物理方向案例，服务物理本科读者。

### Part V. 深度学习与现代 AI

目标：给学生现代 AI 的可操作入口，但避免把本科教材写成深度学习专著。

当前状态：

- `Part V` 已正式启动。
- 第 30 章到第 38 章已经形成一条连续入口：先讲神经网络的最小非线性表达能力，再讲二维卷积与图像局部特征、一维光谱卷积、表示学习与自编码器、Transformer 与注意力，再进入 LLM 辅助科研编程、agentic workflow、文献阅读与报告写作，以及 AI 伦理与使用声明。

第 30 章：神经网络基础

- 主题：张量、层、激活函数、损失函数、反向传播直觉、优化器。
- 工具：教学版首稿优先纯 Python；环境允许时补充 PyTorch 对照。
- 实验：用小型全连接网络做非线性回归。
- 当前状态：正文 / notebook / data 已完成首稿。

第 31 章：卷积神经网络与图像局部特征

- 主题：局部感受野、参数共享、ReLU、池化、位置鲁棒性。
- 实验：教学版星系 cutout 卷积特征提取，与 raw-pixel baseline 对照。
- 当前状态：正文 / notebook / data 已完成首稿，并已补上 source/target 小型 transfer-learning workflow；下一步可继续连接真实图像 CNN。

第 32 章：一维卷积与光谱局部模式

- 主题：一维卷积、局部谱线结构、平移鲁棒性、ReLU、max pooling。
- 实验：先做教学版光谱窗口卷积特征提取与 raw-feature baseline 对照，再用第二组小数据演示 continuum normalization、quality gate、manual review queue 与 clean train/validation/test workflow，最后把 normalized windows 推到一个纯 Python tiny trainable `Conv1d` learner。
- 当前状态：正文 / notebook / data 已完成扩展版教学稿，并已补上第二组 workflow demo 数据与纯 Python 的 tiny trainable `Conv1d`。该 learner 使用 3 个长度为 3 的可学习卷积核、ReLU、global max pooling 和线性分类头，在固定随机种子下训练 1200 个 epoch 后，于 clean validation/test 上达到 `1.00` 分类准确率，并用 validation 最低 clean 置信度校准出 ready threshold `0.5539`，把 `X_do1` 保留到 `manual_review`，同时继续把 `R_low` 与 `R_art` 留在人工复核路径。下一步可再扩到更深的光谱 CNN、更长窗口与更真实噪声条件。

第 33 章：表示学习、自编码器与重构误差

- 主题：latent representation、autoencoder、瓶颈约束、自监督重构、异常分数。
- 实验：先用二维瓶颈自编码器压缩小型光谱窗口并比较正常样本与异常样本的重构误差，再用 validation 正常样本校准阈值，把测试样本路由到 normal-like、manual-review 与 anomaly-candidate 队列。
- 当前状态：正文 / notebook / data 已完成扩展版教学稿，并已补上 validation-calibrated anomaly workflow、latent 诊断、shared 3-bin patch 的 conv-style autoencoder extension、端到端 `Conv1d` autoencoder，以及基于 dense bottleneck latent 的最近邻检索 / anomaly triage。新增的 retrieval 段用 workflow train 正常样本构成 tiny normal reference library，在 validation 上校准出 latent support threshold `0.4683`，在 normal test 上达到 `1.00` 的 family retrieval accuracy，同时显示 `3/4` 异常仍留在这个 latent support 内，从而把 `R16` 解释为 `normal_manifold_edge`，并把 `A02`、`A03`、`A04` 解释成 `localized_anomaly_over_known_family`。端到端 `Conv1d` workflow 仍在 validation 上校准出 `0.1363 / 0.2620` 的整谱阈值，并把 `A04` 从 dense bottleneck workflow 的 manual-review 提升为 anomaly-candidate。下一步可再连接更大谱库与更真实光谱表示检索任务。

第 34 章：Transformer 与科学基础模型概念

- 主题：attention、token、预训练、微调、科学基础模型的机会与限制。
- 实验：只做概念和轻量 demo，不训练大模型。
- 当前状态：正文 / notebook / data 已完成扩展版教学稿；原有 bag-of-tokens vs position-aware attention demo 已保留，并补上 bag-of-2-patches baseline、可训练的单头 tiny self-attention masked-token learner、纯 Python 的 two-head masked-token extension，以及新的 masked-patch workflow / pretraining objective。patch-token baseline 在原 6-token 教学任务上达到 `1.00`，说明局部 patch motif 可以把 `center_mark` 后的类别线索压进 token 身份；单头 learner 在固定随机种子下用 6 条 clean training rows 训练 50 个 epoch 后，在 clean validation/test 上达到 `1.00`，并通过 validation-calibrated confidence threshold `0.979` 把 `R_blend` 与 `R_mask` 路由到 `manual_review`；two-head masked-token extension 再训练 60 个 epoch 后，同样在 clean validation/test 上达到 `1.00`，validation-ready threshold 为 `0.901`；新的 masked-patch workflow 则在 bag-of-visible-patches baseline `0.33` 的前提下，把 two-head masked-patch learner 继续推进到 clean validation/test `1.00`，ready threshold 约为 `0.977`，并把 `R_blend_patch` 与 `R_mask_patch` 留在 `manual_review`。配套数据文件现为 `spectral_masked_token_workflow_demo.csv` 与 `spectral_masked_patch_workflow_demo.csv`；下一步如继续推进，可再连接更长序列、更稳定 patch vocabulary 与更完整的 block-level pretraining objective。

第 35 章：LLM 辅助科研编程

- 主题：prompt、代码生成、调试、测试、解释错误、生成文档。
- 实验：让 LLM 帮助重构一个数据分析脚本，并用测试和人工检查验证。
- 红线：不能把未验证代码、未读文献总结和虚构引用直接写入报告。
- 当前状态：正文 / notebook / data 已完成首稿。

第 36 章：Agentic Research Assistants 与工具工作流

- 主题：工具调用、分步计划、质量门、human handoff、可审计 action log。
- 实验：用最小瞬变候选体分诊数据，对比单次排序 baseline 与显式 agentic workflow。
- 当前状态：正文 / notebook / data 已完成首稿。

第 37 章：LLM 辅助文献阅读与报告写作

- 主题：结构化证据卡片、claim ledger、引用与页码核查、caveat 保留、报告 skeleton 写作。
- 实验：用一组教学化论文证据卡片，对比“直接按显著性摘要”与“先路由到 verified result / caveat / human review / method note / exclude 的安全工作流”。
- 当前状态：正文 / notebook / data 已完成首稿。

第 38 章：AI 伦理、版权与科研规范

- 主题：AI 使用场景卡片、版权与复用许可边界、human signoff、学术诚信与 AI-use statement。
- 实验：用一组教学化 AI 使用场景卡片，对比“只按省时程度分配 AI”与“先过材料 / 共享 / 引用 / 签字边界再路由”的安全 workflow。
- 当前状态：正文 / notebook / data 已完成首稿。

### Part VI. Capstone 项目

目标：完成一个可展示、可复现、科学问题明确的 AI 数据分析项目。

Capstone 项目流程：

1. 选题：明确科学问题和数据来源。
2. 数据：下载、清洗、记录许可证和字段说明。
3. 基线：建立非 ML 或简单 ML baseline。
4. 建模：训练至少两个模型，并做合理诊断。
5. 解释：分析错误样本、不确定度和模型局限。
6. 报告：形成 5 到 8 页项目报告或等价 notebook report。
7. 展示：5 到 10 分钟口头报告。

推荐项目方向：

- 基于 Gaia 的恒星族群探索。
- 基于 SDSS/LAMOST 的光谱分类。
- 基于多波段测光的红移估计。
- 基于 TESS 光变曲线的周期识别。
- 基于公开图像的星系形态分类。
- 基于实验数据的物理参数估计。
- 基于模拟数据的信号/背景分类。

Capstone 评分建议：

- 科学问题清晰度：15%
- 数据处理与可复现性：20%
- 模型建立与评估：25%
- 结果解释与局限性：20%
- 代码质量与 Git 记录：10%
- 报告和展示：10%

## 7. 数据与软件栈

核心软件：

- Python 3.12 或课程开始时稳定的 Python 版本。
- JupyterLab / Notebook。
- NumPy、SciPy、Pandas、Matplotlib、Seaborn。
- Astropy、astroquery、photutils、specutils、lightkurve。
- scikit-learn。
- PyTorch，必要时补充 Keras。
- tqdm、joblib、pooch、requests。

推荐环境管理：

- 本地：`conda` 或 `mamba`。
- 轻量项目：`uv` 或 `pip` + `venv`。
- 课程分发：同时提供 `environment.yml` 和 `requirements.txt`。

数据原则：

- 每章优先使用 1 到 10 MB 的小数据，保证课堂网络条件下可运行。
- 大数据通过下载脚本获取，并缓存到 `data/external/`。
- 所有数据必须注明来源、许可证、下载日期、预处理方法。
- 练习数据应尽量可公开再分发，避免版权和访问权限问题。

候选公开资源：

- Gaia Archive：星表、视差、自行、颜色星等图。
- SDSS：光谱、测光、星系图像。
- LAMOST：光谱分类和参数估计案例。
- TESS / MAST：光变曲线。
- Galaxy Zoo：星系形态教学样本。
- GWOSC：引力波教学数据。
- 教材自制模拟数据：保证作业稳定和可控。

## 8. 外部参照与差异化

主要参照：

- Python for Astronomers: https://prappleizer.github.io/
- Machine Learning for Physics and Astronomy, Viviana Acquaviva: https://press.princeton.edu/books/paperback/9780691206417/machine-learning-for-physics-and-astronomy
- Statistics, Data Mining, and Machine Learning in Astronomy / astroML: https://www.astroml.org/
- AstroML Interactive Book: https://www.astroml.org/astroML-notebooks/
- Python Data Science Handbook: https://jakevdp.github.io/PythonDataScienceHandbook/
- Introduction to Machine Learning with Python: https://www.oreilly.com/library/view/introduction-to-machine/9781449369880/
- AIMA: https://aima.cs.berkeley.edu/
- Deep Learning Book: https://www.deeplearningbook.org/
- 国家天文科学数据中心 Python in Astronomy 培训: https://hebl.china-vo.org/course/PIA2020/

本教材差异化：

- 面向中文天文与物理本科生，而不是计算机专业学生。
- 强调“科学问题 + 数据 + 模型 + 诊断 + 报告”的完整闭环。
- 保留 Linux/Git/Jupyter/可复现研究这些本科生容易缺失但科研必需的基础。
- 将生成式 AI 作为科研助手纳入规范训练，而不是回避或滥用。
- 每章都配 notebook、练习和可复现数据。

版权与授权注意：

- 若继续使用或改写 Python for Astronomers 的内容，必须遵守其 CC BY-NC-SA 4.0 授权，明确署名并保持兼容许可。
- 若计划商业出版，应避免直接依赖 CC BY-NC-SA 内容，改为完全重写并只作为参考引用。
- 所有图像、数据和 notebook 必须有明确许可证。
- 生成式 AI 生成的文字、代码和图片也要保留使用记录，并经过人工核查。

## 9. 写作里程碑

Milestone 0：仓库整理

- 修复 `main.tex` include 问题。
- 添加 `README.md`、`LICENSE`、`references.bib`。
- 添加 `notebooks/`、`data/`、`environments/`。
- 明确教材许可证。

Milestone 1：Part 0 与 Part I 重构

- 将通用 Python 基础内容下沉为 Part 0 先修模块。
- 把 Part I 收束为 Linux、Git、Jupyter、数据 I/O、绘图等科研工作流主线。
- 将现有章节改为统一格式，并明确正文默认前提。
- 补充每章 learning objectives、exercise、notebook。
- 完成授权检查和必要改写。
- 明确每章需要的图表清单，并补充基础图示、命令行截图或流程图。

Milestone 2：Part II 数据处理章节

- 先完成星表、FITS 图像、光谱、时间序列四条数据线。
- 每条数据线至少一个小数据集和一个 notebook。

Milestone 3：Part III 机器学习主线

- 建立统一 ML workflow。
- 完成回归、分类、评估、特征工程、无监督、异常检测章节。
- 所有模型使用 scikit-learn pipeline 规范。

Milestone 4：Part IV 案例项目

- 完成至少 4 个完整案例：Gaia、SDSS/LAMOST 光谱、光度红移、TESS。
- 每个案例包括数据说明、notebook、练习和报告模板。
- 每个案例至少包含数据探索图、模型诊断图和科学解释图。

Milestone 5：Part V 现代 AI 与 LLM

- 已启动；当前已完成 `ch30` 到 `ch38` 九章首稿，覆盖神经网络、二维/一维卷积、表示学习、Transformer、LLM 辅助科研编程、agentic workflow、LLM 辅助文献阅读，以及 AI 伦理与使用声明。
- 其中 `ch31` 已补上最小 transfer-learning workflow，并进一步补上 `cnn_transfer_workflow_demo`、quality gate、validation-calibrated routing，以及纯 Python 的 tiny trainable `Conv2d` learner；`ch32` 已补上 continuum normalization、quality gate、review queue、validation/test workflow，以及纯 Python 的 tiny trainable `Conv1d` learner。
- `ch33` 已补上 validation-calibrated anomaly workflow，并把 latent 维度与连续谱斜率 / Balmer 深度的可解释诊断、latent retrieval / anomaly triage、shared-patch conv-style autoencoder extension，以及 end-to-end Conv1d autoencoder 接回 notebook。
- `ch34` 已从 masked-token workflow 继续推进到可训练的 tiny self-attention masked-token learner，并进一步补上 bag-of-2-patches、pure Python 的 two-head masked-token extension，以及新的 masked-patch workflow / pretraining objective，保留 validation-calibrated confidence threshold 与 manual-review 路由。
- 后续继续补齐更真实的图像 CNN、规模更大的表示检索流程，并按需把 `ch32` 扩到更深光谱 CNN、把 `ch34` 再推进到更长序列、更稳定 patch vocabulary 与更完整的 block-level pretraining objective，同时把相关规范继续收束到 Part VI 的 capstone 模板。
- 建立 AI 使用声明模板和作业规范。

Milestone 6：Capstone 与试教

- `Part VI` 已启动，当前已完成 `ch39` 到 `ch59` 二十一章首稿。
- 形成 12 到 16 周课程大纲（教学版首稿已由 `ch44` 接入）。
- 设计期末项目评分 rubric（教学版首稿已由 `ch42` 接入）。
- 形成教师交接包（教学版首稿已由 `ch47` 接入）。
- 形成公开发布索引与课程维护清单（教学版首稿已由 `ch48` 接入）。
- 形成公开发布 QA 与课程采用说明（教学版首稿已由 `ch49` 接入）。
- 形成采用反馈与维护节奏（教学版首稿已由 `ch50` 接入）。
- 形成最终课程包索引与 Part VI 收束清单（教学版首稿已由 `ch51` 接入）。
- 形成课程包目录页与发布版本说明（教学版首稿已由 `ch52` 接入）。
- 形成开课前预检与学期重启清单（教学版首稿已由 `ch53` 接入）。
- 形成故障模式与升级处理手册（教学版首稿已由 `ch54` 接入）。
- 形成应急演练与替班教师接管手册（教学版首稿已由 `ch55` 接入）。
- 形成学期收尾与下一届 Warm Start（教学版首稿已由 `ch56` 接入）。
- 形成校友案例与导师接力（教学版首稿已由 `ch57` 接入）。
- 形成社群记忆与长期维护账本（教学版首稿已由 `ch58` 接入）。
- 形成外部合作边界与客座项目准入（教学版首稿已由 `ch59` 接入）。
- 找 3 到 5 名学生试跑 notebook（试教运行包首稿已由 `ch43` 接入）。
- 根据运行错误和学生反馈修订。

## 10. 16 周课程建议

课前预备：Part 0 Python 先修模块。

第 1 周：Linux、环境安装、Jupyter。

第 2 周：Git、项目目录规范、notebook 工作流。

第 3 周：NumPy、Pandas、Matplotlib。

第 4 周：Astropy、星表、坐标、HR 图。

第 5 周：FITS 图像、WCS、基础测光。

第 6 周：光谱数据、红移、谱线。

第 7 周：时间序列、周期搜索。

第 8 周：ML 基础、训练/验证/测试、baseline。

第 9 周：回归与光度红移。

第 10 周：分类与光谱/天体分类。

第 11 周：模型评估、交叉验证、数据泄漏。

第 12 周：无监督学习、PCA、聚类、异常检测。

第 13 周：神经网络与 CNN。

第 14 周：LLM 辅助科研编程和文献阅读。

第 15 周：Capstone 工作坊。

第 16 周：项目展示和总结。

## 11. 每章完成标准

每章完成前必须具备：

- 一份 LaTeX 正文章节。
- 一个可从头运行的 notebook。
- 一个小数据集或下载脚本。
- 3 到 5 个基础练习。
- 1 到 2 个进阶练习。
- 一节“常见错误与检查清单”。
- 一节“AI 助手如何使用与如何验证”。
- 参考文献和数据来源。
- 至少一次干净环境运行记录。

教材正文完成标准：

- 全文使用中文写作，术语首次出现时给出中英文对照。
- 每章有明确的科学问题或真实应用场景，而不是孤立讲工具。
- 概念解释、数学直觉、代码实现和科学解释之间要形成闭环。
- 每章至少包含 2 到 4 张有教学价值的图表；图表包括数据可视化、流程图、模型结构图、诊断图或结果解释图。
- 每张图必须在正文中被引用和解释。
- 每章必须包含“方法适用范围”和“常见误区”。
- 章节深度应达到本科高年级能够用于课程作业或科研入门项目的水平。

notebook 完成标准：

- 第一格说明环境和数据来源。
- 所有随机过程设置随机种子。
- 不依赖隐藏的本地绝对路径。
- 运行时间本科课堂可接受，核心 notebook 目标小于 5 分钟。
- 图表有标题、坐标轴、单位和说明。
- 最后一节解释结果，而不是只输出模型分数。

data 完成标准：

- 每个数据集放在清晰命名的子目录中。
- 每个数据集有独立 `README.md` 或集中索引条目。
- 说明数据来源、许可证、下载日期、字段含义、单位、样本量、预处理过程。
- 大数据只保留下载脚本和校验信息，不直接提交。
- notebook 中不得依赖未说明的本地私有数据。

## 12. 近期下一步

根据 2026-05-04 的实际完成状态，建议下一轮工作按这个顺序进行：

1. `Part I` 轻量二轮补强已经通过构建和 smoke test；若尚未提交，先提交当前 checkpoint。
2. `Part II` 第二轮教材化全章检查已经完成并形成本地提交 `0d5dcf1`；当前优先不是继续扩写，而是等待阅读反馈或同步书稿。
3. 如果需要同步书稿，先运行 `bash scripts/sync_book_to_overleaf.sh` dry-run，再运行 `bash scripts/sync_book_to_overleaf.sh --apply`，然后在 `../AIforAstronomers/` 单独提交并推送。
4. 用户正在阅读 `Part I`；等用户反馈后，再回到 `Part I` 做 Linux/Git/脚本/I/O/绘图的教材深度校订。
5. 若继续微调 `Part II`，优先补交叉引用、图表说明、练习分层、术语统一和 notebook 互引，而不是继续增加大量正文。

如果需要从当前状态直接恢复工作，优先入口为：

- `Roadmap.md` 的“当前进展快照（2026-05-04）”
- `book/main_zh.tex`
- `book/chapters/part1/README.md`
- `book/chapters/part1/ch01_unix_linux_scientific_computing.tex`
- `book/chapters/part1/ch02_git_reproducible_research.tex`
- `book/chapters/part1/ch04_libraries_scripts_jupyter.tex`
- `book/chapters/part1/ch06_data_io_fits.tex`
- `book/chapters/part1/ch08_plotting_scientific_figures.tex`
- `notebooks/part2_data_processing/README.md`
- `COURSE_PACKAGE_RELEASE_NOTES.md`
- `RELEASE_SYNC_CHECKLIST.md`
