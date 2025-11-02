import io
from docx import Document
from docx.shared import Pt, Inches
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT
import markdown
from ..models import ExportFormat


class ExportService:
    """Service for exporting cover letters in various formats."""
    
    @staticmethod
    def export_as_txt(content: str) -> bytes:
        """Export as plain text."""
        return content.encode('utf-8')
    
    @staticmethod
    def export_as_markdown(content: str) -> bytes:
        """Export as markdown."""
        return content.encode('utf-8')
    
    @staticmethod
    def export_as_docx(content: str, applicant_name: str) -> bytes:
        """Export as Microsoft Word document."""
        
        doc = Document()
        
        # Set margins
        sections = doc.sections
        for section in sections:
            section.top_margin = Inches(1)
            section.bottom_margin = Inches(1)
            section.left_margin = Inches(1)
            section.right_margin = Inches(1)
        
        # Split content into paragraphs
        paragraphs = content.split('\n\n')
        
        for para_text in paragraphs:
            if para_text.strip():
                paragraph = doc.add_paragraph(para_text.strip())
                
                # Style the paragraph
                paragraph_format = paragraph.paragraph_format
                paragraph_format.line_spacing = 1.15
                paragraph_format.space_after = Pt(10)
                
                # Set font
                for run in paragraph.runs:
                    run.font.name = 'Calibri'
                    run.font.size = Pt(11)
        
        # Save to bytes
        doc_bytes = io.BytesIO()
        doc.save(doc_bytes)
        doc_bytes.seek(0)
        
        return doc_bytes.getvalue()
    
    @staticmethod
    def export_as_pdf(content: str, applicant_name: str) -> bytes:
        """Export as PDF document."""
        
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        
        # Create styles
        styles = getSampleStyleSheet()
        style_normal = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=11,
            leading=14,
            alignment=TA_LEFT,
            spaceAfter=12
        )
        
        # Build the PDF
        story = []
        
        # Split content into paragraphs
        paragraphs = content.split('\n\n')
        
        for para_text in paragraphs:
            if para_text.strip():
                # Replace single newlines with <br/> for proper formatting
                para_text = para_text.replace('\n', '<br/>')
                para = Paragraph(para_text, style_normal)
                story.append(para)
                story.append(Spacer(1, 0.1 * inch))
        
        doc.build(story)
        buffer.seek(0)
        
        return buffer.getvalue()
    
    def export_cover_letter(
        self,
        content: str,
        format: ExportFormat,
        applicant_name: str,
        company_name: str
    ) -> tuple[bytes, str]:
        """
        Export cover letter in specified format.
        Returns (file_content, filename)
        """
        
        # Sanitize filename components
        safe_name = "".join(c for c in applicant_name if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_company = "".join(c for c in company_name if c.isalnum() or c in (' ', '-', '_')).strip()
        
        base_filename = f"CoverLetter_{safe_name}_{safe_company}"
        
        if format == ExportFormat.TXT:
            content_bytes = self.export_as_txt(content)
            filename = f"{base_filename}.txt"
        
        elif format == ExportFormat.MARKDOWN:
            content_bytes = self.export_as_markdown(content)
            filename = f"{base_filename}.md"
        
        elif format == ExportFormat.DOCX:
            content_bytes = self.export_as_docx(content, applicant_name)
            filename = f"{base_filename}.docx"
        
        elif format == ExportFormat.PDF:
            content_bytes = self.export_as_pdf(content, applicant_name)
            filename = f"{base_filename}.pdf"
        
        else:
            raise ValueError(f"Unsupported export format: {format}")
        
        return content_bytes, filename


# Singleton instance
export_service = ExportService()

