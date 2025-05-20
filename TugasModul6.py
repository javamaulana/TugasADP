nilai_indeks = [
    ["A", 4.00],
    ["A-", 3.75],
    ["B+", 3.50],
    ["B", 3.00],
    ["B-", 2.75],
    ["C+", 2.50],
    ["C", 2.00],
    ["D", 1.00],
    ["E", 0.00]
]

n = int(input("Masukkan jumlah mahasiswa: "))

mahasiswa = []
for i in range(n):
    nama = input(f"Masukkan nama mahasiswa ke-{i+1}: ")
    nilai = input(f"Masukkan indeks nilai untuk {nama} (A, A-, B+, B, B-, C+, C, D, E): ").upper()

    ip = 0.00  
    valid = False  
    for indeks in nilai_indeks:
        if nilai == indeks[0]:
            ip = indeks[1]
            valid = True
            break

    if valid:  
        mahasiswa.append([nama, nilai, ip])
    else:
        print("Indeks nilai tidak valid")
        i -= 1 

for i in range(len(mahasiswa)):
    for j in range(len(mahasiswa) - 1 - i):
        if mahasiswa[j][2] < mahasiswa[j + 1][2]: 
            mahasiswa[j], mahasiswa[j + 1] = mahasiswa[j + 1], mahasiswa[j]


print("\nTabel Nilai dan IP Mahasiswa:")
print(f"{'No':<5} {'Nama Mahasiswa':<20} {'Indeks Nilai':<10} {'IP':<15}")

for i in range(len(mahasiswa)):
    nama = mahasiswa[i][0]
    indeks_nilai = mahasiswa[i][1]
    ip = mahasiswa[i][2]
    
    print(f"{i + 1:<5} {nama:<20} {indeks_nilai:<10} {ip:<15.2f}")

