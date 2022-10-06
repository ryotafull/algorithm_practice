input_value = "abbc"

x = list(input_value)
targets = set(x)

ans = ["", 0]
for target in targets:
    c = x.count(target)
    if c > ans[1]:
        ans = [target, c]

print(ans[0])
