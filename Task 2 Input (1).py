totalhari = int(input("Masukkan Jumlah Hari Proyek: "))

tahun = totalhari // 365
sisahari = totalhari % 365

bulan = sisahari // 30
hari = sisahari % 30

print("KOnversi Durasi Proyek :", totalhari, "Hari Adalah", tahun, "Tahun", bulan, "Bulan", hari, "Hari")