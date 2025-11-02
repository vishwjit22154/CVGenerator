# ⚡ Quick Reference Guide

One-page reference for common commands and configurations.

---

## 🚀 Quick Start

### Automatic Setup (Recommended)
```bash
./setup.sh
```

### Manual Setup

**Backend:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

---

## 🔑 Environment Variables

### Backend `.env` (required)
```env
ANTHROPIC_API_KEY=sk-ant-your-key-here
OPENAI_API_KEY=sk-your-key-here
SECRET_KEY=your-random-secret-key
ENVIRONMENT=development
ALLOWED_ORIGINS=http://localhost:5173
```

### Frontend `.env` (optional)
```env
VITE_API_URL=http://localhost:8000/api
```

---

## 🌐 URLs

| Service | URL | Description |
|---------|-----|-------------|
| Frontend | http://localhost:5173 | React application |
| Backend | http://localhost:8000 | API server |
| API Docs | http://localhost:8000/docs | Swagger UI |
| Alt Docs | http://localhost:8000/redoc | ReDoc |
| Health | http://localhost:8000/api/health | Health check |

---

## 📝 Common Commands

### Backend

```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Run development server
uvicorn app.main:app --reload

# Run on different port
uvicorn app.main:app --reload --port 8001

# Install new package
pip install package-name
pip freeze > requirements.txt

# Deactivate virtual environment
deactivate
```

### Frontend

```bash
# Run development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Install new package
npm install package-name

# Run linter
npm run lint
```

---

## 🔧 API Endpoints

### Generate Cover Letter
```bash
POST /api/generate
Content-Type: application/json

{
  "job_title": "Software Engineer",
  "company_name": "TechCorp",
  "job_description": "...",
  "applicant_name": "John Doe",
  "applicant_email": "john@example.com",
  "relevant_experience": "...",
  "key_skills": "...",
  "ai_provider": "claude",
  "template_style": "professional",
  "tone": "formal",
  "word_count": 300
}
```

### Export Cover Letter
```bash
POST /api/export
Content-Type: application/json

{
  "cover_letter": "...",
  "format": "pdf",
  "applicant_name": "John Doe",
  "company_name": "TechCorp"
}
```

### Health Check
```bash
GET /api/health
```

---

## 📦 Project Structure

```
resume-project/
├── backend/           # FastAPI backend
│   ├── app/
│   │   ├── api/      # Routes
│   │   ├── services/ # Business logic
│   │   ├── models.py # Data models
│   │   └── config.py # Settings
│   └── requirements.txt
│
└── frontend/         # React frontend
    ├── src/
    │   ├── components/
    │   ├── services/
    │   └── App.jsx
    └── package.json
```

---

## 🎨 Customization Options

### Template Styles
- `professional` - Traditional business format
- `creative` - Engaging, personality-driven
- `technical` - Focus on technical skills
- `executive` - C-suite level

### Tones
- `formal` - Strictly professional
- `conversational` - Friendly but professional
- `enthusiastic` - Show passion
- `confident` - Strong self-assurance

### AI Providers
- `claude` - Anthropic Claude 3.5 Sonnet
- `openai` - OpenAI GPT-4 Turbo

### Export Formats
- `pdf` - Professional PDF document
- `docx` - Editable Word document
- `txt` - Plain text
- `markdown` - Markdown format

---

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check if virtual environment is activated
which python  # Should show venv path

# Check if dependencies are installed
pip list | grep fastapi

# Check if .env file exists and has API keys
cat .env
```

### Frontend won't start
```bash
# Check if node_modules exists
ls node_modules

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install

# Check for port conflicts
lsof -ti:5173  # Shows process on port 5173
```

### API key errors
```bash
# Verify API keys in .env
cat backend/.env | grep API_KEY

# Test health endpoint
curl http://localhost:8000/api/health
```

---

## 📊 File Sizes & Metrics

| Metric | Value |
|--------|-------|
| Total LOC | ~1,400 lines |
| Backend LOC | ~800 lines |
| Frontend LOC | ~600 lines |
| Dependencies | 25+ packages |
| API Endpoints | 4 endpoints |
| React Components | 5 components |

---

## 🔗 Useful Links

### Documentation
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [React Docs](https://react.dev/)
- [Anthropic API](https://docs.anthropic.com/)
- [OpenAI API](https://platform.openai.com/docs)
- [Tailwind CSS](https://tailwindcss.com/docs)

### API Providers
- [Anthropic Console](https://console.anthropic.com/)
- [OpenAI Platform](https://platform.openai.com/)

### Deployment
- [Vercel](https://vercel.com/)
- [Railway](https://railway.app/)
- [Heroku](https://heroku.com/)

---

## 💡 Tips & Tricks

### Get Better Results
1. Include resume text for better context
2. Write detailed experience descriptions
3. Use specific skills from job posting
4. Try both AI providers and compare
5. Experiment with different tones

### Development
```bash
# Backend hot reload is automatic with --reload
# Frontend hot reload is automatic with Vite

# View real-time logs
# Backend: Terminal output
# Frontend: Browser console (F12)

# Test API without frontend
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d @test_request.json
```

### Performance
```bash
# Backend response time: ~5-15 seconds (AI processing)
# Frontend load time: <1 second
# Export time: <2 seconds
```

---

## 🎯 Next Steps

1. ✅ Complete setup
2. ✅ Add API keys
3. ✅ Test locally
4. 📖 Read FEATURES.md
5. 🎤 Review INTERVIEW_PREP.md
6. 🚀 Deploy (see DEPLOYMENT.md)
7. 💼 Add to resume/portfolio

---

## 🆘 Getting Help

### Check Documentation
- `README.md` - Project overview
- `SETUP_GUIDE.md` - Detailed setup
- `FEATURES.md` - Feature documentation
- `DEPLOYMENT.md` - Deployment options
- `INTERVIEW_PREP.md` - Interview questions

### Common Issues
1. **Port already in use**: Change port in commands
2. **Module not found**: Activate venv, reinstall packages
3. **API errors**: Check API keys, try health endpoint
4. **CORS errors**: Check ALLOWED_ORIGINS setting

---

## 📈 Enhancement Ideas

- [ ] User authentication
- [ ] Save history to database
- [ ] A/B test multiple versions
- [ ] LinkedIn integration
- [ ] Email sending
- [ ] Browser extension
- [ ] Mobile app

---

**Quick Command Reference:**
```bash
# Start everything (two terminals)
Terminal 1: cd backend && source venv/bin/activate && uvicorn app.main:app --reload
Terminal 2: cd frontend && npm run dev
```

**Remember:** This is YOUR project. Customize, extend, and make it unique! 🚀

