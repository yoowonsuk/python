i = 1
while i < 100:
    i += 1
    if i % 2 == 0 or i % 3 == 0:
        continue
    print(i, end = ' ')

