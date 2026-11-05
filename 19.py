n = int(input())
total = 0
for a in range(n + 1):
    for b in range(a + 1, n + 1):
        total += a + b
for a in range(n + 1):
    total += 2 * a
print(total)