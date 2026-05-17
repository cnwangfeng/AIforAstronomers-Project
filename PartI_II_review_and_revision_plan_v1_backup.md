# 《AI for Astronomers》Part I/II 深度评审与后期整合方案

> 评审对象：`AIforAstronomers-Project` 教材 Part I / Part II 及 Ch01 Linux 章节当前内容。  
> 评审重点：教材功能定位、章节层级、精确到节的修改意见、后续整合方案、Ch01 Linux 命令覆盖与深度评估。  
> 评审口径：从“教材”而不是“单个项目文档”出发，重点判断它是否能帮助天文/物理学生从基础工具过渡到可复查的数据分析与机器学习科研项目。

---

## 0. 总体判断

核心结论：

> **Part I/II 不应该继续大幅扩写，而应该被改造成“快速阅读 + 必做实操 + 进入 Part III 的闸门”。**

Part I/II 的功能不是替代 Linux、Git、Python、FITS、天文数据处理或误差分析教材，而是让学生具备进入机器学习科研项目所需的最低工作流能力和数据素养。

更准确地说：

1. **Part I：把学生从“会写一点代码/会敲几个命令”带到“会组织一个可复查的小型科研项目”。**
2. **Part II：把学生从“能打开数据文件”带到“能把数据组织成有单位、有误差、有选择条件、有解释边界的可建模样本”。**

因此，Part I/II 可以快速读，但不能被弱化为“可有可无的基础”。它们应当成为 Part III 机器学习之前的数据契约和工作流闸门。

---

## 1. Part I/II 总体评审意见

### 1.1 最大优点

Part I/II 已经不是普通“工具入门”，而是在围绕科研证据链组织内容。

Part I 的设计重心是：

- Unix/Linux：项目目录、命令、日志、脚本、远程环境；
- Git：版本时间轴与可复查修改；
- Python 脚本/Jupyter：从探索走向可重跑入口；
- 文件 I/O/FITS：数据入口与字段/header 契约；
- 科学图表：把输出变成可以支持 claim 的证据。

Part II 的设计重心是：

- 误差与单位；
- 星表与 HR 图；
- 图像、FITS 与 WCS；
- 光谱、谱线与红移；
- 时间序列与周期信号；
- 物理模型拟合与模拟数据；
- 最终收束到可建模样本。

这个总结构是合理的，尤其适合“AI for Astronomers”这种教材，因为学生需要的不是单纯 Python 教程，而是从数据、物理含义、处理流程、模型输入到结果解释的一整条链。

### 1.2 最大问题

当前 Part I/II 的问题不是“太浅”，而是：

> **读者负担层次还不够清楚。**

对学生来说，Part I/II 中至少有三类内容：

| 类型 | 应该如何读 | 示例 |
|---|---|---|
| 必须理解 | 快速精读 | 项目目录、Git 时间轴、数据契约、误差、单位、图表证据 |
| 必须操作 | notebook / 课堂练习 | 建目录、提交 Git、读入数据、画图、写 record |
| 可按方向选读 | 项目需要时再深入 | 光谱、时间序列、WCS、物理拟合、模拟数据 |

现在这些层次有时混在一起。学生可能误以为每一节都同等重要，于是 Part I/II 显得很长；也可能只快速浏览，错过真正进入 Part III 前必须掌握的证据链。

### 1.3 总体修改原则

建议后续修改遵循四条原则：

1. **不扩成百科。** Part I/II 不要补成完整 Linux/Git/天文数据处理教材。
2. **每章明确“快读内容”和“必须交付内容”。**
3. **每章末尾增加 Exit Gate。** 学生只有通过本章最低交付，才算能进入后续。
4. **Part II 必须显式接到 Part III。** 每类数据最后都要说明：如果进入机器学习，它会变成什么特征、标签、样本、误差或选择效应。

---

## 2. 后期整体整合方案

### 2.1 为 Part I/II 增加统一章首卡片

每章开头建议加入固定格式：

```markdown
### 本章阅读方式

- 阅读层级：快读 / 精读 / 项目方向选读
- 建议时间：正文 30–60 分钟，实操 1–2 小时
- 必须掌握：3–5 条
- 可先跳过：若干高级或方向性内容
- 本章交付：一个 record 或 evidence packet
- 接到 Part III 的方式：说明它如何影响特征、标签、评估或复现
```

这样可以明确告诉学生：Part I/II 不是每一节都要像数学教材那样精读，但每章都有一个最低交付。

### 2.2 每章末尾增加 Exit Gate

每章末尾建议增加：

```markdown
### Exit Gate：进入下一阶段前必须能做到

1. 我能否用自己的话说明本章保护的是哪类科研风险？
2. 我是否完成了本章 record？
3. 我的 record 是否包含输入、处理、输出、诊断和限制？
4. 如果把本章结果交给机器学习模型，我知道哪些信息不能丢吗？
```

Part I 的 Exit Gate 偏工作流；Part II 的 Exit Gate 偏数据契约。

### 2.3 增加统一模板：`evidence_record_template.md`

建议将 Part I/II 的所有记录统一成一个模板族：

```markdown
# Evidence Record Template

## 1. Input
数据/文件/代码从哪里来？

## 2. Operation
做了什么处理？

## 3. Output
生成了什么结果？

## 4. Check
如何检查结果不是偶然或错误？

## 5. Limit
当前结果不能支持什么？

## 6. Reuse in ML
如果进入机器学习，它会成为特征、标签、样本、评估对象，还是复现记录？
```

Part I/II 现在已经有 command log、data intake record、figure record、measurement record、HR diagram record、photometry record、spectrum record、period record、model fit record 等雏形。建议把这些 record 统一收束到一个 Evidence Record 家族中。

---

# 3. Part I 详细评审与修改意见

## 3.1 Part I 总体定位

### 当前定位

Part I 当前定位非常清楚：它不是工具清单，而是科研计算工作流地基。导读中已经列出五章递进链：Linux 建目录和日志，Git 建版本历史，脚本/Jupyter 建可重跑入口，I/O 建字段和元数据契约，绘图建图表证据。

### 评审意见

Part I 应该被定义为：

> **可复现科研项目的最低操作系统。**

不要求学生成为系统管理员、软件工程师或数据工程师，但必须能维护一个小型项目，使别人可以复查：

- 数据在哪里；
- 代码怎么跑；
- 结果从哪里来；
- 中间检查留下了什么；
- 哪一步可能出错。

### 整体修改建议

Part I 保留五章结构，不建议新增大章。需要做的是：

1. 每章减少工具百科感。
2. 增加“本章最小交付”。
3. 每章都显式接到 capstone evidence cards。
4. 将 Ch06 与 Part II 的边界划清：Ch06 只讲“数据入口协议”，不要提前承担完整天文数据处理。

---

## 3.2 Part I 导读：修改意见

### 当前优点

导读已经说明 Part I 的目标是建立最小科研计算工作流，并且列出每章交付件：Linux 运行记录、Git 版本记录、脚本运行记录、data intake record、figure record。

### 主要问题

导读还可以更明确告诉学生：

- 哪些章节可以快读；
- 哪些任务必须动手；
- Part I 结束时必须交付什么；
- Part I 与 Part III 的关系是什么。

### 建议修改到节

#### `第一部分导读：把计算环境变成科研工作流`

保留。

#### `正文和训练材料如何分工`

建议加强为：

```markdown
### 正文、notebook 与交付件如何分工

- 正文：解释为什么这样做。
- notebook/命令练习：训练如何做。
- record：证明你做过，并且别人能复查。
```

#### `本部分的学习顺序`

保留，但增加一列“阅读层级”：

| 章节 | 阅读层级 | 必须交付 |
|---|---|---|
| Ch01 Linux | 快读 + 必做 | command log |
| Ch02 Git | 快读 + 必做 | commit history + tag |
| Ch04 脚本/Jupyter | 精读 + 必做 | reproducible script |
| Ch06 I/O/FITS | 精读 + 必做 | data intake record |
| Ch08 绘图 | 精读 + 必做 | figure record |

#### `每章最终要交出的证据`

保留，并加一句：

> Part I 的评分重点不是命令数量，而是证据链是否可复查。

#### `进入下一部分前的自检`

建议改名为：

```markdown
### Part I Exit Gate：进入数据处理前的最低要求
```

并把自检改成更可评分的 checklist。

---

## 3.3 Ch01 Unix/Linux 与科研计算环境

### 当前评审

这一章的思想非常好：不是背命令，而是建立“先定位、再检查、再操作、再记录、最后自动化”的科研计算习惯。当前章节已经把 Linux 定义为科研计算工作流的最低层接口，并强调文件、目录、命令、日志和可复查证据。

### 主要问题

这一章容易过长，因为 Linux 命令天然可以无限扩展。教材应该避免变成“命令大全”。

### 建议修改到节

#### `本章导读：从会敲命令到会组织科研工作`

保留。建议增加一句：

> 本章不是 Linux 完整教程，而是科研项目目录、命令记录和安全批处理的最低训练。

#### `学习目标与训练目标`

建议拆成两组：

```markdown
### 概念目标
- 路径、shell、命令、参数、重定向、管道、权限、进程、远程环境。

### 交付目标
- 建立项目目录。
- 完成一次只读检查。
- 保存一次运行日志。
- 写一个最小 shell 脚本。
```

#### `为什么科研工作离不开命令行`

保留，但控制篇幅。不要扩写 HPC、容器、集群管理细节；这些可以放到高级提示框。

#### `贯穿本章的微型项目`

建议前移，放在学习目标之后。学生应先看到项目结构，再学命令。

#### `Shell：你和操作系统之间的解释器`

保留，但建议加入一个“危险解释”小表：

| 输入 | shell 实际做了什么 | 风险 |
|---|---|---|
| `*.fits` | 展开成文件列表 | 可能匹配过多 |
| `> output.txt` | 覆盖输出文件 | 可能覆盖旧结果 |
| `"*.fits"` | 保留字符串 | 可能没有匹配 |

#### `一条命令的解剖`

保留。建议增加固定读法：

```markdown
命令 = 程序 + 选项 + 输入对象 + 输出位置 + 是否改变状态
```

#### `帮助系统：把不会用变成会查`

保留，但弱化 `man` 的篇幅。对本科生更实际的是：

- `--help`
- `history`
- `which`
- `type`
- 查官方文档或课程 cheat sheet

#### `文件系统：所有操作都从路径开始`

保留。建议作为本章核心节之一。

#### `目录导航：不要在文件系统里迷路`

保留，但增加一个小练习：

```markdown
给出当前目录，判断以下相对路径是否正确。
```

#### `查看目录内容：从文件名读出项目状态`

保留。建议强化“时间戳”和“文件大小”对科研结果的意义。

#### `创建、复制、移动和删除`

保留，但必须加安全规则：

```markdown
任何批量写操作前，必须有预览命令。
```

#### `通配符与引号`

保留。建议与“批量操作安全”合并或至少前后互相引用。

#### `查看文件内容`

保留。建议明确：这是后续读 CSV、日志、manifest 的基础。

#### `搜索`

保留，但 `grep/rg/find` 不要展开太多参数。

#### 建议新增节：`本章最低交付：command log`

```markdown
### 本章最低交付：command log

必须包含：
1. 项目根目录路径；
2. 原始数据目录；
3. 关键只读检查命令；
4. 一条写操作及其预览；
5. 一个保存的日志文件；
6. 本章风险说明。
```

---

## 3.4 Ch02 Git 与可复现科研

### 当前评审

这一章的定位非常正确：Git 不是备份工具，而是科研时间轴。对本教材而言，Git 的最低目标应该是：

> 学生能把一次科研结果冻结在一个可追踪 commit/tag 上。

### 主要问题

Git 对初学者最容易过载。不要把 branch、merge、remote、conflict 全部讲成同等重要。

### 建议修改到节

#### `本章导读：Git 不是备份工具，而是科研时间轴`

保留。

#### `学习目标与训练目标`

建议分层：

```markdown
### 必须掌握
- status
- diff
- add
- commit
- log
- .gitignore
- tag

### 课堂了解
- branch
- merge
- remote

### 项目需要再学
- conflict
- pull request
- collaborative workflow
```

#### 建议新增节：`Git 追踪什么，不追踪什么`

必须明确：

- 追踪代码、说明文档、小型配置；
- 不追踪大数据、临时输出、缓存文件；
- notebook 是否保留输出要有课程政策；
- results 可以保留小型最终图，不保留大批中间结果。

#### 建议新增节：`一次科研提交应该长什么样`

加入 commit message 模板：

```text
ch11: add HR diagram filtering and figure record

- add parallax quality cut
- regenerate HR diagram
- update hr_record.txt
- note selection-effect limitation
```

#### 建议新增节：`tag：冻结一次可评分结果`

这是连接 capstone 的关键节。学生应学会：

```bash
git tag -a part1-checkpoint -m "Part I workflow checkpoint"
```

#### 建议弱化节：`branch 与 merge`

保留概念即可，不建议在基础 Part I 中训练复杂协作流程。真实多人协作可放 Part VI 或教师/TA 指南。

#### 建议新增节：`本章最低交付：version record`

```markdown
### 本章最低交付：version record

必须包含：
1. `git status` 干净截图或文本；
2. 至少 3 个有意义 commit；
3. `.gitignore`；
4. 一个 tag；
5. 说明哪个 commit 生成了哪个结果图或 record。
```

---

## 3.5 Ch04 库、脚本与 Jupyter

### 当前评审

这一章是 Part I 中最关键的一章，因为它把“会写代码”转成“会交付工作流”。它需要解决学生最常见的问题：

- notebook 里跑通了，但无法从头复跑；
- notebook 单元顺序混乱；
- 图表由哪个单元生成不清楚；
- 依赖环境没有记录；
- 探索代码没有变成脚本入口。

### 建议修改到节

#### `本章导读：从会写代码到会交付工作流`

保留。

#### 建议新增节：`Notebook、script、module 的分工`

| 形态 | 用途 | 不适合做什么 |
|---|---|---|
| Notebook | 探索、解释、展示 | 作为唯一生产入口 |
| Script | 可重跑任务 | 写大量交互解释 |
| Module | 可复用函数 | 直接存放项目叙事 |
| README | 说明入口 | 替代代码 |

#### 建议新增节：`从 notebook 到 script 的转换流程`

```markdown
1. 在 notebook 中探索。
2. 标记稳定单元。
3. 抽出函数。
4. 写成 script。
5. 用命令行运行。
6. 保存 log。
7. 更新 README。
8. commit。
```

#### 建议新增节：`环境记录不是附属品`

至少要求学生记录：

- Python 版本；
- 关键库版本；
- 运行入口；
- 随机种子；
- 相对路径；
- 输出目录。

#### 建议新增节：`参数、随机种子和输出路径`

这节非常重要。后面机器学习会高度依赖随机种子和参数记录。

#### 建议新增节：`本章最低交付：reproducible script`

```markdown
### 本章最低交付：reproducible script

必须包含：
1. 一个 notebook；
2. 一个能从命令行运行的 `.py` 脚本；
3. 一个 `README` 说明运行方式；
4. 一个运行日志；
5. 一个说明 notebook 与 script 分工的段落。
```

---

## 3.6 Ch06 文件 I/O、FITS 与科学数据入口

### 当前评审

这一章的核心观点非常好：I/O 不是“文件能打开”，而是科学数据工作流的第一道质量控制。

### 主要问题

这一章和 Part II 的边界需要更清楚。Ch06 应该只负责“数据入口协议”，不要提前变成完整 FITS、WCS、图像、星表处理章。否则它会和 Ch11、Ch12 重叠。

### 建议修改到节

#### `本章导读：读入文件之前，先读懂数据`

保留。

#### `学习目标与训练目标`

保留，但加一句：

> 本章只建立通用数据入口，不完成完整科学分析。

#### 建议新增节：`数据入口七问`

```markdown
1. 文件从哪里来？
2. 文件格式是什么？
3. 一行/一个像素/一个数组元素代表什么？
4. 字段或 header 是否满足契约？
5. 单位是什么？
6. 缺失、异常、质量标记在哪里？
7. 后续分析会使用哪些列或数组？
```

#### 建议压缩节：`FITS 格式`

只讲：

- header；
- data；
- HDU；
- 最小检查；
- 为什么天文常用 FITS。

WCS、背景、孔径测光应留给 Ch12。

#### 建议新增节：`data intake record 模板`

```markdown
### Data Intake Record

- 文件名：
- 来源：
- 许可证/使用限制：
- 格式：
- 字段/header：
- 单位：
- 缺失值：
- 质量标记：
- 后续使用列：
- 当前不能支持的解释：
```

#### 建议新增节：`本章最低交付：data intake record`

这是 Part I 到 Part II 的桥。

---

## 3.7 Ch08 可视化与科研图表

### 当前评审

这一章非常适合作为 Part I 收束。它应该坚持“图表作为证据”的方向，少讲样式技巧，多讲图表如何支持 claim。

### 建议修改到节

#### `本章导读：图表是科学论证，不是装饰`

保留。

#### 建议新增节：`图表选择决策树`

```markdown
比较两个连续变量 → 散点图
看分布 → 直方图 / KDE
看时间变化 → 折线图 / 带误差点图
看图像阵列 → image + colorbar
看模型错误 → residual plot
看分类混淆 → confusion matrix
```

#### 建议新增节：`图表自审清单`

```markdown
- 横纵轴是否有变量和单位？
- 样本筛选是否写清楚？
- 颜色是否有物理含义？
- 坐标范围是否造成误导？
- 是否需要误差条？
- 图注是否说明 claim 和 limit？
```

#### 建议新增节：`本章最低交付：figure record`

```markdown
### Figure Record

- 图文件：
- 生成脚本：
- 输入数据：
- 代码版本：
- 图表类型：
- 支持的 claim：
- 不能支持的解释：
```

---

# 4. Part II 详细评审与修改意见

## 4.1 Part II 总体定位

### 当前定位

Part II 是从“代码能不能跑”进入“数据是什么物理量记录”的转折点。它要求学生反复追问单位、误差、坐标、采样、选择条件和科学判断。

### 评审意见

Part II 应该定义为：

> **从数据类型到可建模样本的转换训练。**

它不是完整天文数据处理课，而是机器学习前必须有的数据理解课。Part II 的目标不是让所有学生掌握所有天文数据类型，而是让学生形成统一判断：

```markdown
数据对象是什么？
单位和误差是什么？
经过了什么处理？
结果能支持什么？
如果进入机器学习，会变成什么特征/标签/样本？
```

### 整体修改建议

Part II 可以分成：

| 层级 | 章节 | 建议 |
|---|---|---|
| 必修 | Ch10 误差与单位 | 所有人必须精读 |
| 推荐必修 | Ch11 星表与 HR 图 | 最适合作为 Part II 主案例 |
| 方向选读 | Ch12 图像、Ch13 光谱、Ch14 时间序列 | 根据实习方向选 |
| 物理/实验方向选读 | Ch15 模型拟合与模拟数据 | 物理类学生强烈建议读 |
| 必修收束 | Part II synthesis | 所有人必须读 |

---

## 4.2 Part II 导读：修改意见

### 当前优点

导读已经给出五类数据的共同阅读框架：对象、坐标、单位和误差、处理算法、解释边界。

### 主要问题

还需要更明确告诉学生：不同实习方向可以选学不同数据类型，但 Ch10 和收束章不可跳。

### 建议修改到节

#### `第二部分导读：把数据类型读成科学证据`

保留。

#### `正文和训练材料如何配合`

保留，但增加：

```markdown
Part II 的正文可以快读，但每位学生至少要完成一种数据类型的完整 evidence packet。
```

#### `本部分为什么先讲误差和单位`

保留。这个顺序非常正确。

#### `五类数据的共同阅读框架`

保留，并升级成全 Part II 的标准模板。

#### 建议新增节：`不同实习方向的选学路径`

```markdown
### 选学路径

- 星表/恒星方向：Ch10 + Ch11 + synthesis
- 图像/星系/目标检测方向：Ch10 + Ch12 + Ch08 回看 + synthesis
- 光谱方向：Ch10 + Ch13 + synthesis
- 时域方向：Ch10 + Ch14 + synthesis
- 物理实验/模拟方向：Ch10 + Ch15 + synthesis
```

#### `Part II 如何接向机器学习`

保留并加强。建议增加：

```markdown
### Part II 到 Part III 的数据契约

进入机器学习前，每个样本至少要说明：
- sample_id
- input features
- label or target
- uncertainty or quality flag
- selection rule
- preprocessing history
- excluded cases
```

---

## 4.3 Ch10 科学数据、误差与单位

### 当前评审

这章应该是 Part II 的必修核心。它需要比其他 Part II 章节更“理论化”一点，因为它是后面 HR 图、测光、红移、周期、拟合的共同基础。

### 建议修改到节

#### `本章导读：一个数字什么时候才算科学结果`

保留。

#### `学习目标`

建议保留现有随机误差、系统误差、视差距离、误差传播、单位检查、数量级检查等目标，并增加：

- 有效数字；
- 相对误差；
- 信噪比；
- 低信噪比下公式反演的风险；
- 系统误差不能靠重复测量自动消失。

#### `训练目标与贯穿微型项目`

保留。视差测量小例子很好。

#### 建议新增节：`测量值、派生量、模型量`

| 类型 | 例子 | 风险 |
|---|---|---|
| 测量值 | 视差、星等、流量 | 受仪器和观测条件影响 |
| 派生量 | 距离、绝对星等、颜色 | 公式适用范围 |
| 模型量 | 温度、质量、年龄 | 依赖模型假设 |

#### 建议新增节：`误差传播的最小公式`

建议用一元函数开始：

\[
\sigma_y \approx \left|\frac{dy}{dx}\right|\sigma_x
\]

再给出视差距离例子。

#### 建议新增节：`单位检查工作流`

```markdown
1. 写出输入单位。
2. 写出公式。
3. 推导输出单位。
4. 检查数量级。
5. 写出适用条件。
```

#### 建议新增节：`本章最低交付：measurement record`

```markdown
### Measurement Record

- 原始测量值：
- 单位：
- 不确定度：
- 使用公式：
- 派生量：
- 误差传播：
- 数量级检查：
- 适用边界：
```

---

## 4.4 Ch11 表格数据、星表与 HR 图

### 当前评审

这章非常适合作为 Part II 的主案例。它把表格字段、视差、距离模数、颜色指数、绝对星等、HR 图结构、筛选条件和选择效应连在一起。

### 主要问题

这章可以承担 Part II 的“样板章”。因此它需要特别强调：

- 从原始列到派生列；
- 从派生列到图；
- 从图到物理解释；
- 从图到机器学习特征。

### 建议修改到节

#### `本章导读：从星表行列到恒星物理图像`

保留。

#### `学习目标`

保留星表、表观星等、视差、颜色指数、绝对星等、HR 图、主序星/巨星/白矮星、选择效应等目标。

#### `训练目标与贯穿微型项目`

保留。项目结构包括 data、notebook、script、figures、results，很好。

#### 建议新增节：`星表字段契约`

```markdown
每一列必须说明：
- 字段名
- 物理含义
- 单位
- 缺失值
- 质量标记
- 是否进入后续特征
```

#### 建议新增节：`从视差到距离：只在适用条件下使用`

需要强调：

```markdown
d(pc) = 1 / parallax(arcsec)
```

但要说明低信噪比视差不能机械反演。

#### 建议新增节：`从观测量到派生特征`

```markdown
原始列：parallax, apparent magnitude, color
派生量：distance, absolute magnitude, color index
ML 特征：color, absolute magnitude, quality flags
```

#### 建议新增节：`HR 图不是标签本身`

学生容易把图上区域当成天然标签。建议强调：

- 主序/巨星/白矮星区域是解释结构；
- 若作为标签，需要明确判定规则；
- 边界样本不能随意硬分。

#### 建议新增节：`本章最低交付：HR diagram record`

```markdown
### HR Diagram Record

- 使用字段：
- 筛选条件：
- 距离/绝对星等公式：
- 图像文件：
- 图上结构解释：
- 选择效应：
- 可进入机器学习的特征：
```

---

## 4.5 Ch12 天文图像、FITS 与 WCS

### 当前评审

这章的导读很好，尤其是“像素还不是天文测量”这一点。图像章应保持“最小图像测量链条”，不要滑向复杂天文图像处理课程。

### 建议修改到节

#### `本章导读：像素为什么还不是天文测量`

保留。

#### 建议新增节：`显示图像不等于测量图像`

```markdown
imshow 只是显示；
测量需要：
- 背景
- aperture
- 单位
- 坐标
- 误差或质量说明
```

#### 建议新增节：`FITS header 的最低检查`

```markdown
必须检查：
- NAXIS / NAXIS1 / NAXIS2
- 单位相关 keyword
- WCS 相关 keyword
- 观测时间/滤光片/曝光时间
```

#### 建议新增节：`WCS 的最小线性直觉`

不要展开完整 WCS 标准，只讲：

```markdown
像素坐标 → 参考像素 → 角尺度 → 天球坐标近似
```

#### 建议新增节：`孔径测光公式`

建议明确：

\[
F_{\mathrm{net}} = \sum_{\mathrm{aperture}} I_i - N_{\mathrm{aperture}} \cdot B
\]

并解释每一项。

#### 建议新增节：`从图像到机器学习输入`

```markdown
图像进入模型前必须记录：
- cutout 大小
- background subtraction
- normalization
- mask
- pixel scale
- label source
```

#### 建议新增节：`本章最低交付：photometry record`

```markdown
### Photometry Record

- FITS 文件：
- header 检查：
- WCS 检查：
- aperture 设置：
- background 方法：
- net flux：
- 图像显示参数：
- 限制：
```

---

## 4.6 Ch13 光谱数据、谱线与红移

### 当前评审

这章的定位很好：光谱不是普通二维表，而是一条带物理秩序的一维数据。光谱章需要特别防止学生形成“找最高峰/最低谷”的粗糙理解。

### 建议修改到节

#### `本章导读：沿着波长轴读出物理线索`

保留。

#### 建议新增节：`光谱轴的契约`

```markdown
- wavelength 单位
- flux 单位
- 采样间隔
- 分辨率
- 是否已校准
- 是否已归一化
```

#### 建议新增节：`连续谱处理不是装饰`

说明连续谱归一化会改变线深、等效宽度和分类特征。

#### 建议新增节：`红移判断不能只靠一条线`

```markdown
单线识别风险：
- 线身份误认
- 噪声峰
- sky line residual
- 分辨率不足
```

#### 建议新增节：`光谱进入机器学习前的记录`

```markdown
- 波长网格
- 重采样方式
- 归一化方式
- masking
- label source
- S/N
```

#### 建议新增节：`本章最低交付：spectrum record`

```markdown
### Spectrum Record

- 波长单位：
- 流量单位：
- 连续谱处理：
- 候选谱线：
- 红移计算：
- 多线一致性：
- S/N 或质量判断：
- 限制：
```

---

## 4.7 Ch14 时间序列、采样与周期信号

### 当前评审

这章的导读非常准确：周期不是最高峰，而是需要检验的假设。时间序列章必须让学生理解：

> 时间序列的核心不是 y 值，而是 y 与 t 的共同结构。

### 建议修改到节

#### `本章导读：周期不是最高峰，而是一个需要检验的假设`

保留。

#### 建议新增节：`时间戳是数据的一部分`

```markdown
两组 brightness 一样，但 time 不一样，物理解释可能完全不同。
```

#### 建议新增节：`候选周期搜索的最小逻辑`

```markdown
1. 设定周期范围。
2. 对每个周期计算拟合分数。
3. 排序候选周期。
4. 画 period score。
5. 画 phase folded curve。
6. 检查 alias。
```

#### 建议新增节：`不要只报告 best period`

必须报告：

- 最佳周期；
- 次优周期；
- 差距；
- 采样窗口；
- alias 风险；
- 相位折叠图。

#### 建议新增节：`时间序列进入机器学习前的记录`

```markdown
- cadence
- duration
- missing pattern
- normalization
- period feature
- amplitude feature
- label source
```

#### 建议新增节：`本章最低交付：period record`

```markdown
### Period Record

- 数据时间跨度：
- 候选周期范围：
- best period：
- second-best period：
- phase-folded plot：
- alias 风险：
- 物理解释：
- 限制：
```

---

## 4.8 Ch15 物理实验、模型拟合与模拟数据

### 当前评审

这章对物理学生很重要，因为它把数据分析从“描述现象”推向“约束机制模型”。它也应该成为 Part II 到 Part III 的关键桥梁：自然引出“物理模型 vs 数据驱动模型”。

### 建议修改到节

#### `本章导读：拟合曲线不是终点，解释参数才是目标`

保留。

#### 建议新增节：`前向模型、参数和观测`

```markdown
观测数据 = 模型预测 + 噪声 + 系统误差
```

#### 建议新增节：`残差图比拟合曲线更重要`

强调：

- 曲线贴合不代表模型正确；
- 残差结构能暴露模型失败；
- 误差条决定 \(\chi^2\) 的解释。

#### 建议新增节：`Monte Carlo 不确定度`

最小可操作流程：

```markdown
1. 根据误差扰动数据。
2. 重复拟合。
3. 得到参数分布。
4. 报告中位数和区间。
```

#### 建议新增节：`物理模型与机器学习 baseline`

| 方法 | 优点 | 风险 |
|---|---|---|
| 物理模型 | 参数有解释 | 可能模型假设错 |
| 多项式/ML | 拟合灵活 | 参数未必有物理意义 |

#### 建议新增节：`本章最低交付：model fit record`

```markdown
### Model Fit Record

- 模型公式：
- 参数含义和单位：
- 拟合方法：
- 残差图：
- \(\chi^2\) 或误差指标：
- Monte Carlo 区间：
- baseline 比较：
- 解释边界：
```

---

## 4.9 Part II 收束章

### 当前评审

Part II 收束章应从“原始或教学数据”收束到“可解释、可检查、可建模的样本”。如果输入的物理含义、误差来源、采样边界和选择效应没有整理清楚，后面复杂算法只会在混乱基础上给出更复杂的混乱。

### 建议修改到节

#### `第二部分收束：从数据处理到可建模样本`

保留。

#### `本部分的微型项目链`

保留。

#### 建议新增节：`Part II Exit Gate`

```markdown
### Part II Exit Gate：进入机器学习前必须完成

1. 我有一个样本表或样本集合。
2. 每个样本有 sample_id。
3. 每个特征知道来源。
4. 每个标签知道来源。
5. 每个筛选条件写清楚。
6. 误差或质量标记没有被丢掉。
7. 图表或残差支持当前处理结果。
8. 当前数据不能支持什么结论已写明。
```

#### 建议新增节：`Data Card v0.1`

```markdown
# Data Card v0.1

## Dataset
名称、来源、许可证、版本。

## Sample Definition
一行/一个图像/一条光谱/一个时间序列代表什么？

## Inputs
进入模型的变量或数组。

## Target / Label
预测目标或标签来源。

## Uncertainty / Quality
误差、质量标记、缺失值。

## Selection
筛选条件和选择效应。

## Preprocessing
归一化、重采样、背景扣除、派生列。

## Known Limits
不能支持的解释。
```

---

# 5. 建议后的 Part I/II 新结构

## 5.1 Part I：科研计算基础

```markdown
Part I 导读：把工具学成科研工作流

Ch01 Unix/Linux 与科研计算环境
- 本章导读
- 学习目标与交付目标
- 微型项目
- 路径与目录
- 命令结构与 shell
- 只读检查
- 批量操作安全
- 日志与脚本
- Exit Gate：command log

Ch02 Git 与可复现科研
- 本章导读
- Git 时间轴模型
- status/diff/add/commit
- .gitignore
- log/tag
- Git 与 notebook/results
- Exit Gate：version record

Ch04 库、脚本与 Jupyter
- 本章导读
- notebook/script/module 分工
- 从 notebook 到 script
- 环境与依赖记录
- 参数、随机种子、输出路径
- Exit Gate：reproducible script

Ch06 文件 I/O、FITS 与科学数据入口
- 本章导读
- 数据入口七问
- CSV/text/FITS 最小读取
- 字段/header 契约
- 缺失值、单位、质量标记
- Exit Gate：data intake record

Ch08 可视化与科研图表
- 本章导读
- 图表类型选择
- 变量、单位、尺度、误差
- claim--evidence--limit
- 图表自审清单
- Exit Gate：figure record

Part I synthesis
- workflow packet
```

## 5.2 Part II：天文/物理数据处理

```markdown
Part II 导读：把数据类型读成科学证据
- 五类数据共同框架
- 选学路径
- Part II 到 Part III 的数据契约

Ch10 科学数据、误差与单位
- 测量值、派生量、模型量
- 随机误差与系统误差
- 单位检查
- 误差传播
- 视差例子
- Exit Gate：measurement record

Ch11 表格数据、星表与 HR 图
- 星表字段契约
- 视差、距离、绝对星等
- HR 图
- 筛选与选择效应
- ML 特征来源
- Exit Gate：HR diagram record

Ch12 天文图像、FITS 与 WCS
- 像素不是测量
- header/data/WCS
- 背景估计
- 孔径测光
- 图像进入 ML 的记录
- Exit Gate：photometry record

Ch13 光谱数据、谱线与红移
- 波长轴与流量轴
- 连续谱与归一化
- 谱线识别
- 红移估计
- 光谱进入 ML 的记录
- Exit Gate：spectrum record

Ch14 时间序列、采样与周期信号
- 时间戳与采样
- 候选周期搜索
- 相位折叠
- alias 检查
- 时间序列进入 ML 的记录
- Exit Gate：period record

Ch15 物理实验、模型拟合与模拟数据
- 前向模型
- 参数与单位
- 残差与 chi-square
- Monte Carlo 不确定度
- 物理模型 vs ML baseline
- Exit Gate：model fit record

Part II synthesis
- evidence packet
- Data Card v0.1
- Part III readiness checklist
```

---

# 6. Ch01 Linux 当前内容专项评审

## 6.1 结论：命令覆盖是否足够？

结论：

> **当前 Ch01 的 Linux 命令覆盖已经足够，甚至对本科入门教材而言偏完整；不建议继续大幅增加命令数量。**

当前 Ch01 已经覆盖了以下核心能力：

| 能力 | 当前已有命令/概念 | 评价 |
|---|---|---|
| 定位环境 | `pwd`, `hostname`, `which python`, `python --version` | 足够 |
| 查看目录 | `ls`, `ls -l`, `ls -lh`, `ls -lt` | 足够 |
| 目录切换 | `cd`, `.`, `..`, 绝对/相对路径 | 足够 |
| 创建目录 | `mkdir -p` | 足够 |
| 复制/移动/删除 | `cp`, `mv`, `rm`, `find ... -delete` | 足够，但需强调安全边界 |
| 通配符与引号 | `*.fits`, `"*.fits"`, `?` | 足够 |
| 查看文本 | `head`, `tail`, `wc -l`, `less` | 足够 |
| 搜索文件 | `find`, `find -name` | 足够 |
| 搜索内容 | `grep`, `grep -R`, `rg` | 足够 |
| 文本统计 | `cut`, `sort`, `uniq -c`, `sed` | 对入门而言已经偏深 |
| 重定向 | `>`, `>>`, `2>`, `$?` | 很好，科研记录意识强 |
| 管道 | `|`, `tee` | 很好，应保留 |
| 环境检查 | `which`, `type`, `PATH`, `export`, `alias` | 很好 |
| 权限 | `ls -l`, `chmod u+x`, `chmod 755` | 足够 |
| 远程 | `ssh`, `scp` | 基础够用 |
| 进程/长任务 | `ps`, `top`, `time` | 基础够用 |
| 脚本 | shebang, `set -euo pipefail`, `./script.sh` | 对初学者很有价值 |
| 归档 | `tar -czf`, `tar -tzf` | 合理 |
| 运行记录 | `date`, `pwd`, log 文件 | 很好 |

从“学生能否进入后续科研项目”的角度看，当前命令集已经能完成：

1. 建立项目目录；
2. 定位输入数据；
3. 检查日志和文件数量；
4. 批量处理文件列表；
5. 保存证据；
6. 运行脚本；
7. 检查远程环境；
8. 打包阶段性结果。

这已经满足 Part I 作为“科研计算最低工作流”的要求。

---

## 6.2 当前深度是否足够？

结论：

> **概念深度足够，甚至超过普通入门 Linux 章；但教材层级还需要更清楚。**

当前 Ch01 的深度优点在于，它没有停留在“`ls` 是列文件、`cd` 是切目录”的层面，而是已经讲到了：

- shell 如何解释命令；
- 通配符与引号的差异；
- 重定向与覆盖风险；
- 标准输出、标准错误、退出状态；
- `PATH` 与环境变量；
- 权限与可执行脚本；
- 远程环境中的本地/远程路径混淆；
- 长任务日志；
- `set -euo pipefail`；
- 归档与检查归档内容。

这说明该章已经不是浅层命令教程，而是“科研命令行工作流”教程。

但问题在于：

> **目前它对学生来说可能显得“每一节都重要”，缺少核心/选读/了解的分层。**

例如：

- `pwd`, `ls`, `cd`, `find`, `head`, `tail`, `grep`, `>`, `|`, `tee` 是必须掌握；
- `sed`, `xargs`, `chmod 755`, `tar`, `set -euo pipefail` 是课堂了解或项目中逐步掌握；
- `ps`, `top`, `scp`, `ssh` 对有远程服务器实践的学生很重要，但对本地 notebook 课程可暂时降低要求。

所以，这章需要的不是“加深”，而是“分层”。

---

## 6.3 当前 Ch01 中最值得保留的内容

### 6.3.1 “先定位，再检查，再操作，再记录，最后自动化”

这是本章最重要的教学原则，应该保留并在章末反复强调。

建议把它升级为本章核心算法：

```markdown
Linux 科研工作流最小算法：
1. 定位环境：hostname, pwd, which python
2. 定位输入：ls, find, head, wc
3. 预览操作对象：ls / find / echo
4. 执行最小操作：cp / mv / script
5. 保存证据：>, >>, tee, logs
6. 检查结果：ls -lt, wc, tail, exit status
7. 冻结阶段：tar 或 Git tag
```

### 6.3.2 微型项目目录

当前用 `gaia_night1/` 作为贯穿项目非常好。它不是孤立命令练习，而是有科研角色的目录结构：

```text
gaia_night1/
  raw/
  logs/
  scripts/
  results/
  notes/
```

建议保留并贯穿每一节。所有命令都尽量回到这个项目。

### 6.3.3 命令风险分类表

当前对只读检查、写入/移动、破坏性操作、环境改变的分类非常适合初学者。建议保留，并在每次出现 `rm`, `mv`, `>`, `chmod`, `export` 时回引该表。

### 6.3.4 管道 worked example

从“这夜观测中名字带 target 的 FITS 文件有多少个，清单是什么？”到：

```bash
find raw -name "*.fits" \
  | grep "target" \
  | sort \
  | tee logs/target_fits_files.txt \
  | wc -l
```

这个例子非常好，因为它把科研问题、命令组合和证据保存连接起来。应保留。

### 6.3.5 标准输出、标准错误和退出状态

这一节比普通入门教材更有科研价值。后续 Python 脚本、机器学习训练、SLURM/HPC 任务都会依赖这个概念。

建议保留。

---

## 6.4 当前 Ch01 中建议调整的内容

### 6.4.1 `sed` 不宜作为必须掌握命令

当前示例中出现：

```bash
find raw -type f | sed 's/.*\.//' | sort | uniq -c
```

这个例子从命令能力上是好的，但对初学者而言，`sed` 正则替换的认知负担较高。建议把它标注为“了解”或“高级提示”。

替代方案：

```bash
find raw -type f | sort | head
```

或将扩展名统计留到 Python/pandas 中完成。

### 6.4.2 `xargs` 不应提前展开

学习目标中包含 `xargs`，但如果正文没有充分训练，建议不要把它列为必须掌握。`xargs` 对批量删除/移动有潜在风险，初学阶段容易误用。

建议：

- 从学习目标“必须掌握”移到“进阶了解”；
- 若保留，必须配安全示例，例如先 `echo` 再执行。

### 6.4.3 `chmod 755` 可以保留，但不宜成为重点

`chmod u+x` 对学生足够实用。`chmod 755` 可以作为解释权限数字的补充，但不需要要求熟练计算。

建议将节标题改为：

```markdown
权限数字：看懂 755，而不是背 755
```

### 6.4.4 远程服务器部分建议定位为“项目场景选读”

`ssh` 和 `scp` 很重要，但不是所有学生第一周都会用远程服务器。建议标注：

```markdown
本节为远程服务器/实验室集群场景必读；本地教学环境可先快读。
```

### 6.4.5 `tar` 归档可保留，但建议与 Git 分工说明

学生可能会困惑：既然 Ch02 讲 Git，为什么 Ch01 要 tar？

建议增加一句：

> Git 记录代码和小型文本历史；tar 适合冻结一组阶段性交付材料，但不替代版本控制。

---

## 6.5 建议补充的少量命令

不建议大量加命令，但有几类科研高频命令值得少量补入。

### 6.5.1 补充 `du -sh` 与 `df -h`

原因：天文数据常常很大，学生需要知道文件/目录占用空间和磁盘空间。

建议新增小节或提示框：

```bash
du -sh raw results logs
df -h .
```

对应解释：

- `du -sh raw`：查看 `raw/` 目录占用空间；
- `df -h .`：查看当前文件系统剩余空间。

建议定位：必须掌握。

### 6.5.2 补充 `file` 与 `stat`

原因：学生常遇到“文件扩展名和实际格式不一致”“修改时间/大小异常”。

建议示例：

```bash
file raw/night1_target042.fits
stat raw/night1_target042.fits
```

建议定位：了解即可。

### 6.5.3 补充 `sha256sum` 或 `md5sum`

原因：数据下载、归档、交付时需要确认文件是否一致。

建议示例：

```bash
sha256sum results/night1_minimal_package.tar.gz > results/package.sha256
sha256sum -c results/package.sha256
```

建议定位：进阶/项目交付。

### 6.5.4 补充 `realpath` 或 `readlink -f`

原因：初学者经常混淆相对路径和绝对路径。

建议示例：

```bash
realpath raw/night1_target042.fits
```

建议定位：了解即可。

### 6.5.5 补充 `tree` 或替代方案

如果教学环境有 `tree`，非常适合展示项目结构：

```bash
tree -L 2 gaia_night1
```

如果没有 `tree`，用：

```bash
find gaia_night1 -maxdepth 2 -type d | sort
```

建议定位：了解。

### 6.5.6 长任务补充 `nohup` / `tmux` / `screen` 是否需要？

建议：不放入正文必修。原因是这些工具很实用，但会把 Ch01 引向远程服务器/HPC 操作课。

可以放一个选读提示：

```markdown
如果你需要在远程服务器上运行数小时任务，请学习 tmux/screen/nohup 或集群调度系统。本书正文只要求你理解长任务必须保存日志、退出状态和运行环境。
```

---

## 6.6 不建议加入的内容

以下内容不建议放入 Ch01 正文主线：

| 内容 | 不建议原因 |
|---|---|
| 完整 bash 编程 | 会冲淡科研工作流主线 |
| 正则表达式系统教程 | 对 Part I 过重，可放附录 |
| awk 系统教程 | 有用但学习成本高，不是入门必需 |
| SLURM/PBS 作业系统 | 更适合高级/HPC 附录 |
| Docker/Singularity | 与 Ch04/环境章节或附录关系更大 |
| vim/emacs 系统教程 | 工具偏好性强，可给建议不必教学 |
| 用户/组/权限管理深挖 | 不是学生项目最低需求 |
| shell 函数与复杂脚本 | 可留到项目进阶 |

---

## 6.7 Ch01 推荐分层重排方案

建议把 Ch01 内容标成三层：

### A 层：必须掌握

```markdown
- pwd / ls / cd
- mkdir -p
- cp / mv / rm 的风险
- find 基本用法
- head / tail / wc / less
- grep 或 rg
- > / >> / 2>
- | / tee
- which python / python --version
- chmod u+x
- date / logs
- 最小 shell 脚本
```

### B 层：课堂了解

```markdown
- sort / uniq / cut
- PATH / export / alias
- ps / top / time
- ssh / scp
- tar
- chmod 755
- set -euo pipefail
```

### C 层：项目需要再学

```markdown
- sed
- xargs
- sha256sum
- du / df
- realpath
- tmux / screen / nohup
- rsync
- SLURM / PBS
```

其中 `du / df` 我建议从 C 层提升到 A 或 B 层，因为天文数据场景中磁盘空间问题非常常见。

---

## 6.8 Ch01 最推荐的新增小节

如果只允许新增一个小节，我建议新增：

```markdown
### 本章最低交付：Command Log 与目录快照
```

内容如下：

```markdown
本章结束时，你需要提交一个 `logs/ch01_command_log.md` 或 `logs/ch01_command_log.txt`，至少包含：

1. 环境定位
   - `hostname`
   - `pwd`
   - `which python`
   - `python --version`

2. 项目目录快照
   - `find . -maxdepth 2 -type d | sort`
   - 或 `tree -L 2`

3. 输入数据检查
   - `find raw -name "*.fits" | sort | tee logs/input_fits_files.txt`
   - `wc -l logs/input_fits_files.txt`

4. 文本/日志检查
   - `head logs/night1.log`
   - `tail logs/night1.log`
   - `grep "ERROR" logs/night1.log || true`

5. 一次安全写操作
   - 先预览目标；
   - 再执行复制/生成结果；
   - 再检查输出。

6. 一个最小脚本
   - `scripts/run_pipeline.sh`
   - 包含 `set -euo pipefail`
   - 输出到 `logs/` 与 `results/`

7. 风险说明
   - 本次最可能出错的是路径、覆盖、权限、环境还是数据缺失？
```

这个小节比继续增加零散命令更有价值，因为它把命令学习变成可评分交付。

---

# 7. Ch01 精修后的建议目录

```markdown
Ch01 Unix/Linux 与科研计算环境

1. 本章导读：从会敲命令到会组织科研工作
2. 本章阅读方式与最低交付
3. 贯穿本章的微型项目
4. Shell 与命令解析
5. 路径、目录与项目结构
6. 只读检查：pwd / ls / find / head / tail / wc
7. 批量对象：通配符、引号与预览
8. 搜索与快速统计：grep/rg / sort / uniq / cut
9. 重定向、管道与证据保存：> / >> / 2> / tee
10. 环境与权限：which / type / PATH / chmod
11. 远程服务器场景：ssh / scp / hostname / which python
12. 长任务与日志：ps / top / time / date / exit status
13. 最小 shell 脚本：从手动命令到可运行入口
14. 归档与冻结：tar / 检查归档 / 与 Git 分工
15. 破坏性命令前的三步确认
16. 本章最低交付：command log
17. Exit Gate：进入 Git 与 Python 工作流前的检查
```

---

# 8. 实施计划

## Phase 1：结构标注与阅读路径整理

目标：不大改正文，先让学生知道怎么读。

任务：

1. 给 Part I/II 每章增加“本章阅读方式”卡片。
2. 给每章末尾增加 Exit Gate。
3. 在 Part II 导读中加入选学路径。
4. 在 Part II 收束章加入 Data Card v0.1。

交付：

```markdown
- 每章章首学习卡
- 每章 Exit Gate
- Part II 选学路径表
- Data Card v0.1 模板
```

## Phase 2：Part I 精修

目标：把 Part I 从“工具基础”压成“科研工作流最低系统”。

优先级：

1. Ch04 脚本/Jupyter：最高优先级。
2. Ch06 I/O/FITS：明确与 Part II 分工。
3. Ch02 Git：增加 `.gitignore`、tag、notebook/results policy。
4. Ch08 绘图：增加 figure record 与图表自审清单。
5. Ch01 Linux：压缩命令百科倾向，强化安全和日志。

交付：

```markdown
- command log template
- version record template
- reproducible script template
- data intake record template
- figure record template
```

## Phase 3：Part II 精修

目标：把 Part II 明确改造成“从数据类型到可建模样本”。

优先级：

1. Ch10：加强单位、误差传播、测量值/派生量/模型量。
2. Ch11：作为 Part II 样板章精修。
3. Ch12/13/14：按数据类型方向选读化。
4. Ch15：强化物理模型与 ML baseline 的桥梁。
5. Part II synthesis：增加 Part III readiness checklist。

交付：

```markdown
- measurement record
- HR diagram record
- photometry record
- spectrum record
- period record
- model fit record
- Data Card v0.1
```

## Phase 4：notebook 与正文对齐

目标：保证正文说的每个 record，notebook 都能产出。

检查项：

```markdown
- notebook 是否生成本章 record？
- record 是否包含 input / operation / output / check / limit？
- 是否有脚本入口？
- 是否有固定随机种子？
- 是否有输出路径？
- 是否能被 smoke test 覆盖？
```

## Phase 5：试读与课程化反馈

目标：验证 Part I/II 是否真的能快速读、有效练。

建议找三类学生试读：

| 学生类型 | 试读重点 |
|---|---|
| Python 基础弱 | Part I 是否过快 |
| 有科研训练 | Part II 是否太浅 |
| 准备做 ML 项目 | Part II 到 Part III 是否衔接清楚 |

试读后只问五个问题：

```markdown
1. 哪些节可以快读？
2. 哪些任务必须动手？
3. 哪一章最卡？
4. 你是否知道自己进入 Part III 前要交什么？
5. 你能否解释自己的数据如何变成模型输入？
```

---

# 9. 最终建议

最终建议是：

> **Part I/II 不要再追求“讲得更全”，而要追求“通往 Part III 的闸门更清楚”。**

具体说：

- Part I 的关键词是：**路径、版本、脚本、数据入口、图表证据**。
- Part II 的关键词是：**对象、单位、误差、处理、选择效应、可建模样本**。
- 每章都应该有一个 record。
- 每个 record 都应该能进入最终 capstone portfolio。
- Part II 收束章必须明确告诉学生：现在你已经不是在“读数据”，而是在构造机器学习可以使用、也可以被科学复查的样本。

对 Ch01 Linux 的具体结论是：

> **当前 Linux 命令覆盖已经足够，不建议继续堆命令；需要做的是命令分层、补少量科研高频检查命令、强化 command log 交付，并把“哪些必须掌握、哪些选读”明确标出来。**
