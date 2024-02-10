<?php
require ('DPR.php');
// Membuat objek anggota DPR

$anggota1 = new AnggotaDPR("A1", "Ratu", "Pendidikan", "PKS", "picture/ratu.jpg");
$anggota2 = new AnggotaDPR("A2", "Talitha", "Kesehatan", "NasDem", "picture/faya.jpg");
$anggota3 = new AnggotaDPR("A3", "Tia", "Kesenian", "PKB", "picture/tia.jpg");
$anggota4 = new AnggotaDPR("A4", "Rifanny", "Ekonomi", "P3", "picture/lysa.jpg");
$anggota5 = new AnggotaDPR("A5", "Jasmine", "Agama", "PDIP", "picture/mine.jpg");

echo "<h2>Daftar Anggota DPR</h2>";
echo "<link rel='stylesheet' type='text/css' href='style.css'>";
echo "<table border='1'>";
AnggotaDPR::headerInfo();
$anggota1->tampilkanInfo();
$anggota2->tampilkanInfo();
$anggota3->tampilkanInfo();
$anggota4->tampilkanInfo();
$anggota5->tampilkanInfo();
echo "</table>";

$update1 = new AnggotaDPR("A1", "Ratu", "Hukum", "PKS", "picture/ratu.jpg");
$anggota2 = new AnggotaDPR("A2", "Talitha", "Kesehatan", "NasDem", "picture/faya.jpg");
$anggota3 = new AnggotaDPR("A3", "Tia", "Kesenian", "PKB", "picture/tia.jpg");
$anggota4 = new AnggotaDPR("A4", "Rifanny", "Ekonomi", "P3", "picture/lysa.jpg");
$anggota5 = new AnggotaDPR("A5", "Jasmine", "Agama", "PDIP", "picture/mine.jpg");

echo "<br>";
echo "Data Anggota DPR dengan ID A1 berhasil diubah!";
echo "<h2>Daftar Anggota DPR</h2>";
echo "<link rel='stylesheet' type='text/css' href='style.css'>";
echo "<table border='1'>";
AnggotaDPR::headerInfo();
$update1->tampilkanInfo();
$anggota2->tampilkanInfo();
$anggota3->tampilkanInfo();
$anggota4->tampilkanInfo();
$anggota5->tampilkanInfo();
echo "</table>";

$update1 = new AnggotaDPR("A1", "Ratu", "Hukum", "PKS", "picture/ratu.jpg");
$anggota2 = new AnggotaDPR("A2", "Talitha", "Kesehatan", "NasDem", "picture/faya.jpg");
$anggota4 = new AnggotaDPR("A4", "Rifanny", "Ekonomi", "P3", "picture/lysa.jpg");
$anggota5 = new AnggotaDPR("A5", "Jasmine", "Agama", "PDIP", "picture/mine.jpg");

echo "<br>";
echo "Data Anggota DPR dengan ID A3 berhasil dihapus!";
echo "<h2>Daftar Anggota DPR</h2>";
echo "<link rel='stylesheet' type='text/css' href='style.css'>";
echo "<table border='1'>";
AnggotaDPR::headerInfo();
$update1->tampilkanInfo();
$anggota2->tampilkanInfo();
$anggota4->tampilkanInfo();
$anggota5->tampilkanInfo();
echo "</table>";
?>

