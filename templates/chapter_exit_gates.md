# Part I/II Short Exit Gates

用途：每章章末的短收束。Exit Gate 不讲新内容，只检查学生是否完成最低可复查交付。

---

## Ch01 Unix/Linux

```markdown
### Exit Gate

1. 我能否从项目根目录定位输入和输出？
2. 我是否在写操作前做了 preview？
3. 我是否保存了关键命令或日志？
4. 我是否能运行一个最小脚本并检查 Python 路径/版本？

最低交付：Evidence Record + 命令日志或最小脚本。
```

## Ch02 Git

```markdown
### Exit Gate

1. 仓库当前状态是否干净？
2. 关键代码和 record 是否已 commit？
3. 是否有可评分 tag 或 commit？
4. 输出文件能否追踪到版本？

最低交付：Evidence Record + git log/status/tag 记录。
```

## Ch04 Libraries, Scripts, and Jupyter

```markdown
### Exit Gate

1. notebook 和 script 的分工是否清楚？
2. 脚本能否从命令行重跑？
3. 环境、参数、随机种子是否记录？
4. 输出目录是否固定且可定位？

最低交付：Evidence Record + 可运行脚本 + 运行日志。
```

## Ch06 File I/O, FITS, and Data Intake

```markdown
### Exit Gate

1. 数据文件来源和路径是否清楚？
2. 字段/header 和单位是否说明？
3. 缺失值或质量标记是否记录？
4. 哪些列/数组会进入后续分析是否明确？

最低交付：Evidence Record + 数据入口检查输出。
```

## Ch08 Visualization and Scientific Figures

```markdown
### Exit Gate

1. 图的输入数据和脚本是否可定位？
2. 变量、单位、尺度是否清楚？
3. 图支持的 claim 是否明确？
4. 图不能支持的解释是否写清？

最低交付：Evidence Record + 图文件 + 生成脚本。
```

---

## Ch10 Scientific Data, Uncertainty, and Units

```markdown
### Exit Gate

1. 原始测量值、单位和误差是否清楚？
2. 派生量公式和适用条件是否写明？
3. 单位或数量级是否检查？
4. 系统误差或公式反演风险是否说明？

最低交付：Evidence Record + 一个测量/派生量检查。
```

## Ch11 Tables, Catalogs, and HR Diagrams

```markdown
### Exit Gate

1. 星表字段、单位和质量筛选是否清楚？
2. 派生量公式是否可复查？
3. HR 图解释是否区分 claim 和 limit？
4. 可进入 ML 的特征和风险是否说明？

最低交付：Evidence Record + HR 图 + Data Card 草稿。
```

## Ch12 Astronomical Images, FITS, and WCS

```markdown
### Exit Gate

1. FITS header/data 和图像形状是否检查？
2. 坐标、像素尺度或 WCS 风险是否说明？
3. 背景、cutout、aperture 或归一化是否记录？
4. 图像进入 ML 前会丢失什么信息是否说明？

最低交付：Evidence Record + 图像检查结果或 photometry/cutout 结果。
```

## Ch13 Spectra, Lines, and Redshift

```markdown
### Exit Gate

1. 波长和流量单位是否清楚？
2. 连续谱、归一化或重采样是否记录？
3. 谱线/红移判断是否有质量依据？
4. 光谱进入 ML 前的预处理风险是否说明？

最低交付：Evidence Record + 光谱图或红移/谱线记录。
```

## Ch14 Time Series, Sampling, and Periods

```markdown
### Exit Gate

1. 时间戳、时间跨度和采样是否说明？
2. 周期搜索范围是否合理？
3. 是否报告 best period 之外的候选或 alias 风险？
4. 时间序列进入 ML 前的缺失/采样风险是否说明？

最低交付：Evidence Record + period search/phase-folding 结果。
```

## Ch15 Model Fitting and Simulated Data

```markdown
### Exit Gate

1. 模型公式、参数和单位是否清楚？
2. 拟合方法和误差指标是否说明？
3. 是否查看残差或不确定度？
4. 物理模型和 ML baseline 的关系是否说明？

最低交付：Evidence Record + 拟合结果 + 残差/不确定度检查。
```

---

## Part II Synthesis

```markdown
### Part II Exit Gate

进入 Part III 前，学生必须完成：

1. 至少一个 Data Card v0.1；
2. 至少一个 Part III Dataset Contract 草稿；
3. 至少一个方向精做章节的 Evidence Record；
4. 一个说明样本、特征、标签、误差、质量标记、选择效应和预处理历史的摘要。
```
