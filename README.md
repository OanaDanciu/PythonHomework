# 🧮 Math Microservice 

This project implements a production-ready Python microservice that allows users to perform common mathematical operations via a **REST API** 
(FastAPI) and a **CLI interface** (Click). It uses a modular **MVCS architecture**, stores every request in a local **SQLite** database, and 
includes features like **threaded execution**, **caching**, **logging**, **Docker support**, and optional **Redis pub/sub integration**.

---

## 🧠 How It Works (Project Summary)

### 🎯 Main Goal

To provide a fast, modular, extensible and containerized service that exposes endpoints and CLI commands for:

* `power(a, b)`
* `fibonacci(n)`
* `factorial(n)`
* `sum_digits(n)` *(added for extensibility demo)*

### 🔁 Flow (API & CLI)

1. User sends request (via CLI or API `/calculate`)
2. Input is validated via **Pydantic**
3. Math function is run **in a separate thread**
4. Result is returned to the client
5. Request is **logged** and **saved in SQLite DB**
6. (Optional) Request is **published to Redis** (Pub/Sub bonus)

### 🛠️ Example:

```bash
# CLI
python cli.py power 2 10
Result: 1024

# API (POST /calculate)
{
  "operation": "fibonacci",
  "inputs": [10]
}
→ "Result: 55"
```

### 🔍 Technologies Used

* **FastAPI** – API Layer
* **Click** – CLI commands
* **SQLite** – DB persistence
* **Pydantic** – Input validation
* **ThreadPoolExecutor** – Parallel computation
* **functools.lru\_cache** – Caching `fibonacci()`
* **Logging** – File and console logging
* **Docker** – Containerization
* **Redis** – Pub/Sub (Bonus)

---

## ✅ Features Checklist

| Feature                        | Status |
| ------------------------------ | ------ |
| FastAPI REST API               | ✅      |
| CLI with Click                 | ✅      |
| SQLite persistence             | ✅      |
| MVCS Architecture              | ✅      |
| Pydantic validation            | ✅      |
| Caching                        | ✅      |
| Logging                        | ✅      |
| Threaded Execution             | ✅      |
| Dockerfile                     | ✅      |
| docker-compose + Redis (bonus) | ✅      |
| `.gitignore`, `README`, etc.   | ✅      |

---

## 🏗️ How to Run

### 📦 Local (Dev)

```bash
# Activate env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run API
uvicorn main:app --reload
```

Access: [http://localhost:8000/docs](http://localhost:8000/docs)

### 🖥️ CLI Examples

```bash
python cli.py factorial 5
python cli.py sum_digits 1234
```

### 🐳 Docker

```bash
docker build -t math-service .
docker run -p 8000:8000 math-service
```

### 🐳 Docker Compose (with Redis)

```bash
docker compose up --build
```

---

## 📁 Project Structure

```
math/
├── .venv/                 # Virtual environment (excluded)
├── controller/            # Request routing logic
├── model/                 # Pydantic request models
├── service/               # Business logic (math functions)
├── storage/               # Database interaction (SQLite)
├── utils/                 # Logging, threading, pub/sub
├── .dockerignore          # Exclude build context noise
├── .flake8                # Linting config
├── cli.py                 # CLI entrypoint using Click
├── docker-compose.yml     # Multi-container setup (with Redis)
├── Dockerfile             # Docker image definition
├── main.py                # FastAPI application entrypoint
├── math_service.log       # Generated logs
├── README.md              # Project documentation
├── requests.db            # SQLite database
├── requirements.txt       # Dependency freeze

```

