run = True
print(run)
i = 1
while run:
    if i<= 10:
        print(i)
        i +=1
    else: 
        run = False

for i in range(-1, -11, -1):
    print(i)


num = int(input('Enter an integer :'))
total = 0

for i in range(1, num+1):
    total = total + i
    print(i, total)

for i in range(1, 50+1):
    for j in range(2, i):
        if (i % j) == 0:
            break
    else:
        print (i)

