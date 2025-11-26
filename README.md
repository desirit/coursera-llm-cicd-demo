# LLM CI/CD Pipeline Demo

Automated deployment pipeline for LLM inference using:
- Docker containerization
- Trivy security scanning
- Blue-green deployment strategy
- GitHub Actions automation

## Pipeline Steps
1. Build Docker image with layer caching
2. Security scan with Trivy
3. Deploy to green environment
4. Health checks and validation
5. Traffic switch from blue to green
6. Rollback capability if needed
# Updated Wed Nov 26 04:36:01 EST 2025
