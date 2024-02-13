<img width="392" alt="TAMPILKAN" src="https://github.com/queenxhr/LP1DPBO2024C2/assets/135084798/900aaba4-07e9-435f-aab0-001e49f2cff8"># LP1DPBO2024C2

# Janji
Saya Ratu Syahirah Khairunnisa [2200978] 
mengerjakan Latihan Praktikum 1
dalam mata kuliah DPBO
untuk keberkahanNya maka saya tidak melakukan kecurangan 
seperti yang telah dispesifikasikan. 
Aamiin

# Bahasa yang dibahas Java

# Desain Program :
Desain program yang dirancang terdiri dari 2 file yaitu DPR.java dan Main.java.

1. DPR.java: Ini kelas untuk merepresentasikan anggota DPR. Setiap anggota DPR punya ID, nama, bidang, dan partai. Seperti kartu identitas buat anggota DPR, yang bisa kita lihat atau ubah datanya.

2. Main.java: Ini adalah bagian utama dari program. Di sini, dibuat program yang bisa dioperasikan oleh user. Ada menu-menu yang bisa dipilih untuk operasi-operasi yang ingin dilakukan, seperti tambah, ubah, atau hapus anggota DPR.
Ada juga metode bantu, seperti generateLine() untuk membuat garis dalam tabel dan getColumnMaxLength() untuk menentukan lebar kolom berdasarkan data yang ada. 

# Penjelasan Alur
Pada saat menjalankan program, cmd akan menampilkan menu pilihan query yang akan dipilih oleh user, yaitu 

1. Tambah Anggota DPR:
- Pengguna memilih menu "1" 
- Program meminta pengguna untuk memasukkan data anggota DPR baru, yaitu ID, nama, bidang, dan partai.
- Pengguna memasukkan data tersebut.
- Program membuat objek DPR baru dengan data yang dimasukkan.
- Objek DPR tersebut ditambahkan ke dalam ArrayList anggotaDPR.
- Program memberi pesan bahwa anggota DPR berhasil ditambahkan.

2. Ubah Data Anggota DPR:
- Pengguna memilih menu "2".
- Program meminta pengguna untuk memasukkan ID anggota DPR yang ingin diubah.
- Program mencari anggota DPR dengan ID yang dimasukkan.
- Jika anggota DPR dengan ID tersebut ditemukan, program meminta pengguna untuk memasukkan data baru: nama, bidang, dan partai.
- Data anggota DPR tersebut diubah sesuai dengan input pengguna.
- Program memberi pesan bahwa data anggota DPR berhasil diubah.

3. Hapus Anggota DPR:
- Pengguna memilih menu "3".
- Program meminta pengguna untuk memasukkan ID anggota DPR yang ingin dihapus.
- Program mencari anggota DPR dengan ID yang dimasukkan.
- Jika anggota DPR dengan ID tersebut ditemukan, anggota DPR tersebut dihapus dari ArrayList anggotaDPR.
- Program memberi pesan bahwa anggota DPR berhasil dihapus.

4. Tampilkan Daftar Anggota DPR:
- Pengguna memilih menu "4".
- Program menampilkan semua anggota DPR yang ada dalam format tabel.
- Program menghitung lebar kolom yang sesuai dengan data yang ada.
- Program menampilkan informasi anggota DPR berupa ID, nama, bidang, dan partai.
- 
5. Keluar:
- Pengguna memilih menu "5".
- Program keluar dari loop dan program berakhir.

Setelah setiap operasi, pengguna akan kembali ke menu utama untuk memilih operasi selanjutnya atau keluar dari program.

# Dokumentasi
1. Tambah Anggota DPR
   <img width="415" alt="TAMBAH" src="https://github.com/queenxhr/LP1DPBO2024C2/assets/135084798/2206e8f1-6565-4a5a-a09e-e29f6d1a2309">

2. Ubah Anggota DPR
   <img width="266" alt="UBAH" src="https://github.com/queenxhr/LP1DPBO2024C2/assets/135084798/2ac87303-57d4-4ead-beaa-83b6e9fbaff4">

3. Hapus Anggota DPR
   <img width="236" alt="HAPUS" src="https://github.com/queenxhr/LP1DPBO2024C2/assets/135084798/85d21d3a-f3ee-48e4-b6de-ff5ce9a4ca24">

4. Tampilkan Anggota DPR
   <img width="392" alt="TAMPILKAN" src="https://github.com/queenxhr/LP1DPBO2024C2/assets/135084798/4fbf8f07-c232-423b-a6d6-54834f57eebb">

5. Keluar
   <img width="332" alt="KELUAR" src="https://github.com/queenxhr/LP1DPBO2024C2/assets/135084798/c08f67d1-ce78-4544-babd-9bf640c11535">
