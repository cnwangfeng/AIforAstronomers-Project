# Part III Chapter-Specific Fields

用途：这些字段附加在统一的 Model Experiment Record 后面。不要把它们扩写成每章独立 record 模板。

---

## Ch16 AI, ML, and Scientific Inference

```markdown
## Ch16 Fields
- scientific question:
- ML task:
- optimization target:
- Dataset Contract link:
- baseline:
- unsupported mechanism claim:
```

Special requirement: Pass 必须区分 scientific question、ML task 和 optimization target；没有 Dataset Contract，不进入模型实验。

## Ch17 ML Workflow

```markdown
## Ch17 Fields
- split unit:
- split seed:
- stratification / group split:
- baseline:
- model entry point:
- test set opened when:
```

Special requirement: Pass 必须说明测试集何时打开；测试集不能参与特征选择、预处理参数估计、超参数选择、阈值选择或模型选择。

## Ch18 Regression

```markdown
## Ch18 Fields
- target:
- baseline:
- regression model:
- loss / metric:
- residual diagnostic:
- outlier / extrapolation risk:
- Algorithm Card link:
```

Special requirement: Pass 不能只报告 MAE / RMSE；必须提供残差诊断，并说明至少一种系统误差或外推风险。

## Ch19 Classification

```markdown
## Ch19 Fields
- label source:
- class boundary:
- baseline:
- classifier:
- decision rule:
- confusion matrix:
- Algorithm Card link:
```

Special requirement: Pass 必须说明标签来源和类别边界；不能把模型类别直接说成自然类别。

## Ch20 Evaluation and Diagnostics

```markdown
## Ch20 Fields
- metric:
- threshold:
- decision policy:
- scientific cost:
- diagnostic artifact:
- error sample review:
```

Special requirement: Pass 不能只报告 accuracy；必须报告至少一个与科学代价相关的指标，并解释阈值或操作点选择。

## Ch21 Feature Engineering and Preprocessing

```markdown
## Ch21 Fields
- Feature Ledger:
- train-only fit steps:
- leakage risk:
- dropped features:
- quality flags:
- Dataset Contract link:
```

Special requirement: Pass 中任何进入模型的 feature，都必须能追踪到 Data Card / Evidence Record / Dataset Contract；标准化、缺失值填补、PCA 和特征选择只能在训练集上 fit。

## Ch22 Model Selection and Hyperparameters

```markdown
## Ch22 Fields
- candidate model families:
- hyperparameter search range:
- validation strategy:
- selection metric:
- final model:
- test set opened when:
```

Special requirement: Pass 必须记录搜索范围，而不只记录最佳参数。

## Ch23 Unsupervised Learning

```markdown
## Ch23 Fields
- feature space:
- scaling / preprocessing:
- method:
- parameters:
- stability / sensitivity check:
- algorithmic group statement:
- Algorithm Card link:
```

Special requirement: Pass 中任何 cluster 命名前，必须先声明：这是算法分组，不是物理类别；除非有外部证据验证，否则不能命名为真实天体族群。

## Ch24 Anomaly Detection

```markdown
## Ch24 Fields
- anomaly method:
- anomaly score:
- review queue:
- triage level:
- data-quality check:
- human-review fields:
- Algorithm Card link:
```

Special requirement: Pass 不能只给 anomaly score；必须给人工复核字段和候选分层。

## Ch25 Uncertainty, Interpretability, and Trust

```markdown
## Ch25 Fields
- uncertainty estimate:
- interpretability method:
- failure boundary:
- distribution status:
- supported claim:
- unsupported claim:
- Trust Statement link:
```

Special requirement: Pass 必须同时说明 uncertainty、interpretability、failure boundary；解释性解释的是模型行为，不是物理因果。
