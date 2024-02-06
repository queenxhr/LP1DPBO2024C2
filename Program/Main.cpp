//Import library and file.
#include <bits/stdc++.h>  // Importing all standard libraries
#include "DPR.cpp"        // Including the implementation file for AnggotaDPR and DaftarAnggotaDPR classes

using namespace std;

int main() {
    DaftarAnggotaDPR daftarDPR;  // Membuat objek DaftarAnggotaDPR untuk menyimpan daftar anggota DPR

    int pilihan;  // Variabel untuk menyimpan pilihan menu pengguna
    do {
        // Menampilkan menu pilihan
        cout << "Pilih menu:\n";
        cout << "1. Tampilkan daftar anggota DPR\n";
        cout << "2. Tambah anggota DPR\n";
        cout << "3. Ubah anggota DPR\n";
        cout << "4. Hapus anggota DPR\n";
        cout << "5. Keluar\n";
        cout << "Pilihan Anda: ";
        cin >> pilihan;  // Meminta pengguna untuk memilih menu

        // Menjalankan operasi sesuai pilihan pengguna
        switch (pilihan) {
            case 1:
                daftarDPR.tampilkanDaftar();  // Menampilkan daftar anggota DPR
                break;
            case 2: {
                string id, nama, bidang, partai;
                // Meminta pengguna untuk memasukkan data anggota DPR baru
                cout << "Masukkan data anggota DPR\n";
                cout << "Inputkan ID Anggota Baru: ";
                cin >> id ;
                cout << "Inputkan Nama Anggota Baru: ";
                cin >> nama ;
                cout << "Inputkan Bidang Anggota Baru: ";
                cin >> bidang ;
                cout << "Inputkan Partai Anggota Baru: ";
                cin >> partai ;
                // Menambahkan anggota DPR baru ke dalam daftar
                daftarDPR.tambahAnggota(AnggotaDPR(id, nama, bidang, partai));
                break;
            }
            case 3: {
                string id, nama, bidang, partai;
                // Meminta pengguna untuk memasukkan ID anggota DPR yang ingin diubah dan data baru
                cout << "Masukkan ID anggota DPR yang ingin diubah: ";
                cin >> id;
                cout << "Masukkan data baru anggota DPR (Nama, Bidang, Partai):\n";
                cout << "Inputkan Nama Anggota Baru: ";
                cin >> nama ;
                cout << "Inputkan Bidang Anggota Baru: ";
                cin >> bidang ;
                cout << "Inputkan Partai Anggota Baru: ";
                cin >> partai ;
                // Mengubah data anggota DPR berdasarkan ID
                daftarDPR.ubahAnggota(id, AnggotaDPR(id, nama, bidang, partai));
                break;
            }
            case 4: {
                string id;
                // Meminta pengguna untuk memasukkan ID anggota DPR yang ingin dihapus
                cout << "Masukkan ID anggota DPR yang ingin dihapus: ";
                cin >> id;
                // Menghapus anggota DPR berdasarkan ID
                daftarDPR.hapusAnggota(id);
                break;
            }
            case 5:
                cout << "Keluar dari program.\n";  // Menampilkan pesan keluar dari program
                break;
            default:
                cout << "Pilihan tidak valid.\n";  // Menampilkan pesan jika pilihan tidak valid
        }
    } while (pilihan != 5);  // Mengulangi loop hingga pengguna memilih keluar

    return 0;  // Mengembalikan nilai 0 untuk menunjukkan program berjalan dengan sukses
}
