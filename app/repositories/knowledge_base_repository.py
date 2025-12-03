"""
Repository for knowledge base operations.
"""
from typing import List, Optional
from app.models import KnowledgeBase, Document
from django.contrib.auth.models import User


class KnowledgeBaseRepository:
    """Repository for managing knowledge base data."""
    
    @staticmethod
    def create_knowledge_base(name: str, kb_id: str, description: str = "", 
                            user: Optional[User] = None) -> KnowledgeBase:
        """Create a new knowledge base."""
        return KnowledgeBase.objects.create(
            name=name,
            kb_id=kb_id,
            description=description,
            created_by=user
        )
    
    @staticmethod
    def get_knowledge_base(kb_id: str) -> Optional[KnowledgeBase]:
        """Get a knowledge base by ID."""
        try:
            return KnowledgeBase.objects.get(kb_id=kb_id, is_active=True)
        except KnowledgeBase.DoesNotExist:
            return None
    
    @staticmethod
    def list_knowledge_bases(user: Optional[User] = None) -> List[KnowledgeBase]:
        """List all active knowledge bases."""
        if user:
            return list(KnowledgeBase.objects.filter(created_by=user, is_active=True))
        return list(KnowledgeBase.objects.filter(is_active=True))
    
    @staticmethod
    def add_document(kb: KnowledgeBase, title: str, content: str, 
                    file_type: str, file_path: str = "") -> Document:
        """Add a document to a knowledge base."""
        return Document.objects.create(
            knowledge_base=kb,
            title=title,
            content=content,
            file_type=file_type,
            file_path=file_path
        )
    
    @staticmethod
    def get_kb_documents(kb_id: str) -> List[Document]:
        """Get all documents for a knowledge base."""
        try:
            kb = KnowledgeBase.objects.get(kb_id=kb_id)
            return list(kb.documents.all())
        except KnowledgeBase.DoesNotExist:
            return []
    
    @staticmethod
    def delete_knowledge_base(kb_id: str) -> bool:
        """Soft delete a knowledge base."""
        try:
            kb = KnowledgeBase.objects.get(kb_id=kb_id)
            kb.is_active = False
            kb.save()
            return True
        except KnowledgeBase.DoesNotExist:
            return False
