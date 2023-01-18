# Kelvin Soto (no group)

# This website helped me understand how to append more than 1 object from a list
# while following a specific interval (it helped me write char_list[i: i+3])
# URL: https://www.tutorialspoint.com/python3/python_lists.htm

string = input('Enter a string: ')
char_list = list(string)
split_list = []

for i in range(0, len(char_list), 3):
    split_list.append(char_list[i:i+3])

print(str(split_list))
