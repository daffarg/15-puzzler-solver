import os
import os.path
from fifteenPuzzle import startSolve

fileName = input("Masukkan nama file: ")

try:
    if (os.path.basename(os.path.normpath(os.getcwd())) == 'src'):
            os.chdir("..")
    currentDir = os.getcwd() # direktori tempat menjalankan program
    # mendapatkan semua path yang terdapat pada direktori repository (parent directory dari src)
    arrayOfPath = [os.path.join(currentDir, arrayOfPath) for arrayOfPath in os.listdir(currentDir) if os.path.isdir(os.path.join(currentDir, arrayOfPath))]
    # pengecekan apakah terdapat file tsb pada folder test
    for item in arrayOfPath:
        if os.path.exists(item + '\\' + fileName) and os.path.basename(os.path.normpath(item)) == 'test':
            file = item + '\\' + fileName
    f = open(file, 'r')
except:
    print("File tidak ditemukan pada folder test")
    quit()
matriks = []
matriks = [[int(elmt) for elmt in line.split()] for line in f] # ubah file ke dalam matriks

startSolve(matriks) # cari solusi puzzle