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
        print("Sedikit amat bro, itu password apa gaji? Minimal 8 karakter ya bro")
    elif not ada_huruf_kecil:
        print("Badan boleh besar, tapi password harus ada huruf kecil ya bro")
    elif not ada_huruf_kapital:
        print("Huruf kapitalnya jangan dilupain bro")
    elif not ada_angka:
        print("Kamu ada dendam pribadi sama angka ya bro?")
    elif not ada_karakter_khusus:
        print("Biar ga dihack bocil epep, tambahkan karakter khusus bro")
    else:
        print("Nahh gini kan oke passwordnya bro!")
        break
