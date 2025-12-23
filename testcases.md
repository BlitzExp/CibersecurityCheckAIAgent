# Test Stacks for Stack Security Risk Assessment Agent

This document contains realistic production stack examples used to stress-test the
Stack Security Risk Assessment Agent.

Each stack follows the same `stack.json` contract and represents common real-world
scenarios across backend, cloud, DevOps, security, and legacy systems.

---

## Test Case 1 — Enterprise Node.js Backend (API + Auth + Cache)

Context: Typical SaaS / fintech backend stack.

```json
{
  "project": "enterprise-api",
  "environment": "production",
  "language": "nodejs",
  "libraries": [
    { "name": "express", "version": "4.17.1" },
    { "name": "helmet", "version": "6.0.1" },
    { "name": "cors", "version": "2.8.5" },
    { "name": "jsonwebtoken", "version": "8.5.1" },
    { "name": "bcrypt", "version": "5.0.1" },
    { "name": "lodash", "version": "4.17.20" },
    { "name": "mongoose", "version": "6.8.0" },
    { "name": "redis", "version": "4.6.7" },
    { "name": "axios", "version": "0.27.2" }
  ]
}
```

---

## Test Case 2 — Python Microservices (FastAPI + Async)

Context: Cloud-native Python backend with async APIs.

```json
{
  "project": "python-microservices",
  "environment": "production",
  "language": "python",
  "libraries": [
    { "name": "fastapi", "version": "0.88.0" },
    { "name": "uvicorn", "version": "0.20.0" },
    { "name": "pydantic", "version": "1.10.2" },
    { "name": "sqlalchemy", "version": "1.4.44" },
    { "name": "psycopg2", "version": "2.9.5" },
    { "name": "requests", "version": "2.28.1" },
    { "name": "python-jose", "version": "3.3.0" },
    { "name": "cryptography", "version": "38.0.1" }
  ]
}
```

---

## Test Case 3 — Full-Stack Web Application (React + Node)

Context: Frontend + backend application with shared dependencies.

```json
{
  "project": "fullstack-webapp",
  "environment": "production",
  "language": "javascript",
  "libraries": [
    { "name": "react", "version": "18.2.0" },
    { "name": "react-dom", "version": "18.2.0" },
    { "name": "webpack", "version": "5.75.0" },
    { "name": "axios", "version": "0.27.2" },
    { "name": "express", "version": "4.17.1" },
    { "name": "jsonwebtoken", "version": "8.5.1" },
    { "name": "passport", "version": "0.6.0" },
    { "name": "lodash", "version": "4.17.20" }
  ]
}
```

---

## Test Case 4 — Cloud Native / DevOps Stack

Context: Infrastructure-heavy environment with critical components.

```json
{
  "project": "cloud-native-platform",
  "environment": "production",
  "language": "mixed",
  "libraries": [
    { "name": "docker", "version": "20.10.21" },
    { "name": "kubernetes", "version": "1.26.0" },
    { "name": "helm", "version": "3.10.3" },
    { "name": "nginx", "version": "1.23.3" },
    { "name": "openssl", "version": "1.1.1" },
    { "name": "prometheus", "version": "2.40.5" },
    { "name": "grafana", "version": "9.3.2" }
  ]
}
```

---

## Test Case 5 — Legacy High-Risk System

Context: Outdated production system with known vulnerable dependencies.

```json
{
  "project": "legacy-payment-system",
  "environment": "production",
  "language": "nodejs",
  "libraries": [
    { "name": "express", "version": "4.15.0" },
    { "name": "jsonwebtoken", "version": "7.4.3" },
    { "name": "lodash", "version": "4.17.15" },
    { "name": "moment", "version": "2.19.0" },
    { "name": "request", "version": "2.88.0" },
    { "name": "body-parser", "version": "1.18.3" }
  ]
}
```

---

## Test Case 6 — Security & Cryptography Intensive Stack

Context: Authentication and cryptography-focused service.

```json
{
  "project": "secure-auth-service",
  "environment": "production",
  "language": "nodejs",
  "libraries": [
    { "name": "jsonwebtoken", "version": "8.5.1" },
    { "name": "bcrypt", "version": "3.0.6" },
    { "name": "crypto-js", "version": "3.1.9-1" },
    { "name": "node-forge", "version": "0.10.0" },
    { "name": "uuid", "version": "3.3.2" }
  ]
}
```
---

Usage Notes:
- Each JSON block can be copied directly into `stack.json`
- Results may change over time as new CVEs are published

Disclaimer:
These stacks are synthetic test cases intended for educational and demonstration purposes only.
They do not represent actual deployed systems.