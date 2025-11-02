from pydantic import BaseModel, Field
from typing import Optional, Literal
from enum import Enum


class AIProvider(str, Enum):
    """Available AI providers."""
    CLAUDE = "claude"
    OPENAI = "openai"


class TemplateStyle(str, Enum):
    """Cover letter template styles."""
    PROFESSIONAL = "professional"
    CREATIVE = "creative"
    TECHNICAL = "technical"
    EXECUTIVE = "executive"


class ToneStyle(str, Enum):
    """Tone options for cover letter."""
    FORMAL = "formal"
    CONVERSATIONAL = "conversational"
    ENTHUSIASTIC = "enthusiastic"
    CONFIDENT = "confident"


class CoverLetterRequest(BaseModel):
    """Request model for cover letter generation."""
    
    # Main Inputs - Only 2 required!
    resume_text: str = Field(..., description="Your complete resume/CV text")
    job_description: str = Field(..., description="Complete job posting (includes company, title, requirements)")
    
    # Optional - AI will auto-detect if not provided
    job_title: Optional[str] = Field(None, description="Position title (auto-detected if not provided)")
    company_name: Optional[str] = Field(None, description="Company name (auto-detected if not provided)")
    applicant_name: Optional[str] = Field(None, description="Applicant's full name (extracted from resume)")
    applicant_email: Optional[str] = Field(None, description="Applicant's email (extracted from resume)")
    applicant_phone: Optional[str] = Field(None, description="Phone number (extracted from resume)")
    relevant_experience: Optional[str] = Field(None, description="Relevant work experience (extracted from resume)")
    key_skills: Optional[str] = Field(None, description="Key skills (extracted from resume)")
    additional_notes: Optional[str] = Field(None, description="Additional information or requirements")
    
    # Customization
    ai_provider: AIProvider = Field(AIProvider.CLAUDE, description="AI provider to use")
    template_style: TemplateStyle = Field(TemplateStyle.PROFESSIONAL, description="Template style")
    tone: ToneStyle = Field(ToneStyle.FORMAL, description="Tone of the letter")
    word_count: Optional[int] = Field(300, description="Target word count", ge=100, le=800)
    
    class Config:
        json_schema_extra = {
            "example": {
                "resume_text": "John Doe\njohn.doe@email.com | (555) 123-4567\n\nEXPERIENCE\nSenior Software Engineer | Tech Company | 2020-Present\n- Led development of scalable web applications\n- Managed team of 3 developers\n\nSKILLS\nReact, TypeScript, FastAPI, PostgreSQL, AWS",
                "job_description": "Senior Full Stack Developer\nTechCorp Inc.\n\nWe are seeking a talented full stack developer with 5+ years of experience in React, Node.js, and Python. The ideal candidate will have experience with cloud technologies and leading development teams...",
                "ai_provider": "claude",
                "template_style": "professional",
                "tone": "formal",
                "word_count": 300
            }
        }


class CoverLetterResponse(BaseModel):
    """Response model for generated cover letter."""
    
    cover_letter: str = Field(..., description="Generated cover letter")
    word_count: int = Field(..., description="Actual word count")
    ai_provider_used: str = Field(..., description="AI provider that generated the letter")
    generation_time: float = Field(..., description="Time taken to generate (seconds)")
    matched_keywords: list[str] = Field(default_factory=list, description="Keywords matched from job description")


class ExportFormat(str, Enum):
    """Export format options."""
    PDF = "pdf"
    DOCX = "docx"
    TXT = "txt"
    MARKDOWN = "markdown"


class ExportRequest(BaseModel):
    """Request model for exporting cover letter."""
    
    cover_letter: str = Field(..., description="Cover letter content")
    format: ExportFormat = Field(..., description="Export format")
    applicant_name: str = Field(..., description="Applicant name for filename")
    company_name: str = Field(..., description="Company name for filename")


class HealthResponse(BaseModel):
    """Health check response."""
    
    status: str
    version: str
    ai_providers: dict[str, bool]

