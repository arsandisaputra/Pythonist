n = 6

i = 0
while i<n:
    # print space
    j=n-i-1
    cetak = ''
    while j>0:
        cetak += ' '
        j-=1
    k=0
    while k<=i:
        cetak += '#'
        k+=1
    print(cetak)
    i+=1