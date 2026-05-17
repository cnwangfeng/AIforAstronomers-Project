# Part III Dataset Contract Template

用途：进入机器学习之前的正式交接文件。它回答的问题是：**这个数据集如何安全进入模型？**

> 原则：如果本文件不能说明样本、特征、标签、质量信息、选择效应、预处理和 split 风险，就不应进入 Part III。

---

## Provenance Links

- Data Card:
- Key Evidence Records:
- Code version / tag:

## 1. Task Definition

- ML task: regression / classification / clustering / anomaly detection / representation learning / other
- Scientific question:
- Prediction target:
- Intended use:

## 2. Sample Definition

一行、一个 cutout、一条光谱或一条时间序列代表什么？

- Sample unit:
- Number of samples:

## 3. Sample ID

每个样本如何唯一识别？

- Sample ID field:
- Can it trace back to raw data? yes / no

## 4. Input Features

哪些变量或数组会进入模型？

- Feature / array names:
- Units:
- Derived or raw:
- Normalized / standardized:
- Quality flags included:

## 5. Target / Label

预测目标或标签从哪里来？

- Target / label name:
- Label source:
- Label rule:
- Boundary or ambiguous cases:
- Label leakage risk:

## 6. Uncertainty / Quality

误差、质量标记、缺失值如何保留？

- Uncertainty fields:
- Quality flags:
- Missing-value handling:
- Removed or down-weighted samples:

## 7. Selection

样本经过了哪些筛选？

- Selection cuts:
- Excluded cases:
- Selection effects:
- Does training data represent future application data? yes / no / unclear

## 8. Preprocessing

做了哪些归一化、重采样、背景扣除或派生变量计算？

- Preprocessing steps:
- Parameters:
- Fit only on training set? yes / no / not applicable
- Leakage risk:

## 9. Split Readiness

是否可以安全划分 train / validation / test？

- Split unit: sample / object / observation / time / field
- Group key for split, if needed:
- Duplicate object risk:
- Repeated observation risk:
- Spatial / temporal / class leakage risk:

## 10. Baseline Readiness

是否可以建立简单 baseline？

- Rule or physical baseline:
- Constant / mean baseline:
- Simple ML baseline:

## 11. Known Limits

这个数据集不能支持什么科学结论？

- Limit 1:
- Limit 2:
