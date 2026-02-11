# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Muhammad Najmi Khoiri Almunawwar
# NIM : J0403251095
# Kelas :B2
# ==========================================================

nama_file = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_data_barang(nama_file):

    stok_dict = {} # Buat variabel untuk dictionary
    with open(nama_file,"r", encoding="utf-8") as file:
        for baris in file :
            baris = baris.strip()
            parts = baris.split(",")
            if len(parts) != 3:
                continue
            kode_barang,nama_barang,stok_str = parts
            stok_int = int(stok_str)
            # Simpan data barang ke dictionary dengan key Kode Barang
            stok_dict[kode_barang]={        #Key
                "nama_barang": nama_barang, #Values
                "stok":stok_int             #Values
            }
    return stok_dict

# ====================================
# Fungsi: Menyimpan data ke file
# ====================================
def simpan_stok(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode_barang in sorted(stok_dict.keys()):
            nama_barang = stok_dict[kode_barang]["nama_barang"]
            stok = stok_dict[kode_barang]["stok"]
            baris = f"{kode_barang},{nama_barang},{stok}\n"
            file.write(baris)

# ====================================
# Fungsi: Menampilkan data stok barang  
# ====================================

def tampilkan_semua(stok_dict):
    
    # Error Handling jika data kosong
    if len(stok_dict) == 0:
        print(" Data Kosong")
        return
    
    # Membuat Header Tabel
    print ("\n==== Daftar Stok Barang Kantin ====")
    print(f"{'Kode Barang':<15} | {'Nama Barang':<20} | {'Stok':>5}")
    print("-" * 50) # Mencetak garis Header

    for kode_barang in sorted(stok_dict.keys()):
        nama_barang = stok_dict[kode_barang]["nama_barang"]
        stok = stok_dict[kode_barang]["stok"]
        print(f"{kode_barang:<15} | {nama_barang:<20} | {stok:>5}")


# ====================================
# Fungsi cari data barang berdasarkan kode
# ====================================

def cari_barang(stok_dict):
    kode_cari = input("Masukkan Kode Barang yang dicari: ")
    if kode_cari in stok_dict:
        nama_barang = stok_dict[kode_cari]["nama_barang"]
        stok = stok_dict[kode_cari]["stok"]
        print(f"Barang ditemukan: {kode_cari} - {nama_barang}, Stok: {stok}")
    else:
        print("Barang dengan kode tersebut tidak ditemukan.")

# ====================================
# Fungsi tambah barang baru
# ====================================
def tambah_barang(stok_dict):
    kode_baru = input("Masukkan Kode Barang baru: ").strip()
    if kode_baru in stok_dict:
        print("Kode Barang sudah ada. Gunakan kode lain.")
        return
    nama_baru = input("Masukkan Nama Barang: ").strip()
    stok_baru = int(input("Masukkan Stok Barang: ").strip())
    stok_dict[kode_baru] = {
        "nama_barang": nama_baru,
        "stok": stok_baru
    }
    print("Barang baru berhasil ditambahkan.")

# ====================================
# Fungsi update stok barang
# ====================================
def update_stok(stok_dict):
    print("Pilih opsi update stok:")
    print("1. Tambah Stok")
    print("2. Kurangi Stok")    

    pilihan = input("Masukkan pilihan (1/2): ").strip()
    if pilihan not in ['1', '2']:
        print("Pilihan tidak valid. Update dibatalkan.")
        return
    
    kode_barang = input("Masukkan Kode Barang yang akan diupdate: ").strip()
    if kode_barang not in stok_dict:
        print("Kode Barang tidak ditemukan. Update dibatalkan.")
        return
    try:
        jumlah = int(input("Masukkan jumlah stok yang akan diupdate: ").strip())
    except ValueError:
        print("Jumlah harus berupa angka. Update dibatalkan.")
        return
    if pilihan == '1':
        stok_dict[kode_barang]["stok"] += jumlah
        print("Stok berhasil ditambah.")
    elif pilihan == '2':
        if jumlah > stok_dict[kode_barang]["stok"]:
            print("Stok tidak cukup. Update dibatalkan.")
            return
        stok_dict[kode_barang]["stok"] -= jumlah
        print("Stok berhasil dikurangi.")

#===================================
# Program Utama
#===================================

def main():
    stok_dict = baca_data_barang(nama_file)
    while True:
        print("\n=== Menu Stok Barang Kantin ===")
        print("1. Tampilkan Semua Stok Barang")
        print("2. Cari Barang")
        print("3. Tambah Barang Baru")
        print("4. Update Stok Barang")
        print("5. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan menu: ").strip()
        if pilihan == '1':
            tampilkan_semua(stok_dict)
        elif pilihan == '2':
            cari_barang(stok_dict)
        elif pilihan == '3':
            tambah_barang(stok_dict)
        elif pilihan == '4':
            update_stok(stok_dict)
        elif pilihan == '5':
            simpan_stok(nama_file, stok_dict)
            print("Data berhasil disimpan ke file.")
        elif pilihan == '0':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()