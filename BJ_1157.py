string = input().upper()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = [0] * 26
num = 0

for i in alphabet:
    count[num] = string.count(i)
    num += 1

maxcnt = max(count)
if count.count(maxcnt) > 1:
    print('?')
else:
    print(alphabet[count.index(max(count))])