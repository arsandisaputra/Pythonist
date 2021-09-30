if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr1 = list(arr)
    arr1.sort()
    i = len(arr1) - 1
    champ = arr1[i]
    i -= 1
    while i >= 0:
        if arr1[i] != champ:
            print(arr1[i])
            break
        i -= 1
