# Bingo
import copy

input_values = [
    [84, 97, 66],
    [79, 89, 11],
    [61, 59, 7],
    7,
    89,
    7,
    87,
    79,
    24,
    84,
    30,
]
card = input_values[0:3]
balls = input_values[3:]
N = 3
bs = set(balls)

verticals = []

for i in range(N):
    for j in range(N):
        if card[i][j] in bs:
            card[i][j] = 0


for i in range(N):
    verticals.append([v[i] for v in card])

diagonal1 = [v[i] for i, v in enumerate(card)]
diagonal2 = [v[(i + 1) * -1] for i, v in enumerate(card)]

targets = copy.copy(card)
targets = targets + verticals
targets.append(diagonal1)
targets.append(diagonal2)

is_exists = False
for target in targets:
    if sum(target) == 0:
        is_exists = True
        break
print("Yes" if is_exists else "No")
