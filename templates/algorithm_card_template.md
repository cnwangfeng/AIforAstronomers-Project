# Algorithm Card Template

用途：说明一个核心算法为什么这样工作。它回答的问题是：**这个模型相信了什么、优化了什么、会在哪里失败？**

> 原则：Algorithm Card 不是行政表格，而是算法理解层。它应短小，但必须说清模型形式、目标/规则、假设、诊断和科学边界。

使用三种粒度：

- Full card：Part III 中第一次正式讲解核心算法时使用。
- Short card：同一算法思想的后续变体或快速提醒。
- Sidebar card：Part IV 案例章中只需回指 Part III 算法逻辑时使用。

不要为了案例章继续扩字段。若案例需要更多细节，把它写进 Model Experiment Record 的 chapter-specific fields、诊断图或错误分析 artifact。

---

## Algorithm

- Name:
- Task type:
- Typical use in astronomy / physics:

## Model Form

- Mathematical form or decision rule:
- Input:
- Output:

## Objective / Training Rule

- What is optimized?
- What is learned?
- What is fixed by the user?

## Key Assumptions

- Assumption 1:
- Assumption 2:
- Assumption 3:

## Minimal Implementation

- Hand calculation / pseudocode / minimal code:
- What this minimal version reveals:

## Diagnostics

- What should be plotted or checked?
- What failure pattern matters most?

## Failure Modes

- Data issue:
- Model issue:
- Scientific interpretation issue:

## Scientific Boundary

- What the model result can support:
- What it cannot support:
