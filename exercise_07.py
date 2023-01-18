# Kelvin Soto (no group)

list = []
even = []
answer = ''

while (answer != 'QUIT'):
    answer = input('Enter any integer: ')
    if (answer != 'QUIT'):
        list.append(int(answer))

for i in range(len(list)):
    if list[i] % 2 == 0:
        even.append(list[i])

print('All nums: ' + str(list))
print('Even nums: ' + str(even))
