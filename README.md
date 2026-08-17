# Presales Learning: GitHub CI/CD Pipeline

A complete CI/CD pipeline demonstrating:
- Automated testing
- Container vulnerability scanning
- Automated deployment to Google Cloud Run
- GitHub Actions orchestration

## Pipeline Flow

```
Code Push → Tests → Build Container → Security Scan → Deploy to Production
```

## What This Shows

1. **Testing** — Every push runs automated tests
2. **Scanning** — Container images scanned for vulnerabilities (Trivy)
3. **Building** — Docker image built and pushed to Artifact Registry
4. **Deployment** — Automatically deployed to Cloud Run on main branch

## Local Testing

```bash
pip install -r requirements.txt
pytest test_app.py
python app.py  # runs on localhost:8080
```

## GitHub Actions Secrets Required

Set these in GitHub repo settings → Secrets and variables:
- `GCP_SA_KEY` — GCP service account JSON key
- `GCP_PROJECT_ID` — Your GCP project ID

## How to Use This for Presales

Show customers:
- "Every code change is tested automatically"
- "We scan for security vulnerabilities before deployment"
- "Deployment is fully automated—no manual steps, no human error"
