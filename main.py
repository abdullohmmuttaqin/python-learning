# ===== Program Cek Dewasa =====

nama = input("Masukan nama anda: ")
umur = int(input("Masukan umur anda: "))

if umur >= 18:
    status = "Dewasa"
else:
    status = "Belum Dewasa"

print("Nama:", nama)
print("Status:", status)



# ===== Program Cek Kelulusan =====
# Logika nya begini : 
# 1. Program meminta input nilai mahasiswa
# 2. Program membandingkan nilai tersebut
# 3. Jika nilai >75, maka status "Lulus"
# 4. Jika nilai <75, maka status "Tidak Lulus"
# 5. Program menampilkan status kelulusan

nama_mahasiswa = input("Masukan nama mahasiswa: ")
nilai_mahasiswa = int(input("Masukan nilai mahasiswa: "))

if nilai_mahasiswa < 0 or nilai_mahasiswa > 100:
    status = "Nilai tidak valid"
elif nilai_mahasiswa >= 75:
    status = "Lulus"
else:
    status = "Belum lulus"

print("Nama mahasiswa:", nama_mahasiswa)
print("Status:", status)



#===== Program cek angka positif / negatif =====
#1. Program meminta input angka 
#2. Program membandingkan angka tersebut
#3. Jika angka >0, maka status "Positif"
#4. Jika angka <0, maka status "Negatif"
#5. Jika angka = 0, maka status "Angka nol"
#6. Program menampilkan status angka

angka = int(input("Silahkan masukan angka: "))

if angka > 0:
    status = "Angka positif"
elif angka < 0:
    status = "Angka negatif"
else: 
    status = "Angka nol"

print("Angka: ", angka)
print("Status:", status)
