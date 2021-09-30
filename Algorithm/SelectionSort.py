elmnts = [5, 4, 7, 2, 9, 0]
print('before :', elmnts)
# print('----------')
i = 0
while i < len(elmnts):
    mini = elmnts[i]
    j = i
    indexmini = i
    while j < len(elmnts):
        if elmnts[j] < mini:
            mini = elmnts[j]
            indexmini = j
        j += 1
    temp = elmnts[indexmini]
    elmnts[indexmini] = elmnts[i]
    elmnts[i] = temp
    i += 1
print('after :', elmnts)
