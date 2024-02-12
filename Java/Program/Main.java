import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<DPR> anggotaDPR = new ArrayList<>();

        // Program loop
        while (true) {
            System.out.println("\nMenu:");
            System.out.println("1. Tambah Anggota DPR");
            System.out.println("2. Ubah Data Anggota DPR");
            System.out.println("3. Hapus Anggota DPR");
            System.out.println("4. Tampilkan Daftar Anggota DPR");
            System.out.println("5. Keluar");
            System.out.print("Pilih Menu: ");
            int pilihan = scanner.nextInt();
            scanner.nextLine(); // Membuang karakter newline dari buffer

            switch (pilihan) {
                case 1:
                    tambahAnggotaDPR(scanner, anggotaDPR);
                    break;
                case 2:
                    ubahAnggotaDPR(scanner, anggotaDPR);
                    break;
                case 3:
                    hapusAnggotaDPR(scanner, anggotaDPR);
                    break;
                case 4:
                    tampilkanAnggotaDPR(anggotaDPR);
                    break;
                case 5:
                    System.out.println("Program selesai.");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Pilihan tidak valid. Silahkan pilih menu yang benar.");
            }
        }
    }

    // Method untuk menambahkan anggota DPR
    public static void tambahAnggotaDPR(Scanner scanner, ArrayList<DPR> anggotaDPR) {
        System.out.println("\nMasukkan data anggota DPR:");
        System.out.print("Masukkan ID: ");
        String id = scanner.nextLine();
        System.out.print("Masukkan Nama: ");
        String nama = scanner.nextLine();
        System.out.print("Masukkan Bidang: ");
        String bidang = scanner.nextLine();
        System.out.print("Masukkan Partai: ");
        String partai = scanner.nextLine();

        anggotaDPR.add(new DPR(id, nama, bidang, partai));
        System.out.println("Anggota DPR berhasil ditambahkan!");
    }

    // Method untuk mengubah data anggota DPR
    public static void ubahAnggotaDPR(Scanner scanner, ArrayList<DPR> anggotaDPR) {
        System.out.print("\nMasukkan ID anggota DPR yang akan diubah: ");
        String id = scanner.nextLine();
        boolean found = false;

        for (DPR anggota : anggotaDPR) {
            if (anggota.getId().equals(id)) {
                System.out.println("\nMasukkan data baru:");
                System.out.print("Masukkan Nama Baru: ");
                String nama = scanner.nextLine();
                System.out.print("Masukkan Bidang Baru: ");
                String bidang = scanner.nextLine();
                System.out.print("Masukkan Partai Baru: ");
                String partai = scanner.nextLine();

                anggota.setnama(nama);
                anggota.setbidang(bidang);
                anggota.setpartai(partai);
                System.out.println("Data anggota DPR berhasil diubah!");
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("ID anggota DPR tidak ditemukan.");
        }
    }

    // Method untuk menghapus anggota DPR
    public static void hapusAnggotaDPR(Scanner scanner, ArrayList<DPR> anggotaDPR) {
        System.out.print("\nMasukkan ID anggota DPR yang ingin dihapus: ");
        String id = scanner.nextLine();
        boolean found = false;

        for (DPR anggota : anggotaDPR) {
            if (anggota.getId().equals(id)) {
                anggotaDPR.remove(anggota);
                System.out.println("Anggota DPR berhasil dihapus!");
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("ID anggota DPR tidak ditemukan.");
        }
    }

    // Method untuk menampilkan semua anggota DPR dalam bentuk tabel dengan spasi dinamis
    public static void tampilkanAnggotaDPR(ArrayList<DPR> anggotaDPR) {
        if (anggotaDPR.isEmpty()) {
            System.out.println("Belum ada anggota DPR yang terdaftar.");
        } else {
            // Menentukan panjang maksimum untuk setiap kolom
            int idMaxLength = Math.max(2, getColumnMaxLength(anggotaDPR, "ID"));
            int namaMaxLength = Math.max(4, getColumnMaxLength(anggotaDPR, "Nama"));
            int bidangMaxLength = Math.max(6, getColumnMaxLength(anggotaDPR, "Bidang"));
            int partaiMaxLength = Math.max(6, getColumnMaxLength(anggotaDPR, "Partai"));

            // Menampilkan header tabel
            System.out.println("+-" + generateLine('-', idMaxLength) + "-+-" + generateLine('-', namaMaxLength) + "-+-" +
                    generateLine('-', bidangMaxLength) + "-+-" + generateLine('-', partaiMaxLength) + "-+");

            System.out.printf("| %-" + idMaxLength + "s | %-" + namaMaxLength + "s | %-" + bidangMaxLength +
                    "s | %-" + partaiMaxLength + "s |%n", "ID", "Nama", "Bidang", "Partai");

            // Menampilkan baris pemisah antara header dan data
            System.out.println("+-" + generateLine('-', idMaxLength) + "-+-" + generateLine('-', namaMaxLength) + "-+-" +
                    generateLine('-', bidangMaxLength) + "-+-" + generateLine('-', partaiMaxLength) + "-+");

            // Menampilkan data anggota DPR
            for (DPR anggota : anggotaDPR) {
                System.out.printf("| %-" + idMaxLength + "s | %-" + namaMaxLength + "s | %-" + bidangMaxLength +
                        "s | %-" + partaiMaxLength + "s |%n", anggota.getId(), anggota.getnama(), anggota.getbidang(), anggota.getpartai());
            }

            // Menampilkan baris penutup tabel
            System.out.println("+-" + generateLine('-', idMaxLength) + "-+-" + generateLine('-', namaMaxLength) + "-+-" +
                    generateLine('-', bidangMaxLength) + "-+-" + generateLine('-', partaiMaxLength) + "-+");
        }
    }

    // Method untuk menghasilkan string berisi karakter yang diulang sebanyak n kali
    public static String generateLine(char c, int length) {
        return String.format("%-" + length + "s", "").replace(' ', c);
    }

    // Method untuk mendapatkan panjang maksimum dari suatu kolom dalam daftar anggota DPR
    public static int getColumnMaxLength(ArrayList<DPR> anggotaDPR, String columnName) {
        int maxLength = columnName.length();
        for (DPR anggota : anggotaDPR) {
            switch (columnName) {
                case "ID":
                    maxLength = Math.max(maxLength, anggota.getId().length());
                    break;
                case "Nama":
                    maxLength = Math.max(maxLength, anggota.getnama().length());
                    break;
                case "Bidang":
                    maxLength = Math.max(maxLength, anggota.getbidang().length());
                    break;
                case "Partai":
                    maxLength = Math.max(maxLength, anggota.getpartai().length());
                    break;
            }
        }
        return maxLength;
    }
}
