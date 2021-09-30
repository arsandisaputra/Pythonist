scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

i = 1
highest = lowest = scores[0]
best = worst = 0

while i < len(scores):
    if scores[i] > highest:
        highest = scores[i]
        best += 1
    elif scores[i] < lowest:
        lowest = scores[i]
        worst += 1
    i += 1
result = [best, worst]
print(result)
