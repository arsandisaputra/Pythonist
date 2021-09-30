
arr = [[11, 2, 4],
       [4, 5, 6],
       [10, 8, - 12]]

i = 0
leftToRight = 0
rightToLeft = 0
while i < len(arr):
    leftToRight += arr[i][i]
    rightToLeft += arr[len(arr)-i-1][i]
    i += 1
print(abs(leftToRight-rightToLeft))
