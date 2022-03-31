from queue import PriorityQueue
from turtle import left

fileName = input("Masukkan nama file: ")
f = open(fileName, 'r')
matriks = []
matriks = [[int(elmt) for elmt in line.split()] for line in f]

def searchEmptyTile(matriks): 
    '''
        Menerima masukan matriks of integer yang elemennya unik 1-16
        Mengembalikan baris dan kolom letak elemen 16 yang merepresentasikan
        tile kosong
    '''
    for row in range(4):
        for col in range(4):
            if (matriks[row][col] == '16'):
                return row, col

def computeX(matriks):
    '''
        Menerima masukan matriks of integer yang elemennya unik 1-16
        Mengembalikan perhitungan nilai X dalam perhitungan reachable goal
    '''
    row, col = searchEmptyTile(matriks)
    if ((row % 2 == 0 and col % 2 != 0) or (row % 2 != 0 and col % 2 == 0)):
        return 1
    else:
        return 0

def computeKurang(matriks):
    '''
        Menerima masukan matriks of integer yang elemennya unik 1-16
        Mengembalikan perhitungan sigma KURANG(i) + X dalam perhitungan reachable goal
    '''
    sigma = 0
    for i in range(1, 17):
        row = 0
        col = 0
        found = False
        while (row < 4 and not(found)):
            while (col < 4 and not(found)):
                if matriks[row][col] == i:
                    found = True
                else:
                    col += 1   
            if (not found):
                col = 0 
                row += 1
        for j in range(row, 4):
            for k in range(col, 4):
                if (matriks[j][k] < i):
                    sigma += 1
            col = 0
    return sigma + computeX(matriks)

def isReachable(matriks):
    if (computeKurang(matriks) % 2 == 0):
        return True
    else:
        return False

def upMatriks(matriks):
    upMatriks = matriks.copy()
    row, col = searchEmptyTile(matriks)
    if (row - 1 >= 0):
        upMatriks[row][col] = upMatriks[row-1][col]
        upMatriks[row-1][col] = 16
    return upMatriks

def downMatriks(matriks):
    downMatriks = matriks.copy()
    row, col = searchEmptyTile(matriks)
    if (row + 1 < 4):
        downMatriks[row][col] = downMatriks[row+1][col]
        downMatriks[row+1][col] = 16
    return downMatriks

def leftMatriks(matriks):
    leftMatriks = matriks.copy()
    row, col = searchEmptyTile(matriks)
    if (col - 1 >= 0):
        leftMatriks[row][col] = leftMatriks[row][col-1]
        leftMatriks[row][col-1] = 16
    return leftMatriks

def rightMatriks(matriks):
    rightMatriks = matriks.copy()
    row, col = searchEmptyTile(matriks)
    if (col + 1 < 4):
        rightMatriks[row][col] = rightMatriks[row][col+1]
        rightMatriks[row][col+1] = 16
    return rightMatriks

queue = PriorityQueue()


        