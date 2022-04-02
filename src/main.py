import os
import os.path
import tkinter as tk
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

matriks = [[int(elmt) for elmt in line.split()] for line in f] # ubah file ke dalam matriks
finalNode = startSolve(matriks) # cari solusi puzzle

puzzleUI = tk.Tk(className = "15-Puzzle")

# puzzleUI.minsize(300, 300)
# puzzleUI.maxsize(300, 300)

num = 1
tiles = []
for i in range(4):
    for j in range(4):
        tile = tk.Label(puzzleUI, text = str(num), width = 4, height = 2, font=("Calibri", 30))
        tiles.append(tile)
        num += 1

idx = 0
for i in range(4):
    for j in range(4):
        tiles[idx].grid(row = i, column = j, padx = 0.5, pady = 0.5)
        idx += 1

puzzleUI.mainloop()

