# Bank Contoh Soal & Pembahasan: Pemrograman Berorientasi Objek

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Pemrograman Berorientasi Objek Departemen Informatika Universitas Diponegoro (Koleksi Pengampu Panji Wisnu Wirawan, S.T., M.T., Satriyo Adhy, S.Si., M.T., dkk. & Bank Soal HMIF 2017–2024).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (HIERARKI KELAS, ENKAPSULASI & RELASI OBJEK)

### Soal UTS 1: Perancangan Hierarki Kelas, Constructor Chaining & Static Counter (Soal Asli UTS Undip)
**Deskripsi Soal:**
Departemen Informatika ingin membuat sistem inventarisasi tas mahasiswa:
1. Buat kelas abstrak induk bernama `Tas` dengan atribut `warna_dasar` (String) dan `bahan` (String) dengan visibilitas `protected`. Sediakan konstruktor berparameter, getter, setter, dan metode abstrak `public abstract void cetakInfo()`.
2. Buat kelas turunan `BackPack` yang mewarisi `Tas`, menambahkan atribut `jumlah_kantong` (int, `private`), serta variabel statis `counter` (int, `private`) untuk mencatat total objek `BackPack` yang berhasil diinstansiasi.
3. Konstruktor `BackPack` wajib memanggil konstruktor induk via `super`, menginisialisasi atribut khusus, serta menaikkan nilai `counter`. Sediakan metode statis `public static int getCounterBackPack()`.
4. Buat kode Java lengkap dan demonstrasikan pemanggilan konstruktor bertingkat (*constructor chaining*)!

**Kunci Pembahasan & Solusi:**
```java
// 1. Superclass Abstrak Tas
abstract class Tas {
    protected String warnaDasar;
    protected String bahan;

    // Konstruktor Superclass
    public Tas(String warnaDasar, String bahan) {
        this.warnaDasar = warnaDasar;
        this.bahan = bahan;
    }

    public String getWarnaDasar() { return warnaDasar; }
    public void setWarnaDasar(String warnaDasar) { this.warnaDasar = warnaDasar; }

    public String getBahan() { return bahan; }
    public void setBahan(String bahan) { this.bahan = bahan; }

    // Metode Kontrak Polimorfik
    public abstract void cetakInfo();
}

// 2. Subclass Konkret BackPack
class BackPack extends Tas {
    private int jumlahKantong;
    private static int counter = 0; // Static member pelacak jumlah instansi

    // Konstruktor Subclass dengan Constructor Chaining
    public BackPack(String warnaDasar, String bahan, int jumlahKantong) {
        super(warnaDasar, bahan); // Wajib baris pertama memanggil konstruktor superclass
        this.jumlahKantong = jumlahKantong;
        BackPack.counter++;       // Inkrementasi counter statis kelas
    }

    public int getJumlahKantong() { return jumlahKantong; }
    public void setJumlahKantong(int jumlahKantong) { this.jumlahKantong = jumlahKantong; }

    public static int getCounterBackPack() {
        return BackPack.counter;
    }

    @Override
    public void cetakInfo() {
        System.out.println("[BackPack] Bahan: " + bahan + 
                           ", Warna: " + warnaDasar + 
                           ", Kantong: " + jumlahKantong);
    }
}

// 3. Kelas Eksekusi Utama
public class MainTas {
    public static void main(String[] args) {
        System.out.println("Counter awal: " + BackPack.getCounterBackPack()); // Output: 0

        BackPack b1 = new BackPack("Hitam", "Cordura", 4);
        BackPack b2 = new BackPack("Abu-abu", "Kanvas", 6);

        b1.cetakInfo();
        b2.cetakInfo();

        System.out.println("Total BackPack dibuat: " + BackPack.getCounterBackPack()); // Output: 2
    }
}
```

---

### Soal UTS 2: Implementasi Perbedaan Agregasi vs Komposisi dalam Java
**Deskripsi Soal:**
Jelaskan perbedaan struktural antara hubungan **Agregasi (*Weak Has-a*)** dan **Komposisi (*Strong Has-a*)** dalam kode Java melalui studi kasus sistem akademik:
* Hubungan antara `Jurusan` dan `Dosen` (Agregasi)
* Hubungan antara `Komputer` dan `Prosessor` (Komposisi)
Tuliskan potongan kode Java yang membuktikan perbedaan masa hidup (*lifecycle dependency*) dari komponen anak saat objek induk dihancurkan (*garbage collected*)!

**Kunci Pembahasan & Solusi:**
```java
// === KASUS 1: AGREGASI (Masa Hidup Independen) ===
class Dosen {
    private String nama;
    public Dosen(String nama) { this.nama = nama; }
    public String getNama() { return nama; }
}

class Jurusan {
    private String namaJurusan;
    private Dosen kepalaJurusan; // Agregasi: Referensi objek luar disuntikkan via konstruktor

    public Jurusan(String namaJurusan, Dosen kepalaJurusan) {
        this.namaJurusan = namaJurusan;
        this.kepalaJurusan = kepalaJurusan;
    }
}

// === KASUS 2: KOMPOSISI (Masa Hidup Terikat Penuh) ===
class Prosessor {
    private String model;
    public Prosessor(String model) { this.model = model; }
    public String getModel() { return model; }
}

class Komputer {
    private String merk;
    private Prosessor cpu; // Komposisi: Objek dibuat langsung di dalam internal Komputer

    public Komputer(String merk, String cpuModel) {
        this.merk = merk;
        // Instansiasi eksklusif di dalam konstruktor pemilik
        this.cpu = new Prosessor(cpuModel);
    }
}

// Demonstrasi Uji Siklus Hidup:
public class TestLifecycle {
    public static void main(String[] args) {
        // Pada Agregasi:
        Dosen pakBudi = new Dosen("Dr. Budi, M.Kom.");
        Jurusan ifUndip = new Jurusan("Informatika", pakBudi);
        ifUndip = null; // Objek Jurusan dimusnahkan!
        // Objek pakBudi MASIH HIDUP di memori dan tetap dapat diakses:
        System.out.println("Dosen tetap eksis: " + pakBudi.getNama());

        // Pada Komposisi:
        Komputer laptop = new Komputer("Dell XPS", "Intel i7-13700H");
        laptop = null; // Objek Komputer dihancurkan!
        // Objek Prosessor di dalam laptop ikut lenyap dan tidak dapat diakses lagi oleh siapapun.
    }
}
```

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (POLIMORFISME, GENERICS & SERIALISASI)

### Soal UAS 1: Polimorfisme Dinamis (*Dynamic Method Dispatch*) & Downcasting
**Deskripsi Soal:**
Diberikan hierarki kelas karyawan:
* Superclass `Pegawai` dengan metode `hitungGaji()` yang mengembalikan nilai gaji pokok $4.000.000$.
* Subclass `Manajer` yang meng-override `hitungGaji()` dengan menambahkan tunjangan manajerial $3.000.000$, serta memiliki metode unik `jadwalkanRapat()`.
* Subclass `Programmer` yang meng-override `hitungGaji()` dengan menambahkan bonus lembur $1.500.000$, serta memiliki metode unik `debugging()`.

Buatlah program Java yang:
1. Menyimpan berbagai objek pegawai ke dalam satu `List<Pegawai>` polimorfik.
2. Melakukan perulangan untuk mencetak total pengeluaran gaji secara dinamis (*late binding*).
3. Melakukan pengujian tipe (*RTTI*) menggunakan operator `instanceof` untuk mengeksekusi metode spesifik subclass secara aman tanpa memicu `ClassCastException`!

**Kunci Pembahasan & Solusi:**
```java
import java.util.ArrayList;
import java.util.List;

class Pegawai {
    protected String nama;
    public Pegawai(String nama) { this.nama = nama; }
    public double hitungGaji() { return 4000000.0; }
}

class Manajer extends Pegawai {
    public Manajer(String nama) { super(nama); }
    @Override
    public double hitungGaji() { return super.hitungGaji() + 3000000.0; }
    public void jadwalkanRapat() {
        System.out.println(nama + " sedang menjadwalkan rapat divisi.");
    }
}

class Programmer extends Pegawai {
    public Programmer(String nama) { super(nama); }
    @Override
    public double hitungGaji() { return super.hitungGaji() + 1500000.0; }
    public void debugging() {
        System.out.println(nama + " sedang memperbaiki bug kritis sistem.");
    }
}

public class MainPolimorfisme {
    public static void main(String[] args) {
        List<Pegawai> daftarKaryawan = new ArrayList<>();
        daftarKaryawan.add(new Manajer("Andi"));
        daftarKaryawan.add(new Programmer("Budi"));
        daftarKaryawan.add(new Programmer("Citra"));

        double totalGaji = 0;

        for (Pegawai p : daftarKaryawan) {
            // Pemanggilan polimorfik dinamis (Late Binding saat runtime)
            System.out.println("Gaji " + p.nama + " : Rp " + p.hitungGaji());
            totalGaji += p.hitungGaji();

            // Safe Downcasting via instanceof
            if (p instanceof Manajer) {
                Manajer m = (Manajer) p;
                m.jadwalkanRapat();
            } else if (p instanceof Programmer) {
                Programmer pr = (Programmer) p;
                pr.debugging();
            }
        }
        System.out.println("Total Beban Payroll Perusahaan: Rp " + totalGaji);
    }
}
```

---

### Soal UAS 2: Serialisasi Objek ke File Disk dengan Kata Kunci `transient`
**Deskripsi Soal:**
Buatlah kelas `AkunPengguna` yang mengimplementasikan `Serializable` dengan atribut: `username` (String), `passwordHash` (String), dan `sessionToken` (String, sensitif/sementara).
1. Gunakan kata kunci `transient` pada atribut `sessionToken` agar tidak disimpan ke disk.
2. Tuliskan kode Java lengkap untuk melakukan serialisasi objek `AkunPengguna` ke file biner `akun.dat` menggunakan `ObjectOutputStream`.
3. Tuliskan kode untuk membaca kembali (*deserialisasi*) objek dari file menggunakan `ObjectInputStream` dan buktikan bahwa nilai atribut `sessionToken` kembali menjadi `null`!

**Kunci Pembahasan & Solusi:**
```java
import java.io.*;

class AkunPengguna implements Serializable {
    private static final long serialVersionUID = 1L; // Menjamin kompatibilitas versi kelas

    private String username;
    private String passwordHash;
    private transient String sessionToken; // Kata kunci transient: TIDAK diikutsertakan dalam serialisasi

    public AkunPengguna(String username, String passwordHash, String sessionToken) {
        this.username = username;
        this.passwordHash = passwordHash;
        this.sessionToken = sessionToken;
    }

    @Override
    public String toString() {
        return "User: " + username + " | Hash: " + passwordHash + " | Token: " + sessionToken;
    }
}

public class TestSerialisasi {
    public static void main(String[] args) {
        String filename = "akun.dat";
        AkunPengguna userAsli = new AkunPengguna("gathan_undip", "sha256$8f92a...", "TOKEN_XYZ_SECRET_999");

        // 1. SERIALISASI: Tulis objek ke file
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filename))) {
            oos.writeObject(userAsli);
            System.out.println("Objek berhasil diserialisasi: " + userAsli);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 2. DESERIALISASI: Baca objek dari file
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filename))) {
            AkunPengguna userPulih = (AkunPengguna) ois.readObject();
            System.out.println("Objek hasil deserialisasi : " + userPulih);
            // Nilai token otomatis menjadi null karena bersifat transient!
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa dalam bahasa Java kita WAJIB meng-override metode hashCode() jika kita meng-override metode equals() pada sebuah kelas?"
**Jawaban Komprehensif:**
Jika kita meng-override metode `equals()` tetapi mengabaikan `hashCode()`, kita melanggar **Kontrak Umum Objek Java (*The equals and hashCode Contract*)**:
> *"Jika dua objek bernilai sama menurut metode `equals(Object)`, maka pemanggilan `hashCode()` pada kedua objek tersebut WAJIB menghasilkan bilangan integer yang sama persis."*

Jika kontrak ini dilanggar:
* Struktur data berbasis tabel hash di Java Collections (seperti `HashSet`, `HashMap`, dan `Hashtable`) akan mengalami kerusakan fatal.
* Saat kita memasukkan objek ke `HashSet`, Java pertama-tama menghitung `hashCode()` objek untuk menentukan ember memori (*bucket location*).
* Jika dua objek yang menurut logika kita bernilai sama memiliki `hashCode()` yang berbeda, objek kedua akan diletakkan di bucket yang berbeda. Akibatnya, `set.contains(objekIdentik)` akan mengembalikan `false` dan `HashSet` akan menyimpan dua objek duplikat yang seharusnya dilarang.

### Q2: "Jelaskan apa perbedaan antara Checked Exception dan Unchecked Exception, serta kapan Anda sebagai software architect memutuskan membuat Checked Exception baru!"
**Jawaban Komprehensif:**
* **Unchecked Exception (Turunan dari `java.lang.RuntimeException`):**
  * Merepresentasikan cacat logika pemrograman (*programming bugs / programmer error*) yang seharusnya bisa dicegah melalui pemeriksaan kondisi kode yang benar (contoh: membagi dengan nol `ArithmeticException`, dereferensi pointer null `NullPointerException`, atau indeks array di luar batas).
  * Kompiler tidak mewajibkan penanganan klausa `try-catch`.
* **Checked Exception (Turunan dari `java.lang.Exception` di luar RuntimeException):**
  * Merepresentasikan kegagalan lingkungan eksternal (*unpreventable environmental failures*) yang berada di luar kendali alur kode murni, namun sistem masih diharapkan mampu melakukan pemulihan (*recoverable condition*). Contoh: file tidak ditemukan di disk (`FileNotFoundException`), koneksi database terputus (`SQLException`).
* **Kapan Membuat Checked Exception Baru:**
  Sebagai perancang arsitektur, kita membuat Checked Exception kustom ketika kita ingin **secara eksplisit memaksa pemanggil API (*caller*) memikirkan dan mengimplementasikan rencana cadangan (*fallback strategy*)** saat kegagalan bisnis terjadi (contoh: `SaldoTidakCukupException` pada perbankan, memaksa modul UI menampilkan dialog top-up saldo ke nasabah alih-alih membiarkan aplikasi crash mendadak).
