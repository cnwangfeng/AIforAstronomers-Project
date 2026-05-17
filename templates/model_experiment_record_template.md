# Model Experiment Record Template

用途：记录一次机器学习模型实验。它回答的问题是：**这次模型实验怎么做、怎么评估、怎么复查？**

> 原则：Model Experiment Record 是 Evidence Record 的机器学习扩展版。它不替代 Dataset Contract，也不替代 Trust Statement。

---

## 1. Task

- Scientific question:
- ML task: regression / classification / clustering / anomaly detection / representation learning / other
- Prediction target / discovery goal:
- Intended use:

## 2. Dataset Contract

- Dataset Contract link:
- Data Card link:
- Key Evidence Records:

## 3. Split / Role Assignment

- Train / validation / test split:
- Split unit:
- Random seed:
- Stratification / group split:
- When was the test set opened?

## 4. Baseline

- Baseline type:
- Baseline reason:
- Baseline result:

## 5. Model

- Model family:
- Key parameters / hyperparameters:
- Algorithm Card link:
- Training entry point:

## 6. Evaluation

- Metrics:
- Threshold, if any:
- Scientific cost:
- Main diagnostic figure:

## 7. Error Analysis

- Main failure cases:
- Error concentration:
- Relation to data quality / physical regime:

## 8. Limit

- Supported claim:
- Unsupported claim:
- Known leakage / selection / extrapolation risk:

## 9. Reproducibility

- Script / notebook:
- Output files:
- Code version / tag:

---

## Chapter-Specific Fields

按章节只补少量字段。不要把 regression record、classification record、evaluation record 等扩写成独立模板；它们应作为本记录中的 chapter-specific fields 或 evidence sections。

- Field 1:
- Field 2:
- Field 3:
