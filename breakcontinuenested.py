#Break
i=10
while i>0:
    i=i-1
    if i==7:
        break
    print(i)

#Continue
i=10
while i>0:
    i=i-1
    if i==7:
        continue
    print('Value is:', i)
#nested loops
    i=2
    while i>0:
        i=i-1
        j=5
        while j>0:
            print(j)
            j=j-1
