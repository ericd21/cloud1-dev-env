# Cloud1 Dev Environment — Cloud‑Native Deployment Exercise
This project is a small but complete end‑to‑end exercise in cloud‑native application deployment. The application itself is intentionally simple; the focus is on utilizing a modern, reproducible workflow used in AI engineering, evaluation environments, and lightweight production deployments.
## 🌐 Project Overview
This repository shows how to:
- Develop inside a GitHub Codespaces virtual environment
- Provision cloud resources using Infrastructure‑as‑Code (IaC)
- Containerize an application using Docker
- Deploy a containerized service to a serverless cloud platform
 -Configure and manage deployment using Fly.io (`fly.toml`)
- Serve static pages and a small Python backend (`main.py`)
Even though the app is minimal, the workflow follows standard engineering practices used modern cloud deployment.
## 🧱 Tech Stack
- **Python** — lightweight backend built with FastAPI  (main.py)
- **Docker** — containerization
- **Fly.io** — serverless deployment
- **HCL / fly.toml** — infrastructure configuration
- **GitHub Codespaces** — cloud development environment
- **HTML / CSS / JavaScript** — static frontend pages
Languages used in the repo: Dockerfile, Python, JavaScript, HTML, CSS
## 🚀 Deployment Workflow

**1. Cloud Development Environment**
The project was developed entirely inside GitHub Codespaces, ensuring a reproducible, isolated environment without local setup.

**2. Containerization**
A custom `Dockerfile` defines the runtime environment and application dependencies.

**3. Infrastructure‑as‑Code**
The deployment is configured using Fly.io’s HCL-based `fly.toml`, enabling declarative provisioning of the serverless app.

**4. Serverless Deployment**
The container is deployed to Fly.io, where the platform handles scaling, networking, and runtime management.

**5. Static + Backend Integration**
Static pages interact with the Python backend, demonstrating a full-stack deployment pattern.

**6. CI/CD Automation**
A GitHub Actions workflow (`.github/workflows/`) automates the build and deployment process.

## 📁 Repository Structure
```
.devcontainer/     # Codespaces environment setup
.github/workflows/ # CI/CD for deployment
app/               # Backend code and static assets
Dockerfile         # Container definition
fly.toml           # Serverless deployment config
requirements.txt   # Python dependencies
```
## 🎯 Purpose of the Project
This project is designed as a hands-on demonstration of cloud deployment skills, not as a feature-rich application. It shows competency in:
- Cloud-native development
- Containerization
- Serverless deployment
- IaC configuration
- Reproducible engineering workflows
These skills are foundational to modern cloud-native engineering, DevOps workflows, and containerized application deployment.
## 👤 Author
Eric Dritsas
GitHub: https://github.com/ericd21
