# Program Daftar Nilai Mahasiswa Menggunakan Dictionary

data = {}

def tambah():
    print("\n=== Tambah Data ===")
    nim = input("NIM        : ")
    nama = input("Nama       : ")
    tugas = int(input("Nilai Tugas: "))
    uts = int(input("Nilai UTS  : "))
    uas = int(input("Nilai UAS  : "))

    akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    data[nim] = {
        'nama': nama,
        'tugas': tugas,
        'uts': uts,
        'uas': uas,
        'akhir': akhir
    }

    print(">>> Data berhasil ditambahkan\n")


def tampil():
    print("\n=== Daftar Nilai Mahasiswa ===")
    if not data:
        print("Tidak ada data.\n")
        return

    print("===============================================================")
    print("| NIM      | Nama       | Tugas | UTS | UAS | Nilai Akhir |")
    print("===============================================================")

    for nim, mhs in data.items():
        print(f"| {nim:<8} | {mhs['nama']:<10} | {mhs['tugas']:<5} | "
              f"{mhs['uts']:<3} | {mhs['uas']:<3} | {mhs['akhir']:<11.2f} |")

    print("===============================================================\n")


def ubah():
    print("\n=== Ubah Data ===")
    nim = input("Masukkan NIM: ")

    if nim in data:
        nama = input("Nama baru (kosongkan jika tidak diubah): ") or data[nim]['nama']
        tugas = input("Nilai Tugas baru: ")
        uts = input("Nilai UTS baru  : ")
        uas = input("Nilai UAS baru  : ")

        tugas = int(tugas) if tugas else data[nim]['tugas']
        uts = int(uts) if uts else data[nim]['uts']
        uas = int(uas) if uas else data[nim]['uas']

        akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

        data[nim] = {
            'nama': nama,
            'tugas': tugas,
            'uts': uts,
            'uas': uas,
            'akhir': akhir
        }

        print(">>> Data berhasil diubah\n")
    else:
        print(">>> Data tidak ditemukan\n")


def hapus():
    print("\n=== Hapus Data ===")
    nim = input("Masukkan NIM: ")

    if nim in data:
        del data[nim]
        print(">>> Data berhasil dihapus\n")
    else:
        print(">>> Data tidak ditemukan\n")


def cari():
    print("\n=== Cari Data ===")
    nim = input("Masukkan NIM: ")

    if nim in data:
        m = data[nim]
        print("\nData ditemukan:")
        print(f"NIM   : {nim}")
        print(f"Nama  : {m['nama']}")
        print(f"Tugas : {m['tugas']}")
        print(f"UTS   : {m['uts']}")
        print(f"UAS   : {m['uas']}")
        print(f"Akhir : {m['akhir']:.2f}\n")
    else:
        print(">>> Data tidak ditemukan\n")


# Main Loop
while True:
    print("""
================ MENU ================
1. Tambah Data
2. Ubah Data
3. Hapus Data
4. Tampilkan Data
5. Cari Data
6. Keluar
======================================
""")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == '1':
        tambah()
    elif pilihan == '2':
        ubah()
    elif pilihan == '3':
        hapus()
    elif pilihan == '4':
        tampil()
    elif pilihan == '5':
        cari()
    elif pilihan == '6':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!\n")
