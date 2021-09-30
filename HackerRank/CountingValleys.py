steps = 8
path = "DDUUUUDD"
level = 0
valleys = 0
gotoValley = False
for i in path:
    if i == 'U':
        level += 1
        if level == 0 and gotoValley:
            valleys += 1
            gotoValley = False
    else:
        level -= 1
        if level < 0:
            gotoValley = True
print(valleys)