"""
Document processing service for LangChain.
"""
from typing import List, Optional
import os

try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except ImportError:
    from langchain.text_splitter import RecursiveCharacterTextSplitter

try:
    from langchain_core.documents import Document
except ImportError:
    from langchain.schema import Document

from langchain_community.document_loaders import TextLoader, PyPDFLoader


class DocumentService:
    """Service for document processing and management."""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
    
    def load_text_file(self, file_path: str) -> List[Document]:
        """Load and split a text file."""
        try:
            loader = TextLoader(file_path)
            documents = loader.load()
            return self.text_splitter.split_documents(documents)
        except Exception as e:
            raise Exception(f"Error loading text file: {str(e)}")
    
    def load_pdf_file(self, file_path: str) -> List[Document]:
        """Load and split a PDF file."""
        try:
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            return self.text_splitter.split_documents(documents)
        except Exception as e:
            raise Exception(f"Error loading PDF file: {str(e)}")
    
    def process_text(self, text: str) -> List[Document]:
        """Process raw text into documents."""
        return self.text_splitter.create_documents([text])
    
    def process_multiple_texts(self, texts: List[str]) -> List[Document]:
        """Process multiple texts into documents."""
        return self.text_splitter.create_documents(texts)
