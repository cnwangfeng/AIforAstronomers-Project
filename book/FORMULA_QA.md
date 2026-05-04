# 中文书稿公式 QA 记录

本文件记录 `book/main_zh.tex` 当前正文主线的公式盘点状态，用于 Stage C 公式解释、变量定义、单位/量纲和 notebook 计算角色检查。

## 当前快照

- 当前中文主线包含 `68` 个 `\include{...}` 文件。
- 当前中文主线共有 `140` 个 display math block。
- 当前中文主线未使用单独编号的 `equation` / `align` 环境；公式主要作为教材推导和计算说明出现，而不是作为编号定理或编号公式引用。
- 公式最密集的章节集中在 Part II/III：测量不确定度、HR 图、FITS/WCS、光谱、时间序列、实验拟合、回归、分类和模型评估。

## 发布前公式检查标准

每个重要公式附近至少应能回答四个问题：

- 变量含义：公式中的主要符号是否在前后文定义。
- 单位/量纲：涉及物理量、坐标、波长、时间、误差或概率时，单位或量纲边界是否清楚。
- 计算角色：这个公式在 notebook、例题或报告模板中用于什么计算。
- 适用边界：公式依赖的近似、假设、模型条件或失败场景是否说明。

## 当前抽查结论

- `ch10_measurement_uncertainty`：测量模型、视差距离、误差传播和加权平均公式前后均有变量或单位说明。
- `ch13_spectroscopy`：谱线、分辨率、红移、等效宽度和速度近似公式有物理含义与适用边界说明。
- `ch14_time_series_and_periods`：时间序列、正弦模型、相位折叠、分箱和周期搜索相关公式有计算角色说明。
- `ch15_physics_experiment_simulation_data`：RC 放电、最小二乘、Monte Carlo 与参数解释公式已接到实验数据报告语境。
- `ch18_regression` / `ch19_classification` / `ch20_model_evaluation_diagnostics`：模型目标、距离函数、逻辑回归、accuracy / precision / recall / F1 等公式均有指标含义或科学代价说明。

## 后续发布前检查

- 若新增编号公式，必须同步说明是否需要正文 `\ref{...}` 引用；否则优先保持当前非编号 display math 风格。
- 若新增物理公式，必须说明单位、量纲和近似条件。
- 若新增机器学习公式，必须说明它对应的 loss、score、threshold、routing 或 diagnostic role。
- 若新增 notebook 结果公式，必须说明输入字段、输出字段和可复跑位置。
