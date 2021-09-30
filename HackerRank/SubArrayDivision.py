s = [4]
d = 4
m = 1

i = 0
count = 0
while i <= len(s)-m:
    # print(s[i:m+i])
    if sum(s[i:m+i]) == d:
        count += 1
    i += 1

print(count)
