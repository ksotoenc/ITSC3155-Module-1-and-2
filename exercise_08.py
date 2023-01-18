# Kelvin Soto (no group)

list = []
unique = []

for i in range(1,11):
    list.append(int(input('Enter number ' + str(i) + ' :')))

for i in range(len(list)):
    if list.count(list[i]) == 1:
        unique.append(list[i])

print("All nums: " + str(list))
print('Unique nums: ' + str(unique))