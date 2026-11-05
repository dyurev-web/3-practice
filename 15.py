n = int(input())
for a in range(2, n+1):
    if a < 2:
        continue
    else:
        is_prime = True
        i = 2
        while i * i <= a:
            if a % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print(a)