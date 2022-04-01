from fifteenPuzzle import startSolve

fileName = input("Masukkan nama file: ")

try:
    f = open(fileName, 'r')
except:
    print("File tidak ditemukan")
    quit()
matriks = []
matriks = [[int(elmt) for elmt in line.split()] for line in f]

startSolve(matriks)