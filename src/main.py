fileName = input("Masukkan nama file: ")
f = open(fileName, 'r')
matriks = []
matriks = [line.split() for line in f]
print(matriks)
