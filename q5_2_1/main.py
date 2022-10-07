# ゾロ目
# 11...1 * [1-9] でできる
N = 50
digit = N // 9 + 1
y = N % 9
if y == 0:
    digit -= 1
    y = 9
print(int("1" * digit) * y)