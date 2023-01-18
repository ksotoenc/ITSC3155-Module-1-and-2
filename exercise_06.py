# Kelvin Soto (no group)

row_num = int(input('Enter a row number from 1 to 5: '))
col_num = int(input('Enter a column number from 1 to 5: '))

for i in range(1, 6):
    for j in range(1, 6):
        if j == col_num and i == row_num:
            print('1 ', end="")
            continue
        print('0 ', end= "")
    print("")
