elmnts = [3, 3, 3, 3, 2, 3, 3]
print('before :', elmnts)
# print('----------')
i = 1
while i < len(elmnts):
    active = elmnts[i]
    j = i-1
    while j >= 0:
        if active >= elmnts[j]:
            break
        j -= 1
    elmnts.pop(i)
    elmnts.insert(j+1, active)
    i += 1
# print('----------')
print('after :', elmnts)
