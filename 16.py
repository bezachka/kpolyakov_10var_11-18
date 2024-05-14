f = [0] * (9**9 + 1)
f[0] = 0
count = 0
for n in range(1, 9 ** 9 + 1):
    if n < 9:   f[n] = n // 3 + n % 3
    if n >= 9:  f[n] = f[n//9] + f[n%9]

    if f[n] == 33:
        count += 1
        print(count)

#1122 - ans