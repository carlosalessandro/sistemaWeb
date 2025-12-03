"""
Script de teste para verificar o sistema MVC com LangChain.
Execute: python test_system.py
"""
import os
import sys

# Adicionar o diretório do projeto ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistemaWeb.settings')

import django
django.setup()

from app.controllers.ai_controller import AIController


def test_imports():
    """Testa se todos os imports estão funcionando."""
    print("✓ Testando imports...")
    try:
        from app.services.langchain_service import LangChainService
        from app.services.document_service import DocumentService
        from app.repositories.chat_repository import ChatRepository
        from app.repositories.knowledge_base_repository import KnowledgeBaseRepository
        from app.models import ChatSession, ChatMessage, KnowledgeBase, Document
        print("✓ Todos os imports OK!")
        return True
    except Exception as e:
        print(f"✗ Erro nos imports: {e}")
        return False


def test_controller_initialization():
    """Testa se o controller pode ser inicializado."""
    print("\n✓ Testando inicialização do controller...")
    try:
        controller = AIController()
        print("✓ Controller inicializado com sucesso!")
        return True
    except Exception as e:
        print(f"✗ Erro ao inicializar controller: {e}")
        print(f"   Verifique se OPENAI_API_KEY está configurada no .env")
        return False


def test_models():
    """Testa se os modelos estão configurados corretamente."""
    print("\n✓ Testando modelos Django...")
    try:
        from app.models import ChatSession, ChatMessage, KnowledgeBase, Document
        
        # Verificar se as tabelas existem
        from django.db import connection
        tables = connection.introspection.table_names()
        
        required_tables = ['app_chatsession', 'app_chatmessage', 
                          'app_knowledgebase', 'app_document']
        
        missing_tables = [t for t in required_tables if t not in tables]
        
        if missing_tables:
            print(f"⚠ Tabelas faltando: {missing_tables}")
            print("   Execute: python manage.py makemigrations")
            print("   Execute: python manage.py migrate")
            return False
        else:
            print("✓ Todos os modelos OK!")
            return True
    except Exception as e:
        print(f"✗ Erro nos modelos: {e}")
        return False


def test_environment():
    """Testa se as variáveis de ambiente estão configuradas."""
    print("\n✓ Testando variáveis de ambiente...")
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("⚠ OPENAI_API_KEY não encontrada!")
        print("   1. Copie .env.example para .env")
        print("   2. Adicione sua chave OpenAI no arquivo .env")
        return False
    elif api_key == "your_openai_api_key_here":
        print("⚠ OPENAI_API_KEY ainda está com valor padrão!")
        print("   Edite o arquivo .env e adicione sua chave real")
        return False
    else:
        print(f"✓ OPENAI_API_KEY configurada (sk-...{api_key[-4:]})")
        return True


def test_langchain_compatibility():
    """Testa compatibilidade com LangChain."""
    print("\n✓ Testando compatibilidade LangChain...")
    try:
        import langchain
        print(f"✓ LangChain versão: {langchain.__version__}")
        
        # Testar imports específicos
        try:
            from langchain_openai import ChatOpenAI
            print("✓ Usando langchain_openai (versão nova)")
        except ImportError:
            from langchain.chat_models import ChatOpenAI
            print("✓ Usando langchain.chat_models (versão antiga)")
        
        return True
    except Exception as e:
        print(f"✗ Erro no LangChain: {e}")
        return False


def main():
    """Executa todos os testes."""
    print("=" * 60)
    print("TESTE DO SISTEMA MVC COM LANGCHAIN")
    print("=" * 60)
    
    results = []
    
    # Executar testes
    results.append(("Imports", test_imports()))
    results.append(("Variáveis de Ambiente", test_environment()))
    results.append(("LangChain", test_langchain_compatibility()))
    results.append(("Modelos Django", test_models()))
    results.append(("Controller", test_controller_initialization()))
    
    # Resumo
    print("\n" + "=" * 60)
    print("RESUMO DOS TESTES")
    print("=" * 60)
    
    for name, result in results:
        status = "✓ PASSOU" if result else "✗ FALHOU"
        print(f"{name:.<40} {status}")
    
    total_passed = sum(1 for _, result in results if result)
    total_tests = len(results)
    
    print(f"\nTotal: {total_passed}/{total_tests} testes passaram")
    
    if total_passed == total_tests:
        print("\n🎉 Sistema pronto para uso!")
        print("\nPróximos passos:")
        print("1. python manage.py runserver")
        print("2. Acesse http://localhost:8000/ai-chat/")
    else:
        print("\n⚠ Corrija os problemas acima antes de usar o sistema")
    
    print("=" * 60)


if __name__ == "__main__":
    main()
