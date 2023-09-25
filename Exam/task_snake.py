rows = 3
column = 6

tabl = [[0] * column for i in range(rows)] # двухмерный массив с ноликами

for rows in range(rows):
    for column in range(column):
        tabl[rows][column]  = rows * column#1 - номер строки 2 - номер столбца

for rows in range(rows): # строки(тут у нас 3 строчки потому что rows = 3
    print(*tabl[rows])