# Kelvin Soto (no group)

list = []
size = int(input('Enter a number: '))
total = 0

for i in range(1, size + 1):
    num = float(input('Enter number ' + str(i) + ' : '))
    list.append(num)
    total += num

print('List: ' + str(list))
print('Average: ' + str(total/size))
