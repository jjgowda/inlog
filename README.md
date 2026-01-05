
# INLOG 🔐  
A modern authentication service with a clean UI, JSON-based APIs, and secure cookie-based sessions.

INLOG provides:
- Login & Registration UI
- Secure authentication APIs
- HTTP-only cookie sessions
- Demo consumer website
- Ready base for email, verification, and password reset

---

## ✨ Features

- ✅ Modern animated login & registration UI
- ✅ JSON-only API (no form hacks)
- ✅ HTTP-only cookies for session security
- ✅ `/api/me` for authenticated user info
- ✅ Logout support
- ✅ Clean separation: UI ↔ API
- ✅ Built with FastAPI

---

## 🏗 Project Structure

```

INLOG/
├── main.py              # FastAPI backend
├── users.py             # In-memory user store (demo)
├── index.html           # Demo website (consumer app)
├── auth.html            # Login UI
├── register.html        # Registration UI
├── email_utils.py       # (optional) SMTP utilities
├── README.md
└── .env.example

````

---

## ⚙️ Tech Stack

- **Backend:** FastAPI (Python)
- **Auth:** JWT (stored in HTTP-only cookies)
- **Frontend:** Plain HTML, CSS, Vanilla JS
- **Session:** Cookie-based (industry standard)

---

## 🚀 Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/yourname/inlog.git
cd inlog
````

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn python-jose
```

### 4️⃣ Run the server

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 🌐 Available Pages

| URL         | Description                    |
| ----------- | ------------------------------ |
| `/`         | Demo website (uses INLOG auth) |
| `/auth`     | Login page                     |
| `/register` | Registration page              |
| `/docs`     | FastAPI Swagger docs           |

---

## 🔌 API Endpoints

### 🔐 Login

```
POST /api/login
Content-Type: application/json
```

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

---

### 📝 Register

```
POST /api/register
Content-Type: application/json
```

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

---

### 👤 Get Current User

```
GET /api/me
```

* Requires authentication cookie

---

### 🚪 Logout

```
POST /api/logout
```

---

## 🔒 Security Model

* JWT stored in **HTTP-only cookies**
* Frontend never accesses tokens
* Browser auto-sends cookies
* Prevents token leakage & XSS access

> This is the same pattern used by Google, GitHub, Netflix, etc.

---

## ⚠️ Important Notes

* Current `users.py` is **in-memory** (demo only)
* Passwords are **plain-text** (bcrypt should be added before production)
* Cookies are not marked `secure` (HTTPS required in production)

---

## 🛣 Roadmap

* [ ] Password hashing (bcrypt)
* [ ] Email verification
* [ ] Password reset flow
* [ ] Database integration
* [ ] CSRF protection
* [ ] Multi-tenant auth
* [ ] OAuth provider support

---

## 📜 License

MIT License
Free to use, modify, and learn from.

---

## 👤 Author

Built by **INLOG Team**
For learning, experimentation, and future scale 🚀

````

---

# 📄 `.env.example`

```env
# JWT
SECRET_KEY=change_this_in_production
TOKEN_EXPIRE_MINUTES=60

# SMTP (optional – future use)
SMTP_HOST=smtp.zoho.in
SMTP_PORT=587
SMTP_USER=no-reply@inlog.io
SMTP_PASS=your_app_password
````

---

# 📄 `users.py` (README reference version)

```python
users = []

def find_user(email: str):
    return next((u for u in users if u["email"] == email), None)

def add_user(email: str, password: str):
    user = {
        "id": len(users) + 1,
        "email": email,
        "password": password
    }
    users.append(user)
    return user
```
## 🚀 Future Updates & Roadmap

INLOG is designed to be extended incrementally. The following features are planned for future releases:

### 🔐 Security Enhancements
- [ ] Password hashing using **bcrypt**
- [ ] CSRF protection for cookie-based authentication
- [ ] Secure cookie flags (`Secure`, `SameSite=Strict`) for production
- [ ] Rate limiting on auth endpoints
- [ ] Account lockout after repeated failed logins

### 📧 Email & Account Management
- [ ] SMTP integration (Zoho Mail / custom domain)
- [ ] Email verification after registration
- [ ] Login notification emails
- [ ] Forgot password & reset password flow
- [ ] Change email & change password functionality

### 👤 User & Session Management
- [ ] Persistent database storage (PostgreSQL / MySQL)
- [ ] User roles (admin / user)
- [ ] Session expiry & refresh tokens
- [ ] Active session management
- [ ] Logout from all devices

### 🌐 OAuth & SSO
- [ ] OAuth 2.0 support
- [ ] Login with Google / GitHub
- [ ] INLOG as a third-party SSO provider
- [ ] Multi-tenant authentication support

### 🧱 Platform & Infrastructure
- [ ] Docker support
- [ ] Environment-based configuration
- [ ] Production deployment (Render / Railway / VPS)
- [ ] HTTPS & domain configuration
- [ ] Reverse proxy setup (Nginx)

### 🎨 Frontend Improvements
- [ ] User dashboard
- [ ] Profile management UI
- [ ] Error handling & toast notifications
- [ ] Accessibility improvements
- [ ] Dark mode

### 📊 Observability & Maintenance
- [ ] Structured logging
- [ ] Audit logs for authentication events
- [ ] Metrics & monitoring
- [ ] Automated tests (unit & integration)

---

> This roadmap is iterative. Features will be implemented with a strong focus on security, simplicity, and scalability.

