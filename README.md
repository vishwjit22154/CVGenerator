# AI Cover Letter Generator 🚀

A full-stack application that generates personalized cover letters using AI (Claude & ChatGPT APIs). Built with FastAPI, React, and modern web technologies.

## ✨ Simple 2-Input Interface

Paste your resume and job posting - AI extracts company name, job title, and your details automatically to generate a professional cover letter.

<img width="1161" height="679" alt="Screenshot 2025-11-03 at 4 37 34 PM" src="https://github.com/user-attachments/assets/417b4c29-116e-425b-aaba-ce976fd817a5" />


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
- **GitHub Actions**: Automated testing and code quality checks
- **Docker Support**: Containerization configurations included
- **Automated Testing**: pytest test suite for backend
- **Security Scanning**: Vulnerability and secret scanning setup
- **Code Quality**: Automated linting and complexity analysis

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

## 🔑 Environment Variables

Create a `.env` file in the `backend` directory:

```env
ANTHROPIC_API_KEY=your_claude_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY=your_secret_key_here
```

## 📖 Documentation

### Setup & Usage
- `SETUP_GUIDE.md` - Detailed setup with troubleshooting
- `QUICK_REFERENCE.md` - Command cheat sheet

### Technical Details
- `FEATURES.md` - Complete feature documentation
- `PROJECT_STRUCTURE.md` - Code organization guide
- `CI_CD_GUIDE.md` - CI/CD pipeline documentation

### API Documentation
Once the backend is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

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

This project includes CI/CD pipeline configurations:

- **Backend CI**: Linting, testing, security scanning
- **Frontend CI**: ESLint, build verification
- **Security Scans**: Vulnerability checks
- **Code Quality**: Automated linting and quality metrics

See `CI_CD_GUIDE.md` for details.

## 📈 Current Status

✅ **Fully Functional Locally**
- Backend running on FastAPI
- Frontend running on React + Vite
- AI integration with Claude & ChatGPT working
- Export to PDF, DOCX, TXT functional
- All features tested and operational

## 🔮 Potential Future Enhancements

- User authentication system
- Database integration for user profiles
- Cover letter history and templates
- LinkedIn profile integration
- Multi-language support

## 🤝 Contributing

This is a portfolio project, but suggestions are welcome!

## 📄 License

MIT License - feel free to use this for your own projects!

## 👤 Author

Built by **Hvishwajit** - Showcasing full-stack development, AI integration, and modern web practices.

---

**Star this project if you find it useful!** ⭐

