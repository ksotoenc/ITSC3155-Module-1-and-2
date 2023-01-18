# Kelvin Soto (no group)

list1 = []
list2 = []
list3 = []

for i in range(5):
    list1.append(input('Enter a number for the first list: '))

for i in range(5):
    list2.append(input('Enter a number for the second list: '))

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j] and list3.count(list1[i]) == 0:
            list3.append(list1[i])
            break

print('First list: ' + str(list1))
print('Second list: ' + str(list2))
print('Common list: ' + str(list3))




