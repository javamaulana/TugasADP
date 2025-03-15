# M = float(input("Masukkan modal awal: "))
# r = float(input("Masukkan suku bunga tahunan (%): "))
# T = float(input("Masukkan target investasi: "))

# tahun = 0
# while M < T:
#     tahun += 1
#     M += M * (r / 100)
#     print(f"Tahun ke-{tahun}: Rp{int(M)}")

# print(f"Target tercapai dalam {tahun} tahun!")

# tahun = 0
# for tahun in range(1, T+1):
#     M += M * (r / 100)
#     print(f"Tahun ke-{tahun}: Rp{int(M)}")
#     if M >= T:
#         break

# print(f"Target tercapai dalam {tahun} tahun!")

outline = "-"*51
outline2 = "="*58
print(f"""
{outline}
|    Selamat Datang di JM'Invesment Foundation    |
|  Solusi Cerdas untuk Investasi Masa Depan Anda  | 
{outline}
""")

modal = float(input("Masukkan modal awal investasi (Rp): "))
modal_akhir = modal
suku_bunga = float(input("Masukkan suku bunga tahunan (%): "))
target = float(input("Masukkan target investasi (Rp): "))

if target > modal:
    tahun = 0
    print(f"\n{outline}")
    print(f"|            Data /tahun Investasi Anda           |")
    print(f"{outline}")

    while modal < target:
        tahun += 1
        pertambahan = modal * (suku_bunga / 100)
        modal += pertambahan
        print(f"Tahun ke-{tahun}: Rp{modal:,.2f}          | +Rp{pertambahan:,.2f}")

    modal_akhir = modal-modal_akhir 

    print(f"\n{outline}")
    print(f"               Selamat!                 ")                 
    print(f"Target investasi Rp{target:,.2f} tercapai dalam {tahun} tahun")
    print(f"Dengan pertumbuhan modal sebesar Rp{modal_akhir:,.2f}")
    print(f"\n{outline2}")
    print(f"| Terima kasih telah berinvestasi bersama JM'Investment! |")
    print(f"|         Kami tunggu investasi Anda selanjutnya.        |")
    print(f"{outline2}")

else:
    print(f"{outline}")
    print(f"|   Transaksi Gagal: Modal awal investasi harus lebih besar dari target.  |")
    print(f"{outline}")

