import os
import os.path
import tkinter as tk
from turtle import update
from time import sleep
from matplotlib.pyplot import step
from fifteenPuzzle import startSolve, getPath


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

if (finalNode != None):
    puzzleUI = tk.Tk(className = "15-Puzzle")

    puzzleUI.resizable(False, False)

    flag = False

    num = 1
    tiles = []

    for i in range(4):
        for j in range(4):
            if (matriks[i][j] == 16):
                text = ''
            else:   
                text = str(matriks[i][j])
            tile = tk.Label(puzzleUI, text = text, width = 4, height = 2, font=("Calibri", 30))
            tiles.append(tile)
            num += 1

    def resetPuzzle():
        idx = 0
        for i in range(4):
            for j in range(4):
                if (matriks[i][j] == 16):
                    text = ''
                else:
                    text = str(matriks[i][j])
                tiles[idx].config(text = text)
                idx += 1

    idx = 0
    for i in range(4):
        for j in range(4):
            tiles[idx].grid(row = i, column = j, padx = 0.5, pady = 0.5)
            idx += 1

    path = getPath(finalNode, matriks)
    step = -1

    def startPuzzle():
        global step
        if step > -1:
            step = -1
        updatePuzzle()
        
    def updatePuzzle():
        global step
        startButton["state"] = "disabled"
        if (step < len(path)):
            if step == -1:
                resetPuzzle()
            else :
                idx = 0
                for i in range(4):
                    for j in range(4):
                        if (path[step][1][i][j] == 16):
                            text = ''
                        else:
                            text = str(path[step][1][i][j])
                        tiles[idx].config(text = text)
                        idx += 1
            step += 1  
            puzzleUI.after(1000, updatePuzzle)  
        else:
            startButton["state"] = "normal"    

    startButton = tk.Button(puzzleUI, text = "Mulai", command = startPuzzle)
    startButton.grid(row = 4, column = 1, columnspan = 4, padx = 1, pady = 1)

    puzzleUI.mainloop()