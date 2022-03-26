def binary_search(collection, target):
    (lo, hi) = (0, len(collection)-1)
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if target == collection[mid]:
            return mid
        elif target > collection[mid]:
            lo = mid+1
        else:
            hi = mid-1
    return -1


if __name__ == '__main__':
    collection = [2, 3, 5, 7, 8, 10, 12, 15, 18, 20]  # array must be sorted before search
    target = 7
    found = binary_search(collection, target)
    if found == -1:
        print(target,"not found.")
    else:
        print(target,"found at",found,"index.")