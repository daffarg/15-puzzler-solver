from queue import PriorityQueue
from copy import deepcopy
from sys import stdout
import time

def searchEmptyTile(matriks): 
    '''
        Menerima masukan matriks of integer yang elemennya unik 1-16
        Mengembalikan baris dan kolom letak elemen 16 yang merepresentasikan
        tile kosong
    '''
    for row in range(4):
        for col in range(4):
            if (matriks[row][col] == 16):
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
        Mengembalikan perhitungan sigma KURANG(i) dalam perhitungan reachable goal
        dan array of integer yang berisi hasil fungsi KURANG(i) untuk tiap tile
    '''
    arrayKurang = []
    sigma = 0
    for i in range(1, 17):
        sigmaOneTile = 0
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
                    sigmaOneTile += 1
            col = 0
        arrayKurang.append(sigmaOneTile)
    return sigma, arrayKurang

def computeKurangPlusX(kurang, matriks):
    '''
        Menerima hasil sigma KURANG(i) dan matriks puzzle yang ingin dihitung
        Mengembalikan hasil sigma KURANG(i) + X
    '''
    return kurang + computeX(matriks)

def isReachable(result):
    '''
        Menerima hasil sigma KURANG(i) + X
        Mengembalikan true jika goal reachable, false jika tidak
    '''
    if (result % 2 == 0):
        return True
    else:
        return False

def upMatriks(matriks):
    '''
        Menerima matriks puzzle
        Mengembalikan matriks hasil pergerakan UP
    '''
    upMatriks = deepcopy(matriks)
    row, col = searchEmptyTile(matriks)
    if (row - 1 >= 0):
        upMatriks[row][col] = upMatriks[row-1][col]
        upMatriks[row-1][col] = 16
    return upMatriks

def downMatriks(matriks):
    '''
        Menerima matriks puzzle
        Mengembalikan matriks hasil pergerakan DOWN
    '''
    downMatriks = deepcopy(matriks)
    row, col = searchEmptyTile(matriks)
    if (row + 1 < 4):
        downMatriks[row][col] = downMatriks[row+1][col]
        downMatriks[row+1][col] = 16
    return downMatriks

def leftMatriks(matriks):
    '''
        Menerima matriks puzzle
        Mengembalikan matriks hasil pergerakan LEFT
    '''
    leftMatriks = deepcopy(matriks)
    row, col = searchEmptyTile(matriks)
    if (col - 1 >= 0):
        leftMatriks[row][col] = leftMatriks[row][col-1]
        leftMatriks[row][col-1] = 16
    return leftMatriks

def rightMatriks(matriks):
    '''
        Menerima matriks puzzle
        Mengembalikan matriks hasil pergerakan RIGHT
    '''
    rightMatriks = deepcopy(matriks)
    row, col = searchEmptyTile(matriks)
    if (col + 1 < 4):
        rightMatriks[row][col] = rightMatriks[row][col+1]
        rightMatriks[row][col+1] = 16
    return rightMatriks

def computeTaksiran(matriks):
    '''
        Menerima matriks puzzle
        Mengembalikan nilai taksiran atau fungsi g(i), yaitu ongkos untuk
        mencapai simpul tujuan dari simpul i
    '''
    count = 0
    counter = 1
    for i in range(4):
        for j in range(4):
            if (matriks[i][j] != counter):
                count += 1
            counter += 1
    return count

def printPuzzle(matriks):
    '''
        Melakukan print matriks puzzle ke layar
    '''
    for i in range(4):
        for j in range(4):   
            if (matriks[i][j] == 16):
                print('    ', end = '')
            else:
                if (matriks[i][j] < 10):
                    print(matriks[i][j], '  ', end = '')
                else:
                    print(matriks[i][j], ' ', end = '')
        print('\n')

def solvePuzzle(matriks):
    '''
        Menerima matriks puzzle yang ingin di-solve
        Mengembalikan simpul goal dan jumlah simpul yang sudah dibangkitkan
    '''
    queue = PriorityQueue() # instantiasi priority queue
    queue.put((0, matriks, 0, None, None)) # tupel: (cost, matriks, level, parentNode, move)
    nodeBangkit = [] # inisialisasi array penampung simpul yg sudah dibangkitkan

    print("\nSearching...\nPlease wait")

    while (not(queue.empty())):
        currentNode = queue.get() # dequeue (node yg memiliki cost minimum)
        currentMatriks = currentNode[1] # dapatkan matriksnya (array 2D)
        levelNode = currentNode[2] # dapatkan levelnya

        if (computeTaksiran(currentMatriks) == 0): # jika sudah sama dengan goal, maka pencarian solusi berakhir
            break

        # tambahkan kemungkinan semua pergerakan ke dalam array bangkitTemp
        bangkitTemp = []
        bangkitTemp.append((upMatriks(currentMatriks), "UP"))
        bangkitTemp.append((downMatriks(currentMatriks), "DOWN"))
        bangkitTemp.append((leftMatriks(currentMatriks), "LEFT"))
        bangkitTemp.append((rightMatriks(currentMatriks), "RIGHT"))
        
        for mat in bangkitTemp:
            if (mat[0] not in nodeBangkit and mat[0] != matriks): # cek apakah node sudah pernah dibangkitkan
                nodeBangkit.append(mat[0])
                taksiran = computeTaksiran(mat[0])
                cost = taksiran + levelNode + 1
                queue.put((cost, mat[0], levelNode + 1, currentNode, mat[1])) # masukkan node ke antrian

        stdout.write("\rJumlah simpul yang telah dibangkitkan sejauh ini: {0}".format(len(nodeBangkit)))
        stdout.flush()

    return currentNode, len(nodeBangkit)    

def printSolution(finalNode, matriks):
    '''
        Melakukan print ke layar langkah-langkah yang dilakukan untuk memecahkan puzzle
    '''
    path = []
    while True:
        path.insert(0, finalNode)
        if (finalNode[3][1] == matriks):
            break
        finalNode = finalNode[3]

    for i in range (len(path)):
        print("\nLangkah ke-" + str(i + 1), ': ' + path[i][4] + '\n')
        printPuzzle(path[i][1])
        print("================================")

def startSolve(matriks):
    '''
        Prosedur utama untuk memecahkan puzzle yang diinginkan
        Mengecek apakah reachable goal, jika iya maka puzzle akan dipecahkan
        Jika tidak maka program berhenti
    '''
    print("\nPosisi awal: \n")
    printPuzzle(matriks)

    print("================================\n")

    totalKurang, arrayKurang = computeKurang(matriks)
    for i in range(len(arrayKurang)):
        print("Nilai KURANG(i) untuk tile ke-" + str(i+1), " = ", arrayKurang[i])
    kurangPlusX = computeKurangPlusX(totalKurang, matriks)
    print("\nNilai sigma KURANG(i) + X = ", kurangPlusX)

    print("\n================================")

    if (isReachable(kurangPlusX)):
        start = time.time()
        finalNode, nodeBangkit = solvePuzzle(matriks)
        print('\n')
        printSolution(finalNode, matriks)
        print("\nWaktu eksekusi = ", time.time() - start, "s")
        print("Jumlah simpul yang dibangkitkan = ", nodeBangkit, '\n')
    else:
        print("\nBerdasarkan hasil sigma KURANG(i) + x, persoalan tidak dapat diselesaikan (hasil ganjil)\n")