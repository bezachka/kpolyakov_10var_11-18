
for a in range(1, 1000):
    count = 0
    for x in range(1, 555):
        f = ((not (5 <= x <= 54)) and (50 <= x <= 93)) <= (x > a)
        if f == 0:
            count += 1
        


    if count == 20:
        print(a)
        