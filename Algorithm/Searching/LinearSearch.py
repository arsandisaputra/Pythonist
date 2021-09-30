elmnts = [3, 9, 8, 2, 1, 4, 6, 5, 7]
search = 6
found = False
index = 0
while index < len(elmnts):
    if search == elmnts[index]:
        found = True
        print('Find', search, 'in index', index)
        break
    index += 1
if not found:
    print(search, 'not founded!')
