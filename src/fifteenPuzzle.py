from queue import PriorityQueue
import time
from copy import deepcopy

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
    return sigma

def computeKurangPlusX(kurang, matriks):
    return kurang + computeX(matriks)

def isReachable(result):
    if (result % 2 == 0):
        return True
    else:
        return False

def upMatriks(matriks):
    upMatriks = deepcopy(matriks)
    row, col = searchEmptyTile(matriks)
    if (row - 1 >= 0):
        upMatriks[row][col] = upMatriks[row-1][col]
        upMatriks[row-1][col] = 16
    return upMatriks

def downMatriks(matriks):
    downMatriks = deepcopy(matriks)
    row, col = searchEmptyTile(matriks)
    if (row + 1 < 4):
        downMatriks[row][col] = downMatriks[row+1][col]
        downMatriks[row+1][col] = 16
    return downMatriks

def leftMatriks(matriks):
    leftMatriks = deepcopy(matriks)
    row, col = searchEmptyTile(matriks)
    if (col - 1 >= 0):
        leftMatriks[row][col] = leftMatriks[row][col-1]
        leftMatriks[row][col-1] = 16
    return leftMatriks

def rightMatriks(matriks):
    rightMatriks = deepcopy(matriks)
    row, col = searchEmptyTile(matriks)
    if (col + 1 < 4):
        rightMatriks[row][col] = rightMatriks[row][col+1]
        rightMatriks[row][col+1] = 16
    return rightMatriks

def computeTaksiran(matriks):
    count = 0
    counter = 1
    for i in range(4):
        for j in range(4):
            if (matriks[i][j] != counter):
                count += 1
            counter += 1
    return count

def printPuzzle(matriks):
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
    queue = PriorityQueue() # instantiasi priority queue
    queue.put((0, matriks, 0, None)) # tupel: (cost, matriks, level, parentNode)
    nodeBangkit = [] # inisialisasi array penampung simpul yg sudah dibangkitkan

    while (not(queue.empty())):
        currentNode = queue.get() # dequeue (node yg memiliki cost minimum)
        currentMatriks = currentNode[1]
        levelNode = currentNode[2]

        if (computeTaksiran(currentMatriks) == 0): # ketemu
            break

        # tambahkan kemungkinan semua pergerakan ke dalam array expand
        expand = []
        expand.append(upMatriks(currentMatriks))
        expand.append(downMatriks(currentMatriks))
        expand.append(leftMatriks(currentMatriks))
        expand.append(rightMatriks(currentMatriks))
        
        for mat in expand:
            if (mat not in nodeBangkit and mat != matriks):
                nodeBangkit.append(mat)
                taksiran = computeTaksiran(mat)
                cost = taksiran + levelNode + 1
                queue.put((cost, mat, levelNode + 1, currentNode))
    return currentNode, len(nodeBangkit)    

def printSolution(finalNode):
    path = []
    while True:
        path.insert(0, finalNode)
        if (finalNode[3] == None):
            break
        finalNode = finalNode[3]

    for i in range (len(path)):
        print("\nLangkah ke-" + str(i + 1), '\n')
        printPuzzle(path[i][1])
        print("================================")

def startSolve(matriks):
    print("\nPosisi awal: \n")
    printPuzzle(matriks)

    kurang = computeKurang(matriks)
    print("Nilai fungsi KURANG(i) = ", kurang)
    kurangPlusX = computeKurangPlusX(kurang, matriks)
    print("Nilai KURANG(i) + X = ", kurangPlusX)

    print("\n================================")

    if (isReachable(kurangPlusX)):
        start = time.time()
        finalNode, nodeBangkit = solvePuzzle(matriks)
        printSolution(finalNode)
        print("Waktu eksekusi = ", time.time() - start, "s")
        print("Jumlah simpul yang dibangkitkan = ", nodeBangkit)
    else:
        print("Berdasarkan hasil fungsi KURANG(i) + x, persoalan tidak dapat diselesaikan")