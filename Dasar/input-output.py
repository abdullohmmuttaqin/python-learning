# nama_mahasiswa = input("Masukan nama mahasiswa: ")
# umur = input(input("Masukan umur mahasiswa: "))

# if umur <= 2026:
#     status = "Umur anda adalah: "
# else: status >= 2026
#     status = "Umur anda adalah"

# print("Nama mahasiwa: ", nama_mahasiswa)
# print("Umur anda adalah: ", umur)

nama_mahasiswa = input("Masukan nama mahasiswa: ")
tahun_lahir = int(input("Masukan tahun lahir mahasiswa: "))

umur = 2026 - tahun_lahir

print("Nama mahasiswa:", nama_mahasiswa)
print("Umur:", umur, "tahun")
