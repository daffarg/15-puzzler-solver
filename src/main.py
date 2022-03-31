fileName = input("Masukkan nama file: ")
f = open(fileName, 'r')
matriks = []
matriks = [[int(elmt) for elmt in line.split()] for line in f]

print(matriks)

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
        