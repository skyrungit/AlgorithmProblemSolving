num1, num2 = input().split()

listnum1 = []
listnum2 = []

for i in range(len(num1)):
    listnum1.append(num1[len(num1)-1 - i])

for i in range(len(num2)):
    listnum2.append(num2[len(num2)-1 - i]) 

intnum1 = int(''.join(listnum1))
intnum2 = int(''.join(listnum2))

if intnum1 > intnum2:
    print(intnum1)
else:
    print(intnum2)