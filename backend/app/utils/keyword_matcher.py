import re
from typing import List, Set


class KeywordMatcher:
    """Utility for matching keywords between job description and cover letter."""
    
    # Common words to exclude from keyword matching
    STOP_WORDS = {
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
        'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
        'to', 'was', 'will', 'with', 'we', 'you', 'your', 'this', 'they',
        'have', 'has', 'had', 'been', 'being', 'do', 'does', 'did', 'can',
        'could', 'would', 'should', 'may', 'might', 'must', 'shall'
    }
    
    @staticmethod
    def extract_keywords(text: str, min_length: int = 3) -> Set[str]:
        """Extract keywords from text."""
        
        # Convert to lowercase and extract words
        words = re.findall(r'\b[a-z]+\b', text.lower())
        
        # Filter out stop words and short words
        keywords = {
            word for word in words
            if len(word) >= min_length and word not in KeywordMatcher.STOP_WORDS
        }
        
        return keywords
    
    @staticmethod
    def extract_technical_terms(text: str) -> Set[str]:
        """Extract technical terms, abbreviations, and multi-word phrases."""
        
        terms = set()
        
        # Extract abbreviations and acronyms (2-6 uppercase letters)
        acronyms = re.findall(r'\b[A-Z]{2,6}\b', text)
        terms.update(acronyms)
        
        # Extract camelCase and PascalCase terms
        camel_case = re.findall(r'\b[a-z]+[A-Z][a-zA-Z]*\b', text)
        terms.update(camel_case)
        
        # Extract hyphenated terms
        hyphenated = re.findall(r'\b[a-zA-Z]+-[a-zA-Z]+\b', text)
        terms.update(hyphenated)
        
        # Extract version numbers
        versions = re.findall(r'\b[a-zA-Z]+\s*\d+(?:\.\d+)*\b', text)
        terms.update(versions)
        
        return terms
    
    @classmethod
    def match_keywords(cls, job_description: str, cover_letter: str) -> List[str]:
        """
        Find keywords from job description that appear in cover letter.
        Returns list of matched keywords sorted by importance.
        """
        
        # Extract keywords from both texts
        job_keywords = cls.extract_keywords(job_description)
        job_technical = cls.extract_technical_terms(job_description)
        
        letter_keywords = cls.extract_keywords(cover_letter)
        letter_technical = cls.extract_technical_terms(cover_letter)
        
        # Find matches
        matched_keywords = job_keywords & letter_keywords
        matched_technical = job_technical & letter_technical
        
        # Combine and prioritize technical terms
        all_matches = list(matched_technical) + list(matched_keywords - matched_technical)
        
        # Return unique matches, limited to top 20
        return all_matches[:20]
    
    @classmethod
    def calculate_keyword_score(cls, job_description: str, cover_letter: str) -> float:
        """
        Calculate a keyword match score (0-100).
        Higher score means better keyword optimization.
        """
        
        job_keywords = cls.extract_keywords(job_description)
        job_technical = cls.extract_technical_terms(job_description)
        
        letter_keywords = cls.extract_keywords(cover_letter)
        letter_technical = cls.extract_technical_terms(cover_letter)
        
        # Calculate match percentages
        if not job_keywords and not job_technical:
            return 0.0
        
        keyword_matches = len(job_keywords & letter_keywords)
        technical_matches = len(job_technical & letter_technical)
        
        total_job_terms = len(job_keywords) + len(job_technical)
        total_matches = keyword_matches + (technical_matches * 2)  # Weight technical terms higher
        
        score = (total_matches / total_job_terms) * 100
        
        return min(score, 100.0)  # Cap at 100


# Singleton instance
keyword_matcher = KeywordMatcher()

