prev = float(input())
k = 0
cur = float(input())
while cur != 0:
    if cur < prev:
        k += 1
    prev = cur
    cur = float(input())
print(k)