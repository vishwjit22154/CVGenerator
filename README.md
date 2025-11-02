# AI Cover Letter Generator 🚀

A sophisticated full-stack application that generates personalized cover letters using AI (Claude & ChatGPT APIs). Built with FastAPI, React, and modern web technologies.

## ✨ Super Simple - Just 2 Inputs!

No complex forms to fill! Just paste your resume and the job posting - AI extracts everything automatically and generates a perfect cover letter in seconds.

## 🌟 Features

### Core Features
- **🎯 Ultra-Simple UI**: Only 2 inputs needed - resume and job posting!
- **🤖 Smart AI Extraction**: Automatically extracts company, role, your details
- **⚡ Instant Generation**: Professional cover letter in 10-15 seconds
- **🎨 Multi-AI Provider**: Choose between Claude (Anthropic) and ChatGPT (OpenAI)
- **🎭 4 Template Styles**: Professional, Creative, Technical, and Executive
- **🎵 4 Tone Options**: Formal, Conversational, Enthusiastic, Confident
- **📥 Multiple Export Formats**: PDF, DOCX, TXT with one click
- **🎯 Keyword Matching**: Automatically highlights matched keywords

### DevOps & CI/CD 🚀
- **GitHub Actions Pipelines**: Automated testing and deployment
- **Docker Support**: Full containerization for backend and frontend
- **Automated Testing**: pytest for backend, ready for frontend tests
- **Security Scanning**: Weekly vulnerability and secret scanning
- **Code Quality Checks**: Automated linting and complexity analysis
- **Multi-Environment Deploy**: Support for Railway, Vercel, Render, Netlify
- **One-Click Deploy**: Pre-configured for instant deployment

## 🏗️ Architecture

```
resume-project/
├── backend/              # FastAPI Python backend
│   ├── app/
│   │   ├── api/         # API endpoints
│   │   ├── services/    # AI service integrations
│   │   ├── models/      # Data models
│   │   └── utils/       # Utility functions
│   ├── requirements.txt
│   └── .env.example
├── frontend/            # React + Vite frontend
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── services/    # API client
│   │   ├── hooks/       # Custom React hooks
│   │   └── utils/       # Utility functions
│   └── package.json
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js 16+
- API keys for Claude and/or OpenAI

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your API keys

# Run the server
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:5173` to use the application!

## 🌐 Deploy to Production

Ready to make your app live? Choose your deployment method:

### ⚡ Quick Deploy (Recommended) - 20 Minutes
**Free tier available!**

See `QUICK_DEPLOY.md` for step-by-step guide.

**Best Option: Vercel + Railway**
1. Push code to GitHub
2. Deploy backend to Railway (Free tier)
3. Deploy frontend to Vercel (Free tier)
4. Done! 🎉

### 🚀 One-Click Deploy Options

#### Deploy Backend to Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template)

#### Deploy Frontend to Vercel
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone)

#### Deploy Full Stack to Render
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

### 📚 Deployment Guides

- `QUICK_DEPLOY.md` - 20-minute step-by-step guide
- `DEPLOYMENT_OPTIONS.md` - Detailed comparison of all options
- Pre-configured: `vercel.json`, `railway.json`, `render.yaml`

### 💰 Cost Estimate
- **Free Tier**: $0/month (Railway + Vercel free tiers)
- **Low Traffic**: ~$5-10/month + AI API costs
- **Production**: ~$20-50/month depending on usage

### 🌍 After Deployment
Your app will be live at:
- Frontend: `https://your-app.vercel.app`
- Backend API: `https://your-api.railway.app`
- API Docs: `https://your-api.railway.app/docs`

## 🔑 Environment Variables

Create a `.env` file in the `backend` directory:

```env
ANTHROPIC_API_KEY=your_claude_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY=your_secret_key_here
```

## 📖 Documentation

### Setup & Usage
- `GET_STARTED.md` - 15-minute quick start guide
- `SETUP_GUIDE.md` - Detailed setup with troubleshooting
- `QUICK_REFERENCE.md` - Command cheat sheet
- `SIMPLIFIED_VERSION.md` - How the 2-input UI works

### Deployment
- `QUICK_DEPLOY.md` - ⚡ 20-minute deployment guide
- `DEPLOYMENT_OPTIONS.md` - Detailed comparison of all platforms
- `DEPLOYMENT.md` - Production deployment best practices

### Technical Details
- `FEATURES.md` - Complete feature documentation
- `PROJECT_STRUCTURE.md` - Code organization guide
- `INTERVIEW_PREP.md` - Interview preparation & Q&A

### DevOps & CI/CD
- `CI_CD_GUIDE.md` - CI/CD pipeline documentation
- `.github/workflows/` - GitHub Actions configuration

### API Documentation
Once the backend is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🎯 Usage - Super Simple!

### Just 3 Steps:

1. **Paste Your Resume** - Copy your entire resume/CV into the first text box
2. **Paste Job Posting** - Copy the complete job posting into the second text box
3. **Click Generate** - AI does everything else!

### What AI Extracts Automatically:
- ✅ Your name, email, phone from resume
- ✅ Company name and job title from posting
- ✅ Your relevant experience and skills
- ✅ Job requirements and keywords
- ✅ Matches your experience to requirements

### Customize (Optional):
- Choose AI provider (Claude or ChatGPT)
- Select template style (Professional, Creative, Technical, Executive)
- Pick tone (Formal, Conversational, Enthusiastic, Confident)
- Adjust word count

### Export:
- Download as PDF, DOCX, or TXT with one click!

## 🛠️ Technologies Used

### Backend
- **FastAPI**: Modern, fast web framework
- **Python 3.9+**: Core language
- **Anthropic SDK**: Claude AI integration
- **OpenAI SDK**: ChatGPT integration
- **Pydantic**: Data validation
- **python-multipart**: File upload handling

### Frontend
- **React 18**: UI library
- **Vite**: Build tool
- **Tailwind CSS**: Styling
- **Axios**: HTTP client
- **React Query**: Data fetching
- **React Hook Form**: Form management
- **Lucide Icons**: Icon library

## 🎨 Features Showcase

### 1. AI Provider Selection
Toggle between Claude and ChatGPT to compare results and choose the best output.

### 2. Template System
- **Professional**: Traditional, formal tone
- **Creative**: Engaging, personality-driven
- **Technical**: Focus on technical skills
- **Executive**: C-suite level positioning

### 3. Tone Customization
- Formal
- Conversational
- Enthusiastic
- Confident

### 4. Export Formats
- PDF (professionally formatted)
- DOCX (editable Word document)
- Plain text (for email/forms)

## 🔒 Security

- API keys stored securely in environment variables
- Input validation on all endpoints
- Rate limiting implemented
- CORS configured for frontend security

## 🚀 CI/CD Pipeline

This project includes enterprise-grade CI/CD pipelines:

- **Backend CI**: Linting, testing, security scanning, Docker builds
- **Frontend CI**: ESLint, builds, Lighthouse audits
- **Auto Deployment**: Push to main → Deploy to production
- **Security Scans**: Weekly vulnerability checks
- **Code Quality**: Automated complexity and quality metrics

See `CI_CD_GUIDE.md` for complete documentation.

## 📈 Future Enhancements

- [ ] User authentication system
- [ ] Database integration for user profiles
- [ ] A/B testing for cover letter versions
- [ ] LinkedIn profile integration
- [ ] Multi-language support
- [ ] Browser extension
- [ ] Mobile app (React Native)

## 🤝 Contributing

This is a portfolio project, but suggestions are welcome!

## 📄 License

MIT License - feel free to use this for your own projects!

## 👤 Author

Built by **Hvishwajit** - Showcasing full-stack development, AI integration, and modern web practices.

---

**Star this project if you find it useful!** ⭐

