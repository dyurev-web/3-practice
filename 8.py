n = int(input())
q = 0
while 2**q < n:
    q += 1
print(q)