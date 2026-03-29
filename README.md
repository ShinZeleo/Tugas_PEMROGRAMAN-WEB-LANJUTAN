
# FastAPI Microservices - CRUD, JWT Auth, RBAC & Testing

Project ini merupakan implementasi **RESTful API berbasis FastAPI** yang dikembangkan sebagai bagian dari tugas mata kuliah **Pemrograman Web Lanjutan**.

Versi ini merupakan pengembangan dari project sebelumnya dengan penambahan:
- Autentikasi menggunakan JWT
- Role-Based Access Control (RBAC)
- Operasi CRUD lengkap
- Automated Testing menggunakan pytest

---

## 🚀 Fitur Utama

### 🔐 Autentikasi (JWT)
- Register user dan admin
- Login dan generate access token
- Proteksi endpoint menggunakan token

### 📦 CRUD Operasional (Item)
| Method | Endpoint           | Deskripsi                |
|--------|------------------|-------------------------|
| POST   | `/items/`         | Membuat item            |
| GET    | `/items/`         | Menampilkan semua item  |
| PUT    | `/items/{id}`     | Update item             |
| DELETE | `/items/{id}`     | Hapus item (admin only) |

### 🛡️ RBAC (Role-Based Access Control)
- User biasa tidak bisa delete data
- Admin memiliki akses penuh

### 🧪 Automated Testing (Pytest)
- Pengujian autentikasi (register & login)
- Pengujian CRUD lengkap
- Pengujian RBAC (403 Forbidden)
- Pengujian unauthorized (tanpa token)

---

## 🛠️ Teknologi yang Digunakan

- **FastAPI** – Framework backend
- **SQLAlchemy** – ORM database
- **SQLite** – Database
- **Pydantic** – Validasi data
- **JWT (python-jose)** – Autentikasi
- **Passlib (bcrypt)** – Hash password
- **Pytest** – Automated testing
- **Uvicorn** – ASGI server

---

## 📂 Struktur Project

```

Tugas_FastAPI-CRUD/
│
├── app/
│   ├── main.py        # Endpoint + Auth + RBAC
│   ├── models.py      # Model database
│   ├── schemas.py     # Schema Pydantic
│   └── db.py          # Koneksi database
│
├── tests/
│   └── test_main.py   # Test pytest
│
├── requirements.txt
└── README.md

````

---

## ⚙️ Cara Menjalankan Project

### 1. Install Dependencies
```bash
pip install -r requirements.txt
````

### 2. Jalankan Server

```bash
uvicorn app.main:app --reload
```

Server akan berjalan di:

```
http://127.0.0.1:8000
```

---

## 📄 Dokumentasi API

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Cara Menjalankan Testing

```bash
pytest -v
```

### Contoh Output:

```
8 passed
```

---

## 🧠 Konsep yang Digunakan

* RESTful API
* Microservices Architecture
* JWT Authentication
* Role-Based Access Control (RBAC)
* Object Relational Mapping (ORM)
* Automated Testing (pytest)

---

## 📌 Kesimpulan

Project ini berhasil mengimplementasikan sistem backend microservices dengan:

* Autentikasi JWT
* CRUD lengkap
* RBAC
* Testing otomatis

Seluruh pengujian berhasil dijalankan dengan hasil:

```
8 passed
```

---

## 👨‍💻 Author

Dibuat untuk tugas mata kuliah **Pemrograman Web Lanjutan**.


