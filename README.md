# FastAPI CRUD - GET Items API

Project ini merupakan implementasi sederhana **RESTful API menggunakan FastAPI dan SQLAlchemy** untuk memenuhi tugas mata kuliah **Pemrograman Web Lanjutan**.

API ini menggunakan **database SQLite** dan menerapkan konsep **ORM (Object Relational Mapping)** serta **validasi data dengan Pydantic**.

---

## 📌 Fitur API

API ini menyediakan dua endpoint utama:

| Method | Endpoint           | Deskripsi                          |
| ------ | ------------------ | ---------------------------------- |
| GET    | `/items/`          | Mengambil semua data item          |
| GET    | `/items/{item_id}` | Mengambil data item berdasarkan ID |

---

## 🛠️ Teknologi yang Digunakan

* **FastAPI** – Framework untuk membuat REST API
* **SQLAlchemy** – ORM untuk menghubungkan Python dengan database
* **SQLite** – Database ringan berbasis file
* **Pydantic** – Validasi dan serialisasi data
* **Uvicorn** – ASGI server untuk menjalankan FastAPI

---

## 📂 Struktur Project

```
fastapi-crud
│
├── main.py        # Endpoint API
├── models.py      # Model database (SQLAlchemy)
├── schemas.py     # Schema validasi data (Pydantic)
├── db.py    # Konfigurasi koneksi database
└── README.md
```

---

## ⚙️ Cara Menjalankan Project

### 1. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy
```

### 2. Jalankan Server

```bash
python -m uvicorn main:app --reload
```

Server akan berjalan di:

```
http://127.0.0.1:8000
```

---

## 📄 Dokumentasi API

FastAPI menyediakan dokumentasi otomatis menggunakan **Swagger UI**.

Buka di browser:

```
http://127.0.0.1:8000/docs
```

Di halaman tersebut kamu bisa langsung mencoba endpoint API.

---

## 🧠 Konsep yang Digunakan

Project ini menerapkan beberapa konsep dasar dalam pengembangan backend:

* **RESTful API**
* **Object Relational Mapping (ORM)**
* **Validasi data menggunakan Pydantic**
* **Dependency Injection untuk database session**
* **Dokumentasi API otomatis dengan Swagger**

---

## 👨‍💻 Author

Project ini dibuat untuk tugas mata kuliah **Pemrograman Web Lanjutan**.
