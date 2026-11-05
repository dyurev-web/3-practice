n, k, r = map(int, input().split())
dl = n
d = 1
while dl < r:
    dl = dl + dl*(k/100)
    d += 1
print(d)