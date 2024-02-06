
#include <iostream>  // Library standar untuk input/output
#include <vector>    // Library untuk menggunakan vector (array dinamis)
#include <string>    // Library untuk menggunakan string

using namespace std;

// Kelas AnggotaDPR untuk merepresentasikan setiap anggota DPR
class AnggotaDPR {
private:
    string id;      // ID anggota DPR
    string nama;    // Nama anggota DPR
    string bidang;  // Bidang kerja anggota DPR
    string partai;  // Partai politik anggota DPR

public:
    // Konstruktor untuk inisialisasi data anggota DPR
    AnggotaDPR(string id, string nama, string bidang, string partai)
        : id(id), nama(nama), bidang(bidang), partai(partai) {}

    // Metode getter untuk mengambil nilai dari masing-masing atribut
    string getId() const { return id; }
    string getNama() const { return nama; }
    string getBidang() const { return bidang; }
    string getPartai() const { return partai; }

    // Metode setter untuk mengubah nilai dari masing-masing atribut
    void setId(string newId) { id = newId; }
    void setNama(string newNama) { nama = newNama; }
    void setBidang(string newBidang) { bidang = newBidang; }
    void setPartai(string newPartai) { partai = newPartai; }

    /*Destructors.*/

    //default destructor. leave it blank for you.
    ~AnggotaDPR()
    {

    }
};



// Kelas DaftarAnggotaDPR untuk menyimpan daftar anggota DPR
class DaftarAnggotaDPR {
private:
    vector<AnggotaDPR> daftar;  // Vektor untuk menyimpan anggota DPR

public:
    DaftarAnggotaDPR() {}  // Konstruktor default

    // Metode untuk menambahkan anggota DPR ke dalam daftar
    void tambahAnggota(const AnggotaDPR& anggota) {
        daftar.push_back(anggota);
    }

    // Metode untuk menampilkan daftar anggota DPR
    void tampilkanDaftar() const {
        cout << "Daftar Anggota DPR:\n";
        for (const auto& anggota : daftar) {
            cout << "ID: " << anggota.getId() << " \n" << "Nama: " << anggota.getNama() << " \n" << "Bidang: " << anggota.getBidang() << " \n" << "Partai: " << anggota.getPartai() << " \n"<< endl;
        }
    }

    // Metode untuk mengubah data anggota DPR berdasarkan ID
    void ubahAnggota(string id, const AnggotaDPR& anggotaBaru) {
        for (auto& anggota : daftar) {
            if (anggota.getId() == id) {
                anggota = anggotaBaru;
                return;
            }
        }
        cout << "Anggota dengan ID " << id << " tidak ditemukan.\n";
    }

    // Metode untuk menghapus anggota DPR berdasarkan ID
    void hapusAnggota(string id) {
        for (auto it = daftar.begin(); it != daftar.end(); ++it) {
            if (it->getId() == id) {
                it = daftar.erase(it);
                cout << "Anggota dengan ID " << id << " telah dihapus.\n";
                return;
            }
        }
        cout << "Anggota dengan ID " << id << " tidak ditemukan.\n";
    }

    /*Destructors.*/

    //default destructor. leave it blank for you.
    ~DaftarAnggotaDPR()
    {

    }
};
