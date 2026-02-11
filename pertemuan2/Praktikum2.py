#===================================
# Praktikum 2       : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan Dasar 1   : Membuat fungsi load data
#===================================

nama_file = "data_mahasiswa.txt"
def baca_data_mahasiswa(nama_file):

    data_dict = {} # Buat variabel untuk dctionary
    with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
        for baris in file :
            baris = baris.strip()

            parts = baris.split(",")
            if len(parts) != 3:
                continue
            nim,nama,nilai_str = parts
            nilai_int = int(nilai_str)
            #Simpan data mahasiswa ke dictionary dengan key NIM
            data_dict[nim]={        #Key
                "nama": nama,       #Values
                "nilai":nilai_int #Values
            }
    return data_dict

# Memanggil fungsibaca data mahasiswa
buka_data = baca_data_mahasiswa(nama_file)
#print ("jumlah data terbaca", len(buka_data))


#===================================
# Praktikum 2       : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan Dasar 2   : Membuat menampilkan data
#===================================


def tampilkan_data(data_dict):
    
    #Erro Handling jika data nil
    if len(data_dict) == 0:
        print(" Data Kosong")
        return
    
    #Membuat Header Tabel
    print ("\n==== Daftar Mahasiswa ====")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':>5}")
    print("-" * 32) # Mencetak garis Header

    """
    Untuk Tampilam yang Rapi, atur f-string formatting
    {'NIM':<10} artinya:
    tampilkan nim <= rata kiri dengan lebar 10 karakter
    {'Nama':<12} artinya:
    tampilkan nama rata kiri, dengan lebar kolom 12 karakter
    {'Nilai':>5} artinya:
    tampilkan nilai rarta kanan, dengan lebar kolom 5 karakter
    """



    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]['nama']
        nilai= data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}")

#Memanggil fungsi menampilkan data
#tampilkan_data(buka_data)


#===================================
# Praktikum 2       : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan Dasar 3   : Membuat fungsi mencari data
#===================================

def cari_data(data_dict):
    # mencari data mahasiswa berdasarkan NIM
    nim_cari = input("Masukkan NIM yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n==== Data Mahasiswa Ditemukan ====")
        print (f'NIM     : {nim_cari}')
        print(f'Nama    : {nama}')
        print(f"Nilai   : {nilai}")
    else:
        print("\n==== Data Tidak Ditemukan")

#cari_data(buka_data)


#===================================
# Praktikum 2       : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan Dasar 4   : Membuat fungsi update nilai
#===================================

def update_nilai(data_dict):
    nim = input("Masukkan NIM mahasiswa yang akan diupdate nilainya: ").strip()

    # Error Handling
    if nim not in data_dict:
        print("NIM tidak ditemukan, Update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError: 
        print("Nilai harus berupa angka. Update dibatalkan")
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus diantara 0 - 100. Update Dibatalkan")
    
    nilai_lama = data_dict[nim]["nilai"]
    # Memasukkan nilai update baru ke dictionary
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil, Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#update_nilai(buka_data)


#===================================
# Praktikum 2       : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan Dasar 5   : Membuat fungsi menyimpan perubahan data ke file
#===================================

def simpan_data(nama_file,data_dict):
    with open(nama_file, "w",encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f'{nim},{nama},{nilai}\n')

#simpan_data(nama_file,buka_data)
#print ("Data Berhasil disimpan")

#===================================
# Praktikum 2       : Konsep ADT dan File Handling (STUDI KASUS)
# Latihan Dasar 6   : Membuat menu program
#===================================

def main():

    # Menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

while True:
    print("\n ==== Menu Data Mahasiswa ====")
    print("1. Tampilkan semua data")
    print("2. Cari data berdasarkan NIM")
    print("3. Update nilai mahasiswa")
    print("4. Simpan data ke file")
    print("0. Keluar")

    pilihan = input("Pilihan Menu: ").strip()
    
    if pilihan == "1":
        tampilkan_data(buka_data)

    elif pilihan == "2":
        cari_data(buka_data)

    elif pilihan == "3":
        update_nilai(buka_data)

    elif pilihan == "4":
        simpan_data(nama_file,buka_data)

    elif pilihan == "0":
        print("Program Selesai")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()