f = [int(i) for i in open('17-376.txt')]
mx = -1000
ms = -1000
count = 0
for i in f:
    k = hex(i)[2:]
    if len(k) > 1:
        if k[-2] + k[-1] == '0f':
            mx = max(mx, i)

for i in range(len(f) - 1):
    c = 0
    if f[i] % 7 == 0:
        c += 1
    if f[i + 1] % 7 == 0:
        c += 1

    if c == 1:
        if (f[i] + f[i + 1]) % mx == 0:
            count += 1
            ms = max(ms, f[i] + f[i + 1])

print(count, ms)
