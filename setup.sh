#!/bin/bash

# AI Cover Letter Generator - Quick Setup Script
# This script automates the setup process for both backend and frontend

set -e  # Exit on error

echo "🚀 AI Cover Letter Generator - Quick Setup"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check prerequisites
echo "📋 Checking prerequisites..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is not installed. Please install Python 3.9 or higher.${NC}"
    exit 1
else
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1-2)
    echo -e "${GREEN}✅ Python $PYTHON_VERSION found${NC}"
fi

# Check Node.js
if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Node.js is not installed. Please install Node.js 16 or higher.${NC}"
    exit 1
else
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✅ Node.js $NODE_VERSION found${NC}"
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo -e "${RED}❌ npm is not installed.${NC}"
    exit 1
else
    NPM_VERSION=$(npm --version)
    echo -e "${GREEN}✅ npm $NPM_VERSION found${NC}"
fi

echo ""
echo "📦 Setting up backend..."
echo "------------------------"

# Backend setup
cd backend

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
    echo -e "${GREEN}✅ Virtual environment created${NC}"
else
    echo -e "${YELLOW}⚠️  Virtual environment already exists${NC}"
fi

# Activate virtual environment
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt
echo -e "${GREEN}✅ Python dependencies installed${NC}"

# Setup .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo ""
    echo -e "${YELLOW}⚠️  No .env file found. Creating from template...${NC}"
    cp .env.example .env
    echo -e "${GREEN}✅ .env file created${NC}"
    echo ""
    echo -e "${YELLOW}🔑 IMPORTANT: Please edit backend/.env and add your API keys:${NC}"
    echo "   - ANTHROPIC_API_KEY (for Claude)"
    echo "   - OPENAI_API_KEY (for ChatGPT)"
    echo ""
    read -p "Press Enter once you've added your API keys..."
else
    echo -e "${GREEN}✅ .env file already exists${NC}"
fi

cd ..

echo ""
echo "🎨 Setting up frontend..."
echo "------------------------"

# Frontend setup
cd frontend

# Install Node dependencies
echo "Installing Node.js dependencies (this may take a few minutes)..."
npm install
echo -e "${GREEN}✅ Node.js dependencies installed${NC}"

cd ..

echo ""
echo -e "${GREEN}=========================================="
echo "✅ Setup Complete!"
echo "==========================================${NC}"
echo ""
echo "📚 Next steps:"
echo ""
echo "1. Start the backend (in one terminal):"
echo "   ${GREEN}cd backend${NC}"
echo "   ${GREEN}source venv/bin/activate${NC}  # On Windows: venv\\Scripts\\activate"
echo "   ${GREEN}uvicorn app.main:app --reload${NC}"
echo ""
echo "2. Start the frontend (in another terminal):"
echo "   ${GREEN}cd frontend${NC}"
echo "   ${GREEN}npm run dev${NC}"
echo ""
echo "3. Open your browser:"
echo "   Frontend: ${GREEN}http://localhost:5173${NC}"
echo "   API Docs: ${GREEN}http://localhost:8000/docs${NC}"
echo ""
echo "📖 For detailed instructions, see SETUP_GUIDE.md"
echo "🎯 For interview preparation, see INTERVIEW_PREP.md"
echo "🚀 For deployment options, see DEPLOYMENT.md"
echo ""
echo "Happy coding! 🎉"

