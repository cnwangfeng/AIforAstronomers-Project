# Chapters Migration Plan

This directory will become the long-term home for the textbook chapters.

For now, the textbook still uses the legacy flat layout in `book/` to avoid
breaking the current Overleaf workflow before we finish the first cleanup pass.

Draft policy:

- new Chinese chapter drafts can be written here before they are wired into
  `book/main.tex`
- this lets us author the future textbook structure without breaking the current
  stable Overleaf entry point
- once a draft is mature and the Chinese LaTeX toolchain is ready, it can
  replace the legacy chapter file in the main build

Planned migration map:

- `UnixLinux.tex` -> `chapters/part1/ch01_unix_linux.tex`
- `VersionControl/VersionControl.tex` -> `chapters/part1/ch02_git.tex`
- `Chapter2.tex` -> `chapters/part0/ch03_basic_python_prereq.tex`
- `Chapter3.tex` -> `chapters/part1/ch04_libraries_and_scripts.tex`
- `Chapter4.tex` -> `chapters/part0/ch05_conditionals_and_loops.tex`
- `Chapter5.tex` -> `chapters/part1/ch06_data_io_and_fits.tex`
- `Chapter6.tex` -> `chapters/part0/ch07_functions_and_code_organization.tex`
- `Chapter7.tex` -> `chapters/part1/ch08_plotting.tex`
- `Chapter8.tex` -> `chapters/part0/ch09_object_oriented_programming.tex`

Later parts will be added under:

- `chapters/part0/`
- `chapters/part2/`
- `chapters/part3/`
- `chapters/part4/`
- `chapters/part5/`
- `chapters/part6/`

Current draft progress:

- Part 0 has begun absorbing the generic Python prerequisite materials
- Part I currently focuses on Linux, Git, Jupyter, data I/O, and plotting
- Part II is beginning with uncertainty and HR-diagram chapter drafts
