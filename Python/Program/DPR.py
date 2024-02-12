class DPR:  # Mendefinisikan kelas DPR untuk mewakili anggota Dewan Perwakilan Rakyat.
    def __init__(self, id="", nama="", bidang="", partai=""):  # Konstruktor kelas dengan parameter opsional.
        self.id = id  # Menetapkan id anggota DPR.
        self.nama = nama  # Menetapkan nama anggota DPR.
        self.bidang = bidang  # Menetapkan bidang keahlian anggota DPR.
        self.partai = partai  # Menetapkan partai politik anggota DPR.

    # Metode untuk mengambil nilai id.
    def get_id(self):
        return self.id

    # Metode untuk menetapkan nilai id.
    def set_id(self, id):
        self.id = id

    # Metode untuk mengambil nilai nama.
    def get_nama(self):
        return self.nama

    # Metode untuk menetapkan nilai nama.
    def set_nama(self, nama):
        self.nama = nama

    # Metode untuk mengambil nilai bidang.
    def get_bidang(self):
        return self.bidang

    # Metode untuk menetapkan nilai bidang.
    def set_bidang(self, bidang):
        self.bidang = bidang

    # Metode untuk mengambil nilai partai.
    def get_partai(self):
        return self.partai

    # Metode untuk menetapkan nilai partai.
    def set_partai(self, partai):
        self.partai = partai

    # Metode untuk menampilkan informasi tentang anggota DPR.
    def display_info(self):
        print("ID:", self.id)
        print("Nama:", self.nama)
        print("Bidang:", self.bidang)
        print("Partai:", self.partai)
