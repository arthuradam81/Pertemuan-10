# Tugas-Pertemuan_10

# Arthur-Adam-Radhitya
# 312510233

# Flowchart

                     ┌─────────────────────────┐
                     │        MULAI            │
                     └───────────────┬─────────┘
                                     │
                                     ▼
                         ┌─────────────────────────┐
                         │ Inisialisasi data = {}  │
                         └───────────────┬─────────┘
                                         │
                                         ▼
                         ┌────────────────────────────────┐
                         │      Tampilkan Menu:           │
                         │ 1. Tambah Data                 │
                         │ 2. Ubah Data                   │
                         │ 3. Hapus Data                  │
                         │ 4. Tampilkan Data              │
                         │ 5. Cari Data                   │
                         │ 0. Keluar                      │
                         └───────────────┬────────────────┘
                                         │
                                         ▼
                         ┌───────────────────────────┐
                         │    Input pilihan menu     │
                         └───────────────┬───────────┘
                                         │
     ┌───────────────────────────────────┼─────────────────────────────────────┐
     │                                   │                                     │
     ▼                                   ▼                                     ▼
 ┌──────────────┐                ┌────────────────┐                     ┌──────────────────┐
 │ Pilihan = 1? │─Yes──────────▶ │  TAMBAH DATA   │                     │ Pilihan = 2?     │
 └───────┬──────┘                └───┬────────────┘                     └───────┬──────────┘
         │                           │                                          │
         │                           ▼                                          ▼
         │                  ┌───────────────────┐                     ┌───────────────────┐
         │                  │ Input NIM         │                     │     UBAH DATA     │
         │                  │ Input Nama        │                     └───────┬───────────┘
         │                  │ Input Tugas       │                             │
         │                  │ Input UTS         │                             ▼
         │                  │ Input UAS         │                 ┌────────────────────────┐
         │                  │ Hitung NilaiAkhir │                 │ Input NIM              │
         │                  │ Simpan ke dict    │                 │ Jika ketemu → ubah     │
         │                  └───────────────────┘                 │ Jika tidak → error     │
         │                            │                           └────────────────────────┘
         │                            ▼                                     │
         │                  ┌────────────────┐                              │
         │                  │ Kembali ke menu│◀─────────────────────────────┘
         │                  └────────────────┘
         │
         │
         ▼
┌──────────────┐
│ Pilihan = 3? │─────────Yes───────────────▶ HAPUS DATA
└───────┬──────┘                              │
        │                                     ▼
        │                          ┌────────────────────────┐
        │                          │ Input NIM              │
        │                          │ Jika ketemu → hapus    │
        │                          │ Jika tidak → error     │
        │                          └────────────────────────┘
        │                                      │
        │                                      ▼
        │                               Kembali ke menu
        │
        ▼
┌──────────────┐
│ Pilihan = 4? │─────────Yes──────────────▶ TAMPILKAN DATA
└───────┬──────┘                             │
        │                                    ▼
        │                        ┌──────────────────────────┐
        │                        │ Cetak seluruh isi dict   │
        │                        │ Jika kosong → tampilkan  │
        │                        │ pesan "tidak ada data"   │
        │                        └──────────────────────────┘
        │                                     │
        │                                     ▼
        │                             Kembali ke menu
        │
        ▼
┌──────────────┐
│ Pilihan = 5? │─────────Yes──────────────▶ CARI DATA
└───────┬──────┘                             │
        │                                    ▼
        │                        ┌──────────────────────────┐
        │                        │ Input NIM                │
        │                        │ Jika ketemu → tampilkan  │
        │                        │ Jika tidak → error       │
        │                        └──────────────────────────┘
        │                                     │
        │                                     ▼
        │                             Kembali ke menu
        │
        ▼
┌──────────────┐
│ Pilihan = 0? │─────────Yes──────────────▶ SELESAI
└───────┬──────┘
        │
        ▼
┌──────────────────────────┐
│   Tampilkan "Salah!"     │
│   Kembali ke menu        │
└──────────────────────────┘


# Penjelasan

1.  Mulai Program
Program dimulai dan melakukan inisialisasi dictionary kosong:
data = {}
Dictionary ini akan menyimpan semua data mahasiswa dengan format:
data[nim] = {
    "nama": "...",
    "tugas": ...,
    "uts": ...,
    "uas": ...,
    "akhir": ...
}

2. Tampilkan Menu
Program akan menampilkan pilihan:
Tambah Data
Ubah Data
Hapus Data
Tampilkan Data
Cari Data
Keluar
Pengguna harus memilih salah satu nomor.

3. Input Pilihan Menu
User memasukkan angka menu.
Program kemudian mengecek pilihan tersebut:

4. Jika Pilihan = 1 → Tambah Data
Pada menu ini program:
Meminta input:
NIM
Nama
Nilai Tugas
Nilai UTS
Nilai UAS
Menghitung nilai akhir:
akhir = tugas*0.30 + uts*0.35 + uas*0.35
Menyimpan data ke dalam dictionary.
Setelah selesai → kembali ke menu.

5. Jika Pilihan = 2 → Ubah Data
Pada menu ini:
User memasukkan NIM
Program mengecek apakah NIM ada dalam dictionary
Jika ADA → user diminta memasukkan data baru (nama, tugas, uts, uas)
Nilai akhir dihitung ulang
Data diperbarui
Tampilkan pesan sukses
Kembali ke menu
Jika TIDAK ADA → tampilkan pesan error
“Data tidak ditemukan”

6. Jika Pilihan = 3 → Hapus Data
Alurnya:
User memasukkan NIM
Program mencari NIM di dictionary
Jika ADA → data dihapus
Jika TIDAK ADA → tampilkan pesan error

7. Jika Pilihan = 4 → Tampilkan Semua Data
Program akan:
Mengecek apakah dictionary kosong
Jika kosong → tampilkan pesan: “Tidak ada data!”
Jika ada → tampilkan seluruh daftar mahasiswa
Lalu kembali ke menu.

8. Jika Pilihan = 5 → Cari Data
Alur:
User memasukkan NIM
Program mencari NIM tersebut
Jika ADA → tampilkan detail mahasiswa
Jika TIDAK ADA → tampilkan pesan error
Kembali ke menu.

9. Jika Pilihan = 0 → Keluar Program
Program berhenti dan menampilkan pesan:
Program selesai.

10. Jika Input Tidak Valid
Jika user memasukkan angka selain 0–5:
Tampilkan pesan “Menu tidak valid!”
Kembali ke menu utama
