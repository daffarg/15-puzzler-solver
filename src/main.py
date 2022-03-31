fileName = input("Masukkan nama file: ")
f = open(fileName, 'r')
matriks = []
matriks = [line.split() for line in f]

def searchEmptyTile():
    for row in range(4):
        for col in range(4):
            if (matriks[row][col] == '0'):
                return (row, col)

def computeX():
    row, col = searchEmptyTile()
    if ((row % 2 == 0 and col % 2 != 0) or (row % 2 != 0 and col % 2 == 0)):
        return 1
    else:
        return 0
