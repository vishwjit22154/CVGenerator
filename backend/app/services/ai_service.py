import anthropic
import openai
from typing import Optional
import time
from ..config import settings
from ..models import CoverLetterRequest, AIProvider, TemplateStyle, ToneStyle


class AIService:
    """Service for interacting with AI providers."""
    
    def __init__(self):
        self.anthropic_client = None
        self.openai_client = None
        
        if settings.anthropic_api_key:
            self.anthropic_client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
        
        if settings.openai_api_key:
            self.openai_client = openai.OpenAI(api_key=settings.openai_api_key)
    
    def _build_prompt(self, request: CoverLetterRequest) -> str:
        """Build the prompt for AI generation - Smart extraction mode."""
        
        template_instructions = {
            TemplateStyle.PROFESSIONAL: "Use a traditional, formal business letter format. Be concise and professional.",
            TemplateStyle.CREATIVE: "Use an engaging, personality-driven approach. Show enthusiasm and creativity.",
            TemplateStyle.TECHNICAL: "Focus heavily on technical skills, projects, and problem-solving abilities.",
            TemplateStyle.EXECUTIVE: "Write at a C-suite level, focusing on leadership, strategy, and business impact."
        }
        
        tone_instructions = {
            ToneStyle.FORMAL: "Maintain a strictly formal and professional tone throughout.",
            ToneStyle.CONVERSATIONAL: "Use a friendly, conversational tone while remaining professional.",
            ToneStyle.ENTHUSIASTIC: "Express genuine enthusiasm and passion for the role and company.",
            ToneStyle.CONFIDENT: "Project strong confidence in abilities and achievements."
        }
        
        notes_section = f"ADDITIONAL NOTES:\n{request.additional_notes}\n" if request.additional_notes else ""
        
        prompt = f"""You are an expert career advisor and professional writer. Generate a compelling cover letter by analyzing the resume and job description provided.

RESUME/CV:
{request.resume_text}

JOB POSTING:
{request.job_description}

{notes_section}

STYLE REQUIREMENTS:
- Template Style: {request.template_style.value}
  {template_instructions[request.template_style]}
- Tone: {request.tone.value}
  {tone_instructions[request.tone]}
- Target Length: Approximately {request.word_count} words

INSTRUCTIONS:
1. ANALYZE the job posting to extract:
   - Company name
   - Position title
   - Key requirements and qualifications
   - Important keywords

2. ANALYZE the resume to extract:
   - Applicant's name
   - Contact information (email, phone if available)
   - Relevant experience and achievements
   - Key skills that match the job
   - Education and certifications

3. GENERATE a complete, well-structured cover letter that:
   - Includes proper letter formatting (date, greeting with company name, body paragraphs, professional closing with applicant's name)
   - Addresses the specific company and position
   - Highlights relevant experience from the resume that matches job requirements
   - Uses specific examples and achievements from the resume
   - Incorporates keywords from the job description naturally
   - Shows enthusiasm for the role and company
   - Demonstrates clear understanding of both the role and the candidate's qualifications
   - Flows naturally and is engaging to read
   - Feels authentic and personalized

4. ENSURE the letter:
   - Opens with the correct date and company address format
   - Uses "Dear Hiring Manager" or "Dear [Company] Team" as greeting
   - Has 3-4 body paragraphs with clear structure
   - Closes professionally with the applicant's name and contact info

Generate ONLY the cover letter content in proper business letter format. No additional explanations or meta-commentary."""

        return prompt
    
    async def generate_with_claude(self, request: CoverLetterRequest) -> tuple[str, float]:
        """Generate cover letter using Claude API."""
        
        if not self.anthropic_client:
            raise ValueError("Claude API key not configured")
        
        start_time = time.time()
        prompt = self._build_prompt(request)
        
        try:
            message = self.anthropic_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                temperature=0.7,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            
            cover_letter = message.content[0].text
            generation_time = time.time() - start_time
            
            return cover_letter, generation_time
            
        except Exception as e:
            raise Exception(f"Claude API error: {str(e)}")
    
    async def generate_with_openai(self, request: CoverLetterRequest) -> tuple[str, float]:
        """Generate cover letter using OpenAI API."""
        
        if not self.openai_client:
            raise ValueError("OpenAI API key not configured")
        
        start_time = time.time()
        prompt = self._build_prompt(request)
        
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert career counselor and professional writer specializing in creating compelling cover letters."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            cover_letter = response.choices[0].message.content
            generation_time = time.time() - start_time
            
            return cover_letter, generation_time
            
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
    
    async def generate_cover_letter(self, request: CoverLetterRequest) -> tuple[str, float, str]:
        """Generate cover letter using specified AI provider."""
        
        if request.ai_provider == AIProvider.CLAUDE:
            cover_letter, gen_time = await self.generate_with_claude(request)
            provider_used = "claude"
        elif request.ai_provider == AIProvider.OPENAI:
            cover_letter, gen_time = await self.generate_with_openai(request)
            provider_used = "openai"
        else:
            raise ValueError(f"Unsupported AI provider: {request.ai_provider}")
        
        return cover_letter, gen_time, provider_used
    
    def check_provider_status(self, provider: AIProvider) -> bool:
        """Check if an AI provider is configured and available."""
        
        if provider == AIProvider.CLAUDE:
            return self.anthropic_client is not None
        elif provider == AIProvider.OPENAI:
            return self.openai_client is not None
        return False


# Singleton instance
ai_service = AIService()

