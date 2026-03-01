"""Helper utility functions."""

from typing import Any, Dict, List
from datetime import datetime


def format_timestamp(dt: datetime) -> str:
    """Format datetime to ISO string."""
    return dt.isoformat()


def paginate(items: List[Any], page: int = 1, page_size: int = 10) -> Dict:
    """
    Paginate a list of items.
    
    Args:
        items: List of items to paginate
        page: Page number (1-indexed)
        page_size: Number of items per page
    
    Returns:
        dict with keys: items, total, page, page_size, pages
    """
    total = len(items)
    pages = (total + page_size - 1) // page_size
    start = (page - 1) * page_size
    end = start + page_size
    
    return {
        "items": items[start:end],
        "total": total,
        "page": page,
        "page_size": page_size,
        "pages": pages
    }


def calculate_success_rate(solved: int, attempted: int) -> float:
    """Calculate success rate percentage."""
    if attempted == 0:
        return 0.0
    return round((solved / attempted) * 100, 2)


def get_difficulty_weight(difficulty: str) -> int:
    """Get weight for difficulty level."""
    weights = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3
    }
    return weights.get(difficulty, 0)


def calculate_elapsed_time(start_time: datetime, end_time: datetime) -> int:
    """Calculate elapsed time in seconds."""
    delta = end_time - start_time
    return int(delta.total_seconds())
