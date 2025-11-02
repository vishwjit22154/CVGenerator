# 🚀 Complete Setup Guide

This guide will help you set up and run the AI Cover Letter Generator project.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9 or higher** - [Download Python](https://www.python.org/downloads/)
- **Node.js 16 or higher** - [Download Node.js](https://nodejs.org/)
- **pip** (Python package manager) - Usually comes with Python
- **npm** (Node package manager) - Comes with Node.js

### Getting API Keys

You'll need at least one AI provider API key:

#### Option 1: Claude (Anthropic) - Recommended
1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new API key
5. Copy and save the key securely

#### Option 2: ChatGPT (OpenAI)
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Go to API Keys section
4. Create a new secret key
5. Copy and save the key securely

---

## 🔧 Backend Setup

### Step 1: Navigate to Backend Directory

```bash
cd backend
```

### Step 2: Create Virtual Environment

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required Python packages including:
- FastAPI (web framework)
- Anthropic SDK (Claude API)
- OpenAI SDK (ChatGPT API)
- Uvicorn (ASGI server)
- And more...

### Step 4: Configure Environment Variables

1. Create a `.env` file in the `backend` directory:

```bash
touch .env  # macOS/Linux
# or
type nul > .env  # Windows
```

2. Open `.env` and add your API keys:

```env
# AI API Keys (add at least one)
ANTHROPIC_API_KEY=sk-ant-your-key-here
OPENAI_API_KEY=sk-your-key-here

# Application Settings
SECRET_KEY=your-random-secret-key-here
ENVIRONMENT=development

# CORS Settings
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

**Important:**
- Replace `sk-ant-your-key-here` with your actual Anthropic API key
- Replace `sk-your-key-here` with your actual OpenAI API key
- You can add just one API key if you prefer to use only one AI provider

### Step 5: Run the Backend Server

```bash
uvicorn app.main:app --reload
```

You should see output like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 6: Test the Backend

Open your browser and visit:
- API Documentation: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc
- Health Check: http://localhost:8000/api/health

You should see the interactive API documentation!

---

## 🎨 Frontend Setup

Open a **NEW terminal window** (keep the backend running).

### Step 1: Navigate to Frontend Directory

```bash
cd frontend
```

### Step 2: Install Dependencies

```bash
npm install
```

This will install all required packages including:
- React (UI library)
- Vite (build tool)
- Tailwind CSS (styling)
- Axios (HTTP client)
- And more...

This may take a few minutes.

### Step 3: Configure Environment (Optional)

If you're running the backend on a different port or host:

1. Create `.env` file in `frontend` directory:

```bash
touch .env
```

2. Add the API URL:

```env
VITE_API_URL=http://localhost:8000/api
```

### Step 4: Run the Frontend Development Server

```bash
npm run dev
```

You should see output like:
```
  VITE v5.0.11  ready in 500 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

### Step 5: Open the Application

Open your browser and visit: **http://localhost:5173**

You should see the AI Cover Letter Generator interface! 🎉

---

## ✅ Verification Checklist

Make sure everything is working:

- [ ] Backend server is running on port 8000
- [ ] Frontend server is running on port 5173
- [ ] You can access http://localhost:8000/docs
- [ ] You can access http://localhost:5173
- [ ] Health check shows your AI provider is configured
- [ ] No error messages in the terminal

---

## 🎯 Using the Application

### Step 1: Fill in Job Information
1. Enter the job title (e.g., "Senior Full Stack Developer")
2. Enter the company name
3. Paste the complete job description

### Step 2: Add Your Information
1. Enter your full name
2. Enter your email address
3. (Optional) Add phone number
4. Describe your relevant experience
5. List your key skills
6. (Optional) Paste your resume text for better context

### Step 3: Customize Your Letter
1. Choose AI provider (Claude or ChatGPT)
2. Select template style (Professional, Creative, Technical, or Executive)
3. Choose tone (Formal, Conversational, Enthusiastic, or Confident)
4. Set target word count (100-800 words)

### Step 4: Generate
Click "Generate Cover Letter" and wait for the AI to create your letter!

### Step 5: Export
Download your cover letter in PDF, DOCX, or TXT format.

---

## 🐛 Troubleshooting

### Backend Issues

**Error: "No module named 'fastapi'"**
- Make sure you activated the virtual environment
- Run `pip install -r requirements.txt` again

**Error: "Address already in use"**
- Port 8000 is already in use
- Stop other services or use a different port:
  ```bash
  uvicorn app.main:app --reload --port 8001
  ```

**Error: "API key not configured"**
- Check your `.env` file exists in the `backend` directory
- Verify the API key is correct and not expired
- Make sure there are no extra spaces in the `.env` file

### Frontend Issues

**Error: "Failed to fetch"**
- Make sure the backend server is running
- Check the backend URL in `.env` (if you created one)
- Verify no firewall is blocking the connection

**Blank page or errors in browser console**
- Check the browser console (F12) for errors
- Try clearing browser cache
- Make sure you ran `npm install`

**Port 5173 already in use**
- Another Vite server is running
- Stop it or Vite will automatically use the next available port

### API Provider Issues

**Error: "Invalid API key"**
- Double-check your API key in `.env`
- Make sure you copied the entire key
- Verify the key is active in the provider's console

**Error: "Rate limit exceeded"**
- You've exceeded your API quota
- Wait a moment and try again
- Check your usage in the provider's console

---

## 📝 Next Steps

1. **Customize the UI**: Edit files in `frontend/src/components/`
2. **Add features**: Extend the backend in `backend/app/api/routes.py`
3. **Deploy**: See `DEPLOYMENT.md` for production deployment guide
4. **Learn more**: Check out the API documentation at `/docs`

---

## 🆘 Getting Help

If you encounter issues:

1. Check the terminal output for error messages
2. Review this guide carefully
3. Check the main `README.md` for additional information
4. Verify all prerequisites are installed correctly

---

## 🎉 Success!

If everything is working, you now have a fully functional AI-powered cover letter generator! Start creating professional cover letters in seconds.

**Pro Tips:**
- Use the resume text field for better AI context
- Try different AI providers to compare results
- Experiment with different tones and templates
- Keep your API keys secure and never commit them to git

Happy job hunting! 🚀

