# 🧠 Ekagra.ai
### Complete Enterprise Architecture & System Design

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A production-grade, horizontally scalable AI system for personalized learning — featuring real-time mastery tracking, forgetting curve modeling, ML-powered question recommendation, and full observability.

---

## 📌 Table of Contents

- [System Overview](#-system-overview)
- [Architecture](#-architecture)
- [Core Workflows](#-core-workflows)
- [ML System](#-ml-system)
- [Database Design](#-database-design)
- [Caching Strategy](#-caching-strategy)
- [Scaling Strategy](#-scaling-strategy)
- [Observability & Monitoring](#-observability--monitoring)
- [Failure Handling](#-failure-handling)
- [DevOps & Deployment](#-devops--deployment)
- [Why Enterprise-Ready](#-why-this-architecture-is-enterprise-ready)

---

## 🚀 System Overview

The Adaptive AI Learning Platform dynamically tracks what students know, what they're forgetting, and what they should study next. Core capabilities include:

- Per-concept mastery tracking with probabilistic updates
- Exponential forgetting curve applied over time
- Real-time adaptive question recommendation
- Live analytics dashboards
- Horizontal scaling via stateless backend
- ML model versioning & continuous retraining
- Docker / Kubernetes deployment support

---

## 🏗️ Architecture

```
                         ┌────────────────────────────┐
                         │         End Users          │
                         │   Web / Mobile Clients     │
                         └──────────────┬─────────────┘
                                        │ HTTPS
                                        ▼
                         ┌────────────────────────────┐
                         │   Nginx / Load Balancer    │
                         │  SSL Termination + Routing │
                         └──────────────┬─────────────┘
                                        │
                                        ▼
                         ┌────────────────────────────┐
                         │      React Frontend        │
                         │  UI + Charts + State Mgmt  │
                         └──────────────┬─────────────┘
                                        │ REST API + JWT
                                        ▼
  ┌─────────────────────────────────────────────────────────┐
  │                     FastAPI Backend                     │
  │  Auth · Questions · Attempts · Recommendations · Admin  │
  └──────────────┬──────────────────────────┬──────────────┘
                 │                          │
                 ▼                          ▼
  ┌──────────────────────────┐  ┌──────────────────────────┐
  │   ML Inference Service   │  │      PostgreSQL DB       │
  │  (PyTorch / Scikit-learn)│  │  Persistent Data Layer   │
  └──────────┬───────────────┘  └──────────┬───────────────┘
             │                             │
             ▼                             ▼
  ┌──────────────────────────┐  ┌──────────────────────────┐
  │     Model Registry       │  │       Redis Cache        │
  │     Versioned Models     │  │    (Optional Layer)      │
  └──────────────────────────┘  └──────────────────────────┘
```

---

## 📋 Core Workflows

### 1. User Authentication

Users submit credentials → backend validates bcrypt hash → JWT issued → all subsequent requests pass `Authorization: Bearer <token>`. Tokens include expiry, refresh support, and role-based validation.

### 2. Question Recommendation

On each request the backend fetches the student's skill vector, identifies weak concepts, applies forgetting priority, checks confidence instability, selects an appropriate difficulty level, and returns the optimal next question.

### 3. Answer Submission (Core Intelligence Loop)

This is the heart of the system. Each submission triggers a multi-step pipeline:

**A — Evaluate Answer:** Check correctness, measure response time, extract difficulty level.

**B — Update Performance Metrics:** Recalculate accuracy ratio, recency-weighted performance, and difficulty calibration.

**C — Update Mastery Score:**

```
NewMastery = OldMastery + LearningRate × (Correct − PredictedProbability) − DecayPenalty
```

**D — Apply Forgetting Curve:**

```
Retention = e^(−λt)
```

Decay is applied independently to both mastery score and confidence score.

**E — Update Confidence Score:** Derived from variance in recent attempts, streak consistency, difficulty stability, and time since last attempt.

**F — Persist to Database:** Writes to Attempts, Skill_Table, last_attempt_time, and confidence_score.

**G — Refresh Recommendation:** Recomputes weak topics, urgency index, difficulty adjustment, and learning momentum for the next question.

### 4. Analytics Pipeline

The analytics engine queries the database and computes concept mastery heatmaps, accuracy vs. difficulty graphs, mastery progression over time, confidence calibration charts, weak topic rankings, and retention risk analysis. Results are rendered on the React frontend as line charts, bar graphs, heatmaps, and trend visualizations.

---

## 🧠 ML System

### Real-Time Inference

Used for mastery updates, question classification, and difficulty adjustment. Target latency: **< 100ms**.

### Offline Training Pipeline

```
Data Collection → Feature Engineering → Model Training → Validation → Model Registry
```

Steps include extracting historical attempts, training a question classifier and mastery prediction model, validating accuracy, and saving each model with a version tag for deployment to the inference service.

### Model Versioning

Every model is stored with a version ID, accuracy score, timestamp, and training dataset hash. Full rollback is supported.

---

## 🗄️ Database Design

| Table | Key Columns |
|-------|-------------|
| `users` | id, name, email, password_hash, role |
| `questions` | id, statement, concepts, difficulty, tags |
| `attempts` | id, user_id, question_id, correct, response_time, timestamp |
| `skill_table` | user_id, concept, mastery_score, confidence_score, last_attempt_time |

Indexes are applied on `user_id`, `concept`, and `timestamp` for query performance.

---

## ⚡ Caching Strategy

Redis is used to cache frequently requested questions, precomputed dashboard analytics, session validation, and precomputed recommendations. Cache invalidation is handled via TTL and event-based invalidation on data writes.

---

## 🚀 Scaling Strategy

**Backend** — Stateless FastAPI instances sit behind a load balancer and scale horizontally with no shared state.

**ML** — For development, inference is embedded in the backend. In production, a dedicated ML cluster handles inference requests via a service pool.

**Database** — Scaled with read replicas, user_id-based partitioning, query indexing, and connection pooling.

---

## 🔍 Observability & Monitoring

Tracked metrics include API latency, ML inference latency, DB query time, error rate, memory usage, and CPU load.

Exposed at:
- `GET /health` — liveness check
- `GET /metrics` — Prometheus-compatible metrics endpoint

---

## 🛡️ Failure Handling

| Failure | Response |
|---------|----------|
| ML service down | Fallback to heuristic recommendation |
| DB slow / unavailable | Serve cached data + exponential backoff retry |
| Cache miss / failure | Direct DB query |

Circuit breaker pattern is applied across all external service calls.

---

## 🐳 DevOps & Deployment

### Development
Local Docker Compose stack with unit and integration tests.

### CI/CD Pipeline
```
Push to GitHub → Run tests → Build Docker image → Deploy to staging → Promote to production
```

### Production Options

**Option A — Docker Compose** (small scale): Single-host multi-container deployment.

**Option B — Kubernetes** (enterprise): Separate pods for backend and ML services, managed PostgreSQL, and Horizontal Pod Autoscaler for traffic-based scaling.

---

## 📈 End-to-End Data Flow

```
User Input → React Frontend → FastAPI Backend → Auth Layer
     → Business Logic → ML Inference → Database Update
     → Analytics Engine → Recommendation Engine → Dashboard
```

---

## ✅ Why This Architecture Is Enterprise-Ready

| Property | Implementation |
|----------|---------------|
| Scalability | Stateless backend + horizontal pod autoscaling |
| Intelligence | Separated ML inference service with versioned models |
| Performance | Redis caching + DB read replicas |
| Reliability | Circuit breakers + fallback heuristics |
| Security | JWT auth + bcrypt + RBAC |
| Observability | Health + metrics endpoints, latency tracking |
| Maintainability | Model versioning + rollback + CI/CD pipeline |

---

## 👨‍💻 Author

**Indronath Basu**  
AI/ML Engineer | Adaptive Intelligence Systems  
Focused on scalable personalized learning infrastructure
