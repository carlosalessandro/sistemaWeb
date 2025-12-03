"""
Repository for chat-related database operations.
"""
from typing import List, Optional
from app.models import ChatSession, ChatMessage
from django.contrib.auth.models import User


class ChatRepository:
    """Repository for managing chat data."""
    
    @staticmethod
    def create_session(session_id: str, user: Optional[User] = None) -> ChatSession:
        """Create a new chat session."""
        return ChatSession.objects.create(
            session_id=session_id,
            user=user
        )
    
    @staticmethod
    def get_session(session_id: str) -> Optional[ChatSession]:
        """Get a chat session by ID."""
        try:
            return ChatSession.objects.get(session_id=session_id)
        except ChatSession.DoesNotExist:
            return None
    
    @staticmethod
    def get_or_create_session(session_id: str, user: Optional[User] = None) -> ChatSession:
        """Get or create a chat session."""
        session, created = ChatSession.objects.get_or_create(
            session_id=session_id,
            defaults={'user': user}
        )
        return session
    
    @staticmethod
    def save_message(session: ChatSession, role: str, content: str) -> ChatMessage:
        """Save a chat message."""
        return ChatMessage.objects.create(
            session=session,
            role=role,
            content=content
        )
    
    @staticmethod
    def get_session_messages(session_id: str) -> List[ChatMessage]:
        """Get all messages for a session."""
        try:
            session = ChatSession.objects.get(session_id=session_id)
            return list(session.messages.all())
        except ChatSession.DoesNotExist:
            return []
    
    @staticmethod
    def get_user_sessions(user: User) -> List[ChatSession]:
        """Get all sessions for a user."""
        return list(ChatSession.objects.filter(user=user))
