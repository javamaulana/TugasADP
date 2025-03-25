## NOMOR 1
Baris = int(input("Masukkan jumlah baris: "))
Kolom = int(input("Masukkan jumlah kolom: "))
print(""""
Tipe Pola:
1. X O X O X O
   O X O X O X
2. O X O X O x
   X O X O X O
3. X X X X X X
   O O O O O O
4. O O O O O O
   X X X X X X
""")
Tipe = input("Masukkan tipe pola (1/2/3/4): ")

for x in range(Baris): 
    for y in range(Kolom): 
        if Tipe == "1":
            if (x + y) % 2 == 0:
                print("X", end=" ")
            elif (x + y) % 2 == 1:
                print("O", end=" ")
        elif Tipe == "2":
            if (x + y) % 2 == 0:
                print("O", end=" ")
            elif (x + y) % 2 == 1:
                print("X", end=" ")
        elif Tipe == "3":    
            if x % 2 == 0:
                print("X", end=" ")
            elif x % 2 == 1:
                print("O", end=" ")
        elif Tipe == "4":
            if x % 2 == 0:
                print("O", end=" ")
            elif x % 2 == 1:
                print("X", end=" ")
    print()
