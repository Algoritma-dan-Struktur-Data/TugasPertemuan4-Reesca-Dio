Total_detik = int(input("Masukkan Total Detik: "))

Hari = Total_detik // 86400
Sisa_hari = Total_detik % 86400

jam = Sisa_hari // 3600
Sisa_jam = Sisa_hari % 3600

Menit = Sisa_jam // 60
Detik = Sisa_jam % 60

print("Hasil Konversi", Total_detik, "Detik adalah", Hari, "Hari", jam, "Jam", Menit, "Menit", Detik, "Detik")
