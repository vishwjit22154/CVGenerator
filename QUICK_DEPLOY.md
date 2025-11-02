# ⚡ Quick Deploy Guide - 20 Minutes to Live!

Get your app live in 3 simple steps!

---

## 🎯 Recommended: Vercel + Railway (100% Free!)

---

## Step 1: Push to GitHub (5 minutes)

### A. Create GitHub Repository

1. Go to https://github.com/new
2. Name: `ai-cover-letter-generator`
3. Make it **Public** (for free deployment)
4. Don't initialize with README (we have code already)
5. Click "Create repository"

### B. Push Your Code

Open terminal and run:

```bash
cd "/Users/hvishwajit/resume project"

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "feat: AI Cover Letter Generator - Simple 2-input UI"

# Add GitHub remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/ai-cover-letter-generator.git

# Push
git branch -M main
git push -u origin main
```

✅ **Step 1 Complete!** Your code is on GitHub!

---

## Step 2: Deploy Backend to Railway (7 minutes)

### A. Sign Up

1. Go to https://railway.app
2. Click "Login with GitHub"
3. Authorize Railway

### B. Create New Project

1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Find and select `ai-cover-letter-generator`
4. Click "Deploy Now"

Railway will auto-detect Python and start building!

### C. Add Environment Variables

1. Click on your deployed service
2. Go to "Variables" tab
3. Click "New Variable" and add these:

```
ANTHROPIC_API_KEY=your_actual_claude_key
OPENAI_API_KEY=your_actual_openai_key
SECRET_KEY=generate-a-random-string-here
ENVIRONMENT=production
ALLOWED_ORIGINS=*
```

**Generate SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### D. Configure Start Command

1. Go to "Settings" tab
2. Find "Start Command"
3. Change to:
```
cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### E. Get Your Backend URL

1. Go to "Settings" → "Networking"
2. Click "Generate Domain"
3. Copy the URL (e.g., `your-app-production.up.railway.app`)
4. Save it - you'll need it for frontend!

✅ **Step 2 Complete!** Backend is live!

---

## Step 3: Deploy Frontend to Vercel (7 minutes)

### A. Sign Up

1. Go to https://vercel.com
2. Click "Sign Up"
3. Choose "Continue with GitHub"
4. Authorize Vercel

### B. Import Project

1. Click "Add New..." → "Project"
2. Find your `ai-cover-letter-generator` repo
3. Click "Import"

### C. Configure Build Settings

Vercel auto-detects Vite! But configure:

1. **Root Directory**: Click "Edit" and enter `frontend`
2. **Build Command**: `npm run build` (default)
3. **Output Directory**: `dist` (default)
4. **Install Command**: `npm install` (default)

### D. Add Environment Variable

1. Click "Environment Variables"
2. Add:
   - **Key**: `VITE_API_URL`
   - **Value**: `https://your-railway-url.railway.app/api`
   - (Replace with YOUR Railway URL from Step 2E)
3. Click "Add"

### E. Deploy!

1. Click "Deploy"
2. Wait 2-3 minutes for build
3. 🎉 Your app is live!
4. Copy the URL (e.g., `your-app.vercel.app`)

✅ **Step 3 Complete!** Frontend is live!

---

## Step 4: Update CORS (2 minutes)

Go back to Railway and update CORS:

1. Open Railway dashboard
2. Click your project
3. Go to "Variables"
4. Find `ALLOWED_ORIGINS`
5. Change from `*` to your Vercel URL:
   ```
   https://your-app.vercel.app
   ```
6. Service will auto-redeploy

✅ **All Done!** 🎉

---

## 🎊 Your App is LIVE!

**Frontend**: `https://your-app.vercel.app`  
**Backend**: `https://your-app.railway.app`  
**API Docs**: `https://your-app.railway.app/docs`

---

## 🧪 Test It!

1. Open your Vercel URL
2. Paste a sample resume
3. Paste a sample job posting
4. Click "Generate Cover Letter"
5. Watch the magic! ✨

---

## 📱 Share It!

### On LinkedIn:

```
🚀 Excited to share my latest project: AI Cover Letter Generator!

Built with FastAPI (Python), React, and Claude/ChatGPT APIs.
Just paste your resume and a job posting - AI does the rest!

Try it: https://your-app.vercel.app

Tech stack:
• FastAPI + Python
• React + Vite + Tailwind
• Claude & OpenAI APIs
• Deployed on Railway + Vercel
• CI/CD with GitHub Actions

#WebDevelopment #AI #Python #React #FullStack
```

### On Your Resume:

```
AI Cover Letter Generator | https://your-app.vercel.app
• Full-stack web application using FastAPI, React, and AI APIs
• Deployed to Railway and Vercel with CI/CD pipeline
• Processes [X] cover letter generations per day
```

---

## 🔧 Custom Domain (Optional)

### Buy a Domain:
- Namecheap: ~$10/year
- Google Domains: ~$12/year
- Cloudflare: ~$10/year

### Set Up:

**On Vercel:**
1. Project Settings → Domains
2. Add domain: `coverletter.yourname.com`
3. Follow DNS instructions
4. Automatic HTTPS!

**On Railway:**
1. Project Settings → Custom Domain
2. Add: `api.yourname.com`
3. Update DNS
4. Update `VITE_API_URL` on Vercel

---

## 📊 Monitor Your App

### Vercel Dashboard:
- Analytics (page views, performance)
- Logs (errors, warnings)
- Deployments (history, rollback)

### Railway Dashboard:
- Metrics (CPU, memory, requests)
- Logs (application logs)
- Usage (free tier limits)

### AI API Usage:
- Anthropic Console: https://console.anthropic.com
- OpenAI Dashboard: https://platform.openai.com/usage

---

## 🚨 Important Notes

### API Costs:
- Free tiers are LIMITED
- Monitor usage to avoid surprise bills
- Set spending limits on AI platforms

### Billing Alerts:
1. **Anthropic**: Console → Settings → Billing → Set alert at $10
2. **OpenAI**: Dashboard → Settings → Billing → Set limit at $10
3. **Railway**: Free tier is 500 hours/month ($5 credit)

### Rate Limiting (Future):
If you get a lot of users, add rate limiting to prevent abuse!

---

## 🐛 Troubleshooting

### Frontend shows "Failed to fetch"
- Check `VITE_API_URL` is correct
- Verify backend is running (visit Railway URL)
- Check CORS settings

### Backend won't start
- Check environment variables are set
- View logs in Railway dashboard
- Verify start command is correct

### API keys not working
- Double-check keys in Railway variables
- Make sure no extra spaces
- Restart service after adding keys

### Build fails
- Check build logs
- Verify all dependencies in `requirements.txt` and `package.json`
- Try deploying again (sometimes transient errors)

---

## ✅ Post-Deployment Checklist

- [ ] Both frontend and backend are live
- [ ] Can generate cover letters successfully
- [ ] All API providers work (Claude & ChatGPT)
- [ ] Export features work (PDF, DOCX, TXT)
- [ ] Mobile responsive (test on phone)
- [ ] CORS configured correctly
- [ ] API keys secured in environment variables
- [ ] Billing alerts set on AI platforms
- [ ] Added to portfolio/resume
- [ ] Shared on LinkedIn
- [ ] Monitoring dashboards bookmarked

---

## 🎉 Congratulations!

Your AI Cover Letter Generator is now live and accessible worldwide!

You've successfully:
- ✅ Built a full-stack AI application
- ✅ Deployed to production
- ✅ Set up CI/CD pipeline
- ✅ Configured custom domains (optional)
- ✅ Added a great project to your portfolio

**This is a real, production-grade application!** 🚀

---

## 📞 Need Help?

If you run into issues:

1. Check logs (Vercel + Railway dashboards)
2. Review `DEPLOYMENT_OPTIONS.md` for detailed guides
3. Check environment variables are correct
4. Verify API keys are valid
5. Test backend directly: `https://your-app.railway.app/docs`

---

**Ready to deploy? Let's do this!** 🚀

