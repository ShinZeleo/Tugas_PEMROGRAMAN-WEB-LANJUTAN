import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# =====================
# HELPER
# =====================
def random_email():
    return f"user_{uuid.uuid4()}@test.com"

def register(email, password, role="user"):
    return client.post("/register", json={
        "email": email,
        "password": password,
        "role": role
    })

def login(email, password):
    return client.post("/login", json={
        "email": email,
        "password": password
    })

def get_token(email, password):
    res = login(email, password)
    return res.json()["access_token"]


# =====================
# AUTH TEST
# =====================
def test_register():
    email = random_email()
    res = register(email, "123")
    assert res.status_code == 200


def test_login():
    email = random_email()
    register(email, "123")
    res = login(email, "123")
    assert res.status_code == 200
    assert "access_token" in res.json()


# =====================
# CRUD TEST
# =====================

def test_create_item():
    email = random_email()
    register(email, "123")
    token = get_token(email, "123")

    res = client.post("/items/",
        json={"name": "Laptop", "description": "Gaming"},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 200


def test_get_items():
    email = random_email()
    register(email, "123")
    token = get_token(email, "123")

    res = client.get("/items/",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 200


def test_update_item():
    email = random_email()
    register(email, "123")
    token = get_token(email, "123")

    create = client.post("/items/",
        json={"name": "Old", "description": "desc"},
        headers={"Authorization": f"Bearer {token}"}
    )

    item_id = create.json()["id"]

    res = client.put(f"/items/{item_id}",
        json={"name": "New", "description": "updated"},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 200


def test_admin_can_delete():
    email = random_email()
    register(email, "123", "admin")
    token = get_token(email, "123")

    create = client.post("/items/",
        json={"name": "Item", "description": "desc"},
        headers={"Authorization": f"Bearer {token}"}
    )

    item_id = create.json()["id"]

    res = client.delete(f"/items/{item_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 200


# =====================
# RBAC TEST
# =====================

def test_rbac_denied():
    admin_email = random_email()
    user_email = random_email()

    register(admin_email, "123", "admin")
    admin_token = get_token(admin_email, "123")

    create = client.post("/items/",
        json={"name": "Item", "description": "desc"},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    item_id = create.json()["id"]

    register(user_email, "123", "user")
    user_token = get_token(user_email, "123")

    res = client.delete(f"/items/{item_id}",
        headers={"Authorization": f"Bearer {user_token}"}
    )

    assert res.status_code == 403


# =====================
# UNAUTHORIZED TEST
# =====================

def test_no_token():
    res = client.get("/items/")
    assert res.status_code in [401, 403]