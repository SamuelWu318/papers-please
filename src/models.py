from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass
class Paper:
    paper_id: str
    url: str
    title: str
    authors: List[Dict[str, str]]
    publication_date: Optional[str]
    citation_count: int

    chosen: bool
    linked: List[str] = field(default_factory=list)
    notes: Optional[str] = None

    @classmethod
    def build_from_semantic_scholar(cls, details: Dict[str, Any]) -> Paper:
        paper_id: str = details["paperId"]
        url: str = details.get("url") or f"https://www.semanticscholar.org/paper/{paper_id}"
        title: str = details.get("title") or "Untitled"
        authors: List[Dict[str, str]] = [
            {
                "id": author.get("authorId", "none"),
                "url": author.get("url", f"https://www.semanticscholar.org/author/{author['authorId']}"),
                "name": author.get("name", "Unknown")
            }  
            for author in details.get("authors") or []
        ]
        publication_date=details.get("publicationDate") or str(y) if (y := details.get("year")) is not None else None
        citation_count = c if (c := details.get("citationCount")) is not None else -1

        return cls(
            paper_id=paper_id, url=url, title=title,
            authors=authors, publication_date=publication_date,
            citation_count=citation_count, chosen=False
        )





