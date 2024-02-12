from DPR import DPR  # Mengimpor kelas DPR dari file DPR.py.

def tambah_anggota_dpr(anggota_dpr):  # Mendefinisikan fungsi untuk menambahkan anggota DPR ke dalam daftar.
    print("\nMasukkan data anggota DPR:")  # Mencetak pesan instruksi untuk memasukkan data anggota DPR.
    id = input("Masukkan ID: ")  # Meminta input ID dari pengguna.
    nama = input("Masukkan Nama: ")  # Meminta input Nama dari pengguna.
    bidang = input("Masukkan Bidang: ")  # Meminta input Bidang dari pengguna.
    partai = input("Masukkan Partai: ")  # Meminta input Partai dari pengguna.

    anggota_dpr.append(DPR(id, nama, bidang, partai))  # Membuat objek DPR baru dengan data yang dimasukkan, dan menambahkannya ke dalam daftar.
    print("Anggota DPR berhasil ditambahkan!")  # Mencetak pesan konfirmasi bahwa anggota DPR telah berhasil ditambahkan.

def ubah_anggota_dpr(anggota_dpr):  # Mendefinisikan fungsi untuk mengubah data anggota DPR.
    id = input("\nMasukkan ID anggota DPR yang akan diubah: ")  # Meminta input ID anggota DPR yang akan diubah dari pengguna.
    found = False  # Variabel untuk menandai apakah ID anggota DPR ditemukan atau tidak.

    for anggota in anggota_dpr:  # Melakukan iterasi melalui setiap anggota DPR dalam daftar.
        if anggota.get_id() == id:  # Memeriksa apakah ID anggota DPR saat ini sama dengan ID yang dimasukkan pengguna.
            print("\nMasukkan data baru:")  # Mencetak pesan instruksi untuk memasukkan data baru.
            nama = input("Masukkan Nama Baru: ")  # Meminta input Nama Baru dari pengguna.
            bidang = input("Masukkan Bidang Baru: ")  # Meminta input Bidang Baru dari pengguna.
            partai = input("Masukkan Partai Baru: ")  # Meminta input Partai Baru dari pengguna.

            anggota.set_nama(nama)  # Mengubah nama anggota DPR dengan nilai yang baru.
            anggota.set_bidang(bidang)  # Mengubah bidang anggota DPR dengan nilai yang baru.
            anggota.set_partai(partai)  # Mengubah partai anggota DPR dengan nilai yang baru.
            print("Data anggota DPR berhasil diubah!")  # Mencetak pesan konfirmasi bahwa data anggota DPR telah berhasil diubah.
            found = True  # Menandai bahwa ID anggota DPR telah ditemukan.
            break  # Keluar dari loop setelah menemukan ID anggota DPR yang sesuai.

    if not found:  # Jika ID anggota DPR tidak ditemukan.
        print("ID anggota DPR tidak ditemukan.")  # Mencetak pesan bahwa ID anggota DPR tidak ditemukan.

def hapus_anggota_dpr(anggota_dpr):  # Mendefinisikan fungsi untuk menghapus anggota DPR dari daftar.
    id = input("\nMasukkan ID anggota DPR yang ingin dihapus: ")  # Meminta input ID anggota DPR yang ingin dihapus dari pengguna.
    found = False  # Variabel untuk menandai apakah ID anggota DPR ditemukan atau tidak.

    for anggota in anggota_dpr:  # Melakukan iterasi melalui setiap anggota DPR dalam daftar.
        if anggota.get_id() == id:  # Memeriksa apakah ID anggota DPR saat ini sama dengan ID yang dimasukkan pengguna.
            anggota_dpr.remove(anggota)  # Menghapus anggota DPR dari daftar.
            print("Anggota DPR berhasil dihapus!")  # Mencetak pesan konfirmasi bahwa anggota DPR telah berhasil dihapus.
            found = True  # Menandai bahwa ID anggota DPR telah ditemukan.
            break  # Keluar dari loop setelah menemukan ID anggota DPR yang sesuai.

    if not found:  # Jika ID anggota DPR tidak ditemukan.
        print("ID anggota DPR tidak ditemukan.")  # Mencetak pesan bahwa ID anggota DPR tidak ditemukan.

def tampilkan_anggota_dpr(anggota_dpr):  # Mendefinisikan fungsi untuk menampilkan daftar anggota DPR.
    if not anggota_dpr:  # Jika daftar anggota DPR kosong.
        print("Belum ada anggota DPR yang terdaftar.")  # Mencetak pesan bahwa belum ada anggota DPR yang terdaftar.
    else:  # Jika daftar anggota DPR tidak kosong.
        # Menghitung panjang maksimum untuk kolom ID, Nama, Bidang, dan Partai untuk tata letak yang rapi.
        id_max_length = max(2, max(len(anggota.get_id()) for anggota in anggota_dpr))
        nama_max_length = max(4, max(len(anggota.get_nama()) for anggota in anggota_dpr))
        bidang_max_length = max(6, max(len(anggota.get_bidang()) for anggota in anggota_dpr))
        partai_max_length = max(6, max(len(anggota.get_partai()) for anggota in anggota_dpr))

        # Mencetak header tabel.
        print("+-{}-+-{}-+-{}-+-{}-+".format('-' * id_max_length, '-' * nama_max_length, '-' * bidang_max_length, '-' * partai_max_length))
        print("| {:<{}} | {:<{}} | {:<{}} | {:<{}} |".format("ID", id_max_length, "Nama", nama_max_length, "Bidang", bidang_max_length, "Partai", partai_max_length))
        print("+-{}-+-{}-+-{}-+-{}-+".format('-' * id_max_length, '-' * nama_max_length, '-' * bidang_max_length, '-' * partai_max_length))

        # Mencetak baris untuk setiap anggota DPR dalam daftar.
        for anggota in anggota_dpr:
            print("| {:<{}} | {:<{}} | {:<{}} | {:<{}} |".format(anggota.get_id(), id_max_length, anggota.get_nama(), nama_max_length, anggota.get_bidang(), bidang_max_length, anggota.get_partai(), partai_max_length))

        # Mencetak garis pembatas.
        print("+-{}-+-{}-+-{}-+-{}-+".format('-' * id_max_length, '-' * nama_max_length, '-' * bidang_max_length, '-' * partai_max_length))

def main():  # Mendefinisikan fungsi utama.
    anggota_dpr = []  # Membuat daftar kosong untuk menyimpan anggota DPR.

    while True:  # Melakukan loop tak terbatas untuk menampilkan menu dan memproses pilihan pengguna.
        print("\nMenu:")  # Mencetak menu pilihan.
        print("1. Tambah Anggota DPR")
        print("2. Ubah Data Anggota DPR")
        print("3. Hapus Anggota DPR")
        print("4. Tampilkan Daftar Anggota DPR")
        print("5. Keluar")
        pilihan = int(input("Pilih Menu: "))  # Meminta input pilihan menu dari pengguna.

        if pilihan == 1:  # Jika pengguna memilih menu untuk menambah anggota DPR.
            tambah_anggota_dpr(anggota_dpr)  # Memanggil fungsi untuk menambah anggota DPR.
        elif pilihan == 2:  # Jika pengguna memilih menu untuk mengubah data anggota DPR.
            ubah_anggota_dpr(anggota_dpr)  # Memanggil fungsi untuk mengubah data anggota DPR.
        elif pilihan == 3:  # Jika pengguna memilih menu untuk menghapus anggota DPR.
            hapus_anggota_dpr(anggota_dpr)  # Memanggil fungsi untuk menghapus anggota DPR.
        elif pilihan == 4:  # Jika pengguna memilih menu untuk menampilkan daftar anggota DPR.
            tampilkan_anggota_dpr(anggota_dpr)  # Memanggil fungsi untuk menampilkan daftar anggota DPR.
        elif pilihan == 5:  # Jika pengguna memilih menu untuk keluar dari program.
            print("Program selesai.")  # Mencetak pesan bahwa program telah selesai.
            break  # Keluar dari loop utama dan mengakhiri program.
        else:  # Jika pilihan pengguna tidak valid.
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")  # Mencetak pesan bahwa pilihan tidak valid.

if __name__ == "__main__":  # Memastikan bahwa program dijalankan dari file ini langsung, bukan diimpor sebagai modul.
    main()  # Memanggil fungsi utama untuk menjalankan program.
