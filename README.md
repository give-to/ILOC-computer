# ILOC-computer
用来计算ILOC操作序列，帮助判断你的输入和输出程序是否等价。

支持的ILOC操作有：

| Syntax                | Meaning                 | Latency |
| :-------------------- | ----------------------- | ------- |
| load   r1      => r2  | r2 ← MEM(r1)            | 2       |
| loadI  x        => r2 | r2 ← x                  | 1       |
| store  r1      => r2  | MEM(r2) ← r1            | 2       |
| add    r1, r2 => r3   | r3 ← r1 + r2            | 1       |
| sub    r1, r2 => r3   | r3 ← r1 - r2            | 1       |
| mult  r1, r2 => r3    | r3 ← r1 * r2            | 1       |
| lshift  r1, r2 => r3  | r3 ← r1 << r2           | 1       |
| rshift  r1, r2 => r3  | r3 ← r1 >> r2           | 1       |
| output x              | prints MEM(x) to stdout | 1       |
