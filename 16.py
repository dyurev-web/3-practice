n = int(input())
for a in range(2, n + 1):
    s = 0
    for d in range(1, a // 2 + 1):
        if a % d == 0:
            s += d
    if s == a:
        print(a)