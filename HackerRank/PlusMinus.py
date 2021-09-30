arr = [-4, 3, -9, 0, 4, 1]
negative = positive = zero = 0
for x in arr:
    if x < 0:
        negative += 1
    elif x > 0:
        positive += 1
    else:
        zero += 1
# print(positive, negative, zero)
print('{:.6f}'.format(positive/len(arr)))
print('{:.6f}'.format(negative/len(arr)))
print('{:.6f}'.format(zero/len(arr)))
