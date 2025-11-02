# 📁 Project Structure

Complete overview of the project file organization and architecture.

---

## 🗂️ Directory Structure

```
resume-project/
│
├── backend/                          # FastAPI Python backend
│   ├── app/
│   │   ├── __init__.py              # Package initialization
│   │   ├── main.py                  # FastAPI application entry point
│   │   ├── config.py                # Configuration and settings
│   │   ├── models.py                # Pydantic data models
│   │   │
│   │   ├── api/                     # API endpoints
│   │   │   ├── __init__.py
│   │   │   └── routes.py            # REST API routes
│   │   │
│   │   ├── services/                # Business logic layer
│   │   │   ├── __init__.py
│   │   │   ├── ai_service.py        # AI provider integration
│   │   │   └── export_service.py    # File export functionality
│   │   │
│   │   └── utils/                   # Utility functions
│   │       ├── __init__.py
│   │       └── keyword_matcher.py   # Keyword extraction/matching
│   │
│   ├── requirements.txt             # Python dependencies
│   ├── .env.example                 # Environment variables template
│   └── .gitignore                   # Git ignore rules
│
├── frontend/                         # React frontend application
│   ├── src/
│   │   ├── components/              # React components
│   │   │   ├── Header.jsx           # App header
│   │   │   ├── Features.jsx         # Feature showcase
│   │   │   ├── CoverLetterForm.jsx  # Main input form
│   │   │   └── CoverLetterPreview.jsx # Results display
│   │   │
│   │   ├── services/                # API integration
│   │   │   └── api.js               # Axios API client
│   │   │
│   │   ├── App.jsx                  # Root component
│   │   ├── main.jsx                 # Application entry point
│   │   └── index.css                # Global styles + Tailwind
│   │
│   ├── public/                      # Static assets
│   ├── index.html                   # HTML template
│   ├── package.json                 # Node.js dependencies
│   ├── vite.config.js               # Vite configuration
│   ├── tailwind.config.js           # Tailwind CSS configuration
│   ├── postcss.config.js            # PostCSS configuration
│   └── .gitignore                   # Git ignore rules
│
├── README.md                         # Project overview
├── SETUP_GUIDE.md                   # Detailed setup instructions
├── FEATURES.md                      # Feature documentation
├── DEPLOYMENT.md                    # Deployment guide
├── INTERVIEW_PREP.md                # Interview preparation
├── PROJECT_STRUCTURE.md             # This file
└── setup.sh                         # Quick setup script

```

---

## 🔍 File Descriptions

### Backend Files

#### `app/main.py` (Entry Point)
**Purpose**: FastAPI application setup and configuration
- Creates FastAPI app instance
- Configures CORS middleware
- Includes API routers
- Global exception handlers
- Root endpoint with API info

**Key Code**:
```python
app = FastAPI(title="AI Cover Letter Generator", ...)
app.add_middleware(CORSMiddleware, ...)
app.include_router(router, prefix="/api")
```

---

#### `app/config.py` (Configuration)
**Purpose**: Centralized configuration management
- Environment variable loading
- Settings validation with Pydantic
- Default values
- Type hints for all settings

**Key Settings**:
- `anthropic_api_key`: Claude API key
- `openai_api_key`: ChatGPT API key
- `secret_key`: Application secret
- `allowed_origins`: CORS origins list

---

#### `app/models.py` (Data Models)
**Purpose**: Define request/response data structures

**Models**:
1. **CoverLetterRequest**: Input data for generation
   - Job information (title, company, description)
   - Personal information (name, email, phone)
   - Experience and skills
   - Customization options

2. **CoverLetterResponse**: Generation result
   - Generated letter text
   - Word count
   - AI provider used
   - Generation time
   - Matched keywords

3. **ExportRequest**: Export parameters
4. **HealthResponse**: Health check data
5. **Enums**: AIProvider, TemplateStyle, ToneStyle, ExportFormat

---

#### `app/api/routes.py` (API Endpoints)
**Purpose**: HTTP endpoint definitions

**Endpoints**:

1. **GET /api/health**
   - Returns API status
   - Shows available AI providers
   
2. **POST /api/generate**
   - Generates cover letter
   - Validates input
   - Returns letter + metadata
   
3. **POST /api/export**
   - Exports letter to file
   - Supports multiple formats
   - Returns downloadable file
   
4. **POST /api/analyze-keywords**
   - Analyzes keyword matches
   - Returns match score

---

#### `app/services/ai_service.py` (AI Integration)
**Purpose**: AI provider integration and management

**Key Methods**:
- `_build_prompt()`: Constructs AI prompt
- `generate_with_claude()`: Claude API call
- `generate_with_openai()`: OpenAI API call
- `generate_cover_letter()`: Main entry point
- `check_provider_status()`: Availability check

**Features**:
- Template-based prompt construction
- Tone and style instructions
- Context injection
- Error handling
- Performance timing

---

#### `app/services/export_service.py` (Export)
**Purpose**: File generation in multiple formats

**Key Methods**:
- `export_as_txt()`: Plain text
- `export_as_markdown()`: Markdown format
- `export_as_docx()`: Word document
- `export_as_pdf()`: PDF with formatting
- `export_cover_letter()`: Main entry point

**Libraries Used**:
- **ReportLab**: PDF generation
- **python-docx**: Word documents
- **io.BytesIO**: In-memory file handling

---

#### `app/utils/keyword_matcher.py` (NLP)
**Purpose**: Keyword extraction and matching

**Key Methods**:
- `extract_keywords()`: General keywords
- `extract_technical_terms()`: Technical vocabulary
- `match_keywords()`: Find matches
- `calculate_keyword_score()`: Match percentage

**Techniques**:
- Stop word filtering
- Regex pattern matching
- Technical term recognition
- Set operations for matching

---

### Frontend Files

#### `src/App.jsx` (Root Component)
**Purpose**: Main application component
- State management (generated letter, form data)
- Conditional rendering (form vs preview)
- Layout structure
- Toast notification container

**State**:
- `generatedLetter`: AI-generated result
- `formData`: User's input data

---

#### `src/components/Header.jsx`
**Purpose**: Application header
- Branding
- Logo with icon
- Tagline
- Responsive design

---

#### `src/components/Features.jsx`
**Purpose**: Feature showcase cards
- Grid layout
- Icon + title + description
- Hover effects
- Marketing content

---

#### `src/components/CoverLetterForm.jsx`
**Purpose**: Main input form
- 3 sections: Job Info, Personal Info, Customization
- Form validation with react-hook-form
- Loading states
- Error handling
- Submit button with animation

**Form Fields**:
- Job title, company, description
- Name, email, phone
- Experience, skills
- AI provider, template, tone, word count

---

#### `src/components/CoverLetterPreview.jsx`
**Purpose**: Display generated letter
- Statistics dashboard
- Keyword tags
- Letter display area
- Copy to clipboard
- Export buttons (PDF, DOCX, TXT)
- Reset button

**Features**:
- File download handling
- Toast notifications
- Responsive grid layout

---

#### `src/services/api.js` (API Client)
**Purpose**: Backend communication
- Axios instance configuration
- API endpoint methods
- Error handling
- File download handling

**Methods**:
- `checkHealth()`: Health check
- `generateCoverLetter()`: Generate request
- `exportCoverLetter()`: Export request
- `analyzeKeywords()`: Keyword analysis

---

#### `src/index.css` (Styles)
**Purpose**: Global styles and Tailwind setup
- Tailwind directives
- Custom CSS classes
- Utility components
- Animations
- Custom scrollbar

**Custom Classes**:
- `.input-field`: Styled inputs
- `.btn-primary`: Primary buttons
- `.btn-secondary`: Secondary buttons
- `.card`: Card containers
- `.label`: Form labels

---

## 🎯 Key Architectural Patterns

### 1. **Service Layer Pattern**
```
Routes (HTTP) → Services (Logic) → External APIs
```
- Clear separation of concerns
- Easy to test
- Reusable business logic

### 2. **Component Composition**
```
App → Header + Features + Form + Preview
```
- Small, focused components
- Props-based communication
- Conditional rendering

### 3. **Configuration Management**
```
Environment Variables → Settings Class → Application
```
- Centralized config
- Type-safe settings
- Easy environment switching

### 4. **Error Handling Hierarchy**
```
Global Handler → Route Handler → Service Handler
```
- Multiple levels of protection
- User-friendly messages
- Detailed logging

---

## 🔄 Data Flow

### Generation Flow
```
1. User fills form (CoverLetterForm)
2. Form validation (react-hook-form)
3. API call (api.js)
4. Backend receives (routes.py)
5. Service processes (ai_service.py)
6. AI API call (Claude/OpenAI)
7. Keyword matching (keyword_matcher.py)
8. Response formatted (models.py)
9. Frontend receives (api.js)
10. Preview renders (CoverLetterPreview)
```

### Export Flow
```
1. User clicks export button
2. API call with format (api.js)
3. Backend receives (routes.py)
4. Export service generates (export_service.py)
5. File streamed to client
6. Browser downloads file
```

---

## 📦 Dependencies

### Backend (Python)
```
fastapi==0.109.0          # Web framework
uvicorn[standard]==0.27.0 # ASGI server
anthropic==0.18.0         # Claude API
openai==1.12.0            # ChatGPT API
pydantic==2.6.0           # Data validation
python-docx==1.1.0        # Word documents
reportlab==4.0.9          # PDF generation
```

### Frontend (JavaScript)
```
react==^18.2.0            # UI library
react-dom==^18.2.0        # React DOM
axios==^1.6.5             # HTTP client
lucide-react==^0.312.0    # Icons
react-hook-form==^7.49.3  # Form handling
react-hot-toast==^2.4.1   # Notifications
vite==^5.0.11             # Build tool
tailwindcss==^3.4.1       # CSS framework
```

---

## 🧪 Testing Strategy (Future)

### Backend Tests
```
tests/
├── test_api/
│   ├── test_routes.py        # Endpoint tests
│   └── test_models.py        # Model validation
├── test_services/
│   ├── test_ai_service.py    # AI integration (mocked)
│   └── test_export_service.py # Export functions
└── test_utils/
    └── test_keyword_matcher.py # Keyword algorithms
```

### Frontend Tests
```
src/tests/
├── components/
│   ├── Header.test.jsx
│   ├── Features.test.jsx
│   ├── CoverLetterForm.test.jsx
│   └── CoverLetterPreview.test.jsx
└── services/
    └── api.test.js
```

---

## 🔐 Security Considerations

### Backend
- ✅ Environment variables for secrets
- ✅ CORS configuration
- ✅ Input validation (Pydantic)
- ✅ Error message sanitization
- 🔄 Rate limiting (ready to add)
- 🔄 Authentication (ready to add)

### Frontend
- ✅ XSS protection (React escaping)
- ✅ HTTPS in production
- ✅ No secrets in code
- ✅ Input validation
- 🔄 CSP headers (deployment)

---

## 📈 Performance Optimization

### Backend
- ✅ Async/await operations
- ✅ Streaming file downloads
- 🔄 Redis caching (future)
- 🔄 Request pooling (future)

### Frontend
- ✅ Code splitting (Vite)
- ✅ Tree shaking
- ✅ CSS purging (Tailwind)
- 🔄 Lazy loading (future)
- 🔄 Service worker (future)

---

This structure provides a solid foundation for a scalable, maintainable application! 🚀

