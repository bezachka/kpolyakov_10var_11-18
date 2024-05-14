sp = []

for x in range(17):
    f1 = 5 * 17 ** 4 + x * 17 ** 3 + x * 17 ** 2 + 7 * 17 ** 1 + 8 * 17 ** 0
    
    f2 = 4 * 18 ** 3 + x * 18 ** 2 + x * 18 ** 1 + 9 * 18 ** 0
        
    f3 = 8 * 19 ** 4 + 8 * 19 ** 3 + x * 19 ** 2 + x * 19 ** 1 + 5 * 19 ** 0
    
    for y in range(22):
        f4 = 6 * 22 ** 4 + x * 22 ** 3 + y * 22 ** 2 + 2 * 22 ** 1 + 3 * 22 ** 0
        f = f1 + f2 + f3 - f4

        if f > 0 and f % 405 == 0:
            sp.append(x)
            sp.append(y)

k = 1
for i in sp:
    k = k * i

print(k)
        