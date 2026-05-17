# Part I/II Chapter-Specific Fields

用途：这些字段附加在统一的 Evidence Record 后面。不要把它们扩写成每章独立模板。

---

## Ch01 Unix/Linux

```markdown
## Ch01 Fields
- project root:
- key read-only checks:
- preview before write:
- log file:
- script or command entry:
- python path/version check:
```

Special requirement: Pass 必须包含一次写操作前的 preview，或明确说明本章操作全部为只读。

## Ch02 Git

```markdown
## Ch02 Fields
- repository root:
- relevant commit:
- tag/checkpoint:
- tracked files:
- ignored files:
- output linked to commit:
```

Special requirement: Pass 必须能指出哪个 commit 或 tag 生成了哪个输出文件。

## Ch04 Libraries, Scripts, and Jupyter

```markdown
## Ch04 Fields
- notebook:
- script entry:
- command to run:
- python version:
- key package versions:
- random seed:
- output directory:
```

Special requirement: Pass 必须包含一个能从命令行运行的脚本入口，而不仅是 notebook。

## Ch06 File I/O, FITS, and Data Intake

```markdown
## Ch06 Fields
- file path:
- data source:
- file format:
- fields/header checked:
- units:
- missing values:
- quality flags:
- columns/arrays used later:
```

Special requirement: Pass 必须说明字段/header、单位、缺失值或质量标记；不能只说“文件可以打开”。

## Ch08 Visualization and Scientific Figures

```markdown
## Ch08 Fields
- figure file:
- plotting script:
- input data:
- axis variables and units:
- sample selection:
- visual encoding:
- claim supported:
- claim not supported:
```

Special requirement: Pass 必须写清图表支持的 claim 和不能支持的 limit。

---

## Ch10 Scientific Data, Uncertainty, and Units

```markdown
## Ch10 Fields
- measured quantity:
- unit:
- uncertainty:
- derived quantity:
- formula used:
- error propagation:
- order-of-magnitude check:
- systematic risk:
```

Special requirement: Pass 必须包含单位检查和至少一种误差/数量级检查。

## Ch11 Tables, Catalogs, and HR Diagrams

```markdown
## Ch11 Fields
- catalog/table path:
- source columns:
- units:
- quality cuts:
- derived quantities:
- HR diagram file:
- structures identified:
- selection effects:
- possible ML features:
```

Special requirement: Pass 必须说明筛选条件和选择效应；不能只给 HR 图。

## Ch12 Astronomical Images, FITS, and WCS

```markdown
## Ch12 Fields
- FITS file:
- HDU/header checked:
- image shape:
- pixel scale / WCS:
- background method:
- aperture or cutout setting:
- normalization:
- mask / bad pixels:
- possible ML input shape:
```

Special requirement: Pass 必须说明背景/归一化/cutout 或 aperture 设置中的至少一项；不能只给 imshow 图。

## Ch13 Spectra, Lines, and Redshift

```markdown
## Ch13 Fields
- spectrum file:
- wavelength unit/grid:
- flux unit:
- calibration status:
- continuum treatment:
- line candidates:
- redshift estimate:
- S/N or quality flag:
- resampling/normalization:
```

Special requirement: Pass 必须说明红移或谱线判断的质量依据；不能只标出一个峰。

## Ch14 Time Series, Sampling, and Periods

```markdown
## Ch14 Fields
- time series file:
- time unit/system:
- cadence:
- duration:
- missing pattern:
- period search range:
- best period:
- second-best period:
- phase-folded plot:
- alias risk:
```

Special requirement: Pass 不能只报告 best period；必须说明 second-best period 或 alias 风险。

## Ch15 Model Fitting and Simulated Data

```markdown
## Ch15 Fields
- model formula:
- parameter meanings:
- parameter units:
- fitting method:
- residual plot:
- error metric / chi-square:
- uncertainty estimate:
- baseline comparison:
- physical interpretation limit:
```

Special requirement: Pass 必须包含残差或误差诊断；不能只给拟合曲线。
