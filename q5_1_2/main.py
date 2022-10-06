# Takahashi's Information
input_values = [
    [1, 0, 1],  # i=1
    [2, 1, 2],  # i=2
    [1, 0, 1],  # i=3
]
# a1 + b1 = 1 a1 + b2 = 0 a1 + b3 = 1
# a2 + b1 = 2 a2 + b2 = 1 a2 + b3 = 2
# a3 + b1 = 1 a3 + b2 = 0 a3 + b3 = 1
# 各行 or 列 の差分がどれも等しくならなければならない

import numpy as np

a = np.array(input_values)

is_true = True
# 縦
for i in range(-1, 2):
    tmp = list(a[:, i] - a[:, i + 1])
    is_true = is_true and (tmp.count(tmp[0]) == 3)

# 横
for i in range(-1, 2):
    tmp = list(a[i] - a[i + 1])
    is_true = is_true and (tmp.count(tmp[0]) == 3)

print("Yes" if is_true else "No")
