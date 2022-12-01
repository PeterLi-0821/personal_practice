tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

# Functions
def printTable(list):
    for x in range(0, len(list[0])):
        for y in range(0, len(list)):
            print(str(list[y][x]).rjust(8), end=' ')
        print('')

printTable(tableData)
