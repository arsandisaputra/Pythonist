if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    records.sort(key=lambda x: x[1])
    lowest = records[0][1]
    secondLowestNames = []
    secondLowestValue = -1
    for record in records:
        if record[1] != lowest:
            secondLowestValue = record[1]
            break
    print(secondLowestValue)
    for record in records:
        if record[1] == secondLowestValue:
            secondLowestNames.append(record[0])
    secondLowestNames.sort()
    for name in secondLowestNames:
        print(name)
