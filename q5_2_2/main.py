# Golf
K = 7  # 1 <= K <= 1000
A,B = 500, 600 # 1 <= A < B <= 1000

syou = A // K
if B >= (syou + 1) * K:
    print("OK")
else:
    print("NG")
