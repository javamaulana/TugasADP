data = """\
Java Maulana,2410431021,A1,ketua acara,85,Acara
Raditya Irawan,2410432003,A1,anggota acara,80,Acara
Ghefira Rhoudotul Jannah,2410431002,A2,anggota acara,82,Acara
Aisyah Ashari,2410431003,A1,ketua acara,90,Acara
Muhammad Arifin Ilham,2410431008,A2,anggota pubdok,90,Pubdok
Naila Farizka Azzahra,2410431016,A2,ketua pubdok,93,Pubdok
Yazid Riyanda Putra,2410431005,A3,anggota pubdok,78,Pubdok
Wahyu andani,2410432004,A2,anggota pubdok,85,Pubdok
Dhea Hafiza,2410431006,A3,ketua danus,75,Danus
Gibran Ramadhan,2410431032,A3,anggota danus,88,Danus
Azhari Fauzi,2410433008,A1,anggota danus,80,Danus
Dinda Rahma Mulyana,2410431034,A2,ketua danus,86,Danus
Mutiara Aviva,2410432045,A3,anggota perlengkapan,83,Perlengkapan
Zazkia Avris Yaumi,2410431039,A1,ketua perlengkapan,89,Perlengkapan
Fauzi Taufiqur Rahman,2410431036,A2,anggota perlengkapan,92,Perlengkapan
Aisyah Zahradiva,2410432010,A2,anggota perlengkapan,85,Perlengkapan
"""

with open("OrPSB22.txt", "w") as file:
    file.write(data)

print("File OrPSB22.txt berhasil dibuat dengan 4 calon per bidang.")

def hitung_poin_pengalaman(teks_pengalaman, bidang_dipilih):
    poin = 0
    teks_pengalaman = teks_pengalaman.lower()
    bidang_dipilih = bidang_dipilih.lower()

    if "ketua" in teks_pengalaman:
        poin += 2
    if bidang_dipilih in teks_pengalaman:
        poin += 3
    return poin

def baca_data():
    with open("OrPSB22.txt", "r") as file:
        baris = file.readlines()

    daftar_calon = []

    for data in baris:
        nama, nim, kelas, pengalaman, nilai_wawancara, bidang = data.strip().split(",")
        nilai_wawancara = int(nilai_wawancara)
        tambahan_poin = hitung_poin_pengalaman(pengalaman, bidang)
        nilai_akhir = (nilai_wawancara + tambahan_poin) * 100 / 100

        calon = {
            "nama": nama,
            "nim": nim,
            "kelas": kelas,
            "bidang": bidang,
            "nilai": nilai_akhir
        }
        daftar_calon.append(calon)

    return daftar_calon

def pilih_koordinator(daftar_calon):
    bidang_dic = {}

    for calon in daftar_calon:
        bidang = calon["bidang"]
        if bidang not in bidang_dic:
            bidang_dic[bidang] = []
        bidang_dic[bidang].append(calon)

    hasil = {}

    for bidang in bidang_dic:
        calon_list = bidang_dic[bidang]

        for i in range(len(calon_list)):
            idx_max = i
            for j in range(i + 1, len(calon_list)):
                if calon_list[j]["nilai"] > calon_list[idx_max]["nilai"]:
                    idx_max = j
            calon_list[i], calon_list[idx_max] = calon_list[idx_max], calon_list[i]

        if len(calon_list) >= 2:
            hasil[bidang] = [calon_list[0], calon_list[1]]
        elif len(calon_list) == 1:
            hasil[bidang] = [calon_list[0]]

    return hasil


data_calon = baca_data()
hasil_koordinator = pilih_koordinator(data_calon)

print("\nKoordinator Terpilih Tiap Bidang:")
for bidang, dua_teratas in hasil_koordinator.items():
    print(f"\nBidang: {bidang}")
    for calon in dua_teratas:
        print(f"- {calon['nama']} (NIM: {calon['nim']}) - Nilai: {calon['nilai']}")
