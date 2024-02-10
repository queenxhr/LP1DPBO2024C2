<?php

class AnggotaDPR {
    private $id;
    private $nama;
    private $bidang;
    private $partai;
    private $fotoProfil;

    public function getId() {
        return $this->id;
    }

    public function setId($id) {
        $this->id = $id;
    }

    public function getNama() {
        return $this->nama;
    }

    public function setNama($nama) {
        $this->nama = $nama;
    }

    public function getBidang() {
        return $this->bidang;
    }

    public function setBidang($bidang) {
        $this->bidang = $bidang;
    }

    public function getPartai() {
        return $this->partai;
    }

    public function setPartai($partai) {
        $this->partai = $partai;
    }

    public function getFotoProfil() {
        return $this->fotoProfil;
    }

    public function setFotoProfil($fotoProfil) {
        $this->fotoProfil = $fotoProfil;
    }

    public function __construct($id, $nama, $bidang, $partai, $fotoProfil) {
        $this->id = $id;
        $this->nama = $nama;
        $this->bidang = $bidang;
        $this->partai = $partai;
        $this->fotoProfil = $fotoProfil;
    }

    public static function headerInfo() {
        // Menampilkan tabel informasi anggota DPR
        
        echo "<tr>";
        echo "<th>ID</th>";
        echo "<th>Nama</th>";
        echo "<th>Bidang</th>";
        echo "<th>Partai</th>";
        echo "<th>Foto Profil</th>";
        echo "</tr>";
    }

    public function tampilkanInfo() {
        echo "<tr>";
        echo "<td>" . $this->getId() . "</td>";
        echo "<td>" . $this->getNama() . "</td>";
        echo "<td>" . $this->getBidang() . "</td>";
        echo "<td>" . $this->getPartai() . "</td>";
        echo "<td><img src='" . $this->getFotoProfil() . "' alt='Foto Profil' width='90' height='120'></td>";
        echo "</tr>";
    }
}

?>
