Outline = "-"*46

print(f"""
    {Outline}
    |      SELAMAT DATANG DI JAVA'S CINEMA       |
    {Outline}
    | Kode Film |   Judul Film     | Harga Tiket |
    {Outline}
    | 01.       | Captain Amerika  | Rp55.000    |
    | 02.       | Keluarga Cemara  | Rp40.000    |
    | 03.       | Dilan 1990       | Rp45.000    |
    | 04.       | Ayat-Ayat Cinta  | Rp50.000    |
    | 05.       | Merindukan Surga | Rp60.000    |
    | 06.       | Marvel Avengers  | Rp75.000    |
    | 07.       | Harry Potter     | Rp65.000    |
    {Outline}
""")

Nama = input("Silahkan masukkan nama anda: " )
Pilih_Film = input("Masukkan kode film yang ingin anda pesan (01/02/03.../07): " )
Nominal_Tiket = int(input("Berapa banyak tiket yang ingin anda beli? (1/2/3...n-1/n): " ))

if Pilih_Film == "01":
    NamaFilm = "Captain Amerika"
    Harga = 55000
elif Pilih_Film == "02":
    NamaFilm = "Keluarga Cemara"
    Harga = 40000
elif Pilih_Film == "03":
    NamaFilm = "Dilan 1990"
    Harga = 45000
elif Pilih_Film == "04":
    NamaFilm = "Ayat-Ayat Cinta"
    Harga = 50000
elif Pilih_Film == "05":
    NamaFilm = "Merindukan Surga"
    Harga = 60000
elif Pilih_Film == "06":
    NamaFilm = "Marvel Avengers"
    Harga = 75000
elif Pilih_Film == "07":
    NamaFilm = "Harry Potter"
    Harga = 65000
else:
    print(f"{Outline}")
    print("Transaksi Gagal: Salah memasukkan kode film")
    print(f"{Outline}")

HargaTotal = Harga*Nominal_Tiket
if HargaTotal <= 100000:
    Diskon = 0
    HargaAkhir = HargaTotal - Diskon
elif 100000 < HargaTotal <= 250000:
    Diskon = int(HargaTotal * (15/100))
    HargaAkhir = HargaTotal - Diskon
elif HargaTotal > 250000:
    Diskon = int(HargaTotal * (35/100))
    HargaAkhir = HargaTotal - Diskon

if Pilih_Film == "01" or Pilih_Film == "02" or Pilih_Film == "03" or Pilih_Film == "04" or Pilih_Film == "05" or Pilih_Film == "06" or Pilih_Film == "07":
    print(f"{Outline}")
    print("Transaksi Sukses")
    print(f"{Outline}")
    print(f"Nama           : {Nama}")
    print(f"Judul Film     : {NamaFilm}")
    print(f"Jumlah Tiket   : {Nominal_Tiket}")
    print(f"Harga Satuan   : Rp{Harga:,}")
    print(f"Total Harga    : Rp{HargaTotal:,}")
    print(f"Potongan Harga : Rp{Diskon:,}")
    print(f"{Outline}")
    print(f"Harga Akhir    : Rp{HargaAkhir:,}")
    print(f"{Outline}")
