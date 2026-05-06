# API Contract

## 1. User Profile

**Endpoint:** `/api/v1/profile`

**Method:** `GET`

### Response Body

```json
{
  "id": 1,
  "username": "mahasiswa_sd",
  "email": "mhs@univ.ac.id",
  "avatar_url": "https://image.com/avatar.png"
}
```

---

## 2. User Login

**Endpoint:** `/api/v1/login`

**Method:** `POST`

### Request Body

```json
{
  "email": "mhs@univ.ac.id",
  "password": "password123"
}
```

### Response Body Success

```json
{
  "success": true,
  "message": "Login berhasil",
  "token": "jwt_token_example",
  "user": {
    "id": 1,
    "username": "mahasiswa_sd",
    "email": "mhs@univ.ac.id"
  }
}
```

### Response Body Failed

```json
{
  "success": false,
  "message": "Email atau password salah"
}
```