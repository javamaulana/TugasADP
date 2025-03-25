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
