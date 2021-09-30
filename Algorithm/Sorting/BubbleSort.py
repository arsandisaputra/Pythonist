elmnts = [5, 4, 7, 2, 9, 0]
print('before :', elmnts)
# print('----------')
i = len(elmnts) - 1
while i >= 0:
    j = 0
    while j <= i - 1:
        k = j+1
        if elmnts[j] > elmnts[k]:
            temp = elmnts[k]
            elmnts[k] = elmnts[j]
            elmnts[j] = temp
            # print(elmnts)
        j += 1
    i -= 1
# print('----------')
print('after :', elmnts)
