import pytest
from app.utils.keyword_matcher import KeywordMatcher


def test_extract_keywords():
    """Test keyword extraction."""
    text = "Python developer with experience in FastAPI and React"
    keywords = KeywordMatcher.extract_keywords(text)
    
    assert isinstance(keywords, set)
    assert "python" in keywords
    assert "developer" in keywords
    assert "experience" in keywords
    # Stop words should be filtered
    assert "with" not in keywords
    assert "in" not in keywords


def test_extract_technical_terms():
    """Test technical term extraction."""
    text = "Experience with AWS, React 18, and Python3.9"
    terms = KeywordMatcher.extract_technical_terms(text)
    
    assert isinstance(terms, set)
    assert "AWS" in terms


def test_match_keywords():
    """Test keyword matching between two texts."""
    job_desc = "Looking for Python developer with FastAPI experience"
    cover_letter = "I am a Python developer with 5 years FastAPI experience"
    
    matched = KeywordMatcher.match_keywords(job_desc, cover_letter)
    
    assert isinstance(matched, list)
    assert "python" in matched or "Python" in matched
    assert "developer" in matched


def test_calculate_keyword_score():
    """Test keyword score calculation."""
    job_desc = "Python developer FastAPI React"
    cover_letter = "Python developer with FastAPI and React experience"
    
    score = KeywordMatcher.calculate_keyword_score(job_desc, cover_letter)
    
    assert isinstance(score, float)
    assert 0 <= score <= 100
    assert score > 50  # Should have good match

