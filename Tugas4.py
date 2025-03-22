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

# NOMOR 2 
karakter_khusus = "!@#$%^&*()-=+[]{ }|;:'\",.<>?/`~"

while True:
    password = input("Masukkan password: ")
    
    Cek_Panjang = len(password) >= 8
    ada_huruf_kecil = False
    ada_huruf_kapital = False
    ada_angka = False
    ada_karakter_khusus = False
    
    for karakter in password:
        if karakter.islower(): 
            ada_huruf_kecil = True
        elif karakter.isupper():  
            ada_huruf_kapital = True
        elif karakter.isdigit():  
            ada_angka = True
        elif karakter in karakter_khusus:  
            ada_karakter_khusus = True
    
    if not Cek_Panjang:
        print("Panjang password minimal 8 karakter.")
    elif not ada_huruf_kecil:
        print("Password harus mengandung setidaknya 1 huruf kecil.")
    elif not ada_huruf_kapital:
        print("Password harus mengandung setidaknya 1 huruf kapital.")
    elif not ada_angka:
        print("Password harus mengandung setidaknya 1 angka.")
    elif not ada_karakter_khusus:
        print("Password harus mengandung setidaknya 1 karakter khusus.")
    else:
        print("Password Valid.")
        break
    print("Silakan coba lagi.\n")
