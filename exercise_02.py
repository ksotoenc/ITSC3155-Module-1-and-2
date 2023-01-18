# Kelvin Soto (no group)

# I found out about the endswith() string method on this page, as I wanted to check
# if there is anything already built in that might help me.
# link: https://www.w3schools.com/python/python_ref_string.asp

str1 = input('Enter a string: ')
str2 = input('Enter another string: ')

if str1.endswith(str2):
    print('true')
elif str2.endswith(str1):
    print('true')
else:
    print('false')

