import os
import os.path
import tkinter as tk
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
except: # file tidak ditemukan
    print("File tidak ditemukan pada folder test")
    quit()

matriks = [[int(elmt) for elmt in line.split()] for line in f] # ubah file ke dalam matriks
finalNode = startSolve(matriks) # cari solusi puzzle

# jika puzzle bisa dipecahkan, tampilkan UI
if (finalNode != None):
    puzzleUI = tk.Tk(className = "15-Puzzle")
    puzzleUI.resizable(False, False)

    tiles = [] # array penampung label yang merepresentasikan tile pada UI

    # inisialisasi puzzle dengan keadaan awal
    for i in range(4):
        for j in range(4):
            if (matriks[i][j] == 16): # jika tile kosong
                relief = "flat"
                text = ''
                bgColor = "#ffffff"
                fgColor = "#ffffff"
            else:   
                relief = "raised"
                bgColor = "#247881"
                fgColor = "#17252a"
                text = str(matriks[i][j])
            tile = tk.Label(puzzleUI, text = text, width = 4, height = 2, font=("Segoe UI Semibold", 30), bg= bgColor, fg = fgColor, relief = relief)
            tiles.append(tile)

    # posisikan tile dengan grid
    idx = 0
    for i in range(4):
        for j in range(4):
            tiles[idx].grid(row = i, column = j, padx = 0.5, pady = 0.5)
            idx += 1

    path = getPath(finalNode, matriks)
    step = -1 # counter untuk menghitung step yang sudah ditampilkan pada UI

    def resetPuzzle():
        '''
            Mereset tampilan puzzle kembali ke tampilan awal
        '''
        idx = 0
        for i in range(4):
            for j in range(4):
                if (matriks[i][j] == 16): # jika tile kosong
                    relief = "flat"
                    text = ''
                    bgColor = "#ffffff"
                    fgColor = "#ffffff"
                else:
                    relief = "raised"
                    bgColor = "#247881"
                    fgColor = "#17252a"
                    text = str(matriks[i][j])
                tiles[idx].config(text = text, background = bgColor, fg = fgColor, relief = relief)
                idx += 1

    def startPuzzle():
        '''
            Prosedur untuk memulai menampilkan pergerakan puzzle pada UI
        '''
        global step
        if step > -1: 
            step = -1 # reset step ke -1
        updatePuzzle()
        
    def updatePuzzle():
        '''
            Melakukan pergantian tampilan puzzle pada UI
            sesuai dengan urutan pergerakan yang dilakukan
        '''
        global step
        startButton["state"] = "disabled" # disable tombol Mulai
        if (step < len(path)): # jika belum mencapai step terakhir
            if step == -1:
                resetPuzzle()
            else :
                idx = 0
                for i in range(4):
                    for j in range(4):
                        if (path[step][1][i][j] == 16): # jika tile kosong
                            relief = "flat"
                            text = ''
                            bgColor = "#ffffff"
                            bgColor = "#ffffff"
                        else:
                            relief = "raised"
                            bgColor = "#247881"
                            fgColor = "#17252a"
                            text = str(path[step][1][i][j])
                        tiles[idx].config(text = text, background = bgColor, fg = fgColor, relief = relief)
                        idx += 1
            step += 1  
            puzzleUI.after(1000, updatePuzzle) # panggil kembali prosedur updatePuzzle setelah 1 detik
        else: # pergerakan sudah selesai
            startButton["state"] = "normal" # aktifkan kembali tombol Mulai

    # tambahkan tombol Mulai
    startButton = tk.Button(puzzleUI, text = "Mulai", font=("Segoe UI Semibold", 12), command = startPuzzle, width = 5, height = 2) 
    startButton.grid(row = 4, column = 1, columnspan = 2, padx = 1, pady = 1)

    puzzleUI.mainloop()