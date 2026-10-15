# Bank Contoh Soal & Pembahasan: Pengembangan Berbasis Platform

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Pengembangan Berbasis Platform Departemen Informatika Universitas Diponegoro (Koleksi Pengampu Panji Wisnu Wirawan, S.T., M.T., Rismiyati, B.Eng., M.Cs., dkk. & Bank Soal HMIF 2017–2024).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (PEMROGRAMAN WEB, AJAX & PHP SESSION)

### Soal UTS 1: Autentikasi Login Aman PHP & MySQL PDO (Soal Asli UTS Undip)
**Deskripsi Soal:**
Buatlah skrip backend PHP bernama `login_process.php` yang memproses form login pengguna (`username` dan `password`):
1. Menggunakan koneksi database **PHP Data Objects (PDO)** dengan penanganan error `PDOException`.
2. Melakukan kueri pencarian akun menggunakan **Prepared Statements** berparameter untuk mencegah celah **SQL Injection**.
3. Memverifikasi kecocokan password menggunakan fungsi bawaan aman **`password_verify()`**.
4. Jika login sukses, buat sesi server (`$_SESSION`), regenerasi ID sesi untuk mencegah *Session Fixation*, simpan data username, dan lakukan pengalihan (*redirect*) ke `dashboard.php`.
5. Jika gagal, kembalikan ke halaman `login.php` dengan pesan error.

**Kunci Pembahasan & Solusi:**
```php
<?php
// login_process.php
session_start();

// 1. Konfigurasi Koneksi Database via PDO
$host     = 'localhost';
$db       = 'db_akademik';
$user     = 'root';
$pass     = '';
$charset  = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false, // Menjamin prepared statements native di engine DBMS
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (PDOException $e) {
    die("Koneksi basis data gagal: " . $e->getMessage());
}

// 2. Validasi Masukan Form
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username'] ?? '');
    $password = trim($_POST['password'] ?? '');

    if (empty($username) || empty($password)) {
        header("Location: login.php?error=Semua+bidang+wajib+diisi");
        exit;
    }

    // 3. Eksekusi Kueri Aman Menggunakan Prepared Statement
    $stmt = $pdo->prepare("SELECT id, username, password_hash, role FROM users WHERE username = :username LIMIT 1");
    $stmt->execute([':username' => $username]);
    $userAccount = $stmt->fetch();

    // 4. Verifikasi Password Menggunakan password_verify
    if ($userAccount && password_verify($password, $userAccount['password_hash'])) {
        // Regenerasi ID sesi untuk mencegah serangan Session Fixation
        session_regenerate_id(true);

        // Simpan status login di sesi server
        $_SESSION['is_logged_in'] = true;
        $_SESSION['user_id']      = $userAccount['id'];
        $_SESSION['username']     = $userAccount['username'];
        $_SESSION['role']         = $userAccount['role'];

        header("Location: dashboard.php");
        exit;
    } else {
        // Login gagal (Gunakan pesan generik agar penyerang tidak tahu apakah user atau pass yang salah)
        header("Location: login.php?error=Username+atau+password+salah");
        exit;
    }
}
?>
```

---

### Soal UTS 2: Asynchronous Form Validation Menggunakan JavaScript Fetch API
**Deskripsi Soal:**
Buatlah kode JavaScript sisi klien (*client-side*) yang mendengarkan event input pada field `<input type="text" id="nim">`:
* Setiap kali pengguna selesai mengetikkan 14 digit NIM, lakukan permintaan asinkron (*AJAX*) ke endpoint backend `/api/check_nim.php?nim=...` menggunakan **Fetch API**.
* Tampilkan indikator status *"Memeriksa..."*, lalu jika NIM sudah terdaftar, tampilkan pesan peringatan merah *"NIM sudah digunakan"* dan nonaktifkan tombol submit form. Jika belum terdaftar, tampilkan teks hijau *"NIM tersedia"*.

**Kunci Pembahasan & Solusi:**
```javascript
// Script validasi asinkron NIM
const nimInput = document.getElementById('nim');
const statusMsg = document.getElementById('status-nim');
const submitBtn = document.getElementById('btn-submit');

nimInput.addEventListener('blur', async () => {
    const nimVal = nimInput.value.trim();

    if (nimVal.length === 14) {
        statusMsg.textContent = "Sedang memeriksa ketersediaan NIM...";
        statusMsg.style.color = "blue";

        try {
            const response = await fetch(`/api/check_nim.php?nim=${encodeURIComponent(nimVal)}`, {
                method: 'GET',
                headers: { 'Accept': 'application/json' }
            });

            if (!response.ok) throw new Error("Respon jaringan bermasalah");

            const result = await response.json(); // Menguraikan payload JSON

            if (result.exists) {
                statusMsg.textContent = "Peringatan: NIM ini sudah terdaftar!";
                statusMsg.style.color = "red";
                submitBtn.disabled = true; // Kunci form
            } else {
                statusMsg.textContent = "NIM tersedia untuk didaftarkan.";
                statusMsg.style.color = "green";
                submitBtn.disabled = false; // Buka kunci form
            }
        } catch (error) {
            statusMsg.textContent = "Gagal memvalidasi NIM: " + error.message;
            statusMsg.style.color = "orange";
        }
    }
});
```

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (ANDROID SERVICE & INTENT NAVIGATION)

### Soal UAS 1: Implementasi Android Background Service Pemutar Audio (Soal Asli UAS Undip 2022)
**Deskripsi Soal:**
Buatlah sebuah kelas **Service** dalam Android bernama `AudioPlaybackService` yang digunakan untuk memainkan dan menghentikan file audio `demo.mp3` yang tersimpan pada direktori `/res/raw/demo.mp3`!
1. Tuliskan kode kelas `AudioPlaybackService` lengkap dengan pengelolaan objek `MediaPlayer`!
2. Jelaskan dan tuliskan contoh kode pemanggilan service tersebut dari dalam kelas `MainActivity` saat pengguna menekan tombol **Play** dan tombol **Stop**!

**Kunci Pembahasan & Solusi:**
1. **Implementasi Kelas Android Service (`AudioPlaybackService.java`):**
```java
package id.ac.undip.pbp;

import android.app.Service;
import android.content.Intent;
import android.media.MediaPlayer;
import android.os.IBinder;
import android.widget.Toast;

public class AudioPlaybackService extends Service {
    private MediaPlayer mediaPlayer;

    @Override
    public IBinder onBind(Intent intent) {
        // Mengembalikan null karena ini adalah Started Service (bukan Bound Service)
        return null;
    }

    @Override
    public void onCreate() {
        super.onCreate();
        // Inisialisasi media player dari file audio lokal di res/raw
        mediaPlayer = MediaPlayer.create(this, R.raw.demo);
        mediaPlayer.setLooping(false); // Tidak berulang otomatis
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        if (!mediaPlayer.isPlaying()) {
            mediaPlayer.start();
            Toast.makeText(this, "Audio mulai diputar di background...", Toast.LENGTH_SHORT).show();
        }
        return START_STICKY; // Jika sistem membunuh service karena memori rendah, buat ulang
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        if (mediaPlayer != null) {
            if (mediaPlayer.isPlaying()) {
                mediaPlayer.stop();
            }
            mediaPlayer.release(); // Bebaskan sumber daya hardware audio
            mediaPlayer = null;
        }
        Toast.makeText(this, "Audio service dihentikan.", Toast.LENGTH_SHORT).show();
    }
}
```
*(Catatan: Jangan lupa mendaftarkan service di `AndroidManifest.xml`: `<service android:name=".AudioPlaybackService" />`)*.

2. **Pemanggilan Service dari `MainActivity.java`:**
```java
public class MainActivity extends AppCompatActivity {
    private Button btnPlay, btnStop;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnPlay = findViewById(R.id.btn_play);
        btnStop = findViewById(R.id.btn_stop);

        // Aksi Tombol Play: Memulai Service Latar Belakang
        btnPlay.setOnClickListener(v -> {
            Intent playIntent = new Intent(MainActivity.this, AudioPlaybackService.class);
            startService(playIntent);
        });

        // Aksi Tombol Stop: Menghentikan Service Latar Belakang
        btnStop.setOnClickListener(v -> {
            Intent stopIntent = new Intent(MainActivity.this, AudioPlaybackService.class);
            stopService(stopIntent);
        });
    }
}
```

---

### Soal UAS 2: Navigasi Antar-Activity Menggunakan Explicit Intent & Passing Data
**Deskripsi Soal:**
Sebuah aplikasi katalog mahasiswa memiliki `MainActivity` yang menampilkan daftar nama. Ketika item diklik, aplikasi harus berpindah ke `DetailMahasiswaActivity` sambil membawa data: `NIM` (String), `Nama` (String), dan `IPK` (Double).
Tuliskan potongan kode Java untuk:
1. Mengirim data menggunakan **Explicit Intent** dari `MainActivity`!
2. Menerima dan menampilkan data tersebut pada `DetailMahasiswaActivity`!

**Kunci Pembahasan & Solusi:**
1. **Pengiriman Data dari `MainActivity`:**
```java
Intent intent = new Intent(MainActivity.this, DetailMahasiswaActivity.class);
intent.putExtra("EXTRA_NIM", "24060122120034");
intent.putExtra("EXTRA_NAMA", "Gathan");
intent.putExtra("EXTRA_IPK", 3.85);
startActivity(intent);
```

2. **Penerimaan Data di `DetailMahasiswaActivity`:**
```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_detail_mahasiswa);

    Intent intent = getIntent();
    if (intent != null) {
        String nim = intent.getStringExtra("EXTRA_NIM");
        String nama = intent.getStringExtra("EXTRA_NAMA");
        double ipk = intent.getDoubleExtra("EXTRA_IPK", 0.0);

        TextView tvInfo = findViewById(R.id.tv_detail);
        tvInfo.setText("NIM: " + nim + "\nNama: " + nama + "\nIPK: " + ipk);
    }
}
```

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa arsitektur RESTful API bersifat Stateless, dan apa dampak positif dari prinsip Statelessness ini terhadap skalabilitas sistem backend modern?"
**Jawaban Komprehensif:**
* **Makna Statelessness:** Setiap permintaan HTTP dari klien ke server wajib memuat semua konteks informasi otentikasi dan data yang diperlukan untuk memproses permintaan tersebut secara mandiri (misal via token `Authorization: Bearer <JWT>`). Server tidak menyimpan status sesi (*session state*) klien di memori lokal RAM-nya.
* **Dampak Positif terhadap Skalabilitas Backend:**
  1. *Horizontal Scaling Bebas Hambatan:* Server dapat ditambah menjadi ratusan node di balik Load Balancer tanpa memerlukan konfigurasi *Sticky Sessions* atau sinkronisasi session storage yang rumit. Setiap permintaan dari pengguna dapat ditangani secara acak oleh sembarang server yang sedang longgar.
  2. *Fault Tolerance Tinggi:* Jika salah satu instance server backend mengalami crash di tengah jalan, pengguna tidak akan tiba-tiba ter-logout paksa; request berikutnya langsung dilayani oleh node server lain yang sehat.
  3. *Mereduksi Beban Memori Server:* Server tidak perlu mengalokasikan ruang memori untuk menahan jutaan data sesi pengguna yang sedang idle.

### Q2: "Jelaskan apa yang terjadi pada siklus hidup Activity Android ketika pengguna sedang mengetik form lalu tiba-tiba memutar layar ponsel dari mode Potret ke mode Lanskap (Screen Rotation)!"
**Jawaban Komprehensif:**
Secara default pada sistem operasi Android, peristiwa rotasi layar dianggap sebagai perubahan konfigurasi perangkat (*Runtime Configuration Change*).
Alur siklus hidup yang terjadi adalah:
1. Sistem Android **MENGHANCURKAN Activity yang sedang berjalan**: secara berurutan mengeksekusi `onPause()` $\rightarrow$ `onStop()` $\rightarrow$ `onDestroy()`.
2. Kemudian sistem **MEMBUAT ULANG Activity dari awal** untuk memuat layout sumber daya lanskap: mengeksekusi `onCreate()` $\rightarrow$ `onStart()` $\rightarrow$ `onResume()`.
* **Dampak Negatif:** Jika pengembang tidak menangani ini dengan benar, seluruh data sementara yang telah diketik pengguna di form atau status variabel memori akan hilang/reset kembali ke nilai awal.
* **Solusi Arsitektural:** Menggunakan komponen **ViewModel** dari Android Jetpack (karena siklus hidup ViewModel bertahan melintasi penghancuran konfigurasi) atau menyimpan status sementara menggunakan callback bundle `onSaveInstanceState(Bundle outState)` dan memulihkannya kembali di `onRestoreInstanceState(Bundle savedInstanceState)`.
