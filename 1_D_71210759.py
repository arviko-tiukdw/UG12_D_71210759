print ("Program Menampilkan Baris Deret Angka Genap")

a = int(input("Masukkan Awal Deret : "))
b = int(input("Masukkan Akhir Deret : "))

for c in range(a,b,2):
    print(c)

d = str(c%3 !=0 & c&7 !=0)
print(d)





