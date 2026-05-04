# AIforAstronomers-Project

教材正式题目：面向天文与物理本科生的 AI 科研实战

英文副标题：Practical AI for Astronomy and Physics

仓库命名约定：

- 完整项目仓库保留 `AIforAstronomers-Project`
- Overleaf 书稿仓库保留 `AIforAstronomers`

本仓库是完整项目仓库，保存中文教材、配套 notebooks、教学数据、脚本、环境文件和课程资源。Overleaf 只同步轻量书稿仓库，不直接同步本仓库。

当前教学结构采用：

- `Part 0`：Python 先修模块，只补进入本书所必需的基础语法和代码阅读能力；
- `Part I` 到 `Part VI`：教材正文主线，聚焦科研工作流、数据处理、机器学习和案例。

也就是说，通用 Python 入门不再占用正文主线篇幅；正文默认读者已经完成 `Part 0`，或者具备同等基础。

## 仓库分工

建议使用两个本地/GitHub 仓库：

```text
AIforAstronomers-Project/   # 完整项目仓库
AIforAstronomers/           # Overleaf 同步书稿仓库
```

本仓库负责：

- 教材正文源文件：`book/`
- 配套 notebooks：`notebooks/`
- 小型教学数据和数据说明：`data/`
- 数据下载、图表生成、notebook 清理等脚本：`scripts/`
- Python 环境文件：`environments/`
- 路线图和课程资源：`Roadmap.md`
- 统一课程包发布说明：`COURSE_PACKAGE_RELEASE_NOTES.md`
- 同步/发布检查清单：`RELEASE_SYNC_CHECKLIST.md`
- 发布前非技术决策清单：`PUBLICATION_DECISIONS.md`

Overleaf 同步仓库只保留：

- `.tex` 书稿文件
- `.bib` 参考文献
- 教材编译所需图片
- 少量样式文件

## 目录结构

```text
book/             # LaTeX 中文教材源码
notebooks/        # 每章配套 Jupyter notebooks
data/             # 小数据、数据说明、下载脚本
figures/          # 项目级图表输出；教材最终图表应同步到 book/figures 或对应章节目录
scripts/          # 本地/CI 辅助脚本
environments/     # Python 环境定义
assignments/      # 作业说明与模板
slides/           # 课堂讲义
Roadmap.md        # 教材路线图
COURSE_PACKAGE_RELEASE_NOTES.md  # 当前课程包发布说明
RELEASE_SYNC_CHECKLIST.md        # 最终同步与发布检查清单
```

其中：

- `book/main_zh.tex` 对应教材正文主线；
- `notebooks/part0_python_prereq/` 对应 Python 先修材料；
- `Part 0` 保持正文外 notebook-first 先修定位，不作为主书稿的正式部分扩写。

## 基本工作流

1. 在本仓库中编写教材、运行 notebooks、生成图表和整理数据。
2. 将教材需要的最终图表放入 `book/` 下的相应图片目录。
3. 使用同步脚本预览要同步到 Overleaf 书稿仓库的变化：

```bash
bash scripts/sync_book_to_overleaf.sh
```

4. 确认无误后执行真实同步：

```bash
bash scripts/sync_book_to_overleaf.sh --apply
```

5. 在 `../AIforAstronomers/` 中提交书稿变化，并由 GitHub/Overleaf 同步。

6. 在提交 notebook 变更前，可先运行轻量 smoke test：

```bash
python scripts/smoke_test_notebooks.py
```

7. 在同步书稿前，可先做本地 LaTeX 编译检查：

```bash
bash scripts/build_book_local.sh main
bash scripts/build_book_local.sh zh
```

默认输出目录：

- `main.tex` -> `/tmp/aifor_book_main/main.pdf`
- `main_zh.tex` -> `/tmp/aifor_book_main_zh/main_zh.pdf`

8. 在准备正式同步或发布前，建议先对照：

- `COURSE_PACKAGE_RELEASE_NOTES.md`
- `RELEASE_SYNC_CHECKLIST.md`

## 数据原则

- 小数据可以放在 `data/small/`。
- 大数据不要提交到 Git；只放下载脚本、来源、许可证和校验信息。
- `data/external/` 是本地缓存目录，默认被 `.gitignore` 忽略。

## 许可证

教材、代码和数据许可证尚未最终确定。正式发布前必须分别确认：

- 教材文字与图表许可证
- 代码许可证
- 教学数据许可证
- 外部材料引用和改写授权

发布路径、许可证拆分、引用归属和项目级 AI-use statement 的待决事项集中记录在 `PUBLICATION_DECISIONS.md`。
