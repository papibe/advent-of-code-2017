# init registers
b = c = d = e = f = g = h = 0

# a = 1 causes these values
b = 108400
c = 125400

e = 2
g = 2

while g != 0:

    f = 1
    for d in range(2, b + 1):
        # d * e - b == 0
        if b % d == 0 and 2 <= (b // d) <= b:
            f = 0
            break
    if f == 0:
        h -= -1

    g = b - c
    b -= -17

print(h)  # 903
