"""
LangChain service for AI operations.
"""
from typing import List, Dict, Any, Optional
import os

try:
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
except ImportError:
    try:
        from langchain_community.chat_models import ChatOpenAI
        from langchain_community.embeddings import OpenAIEmbeddings
    except ImportError:
        raise ImportError(
            "Instale langchain-openai: pip install langchain-openai"
        )

try:
    from langchain_community.vectorstores import FAISS
except ImportError:
    raise ImportError(
        "Instale langchain-community: pip install langchain-community"
    )

try:
    from langchain.chains import ConversationalRetrievalChain, LLMChain
    from langchain.memory import ConversationBufferMemory
    from langchain.prompts import PromptTemplate
except ImportError:
    from langchain_classic.chains import ConversationalRetrievalChain, LLMChain
    from langchain_classic.memory import ConversationBufferMemory
    from langchain_classic.prompts import PromptTemplate

from langchain_text_splitters import RecursiveCharacterTextSplitter


class LangChainService:
    """Service for managing LangChain operations."""
    
    def __init__(self, model_name: str = "gpt-3.5-turbo", temperature: float = 0.7):
        self.model_name = model_name
        self.temperature = temperature
        self.llm = self._initialize_llm()
        self.embeddings = OpenAIEmbeddings()
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )
    
    def _initialize_llm(self) -> ChatOpenAI:
        """Initialize the language model."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        return ChatOpenAI(
            model_name=self.model_name,
            temperature=self.temperature,
            openai_api_key=api_key
        )
    
    def create_simple_chain(self, template: str) -> LLMChain:
        """Create a simple LLM chain with a custom template."""
        prompt = PromptTemplate(
            input_variables=["input"],
            template=template
        )
        return LLMChain(llm=self.llm, prompt=prompt)
    
    def generate_response(self, prompt: str) -> str:
        """Generate a simple response from the LLM."""
        try:
            # Try new invoke method first
            if hasattr(self.llm, 'invoke'):
                response = self.llm.invoke(prompt)
                return response.content if hasattr(response, 'content') else str(response)
            # Fallback to older predict method
            else:
                return self.llm.predict(prompt)
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def create_vector_store(self, documents: List[str]) -> FAISS:
        """Create a vector store from documents."""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        texts = text_splitter.create_documents(documents)
        return FAISS.from_documents(texts, self.embeddings)
    
    def create_qa_chain(self, vector_store: FAISS) -> ConversationalRetrievalChain:
        """Create a conversational QA chain with retrieval."""
        return ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vector_store.as_retriever(),
            memory=self.memory,
            return_source_documents=True
        )
    
    def chat_with_memory(self, message: str, chat_history: List[tuple] = None) -> Dict[str, Any]:
        """Chat with conversation memory."""
        if chat_history is None:
            chat_history = []
        
        try:
            if hasattr(self.llm, 'invoke'):
                response = self.llm.invoke(message)
                response_text = response.content if hasattr(response, 'content') else str(response)
            else:
                response_text = self.llm.predict(message)
            
            chat_history.append((message, response_text))
            return {
                "response": response_text,
                "chat_history": chat_history
            }
        except Exception as e:
            return {
                "response": f"Error: {str(e)}",
                "chat_history": chat_history
            }
