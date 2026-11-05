mx = -1          # пока максимум не найден
x = int(input())

while x != -1:
    if x > mx:
        mx = x
    x = int(input())

print(mx)