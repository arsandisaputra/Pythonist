c = [0, 1, 0, 0, 0, 1, 0]

i = 0
jumps = 0
if len(c) == 2:
    print(1)
while i < len(c):
    if (c[i] == 1):
        i -= 1
    else:
        jumps += 1
        if i == len(c) - 2:
            i += 1
        else:
            i += 2
print(jumps)
