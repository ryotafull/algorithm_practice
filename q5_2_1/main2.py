# ゾロ目
# 11...1 * [1-9] でできる
import math
N = 50
digit = math.ceil(N / 9)
y = N % 9
if y == 0:
    y = 9
print(int("1" * digit) * y)