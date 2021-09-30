grades = [73, 67, 38, 33]

for v in grades:
    mult5 = round(v / 5)
    if mult5*5 < 40:
        print(v)
        continue
    if mult5*5 >= v:
        print(mult5*5)
    else:
        print(v)
