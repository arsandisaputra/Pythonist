q = [2, 1, 5, 3, 4]

how = 0
tooChaotic = False
i = 0
while i < len(q):
    must = i+1
    if q[i] > must:
        if q[i] - must > 2:
            print("Too chaotic")
            tooChaotic = True
            break
        else:
            how += (q[i] - must)
    i += 1
if tooChaotic == False:
    print(how)
