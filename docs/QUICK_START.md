# ⚡ Quick Start Guide

Comece a usar o LangChain AI System em 5 minutos!

## 🚀 Instalação Rápida

### 1. Clone e Configure
```bash
git clone https://github.com/seu-usuario/langchain-ai-system.git
cd langchain-ai-system
pip install -r requirements.txt
cp .env.example .env
```

### 2. Configure API Key
Edite `.env`:
```env
OPENAI_API_KEY=sk-sua-chave-aqui
```

### 3. Inicie o Sistema
```bash
python manage.py migrate
python manage.py runserver
```

### 4. Acesse
```
http://localhost:8000
```

## 🎯 Primeiros Passos

### 1. Teste o Chat
1. Acesse http://localhost:8000/ai-chat/
2. Digite "Olá!"
3. Veja a resposta da IA

### 2. Crie uma Knowledge Base
1. Acesse http://localhost:8000/knowledge-base/
2. Digite um nome: `kb_teste`
3. Adicione documentos (um por linha)
4. Clique em "Criar Knowledge Base"

### 3. Construa um Workflow
1. Acesse http://localhost:8000/workflow/
2. Arraste nós da paleta
3. Conecte os nós
4. Clique em "Executar"

## 📚 Próximos Passos

- Explore o [Dashboard](http://localhost:8000/dashboard/)
- Leia a [Documentação Completa](../README_LANGCHAIN.md)
- Veja [Exemplos de Uso](EXAMPLES.md)

## 🆘 Problemas?

- Verifique se Python 3.8+ está instalado
- Confirme que a API key está correta
- Execute `python manage.py check`
- Consulte [Troubleshooting](TROUBLESHOOTING.md)

**Pronto para começar!** 🎉
