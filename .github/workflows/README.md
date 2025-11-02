# GitHub Actions CI/CD Pipelines

This directory contains automated workflows for continuous integration and deployment.

## 📋 Workflows

### 1. Backend CI (`backend-ci.yml`)
**Trigger**: Push/PR to `backend/` files

**Jobs**:
- **Lint & Test**: Flake8, Black, MyPy, Pytest
- **Security Scan**: Bandit, Safety
- **Docker Build**: Build and test Docker image

**Runs on**: Every push and pull request affecting backend

---

### 2. Frontend CI (`frontend-ci.yml`)
**Trigger**: Push/PR to `frontend/` files

**Jobs**:
- **Lint & Test**: ESLint, build verification
- **Lighthouse Audit**: Performance and accessibility
- **Docker Build**: Build frontend container

**Runs on**: Every push and pull request affecting frontend

---

### 3. Deploy Production (`deploy-production.yml`)
**Trigger**: Push to `main` branch or manual dispatch

**Jobs**:
- **Deploy Backend**: Railway or Heroku
- **Deploy Frontend**: Vercel or Netlify
- **Health Check**: Verify deployment
- **Notify**: Send deployment status

**Runs on**: Main branch commits (production)

---

### 4. Security Scanning (`security-scan.yml`)
**Trigger**: Weekly schedule (Mondays) + main branch pushes

**Jobs**:
- **Dependency Check**: Safety, npm audit
- **Code Scanning**: CodeQL analysis
- **Secret Scanning**: TruffleHog
- **Container Scanning**: Trivy

**Runs on**: Weekly schedule + on-demand

---

### 5. Code Quality (`code-quality.yml`)
**Trigger**: Pull requests

**Jobs**:
- **Backend Quality**: Flake8, Pylint, Radon complexity
- **Frontend Quality**: ESLint, complexity analysis, bundle size
- **PR Comment**: Post results

**Runs on**: All pull requests

---

## 🔐 Required Secrets

Configure these in GitHub Settings → Secrets and variables → Actions:

### For Backend Deployment
```
RAILWAY_TOKEN              # Railway CLI token
HEROKU_API_KEY            # Heroku API key
HEROKU_BACKEND_APP_NAME   # Heroku app name
HEROKU_EMAIL              # Heroku account email
BACKEND_URL               # Production backend URL
```

### For Frontend Deployment
```
VERCEL_TOKEN              # Vercel authentication token
VERCEL_ORG_ID            # Vercel organization ID
VERCEL_PROJECT_ID        # Vercel project ID
NETLIFY_AUTH_TOKEN       # Netlify auth token
NETLIFY_SITE_ID          # Netlify site ID
FRONTEND_URL             # Production frontend URL
```

### For Testing
```
ANTHROPIC_API_KEY_TEST   # Test Claude API key
OPENAI_API_KEY_TEST      # Test OpenAI API key
```

---

## 🚀 Setup Instructions

### 1. Enable GitHub Actions
1. Go to your repository
2. Click **Actions** tab
3. Enable workflows

### 2. Add Secrets
1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Add each secret from the list above

### 3. Configure Deployment

#### For Railway:
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login and get token
railway login
railway tokens

# Add RAILWAY_TOKEN to GitHub secrets
```

#### For Vercel:
```bash
# Install Vercel CLI
npm i -g vercel

# Link project
cd frontend
vercel link

# Get tokens
vercel --token  # Follow prompts

# Add to GitHub secrets:
# - VERCEL_TOKEN
# - VERCEL_ORG_ID (from .vercel/project.json)
# - VERCEL_PROJECT_ID (from .vercel/project.json)
```

---

## 📊 Workflow Status Badges

Add these to your README.md:

```markdown
![Backend CI](https://github.com/YOUR_USERNAME/YOUR_REPO/workflows/Backend%20CI/badge.svg)
![Frontend CI](https://github.com/YOUR_USERNAME/YOUR_REPO/workflows/Frontend%20CI/badge.svg)
![Deploy Production](https://github.com/YOUR_USERNAME/YOUR_REPO/workflows/Deploy%20to%20Production/badge.svg)
![Security](https://github.com/YOUR_USERNAME/YOUR_REPO/workflows/Security%20Scanning/badge.svg)
```

---

## 🔄 Workflow Diagram

```
┌─────────────────┐
│   Code Push     │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼───┐ ┌──▼────┐
│Backend│ │Frontend│
│  CI   │ │  CI   │
└───┬───┘ └──┬────┘
    │         │
    │    ┌────┴────┐
    │    │  Tests  │
    │    │ Passing?│
    │    └────┬────┘
    │         │ Yes
    └────┬────┘
         │
    ┌────▼────────┐
    │   Deploy    │
    │ Production  │
    └─────────────┘
```

---

## 🧪 Local Testing

Test workflows locally with [act](https://github.com/nektos/act):

```bash
# Install act
brew install act  # macOS
# or
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Run backend CI locally
act -j lint-and-test -W .github/workflows/backend-ci.yml

# Run frontend CI locally
act -j lint-and-test -W .github/workflows/frontend-ci.yml
```

---

## 📝 Customization

### Add New Job
```yaml
new-job:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - name: Your step
      run: echo "Hello"
```

### Add Environment
```yaml
jobs:
  deploy:
    environment: staging  # or production
    steps:
      - name: Deploy
        run: deploy-command
```

### Add Notification
```yaml
- name: Slack Notification
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

---

## 🎯 Best Practices

1. **Branch Protection**: Require CI to pass before merging
2. **Code Reviews**: Require approvals for production
3. **Secrets Rotation**: Update secrets regularly
4. **Cache Dependencies**: Speed up builds
5. **Parallel Jobs**: Run tests concurrently
6. **Fail Fast**: Stop on first failure

---

## 📈 Metrics to Track

- Build time
- Test coverage
- Deployment frequency
- Success rate
- Security vulnerabilities found
- Code quality scores

---

## 🆘 Troubleshooting

### Workflow fails on secrets
- Verify secrets are added correctly
- Check secret names match workflow file
- Ensure secrets have correct permissions

### Docker build fails
- Check Dockerfile syntax
- Verify base images are accessible
- Review build logs for errors

### Deployment fails
- Check deployment platform status
- Verify API tokens are valid
- Review deployment logs

---

## 📚 Resources

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Railway Docs](https://docs.railway.app/)
- [Vercel Docs](https://vercel.com/docs)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

---

**Your CI/CD pipeline is production-ready!** 🚀

