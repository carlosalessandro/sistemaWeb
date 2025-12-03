"""
AI Controller for managing AI-related operations.
"""
from typing import Dict, Any, List, Optional
from app.services.langchain_service import LangChainService
from app.services.document_service import DocumentService


class AIController:
    """Controller for AI operations."""
    
    def __init__(self):
        self.langchain_service = LangChainService()
        self.document_service = DocumentService()
        self.vector_stores = {}
    
    def process_chat_message(self, message: str, session_id: str = "default") -> Dict[str, Any]:
        """Process a chat message and return response."""
        try:
            result = self.langchain_service.generate_response(message)
            return {
                "success": True,
                "response": result,
                "session_id": session_id
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "session_id": session_id
            }
    
    def create_knowledge_base(self, documents: List[str], kb_id: str) -> Dict[str, Any]:
        """Create a knowledge base from documents."""
        try:
            vector_store = self.langchain_service.create_vector_store(documents)
            self.vector_stores[kb_id] = vector_store
            return {
                "success": True,
                "message": f"Knowledge base '{kb_id}' created successfully",
                "kb_id": kb_id
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def query_knowledge_base(self, query: str, kb_id: str) -> Dict[str, Any]:
        """Query a knowledge base."""
        try:
            if kb_id not in self.vector_stores:
                return {
                    "success": False,
                    "error": f"Knowledge base '{kb_id}' not found"
                }
            
            vector_store = self.vector_stores[kb_id]
            qa_chain = self.langchain_service.create_qa_chain(vector_store)
            result = qa_chain({"question": query})
            
            return {
                "success": True,
                "answer": result["answer"],
                "sources": [doc.page_content for doc in result.get("source_documents", [])]
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def process_document(self, file_path: str, file_type: str = "txt") -> Dict[str, Any]:
        """Process a document file."""
        try:
            if file_type == "txt":
                documents = self.document_service.load_text_file(file_path)
            elif file_type == "pdf":
                documents = self.document_service.load_pdf_file(file_path)
            else:
                return {
                    "success": False,
                    "error": f"Unsupported file type: {file_type}"
                }
            
            return {
                "success": True,
                "documents": documents,
                "count": len(documents)
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
