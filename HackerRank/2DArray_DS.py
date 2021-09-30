arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

maxHourglass = -50
i = 1
while i <= 4:
    j = 1
    while j <= 4:
        temp = arr[i][j]+sum(arr[i-1][j-1:j+2])+sum(arr[i+1][j-1:j+2])
        if temp > maxHourglass:
            maxHourglass = temp
        j += 1
    i += 1
print(maxHourglass)
