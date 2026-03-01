# 🧠 Adaptive AI Revision Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)
![PRs](https://img.shields.io/badge/PRs-Welcome-brightgreen)
![Contributions](https://img.shields.io/badge/Contributions-Open-blueviolet)

An intelligent AI-powered revision engine that personalizes learning using skill modeling, probabilistic mastery tracking, performance analytics, and adaptive question recommendation.

---

## 🚀 Overview

The **Adaptive AI Revision Platform** dynamically models student knowledge and continuously updates mastery levels based on:

- Accuracy trends
- Confidence scores
- Time-based forgetting
- Concept-level performance
- Adaptive difficulty scaling

Designed for scalable EdTech systems, coding practice platforms, and competitive exam preparation tools.

---

## 🏗️ Architecture

```
adaptive-backend/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── security.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── problem.py
│   │
│   └── student_model/
│       ├── skill_vector.py
│       ├── performance_metrics.py
│       ├── mastery_update.py
│       ├── forgetting_curve.py
│       └── analytics_generator.py
│
└── requirements.txt
```

---

## 🔥 Core Modules

### 🧠 Student Skill Vector (`skill_vector.py`)

Tracks per-student knowledge state including concept mastery (0–1), confidence score, attempt history, accuracy ratio, and time-based decay state.

### 📊 Performance Metrics Engine (`performance_metrics.py`)

Computes concept-level accuracy, recency-weighted performance, response time analytics, and confidence calibration.

### 📈 Mastery Update Engine (`mastery_update.py`)

Implements Bayesian Knowledge Tracing-inspired updates with confidence-weighted reinforcement and adaptive difficulty shifts.

### ⏳ Forgetting Curve Module (`forgetting_curve.py`)

Applies exponential decay to model memory retention over time:

$$\text{Retention} = e^{-\lambda t}$$

Where `λ` is the decay constant and `t` is time elapsed since last attempt.

### 📊 Analytics Generator (`analytics_generator.py`)

Produces weak-area detection, revision priority rankings, mastery heatmaps, and confidence progression trends.

---

## 🧩 Question Schema

```json
{
  "problem_statement": "Reverse a linked list recursively.",
  "concepts": ["Linked List", "Recursion"],
  "skills_tested": ["Pointer Manipulation", "Recursion Logic"],
  "difficulty": "Medium"
}
```

Supports multi-label classification, concept tagging, and difficulty adaptation.

---

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/Indronathbasu/adaptive-ai-revision.git
cd adaptive-ai-revision
```

**2. Create a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the server**

```bash
uvicorn app.main:app --reload
```

- API: `http://127.0.0.1:8000`
- Interactive Docs: `http://127.0.0.1:8000/docs`

---

## 📊 Adaptive Workflow

```
Student attempts question
        ↓
System evaluates response
        ↓
Performance metrics updated
        ↓
Mastery recalculated
        ↓
Forgetting decay applied
        ↓
Analytics refreshed
        ↓
Next best question recommended
```

---

## 🛡️ Security

- JWT Authentication
- Password hashing (bcrypt)
- Role-based access control
- Configurable rate limiting

---

## 📦 Tech Stack

| Layer | Technologies |
|-------|-------------|
| **Backend** | FastAPI, Pydantic, SQLAlchemy |
| **Database** | PostgreSQL / SQLite |
| **AI / ML** | NumPy, Pandas, Scikit-learn, PyTorch *(optional)* |

---

## 🧪 Testing

```bash
pytest
```

Test coverage includes mastery update validation, forgetting curve tests, skill vector consistency, and metric calculation integrity.

---

## 🎯 Target Applications

- Coding interview preparation platforms
- Competitive exam systems
- Adaptive school learning tools
- Corporate upskilling platforms
- AI-driven EdTech products

---

## 📌 Roadmap

- [ ] Deep Knowledge Tracing (LSTM-based)
- [ ] Reinforcement Learning policy for question selection
- [ ] Real-time dashboard visualization
- [ ] Gamified progress tracking
- [ ] AI-generated hints
- [ ] Full analytics web frontend

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Indronath Basu**  
AI/ML Developer | Adaptive Learning Systems  
Focused on intelligent student modeling & personalized AI education platforms
