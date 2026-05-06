# Database Schema

## 1. Table: users

Menyimpan data pengguna aplikasi.

| Field | Type | Description |
|---|---|---|
| id | BIGINT | Primary key |
| username | VARCHAR(100) | Username pengguna |
| email | VARCHAR(100) | Email pengguna |
| password | VARCHAR(255) | Password hash |
| avatar_url | VARCHAR(255) | Foto profil pengguna |
| created_at | TIMESTAMP | Tanggal dibuat |

---

## 2. Table: login_logs

Menyimpan riwayat login pengguna.

| Field | Type | Description |
|---|---|---|
| id | BIGINT | Primary key |
| user_id | BIGINT | Relasi ke users |
| login_time | TIMESTAMP | Waktu login |
| ip_address | VARCHAR(100) | IP pengguna |

---

## 3. Table: sessions

Menyimpan token session login pengguna.

| Field | Type | Description |
|---|---|---|
| id | BIGINT | Primary key |
| user_id | BIGINT | Relasi ke users |
| token | TEXT | JWT token/session |
| expired_at | TIMESTAMP | Masa berlaku token |
| created_at | TIMESTAMP | Tanggal dibuat |