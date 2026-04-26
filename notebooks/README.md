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

- `part0_python_prereq/` 已开始接收 Python 入门、条件循环、函数与轻量 OOP 材料。
- `part1_scientific_computing/` 已从“Python 零基础”调整为“科研计算与可复现工作流”主线。
- `part2_data_processing/` 已开始加入误差传播与 HR 图 notebook。
- `part3_machine_learning/` 已开始加入规则 baseline 和最小分类工作流 notebook。
- `part4_cases/` 已开始接收 Gaia HR 图、光度红移估计、光谱分类等案例型 notebook。
- 后续优先将这些骨架扩展为真正的教学 notebook，再依次推进 Part II 到 Part VI。
