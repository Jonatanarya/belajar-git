# FINAL REPORT — Kontribusi Individu
## Mata Kuliah: Rekayasa Perangkat Lunak / Software Development
## Semester Genap 2025/2026

---

## Identitas

| | |
|---|---|
| **Nama** | Jonatan Arya Santosa |
| **Peran** | Frontend Developer (FE) |
| **Repositori Kelompok** | https://github.com/pidz14/website-showroom-sepeda-motor- |
| **Branch Utama** | `development` |

---

## Deskripsi Proyek

**Bagong Jaya Motor** — Website showroom sepeda motor berbasis web yang memungkinkan pelanggan melihat katalog motor, detail kendaraan, dan mengajukan permohonan test drive. Sistem dibangun menggunakan arsitektur MVC dengan CodeIgniter 4 (frontend) dan FastAPI Python (backend API), serta di-deploy menggunakan Docker.

---

## Kontribusi Selama 16 Minggu

### Fase 1 — Perencanaan & Setup Awal (Minggu 1–4)

- Mempelajari arsitektur proyek (MVC, CI4, Docker)
- Menyepakati pembagian tugas dengan tim (Backend, Frontend, Product Lead)
- Setup struktur awal folder CI4: `Views/`, `Controllers/`, `public/assets/`

**Commit terkait:**
- [`12196fb`](https://github.com/pidz14/website-showroom-sepeda-motor-/commit/12196fb) — `feat(frontend): initial structure`
- [`0e6e62d`](https://github.com/pidz14/website-showroom-sepeda-motor-/commit/0e6e62d) — `feat(frontend): setup CI4 views and assets structure`

---

### Fase 2 — Pengembangan UI & Assets (Minggu 5–8)

- Membangun design system dengan CSS custom: color tokens, typography, layout grid
- Membuat komponen UI: motor card, filter panel, hero banner, status badge
- Menulis `showroom.js` — logika SPA (Single Page Application) dengan hash routing
- Implementasi fetch API ke backend untuk load data motor secara dinamis

**Commit terkait:**
- [`f6df868`](https://github.com/pidz14/website-showroom-sepeda-motor-/commit/f6df868) — `fix(frontend): add initial content to views and assets`
- [`2c40031`](https://github.com/pidz14/website-showroom-sepeda-motor-/commit/2c40031) — `feat: implement main showroom UI`

---

### Fase 3 — Integrasi Frontend ↔ Backend API (Minggu 9–12)

- Mengintegrasikan JavaScript `showroom.js` dengan endpoint API backend (`/motors`, `/motors/{id}`)
- Implementasi normalisasi response JSON dari API ke komponen UI
- Menambahkan filter motor (merek, harga, ketersediaan) dan search real-time
- Membuat halaman detail motor yang di-load dari API secara dinamis

**Commit terkait:**
- [`17b7355`](https://github.com/pidz14/website-showroom-sepeda-motor-/commit/17b7355) — `Integrate frontend with motor API`
- [`4c515ab`](https://github.com/pidz14/website-showroom-sepeda-motor-/commit/4c515ab) — Merge PR #20 integrasi frontend

---

### Fase 4 — Dockerisasi & Deployment (Minggu 13–14)

- Membuat `Dockerfile` untuk container frontend CI4 + Apache
- Mengkonfigurasi Apache agar DocumentRoot mengarah ke `/public` (CI4 standard)
- Setup bind mount assets di `docker-compose.yml`
- Menemukan dan memperbaiki bug: `ENV API_URL=http://localhost:5000` yang salah port

**Commit terkait:**
- [`8d16350`](https://github.com/pidz14/website-showroom-sepeda-motor-/commit/8d16350) — `feat: add dockerfile and dockerignore for frontend (codeigniter)`
- [`8222d97`](https://github.com/pidz14/website-showroom-sepeda-motor-/commit/8222d97) — `fix: install php-intl extension and fix dockerfile casing`

---

### Fase 5 — Views, Controllers, Bug Fix Final (Minggu 15–16)

Kontribusi terbesar di sprint akhir:

**Views yang dibuat:**
- `layouts/main.php` — layout utama dengan `base_url()` CI4 dan injeksi `window.SHOWROOM_API_BASE_URL` ke JS
- `home/index.php` — SPA dengan 3 section (Landing, Katalog, Detail Motor)
- `auth/login.php` & `auth/register.php` — form autentikasi dengan CSRF protection
- `test-drive/form.php` — form test drive + info box
- `admin/motors.php` — panel admin dengan tabel data dari API

**Controllers yang diisi:**
- `Home.php`, `Auth.php` (login/register/logout), `Motors.php` (index/show), `TestDrive.php` (index/create), `Admin/Motors.php`

**Bug fix kritis:**
- **Fix CORS**: Menambahkan `CORSMiddleware` ke FastAPI agar browser bisa fetch ke API (beda port = beda origin)
- **Fix pathing assets**: Mengganti hardcode `/assets/...` dengan `base_url()` CI4 agar tidak 404 saat diakses via IP server
- **Fix Docker ENV**: `API_URL_INTERNAL=http://backend-api:8000` untuk PHP server-side, `API_URL_BROWSER=http://localhost:8000` untuk JavaScript browser
- **Resolve merge conflict**: `README.md` conflict antara branch lokal dan remote

**Commit terkait:**
- [`f92d2f3`](https://github.com/pidz14/website-showroom-sepeda-motor-/commit/f92d2f3) — `feat-fe: complete frontend views, controllers, fix CORS & pathing, deployment tested` ⭐ **Commit Terbaik**

---

## Commit Terbaik (Highlight)

### ⭐ [`f92d2f3`](https://github.com/pidz14/website-showroom-sepeda-motor-/commit/f92d2f3)
> `feat-fe: complete frontend views, controllers, fix CORS & pathing, deployment tested`

Commit ini merupakan kontribusi paling komprehensif yang saya lakukan, mencakup:
- 5 file View HTML baru
- 5 Controller PHP yang diisi penuh dengan logika
- Fix bug CORS yang menyebabkan `Failed to fetch` di browser
- Fix pathing assets agar tidak 404 saat deploy via IP server
- Fix konfigurasi Docker (ENV variable yang salah)
- Resolve merge conflict README
- Verifikasi deployment berhasil: CSS/JS status 200, data motor load dari API

---

## Teknologi yang Dikuasai Selama Proyek

| Teknologi | Penggunaan |
|---|---|
| **PHP CodeIgniter 4** | MVC framework, routing, views, controllers, CSRF, session |
| **HTML + CSS (Vanilla)** | Design system, responsive layout, komponen UI |
| **JavaScript (Vanilla)** | SPA routing, Fetch API, DOM manipulation, filter real-time |
| **Docker + Docker Compose** | Containerisasi, bind mount, environment variables, multi-service |
| **Apache (PHP container)** | mod_rewrite, DocumentRoot, .htaccess |
| **FastAPI (Python)** | Memahami struktur API, menambahkan CORS middleware |
| **Git & GitHub** | Branch strategy, commit, merge conflict resolution |

---

## Tantangan & Pembelajaran

| Tantangan | Solusi |
|---|---|
| CORS error: browser blokir fetch dari port 8080 ke 8000 | Tambah `CORSMiddleware` di FastAPI dengan `allow_origins=["*"]` |
| Pathing assets 404 saat akses via IP server | Gunakan `base_url()` helper CI4, bukan hardcode `/assets/` |
| Docker: PHP tidak bisa reach `localhost:8000` | Pakai nama service Docker `backend-api:8000` sebagai `API_URL_INTERNAL` |
| Merge conflict README.md | Resolve manual, ambil versi terlengkap dari kedua branch |
| PHP inject API URL ke browser JS | Pisah dua env: `API_URL` (internal) dan `API_URL_BROWSER` (untuk JS) |

---

*Laporan ini dibuat sebagai bukti kontribusi individu dalam proyek kelompok Website Showroom Sepeda Motor.*
