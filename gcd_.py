def gcd(x, y):
    if y > x:
        x, y = y, x
    if y == 0:
        return x
        # Рекурсивный вызов, формула: gcd (a, b) = gcd (b, a% b) {a> b}
    return gcd(y, x % y)
x = input(print('num1: '))
y = input(print('num2: '))
num = gcd(x,y)
print('answer: ',num)