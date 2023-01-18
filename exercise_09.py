# Kelvin Soto (no group)

word = ''
string = ''
list = []

for i in range(5):
    word = input('Enter a word: ')
    list.append(word.strip())
    string += word.strip() + " "

print('Words: ' + str(list))
print(string)