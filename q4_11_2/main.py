# 3番目
input_values = "4 18 25 20 9 13"

inputs = list(map(int, input_values.split(" ")))
inputs.sort()

print(inputs[-3])
