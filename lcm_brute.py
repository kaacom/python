a, b = int(input()), int(input())
i = min(a, b)
while True:
    if i % a == 0 and i % b == 0:
        break
    i += 1
print(i)