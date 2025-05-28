def hitung_glbb(kecepatan_awal, percepatan, waktu):
    kecepatan_akhir = kecepatan_awal + (percepatan * waktu)
    jarak = (kecepatan_awal * waktu) + (0.5 * percepatan * waktu**2)
    return kecepatan_akhir, jarak

print("Program Menghitung GLBB")
print("=======================")
n = int(input("Masukkan jumlah data (n): "))
list_v0 = []  
list_a = []
list_t = []

for i in range(n):
    print(f"\nData ke-{i+1}")
    input_v0 = float(input("Kecepatan awal (m/s): "))
    input_a = float(input("Percepatan (m/s²): "))
    input_t = float(input("Waktu (s): "))
    
    list_v0.append(input_v0)
    list_a.append(input_a)
    list_t.append(input_t)

print("\nHasil Perhitungan GLBB")
print("=" * 80)
print(f"| {'No':<3} | {'Kecepatan Awal':<15} | {'Percepatan':<10} | {'Waktu':<6} | {'Kecepatan Akhir':<15} | {'Jarak':<10} |")
print("-" * 80)

for i in range(n):
    vt, s = hitung_glbb(list_v0[i], list_a[i], list_t[i])
    print(f"| {i+1:<3} | {list_v0[i]:<15,.2f} | {list_a[i]:<10,.2f} | {list_t[i]:<6,.2f} | {vt:<15,.2f} | {s:<10,.2f} |")

print("=" * 80)
