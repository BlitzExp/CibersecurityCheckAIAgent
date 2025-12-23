# Stack Security Report

_Generated on 2025-12-23T18:07:35.725417 UTC_

## Project Information

- **Project:** python-microservices
- **Environment:** production

## Summary

- Total libraries analyzed: 8
- 🔴 Insecure: 4
- 🟡 Doubtful: 3
- 🟢 Safe: 1

---

## Dependency Analysis

### 🔴 fastapi (0.88.0)

**Risk Level:** `INSECURE`  
**Reason:** High severity vulnerabilities detected in public CVE database  
**CVEs Found:** 5

#### ✅ Recommended Action

- Upgrade to a patched version or apply mitigations immediately

---

### 🟡 uvicorn (0.20.0)

**Risk Level:** `DOUBTFUL`  
**Reason:** Known vulnerabilities exist, but none rated as high severity  
**CVEs Found:** 3

#### ✅ Recommended Action

- Review CVEs and monitor for updates

---

### 🟡 pydantic (1.10.2)

**Risk Level:** `DOUBTFUL`  
**Reason:** Known vulnerabilities exist, but none rated as high severity  
**CVEs Found:** 3

#### ✅ Recommended Action

- Review CVEs and monitor for updates

---

### 🔴 sqlalchemy (1.4.44)

**Risk Level:** `INSECURE`  
**Reason:** High severity vulnerabilities detected in public CVE database  
**CVEs Found:** 5

#### ✅ Recommended Action

- Upgrade to a patched version or apply mitigations immediately

---

### 🟢 psycopg2 (2.9.5)

**Risk Level:** `SAFE`  
**Reason:** No known CVEs found in public databases  
**CVEs Found:** 0

#### ✅ Recommended Action

- Keep dependency updated

---

### 🟡 requests (2.28.1)

**Risk Level:** `DOUBTFUL`  
**Reason:** Known vulnerabilities exist, but none rated as high severity  
**CVEs Found:** 5

#### ✅ Recommended Action

- Review CVEs and monitor for updates

---

### 🔴 python-jose (3.3.0)

**Risk Level:** `INSECURE`  
**Reason:** High severity vulnerabilities detected in public CVE database  
**CVEs Found:** 5

#### ✅ Recommended Action

- Upgrade to a patched version or apply mitigations immediately

---

### 🔴 cryptography (38.0.1)

**Risk Level:** `INSECURE`  
**Reason:** High severity vulnerabilities detected in public CVE database  
**CVEs Found:** 5

#### ✅ Recommended Action

- Upgrade to a patched version or apply mitigations immediately

---
