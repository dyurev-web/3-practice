x = int(input())
count = 0
a = 1
while a * a <= x:
    b2 = x - a * a
    b = int(b2 ** 0.5)
    if b >= a and b * b == b2:
        count += 1
    a += 1
print(count)