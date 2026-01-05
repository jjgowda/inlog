from fastapi import FastAPI, HTTPException, Response, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
from jose import jwt, JWTError
from datetime import datetime, timedelta
from users import find_user, add_user

# ---------------- CONFIG ----------------
SECRET_KEY = "O3EzEGgNVVgv51N06sCucBHOG9mCP66dvkgMlKJVb2i"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 60

app = FastAPI(title="INLOG Auth Service")

# ---------------- MODELS ----------------
class LoginPayload(BaseModel):
    email: str
    password: str

class RegisterPayload(BaseModel):
    email: str
    password: str

# ---------------- JWT HELPERS ----------------
def create_token(user_id: int, email: str):
    payload = {
        "user_id": user_id,
        "email": email,
        "exp": datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None

# ---------------- PAGES ----------------
@app.get("/")
def index():
    return FileResponse("index.html")

@app.get("/auth")
def auth_page():
    return FileResponse("auth.html")

@app.get("/register")
def register_page():
    return FileResponse("register.html")

# ---------------- AUTH APIs ----------------

@app.post("/api/login")
def login(data: LoginPayload, response: Response):
    user = find_user(data.email)

    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(user["id"], user["email"])

    # ✅ HTTP-only cookie (industry standard)
    response.set_cookie(
        key="inlog_token",
        value=token,
        httponly=True,
        samesite="lax",
        max_age=TOKEN_EXPIRE_MINUTES * 60
    )

    return {
        "status": "authenticated",
        "provider": "INLOG",
        "user": {
            "user_id": user["id"],
            "email": user["email"]
        }
    }

@app.post("/api/register")
def register(data: RegisterPayload, response: Response):
    if find_user(data.email):
        raise HTTPException(status_code=400, detail="User already exists")

    user = add_user(data.email, data.password)
    token = create_token(user["id"], user["email"])

    response.set_cookie(
        key="inlog_token",
        value=token,
        httponly=True,
        samesite="lax",
        max_age=TOKEN_EXPIRE_MINUTES * 60
    )

    return {
        "status": "registered",
        "provider": "INLOG",
        "user": {
            "user_id": user["id"],
            "email": user["email"]
        }
    }

@app.post("/api/logout")
def logout(response: Response):
    response.delete_cookie("inlog_token")
    return {"status": "logged_out"}

@app.get("/api/me")
def me(request: Request):
    token = request.cookies.get("inlog_token")

    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {
        "user_id": payload["user_id"],
        "email": payload["email"]
    }
