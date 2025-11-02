# 🚀 Deployment Guide

This guide covers various deployment options for the AI Cover Letter Generator.

---

## 📋 Pre-Deployment Checklist

Before deploying to production:

- [ ] Update `ENVIRONMENT=production` in backend `.env`
- [ ] Generate a secure `SECRET_KEY` (use `openssl rand -hex 32`)
- [ ] Update `ALLOWED_ORIGINS` with your production domain
- [ ] Test all features locally
- [ ] Review API rate limits with AI providers
- [ ] Set up monitoring and logging
- [ ] Prepare backup strategy for user data (if storing)

---

## 🌐 Deployment Options

### Option 1: Vercel (Frontend) + Railway (Backend)

**Best for**: Quick deployment with minimal configuration

#### Backend - Railway

1. **Create Railway Account**: Visit [Railway.app](https://railway.app)

2. **Create New Project**:
   ```bash
   # Install Railway CLI
   npm i -g @railway/cli
   
   # Login
   railway login
   
   # Initialize in backend directory
   cd backend
   railway init
   ```

3. **Add Environment Variables** in Railway dashboard:
   ```
   ANTHROPIC_API_KEY=your_key
   OPENAI_API_KEY=your_key
   SECRET_KEY=your_secret
   ENVIRONMENT=production
   ```

4. **Deploy**:
   ```bash
   railway up
   ```

5. **Get Backend URL**: Copy from Railway dashboard (e.g., `https://your-app.railway.app`)

#### Frontend - Vercel

1. **Create Vercel Account**: Visit [Vercel.com](https://vercel.com)

2. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

3. **Deploy from frontend directory**:
   ```bash
   cd frontend
   vercel
   ```

4. **Add Environment Variable**:
   - In Vercel dashboard, add `VITE_API_URL` with your Railway backend URL

5. **Redeploy**:
   ```bash
   vercel --prod
   ```

---

### Option 2: Heroku (Full Stack)

**Best for**: Traditional deployment approach

#### Backend

1. **Install Heroku CLI**: Download from [Heroku](https://devcenter.heroku.com/articles/heroku-cli)

2. **Create Heroku App**:
   ```bash
   cd backend
   heroku create your-app-name-api
   ```

3. **Add Procfile** in backend directory:
   ```
   web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

4. **Set Environment Variables**:
   ```bash
   heroku config:set ANTHROPIC_API_KEY=your_key
   heroku config:set OPENAI_API_KEY=your_key
   heroku config:set SECRET_KEY=your_secret
   heroku config:set ENVIRONMENT=production
   ```

5. **Deploy**:
   ```bash
   git init
   heroku git:remote -a your-app-name-api
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

#### Frontend

1. **Build the frontend**:
   ```bash
   cd frontend
   npm run build
   ```

2. **Deploy to Heroku**:
   ```bash
   heroku create your-app-name-frontend
   heroku buildpacks:set heroku/nodejs
   # Add static site buildpack
   heroku buildpacks:add https://github.com/heroku/heroku-buildpack-static
   ```

3. **Create `static.json`** in frontend directory:
   ```json
   {
     "root": "dist/",
     "routes": {
       "/**": "index.html"
     }
   }
   ```

4. **Deploy**:
   ```bash
   git push heroku main
   ```

---

### Option 3: Docker + AWS/GCP/Azure

**Best for**: Full control and scalability

#### Create Dockerfiles

**Backend Dockerfile** (`backend/Dockerfile`):
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Frontend Dockerfile** (`frontend/Dockerfile`):
```dockerfile
FROM node:18-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

**nginx.conf** (`frontend/nginx.conf`):
```nginx
server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

#### Docker Compose

**docker-compose.yml** (in root directory):
```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - SECRET_KEY=${SECRET_KEY}
      - ENVIRONMENT=production
    restart: unless-stopped

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend
    restart: unless-stopped
```

#### Deploy to AWS ECS

1. **Build and push to ECR**:
   ```bash
   aws ecr create-repository --repository-name cover-letter-generator
   docker build -t cover-letter-generator ./backend
   docker tag cover-letter-generator:latest YOUR_ECR_URI
   docker push YOUR_ECR_URI
   ```

2. **Create ECS Task Definition** and Service via AWS Console

3. **Configure Load Balancer** for HTTPS

---

### Option 4: DigitalOcean App Platform

**Best for**: Simplicity and cost-effectiveness

1. **Create DigitalOcean Account**: Visit [DigitalOcean](https://www.digitalocean.com)

2. **Create App**:
   - Connect your GitHub repository
   - Select "Split into components"
   - Configure backend (Python service)
   - Configure frontend (Static site)

3. **Set Environment Variables** in dashboard

4. **Deploy**: Automatic on git push

---

## 🔒 Security Considerations

### Production Checklist

1. **API Keys**:
   - Never commit to git
   - Use environment variables
   - Rotate regularly

2. **CORS**:
   - Restrict to specific origins
   - Update `ALLOWED_ORIGINS` in production

3. **Rate Limiting**:
   - Implement API rate limiting
   - Consider using Redis for distributed rate limiting

4. **HTTPS**:
   - Always use HTTPS in production
   - Configure SSL certificates

5. **Input Validation**:
   - Already implemented with Pydantic
   - Add additional sanitization for user inputs

6. **Monitoring**:
   - Set up error tracking (Sentry)
   - Monitor API usage and costs

---

## 📊 Performance Optimization

### Backend

1. **Caching**:
   ```python
   # Add Redis caching for repeated requests
   from fastapi_cache import FastAPICache
   from fastapi_cache.backends.redis import RedisBackend
   ```

2. **Database Connection Pooling** (if adding database):
   ```python
   from sqlalchemy.pool import QueuePool
   ```

3. **Async Everything**:
   - Already using async/await
   - Consider async database driver

### Frontend

1. **Code Splitting**:
   ```javascript
   // Lazy load components
   const CoverLetterPreview = lazy(() => import('./components/CoverLetterPreview'));
   ```

2. **Image Optimization**:
   - Use WebP format
   - Implement lazy loading

3. **CDN**:
   - Serve static assets from CDN
   - Vercel/Netlify include this automatically

---

## 💰 Cost Optimization

### AI API Costs

1. **Monitor Usage**:
   - Track API calls per user
   - Set up billing alerts

2. **Caching**:
   - Cache similar requests
   - Store generated letters temporarily

3. **Rate Limiting**:
   - Limit generations per user
   - Implement cooldown periods

### Infrastructure Costs

1. **Serverless Options**:
   - AWS Lambda + API Gateway
   - Vercel Serverless Functions

2. **Auto-scaling**:
   - Scale based on demand
   - Reduce resources during off-peak

---

## 🔍 Monitoring & Logging

### Error Tracking

```python
# Add Sentry
import sentry_sdk

sentry_sdk.init(
    dsn="your-sentry-dsn",
    traces_sample_rate=1.0
)
```

### Logging

```python
# Structured logging
import logging
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
```

### Metrics

- Track API response times
- Monitor AI provider latency
- Track success/error rates
- Monitor AI API costs

---

## 🔄 CI/CD Pipeline

### GitHub Actions Example

**.github/workflows/deploy.yml**:
```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Railway
        run: |
          npm i -g @railway/cli
          railway up
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}

  deploy-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Vercel
        run: |
          npm i -g vercel
          vercel --prod --token=${{ secrets.VERCEL_TOKEN }}
```

---

## 📱 Custom Domain Setup

### Backend (Railway/Heroku)

1. **Add custom domain** in platform dashboard
2. **Update DNS records**:
   ```
   Type: CNAME
   Name: api
   Value: your-app.railway.app
   ```

### Frontend (Vercel)

1. **Add domain** in Vercel dashboard
2. **Update nameservers** or add DNS records

---

## 🧪 Pre-Launch Testing

```bash
# Backend health check
curl https://api.yourdomain.com/api/health

# Frontend build test
cd frontend && npm run build

# Load testing (optional)
pip install locust
locust -f load_test.py
```

---

## 🎉 Post-Deployment

1. **Update README** with production URLs
2. **Share on portfolio** and LinkedIn
3. **Monitor for 24-48 hours**
4. **Gather user feedback**
5. **Plan next features**

---

## 📞 Support & Maintenance

### Regular Tasks

- [ ] Monitor API costs weekly
- [ ] Review error logs
- [ ] Update dependencies monthly
- [ ] Backup user data (if storing)
- [ ] Review security vulnerabilities
- [ ] Test new AI model versions

---

Your app is now ready for the world! 🚀

