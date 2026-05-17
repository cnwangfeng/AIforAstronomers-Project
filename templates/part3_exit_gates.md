# Part III Exit Gates

用途：为 Part III 各章提供短版出口检查。Exit Gate 只负责收束，不负责再讲一遍正文。

---

## Common Part III Exit Gate

回答 4 个问题：

1. 任务是什么？
2. 数据入口和 split 是否可复查？
3. 模型结果支持什么 claim？
4. 当前限制、泄漏风险或可信边界是什么？

最低交付：

- 一个 Model Experiment Record
- 至少一个可复查 artifact：脚本、notebook、指标表、诊断图、错误样本表或候选清单

最多 100-150 字。

---

## Ch16 Exit Gate

- 必须交代 scientific question、ML task、optimization target。
- 必须链接 Dataset Contract 或说明为什么当前只是概念练习。
- 必须写出 baseline 和 unsupported mechanism claim。

## Ch17 Exit Gate

- 必须交代 split unit、split seed、stratification/group split。
- 必须说明 test set opened when。
- 必须说明 baseline 结果和最小模型入口。

## Ch18 Exit Gate

- 必须报告 baseline、回归模型、metric。
- 必须提供残差诊断。
- 必须说明至少一种系统误差、离群点或外推风险。

## Ch19 Exit Gate

- 必须说明标签来源和类别边界。
- 必须报告 baseline、分类器和 confusion matrix。
- 必须说明模型类别不是自然类别本身。

## Ch20 Exit Gate

- 不能只报告 accuracy。
- 必须说明 metric、threshold、decision policy 和 scientific cost。
- 必须包含错误样本或阈值扫描 artifact。

## Ch21 Exit Gate

- 必须提交 Feature Ledger。
- 必须说明哪些预处理步骤 fit on train only。
- 必须说明 feature 与 Data Card / Evidence Record / Dataset Contract 的追踪关系。

## Ch22 Exit Gate

- 必须记录候选模型和超参数搜索范围。
- 必须说明验证策略和最终测试集何时打开。
- 必须说明最终选择不是测试集挑出来的。

## Ch23 Exit Gate

- 必须说明 feature space、scaling 和算法参数。
- 必须包含 stability / sensitivity check。
- 必须声明 algorithmic group is not physical class unless externally validated。

## Ch24 Exit Gate

- 不能只给 anomaly score。
- 必须包含 Anomaly Review Triage：bad data / boundary ordinary / interesting candidate。
- 必须说明人工复核字段。

## Ch25 Exit Gate

- 必须提交 Trust Statement。
- 必须同时说明 uncertainty、interpretability 和 failure boundary。
- 必须写清 supported claim 与 unsupported claim。
