# 中文书稿 Capstone Evidence Card QA 记录

本文件记录 `book/main_zh.tex` 当前正文主线的 capstone evidence card 对齐状态，用于 Stage C 章节交叉引用、证据卡入口和最终项目包收束检查。

## Canonical 八张证据卡

当前中文主线以 `book/main_zh.tex` 的读者准备页为 canonical 定义：

- `Project card`：科学问题、范围和可回答性。
- `Data card`：数据来源、字段、单位、误差、许可证和筛选。
- `Baseline card`：简单方法的结果和科学意义。
- `Model card`：模型选择、输入输出、训练验证和失败样本。
- `Evaluation card`：指标、诊断图、误差分析和测试边界。
- `Interpretation card`：主要 claim、局限性、不确定度和 caveat。
- `Reproducibility card`：环境、运行入口、随机种子、Git 记录和复跑说明。
- `Integrity card`：引用核查、AI 使用记录、公开边界和 human signoff。

## 当前桥接状态

- 开篇读者准备页已提前说明八张证据卡，并把 Part I--VI 的学习路径解释为逐步补齐 capstone portfolio。
- Part I 收束已把目录、命令行、Git、数据入口、图表说明和 AI 使用记录接到 Reproducibility / Data / Interpretation / Integrity cards。
- Part II 收束已把数据来源、派生算法、误差预算、质量标记、解释边界和共享限制接到 Data / Reproducibility / Evaluation / Interpretation / Integrity cards。
- Part III 收束已把任务定义、预处理、baseline、模型设置、评估设计、错误分析、随机种子和泄漏检查接到全部模型相关 cards。
- Part IV 收束已把四个案例的项目定义、数据契约、baseline、诊断图、错误案例、复跑说明和公开边界接到 capstone case template。
- Part V 收束已把深度模型交付、verification loop、action log、claim ledger、usage log 和 AI-use statement 接到 Model / Evaluation / Interpretation / Reproducibility / Integrity cards。
- Part VI 学生视角最小交付件和全书收束页已回到同一套八张 evidence cards。

## 当前 QA 结论

- 八张 card 名称在读者准备页、Part I--VI 收束层和全书收束页中保持一致。
- 当前 canonical card 名称在正文中均有多处入口；没有发现只在开篇定义、后文完全不再使用的 card。
- 已对齐全书收束页的 `Data card` 字段顺序，使其与读者准备页保持一致。
- Part V 收束已明确区分：模型训练验证进入 Model / Evaluation，质量门和复核队列进入 Data / Reproducibility / Evaluation，claim ledger 进入 Interpretation / Integrity，usage log 与 AI-use statement 进入 Integrity。

## 后续发布前检查

- 若新增章节或收束段，优先复用这八个 canonical 名称，不新造近义 card 名称。
- 若新增 AI / agent / LLM 相关内容，必须说明 verification loop、action log、claim ledger、usage log 或 AI-use statement 分别进入哪张 card。
- 若新增 capstone workflow 表格，必须说明它服务于学生项目、教师运行、发布维护还是外部合作，避免把课程运维表误写成学生必交证据。
