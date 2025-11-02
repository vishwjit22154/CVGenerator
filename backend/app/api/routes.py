from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import StreamingResponse
import io
from ..models import (
    CoverLetterRequest,
    CoverLetterResponse,
    ExportRequest,
    ExportFormat,
    HealthResponse,
    AIProvider
)
from ..services.ai_service import ai_service
from ..services.export_service import export_service
from ..utils.keyword_matcher import keyword_matcher
from ..config import settings

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Check API health and provider status."""
    
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        ai_providers={
            "claude": ai_service.check_provider_status(AIProvider.CLAUDE),
            "openai": ai_service.check_provider_status(AIProvider.OPENAI)
        }
    )


@router.post("/generate", response_model=CoverLetterResponse)
async def generate_cover_letter(request: CoverLetterRequest):
    """
    Generate a cover letter based on job description and applicant information.
    
    This endpoint uses AI (Claude or ChatGPT) to create a personalized,
    professionally formatted cover letter.
    """
    
    try:
        # Generate the cover letter
        cover_letter, gen_time, provider_used = await ai_service.generate_cover_letter(request)
        
        # Count words
        word_count = len(cover_letter.split())
        
        # Find matched keywords
        matched_keywords = keyword_matcher.match_keywords(
            request.job_description,
            cover_letter
        )
        
        return CoverLetterResponse(
            cover_letter=cover_letter,
            word_count=word_count,
            ai_provider_used=provider_used,
            generation_time=round(gen_time, 2),
            matched_keywords=matched_keywords
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating cover letter: {str(e)}")


@router.post("/export")
async def export_cover_letter(request: ExportRequest):
    """
    Export a cover letter in the specified format (PDF, DOCX, TXT, Markdown).
    
    Returns the file as a downloadable attachment.
    """
    
    try:
        # Generate export file
        file_content, filename = export_service.export_cover_letter(
            content=request.cover_letter,
            format=request.format,
            applicant_name=request.applicant_name,
            company_name=request.company_name
        )
        
        # Determine media type
        media_types = {
            ExportFormat.PDF: "application/pdf",
            ExportFormat.DOCX: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            ExportFormat.TXT: "text/plain",
            ExportFormat.MARKDOWN: "text/markdown"
        }
        
        media_type = media_types.get(request.format, "application/octet-stream")
        
        # Return file as streaming response
        return StreamingResponse(
            io.BytesIO(file_content),
            media_type=media_type,
            headers={
                "Content-Disposition": f"attachment; filename={filename}"
            }
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error exporting cover letter: {str(e)}")


@router.post("/analyze-keywords")
async def analyze_keywords(
    job_description: str,
    cover_letter: str
):
    """
    Analyze keyword matching between job description and cover letter.
    
    Returns matched keywords and an optimization score.
    """
    
    try:
        matched_keywords = keyword_matcher.match_keywords(job_description, cover_letter)
        score = keyword_matcher.calculate_keyword_score(job_description, cover_letter)
        
        return {
            "matched_keywords": matched_keywords,
            "match_score": round(score, 1),
            "total_matches": len(matched_keywords)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing keywords: {str(e)}")

