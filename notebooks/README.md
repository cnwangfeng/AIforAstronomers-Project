# Notebooks 目录说明

本目录保存教材配套的可运行 Jupyter notebooks。notebook 是教材的核心组成部分，不是附属材料；每个主要章节都应至少有一个 notebook，用来展示从数据读取、清洗、建模、可视化到科学解释的完整流程。

建议目录结构：

```text
notebooks/
  part0_python_prereq/
  part1_scientific_computing/
  part2_data_processing/
  part3_machine_learning/
  part4_cases/
  part5_deep_learning_ai/
  part6_capstone/
```

说明：

- `part0_python_prereq/` 是进入教材正文前的先修模块；
- `part1_scientific_computing/` 开始进入正文主线，默认读者已经能阅读和修改基础 Python 代码。

命名规范：

- 使用章节编号和简短英文主题，例如 `ch11_gaia_hr_diagram.ipynb`。
- notebook 标题和正文说明使用中文。
- 代码变量名优先使用清晰英文，便于和 Python 生态一致。

每个 notebook 应满足：

- 第一格说明所属章节、学习目标、依赖环境和数据来源。
- 不依赖隐藏的本地绝对路径。
- 所有随机过程设置随机种子。
- 核心 notebook 运行时间原则上小于 5 分钟。
- 输出图表必须有标题、坐标轴、单位和必要注释。
- 最后一节用中文解释结果、局限性和下一步。

当前进展：

- `part0_python_prereq/` 已覆盖 Python 入门、条件循环、函数模块与轻量 OOP。
- `part1_scientific_computing/` 已对应 Linux、Git、脚本/Jupyter、数据 I/O 与科学绘图。
- `part2_data_processing/` 已对应误差、不确定度、Gaia HR 图、FITS/WCS、光谱、时间序列与实验/模拟数据。
- `part3_machine_learning/` 已对应 AI/ML 科学推断、最小 workflow、回归、分类、评估、预处理、模型选择、无监督、异常检测和可信度。
- `part4_cases/` 已对应 Gaia HR 图、光度红移估计、光谱分类和星系形态分类案例。
- `part5_deep_learning_ai/` 已对应神经网络、CNN、一维卷积、自编码器、Transformer/注意力、LLM 辅助编程、agentic workflow、文献阅读/报告写作和 AI 伦理。
- `part6_capstone/` 已对应 capstone workflow、选题、报告展示、rubric、试教、课程运行、发布维护、交接和长期维护。

最近一次完整 smoke test 已通过 `59` 个 notebook。后续 notebook 工作的重点不再是补空目录，而是和正文一起做细读：统一术语、控制运行时间、补图表解释、补失败案例和维护每章数据契约。
