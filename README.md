# 🤖 LangChain AI System - Sistema MVC Escalável com IA

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-3.2+-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-1.1.0-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Sistema completo de automação e IA com interface no-code**

[Demo](#-demo) • [Instalação](#-instalação) • [Documentação](#-documentação) • [Funcionalidades](#-funcionalidades)

</div>

---

## 📋 Sobre o Projeto

Sistema web completo desenvolvido com **Django** e **LangChain**, oferecendo uma plataforma escalável para automação de IA com interface visual no-code. Inclui um **Workflow Builder inspirado no N8N** para criar automações complexas através de drag-and-drop. Ideal para criar chatbots, processar documentos, construir workflows e gerenciar bases de conhecimento.

### 🎯 Principais Características

- 🎨 **Interface No-Code** - Use sem programar
- 🔄 **Workflow Builder N8N-Style** - Construtor visual de automações
- 💬 **Chat com IA** - GPT-3.5, GPT-4 integrados
- 📚 **Knowledge Base (RAG)** - Busca semântica em documentos
- 📄 **Processamento de Documentos** - TXT, PDF, DOCX, CSV
- 🎯 **Arquitetura MVC** - Código organizado e escalável
- 📱 **Design Responsivo** - Funciona em desktop e mobile
- ⚡ **21 Tipos de Nós** - Triggers, IA, Dados, Lógica, Integrações

---

## 🚀 Demo

### Screenshots

#### Dashboard No-Code
![Dashboard](docs/images/dashboard.png)

#### Workflow Builder (N8N-Style)
![Workflow](docs/images/workflow.png)
*Interface inspirada no N8N com drag-and-drop completo*

#### Chat com IA
![Chat](docs/images/chat.png)

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND (No-Code)                    │
│  Dashboard Visual │ Chat Interface │ Workflow Builder   │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                    VIEWS (Django)                        │
│     Renderização │ APIs REST │ Validação de Dados       │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                   CONTROLLERS (MVC)                      │
│              AIController - Lógica de Negócio           │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                   SERVICES (LangChain)                   │
│  LangChainService │ DocumentService │ Embeddings         │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                  REPOSITORIES (Data)                     │
│  ChatRepository │ KnowledgeBaseRepository │ ORM          │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                   MODELS (Database)                      │
│  ChatSession │ ChatMessage │ KnowledgeBase │ Document    │
└─────────────────────────────────────────────────────────┘
```

---

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Conta OpenAI com API key

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/langchain-ai-system.git
cd langchain-ai-system
```

2. **Crie um ambiente virtual**
```bash
python -m venv envt
```

3. **Ative o ambiente virtual**

Windows:
```bash
.\envt\Scripts\activate
```

Linux/Mac:
```bash
source envt/bin/activate
```

4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

5. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione sua chave OpenAI:
```env
OPENAI_API_KEY=sk-sua-chave-aqui
```

6. **Execute as migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Crie um superusuário (opcional)**
```bash
python manage.py createsuperuser
```

8. **Inicie o servidor**
```bash
python manage.py runserver
```

9. **Acesse o sistema**
```
http://localhost:8000
```

---

## 🎯 Funcionalidades

### 1. 💬 Chat com IA

Converse com modelos GPT da OpenAI:
- Interface interativa
- Histórico de conversas
- Múltiplas sessões
- Respostas em tempo real

### 2. 🎨 Dashboard No-Code

Interface visual completa:
- 4 abas organizadas
- Chat, KB, Documentos, Configurações
- Sem necessidade de código
- Feedback visual em tempo real

### 3. 🔄 Workflow Builder (Inspirado no N8N)

Construtor visual de automações estilo N8N:
- **Interface drag-and-drop** completa
- **21 tipos de nós** disponíveis
- **Conexões visuais** com curvas Bezier
- **Canvas infinito** com grid
- Salvar/Carregar workflows
- Exportar para JSON
- Execução de workflows

**Categorias de Nós (Inspiradas no N8N):**
- ▶️ **Triggers** (Manual, Schedule, Webhook)
- 🤖 **IA & LangChain** (Chat GPT, Embeddings, RAG, Summarize, Translate)
- 📄 **Documentos** (Load, Split, Extract)
- 💾 **Dados** (Input, Output, Transform, Filter)
- 🔀 **Lógica** (IF, Switch, Loop)
- 🔌 **Integrações** (HTTP, Email, Database)

**Funcionalidades N8N-Style:**
- ✅ Canvas infinito com grid visual
- ✅ Drag-and-drop de nós da paleta
- ✅ Conexões visuais com curvas Bezier
- ✅ Painel de propriedades dinâmico
- ✅ Salvar/Carregar workflows
- ✅ Exportar para JSON
- ✅ Execução de workflows
- ✅ Validação de conexões

> 💡 **Nota:** Nosso Workflow Builder foi inspirado no [N8N](https://n8n.io/), adaptado para automação de IA com LangChain. Veja a [comparação completa](docs/N8N_COMPARISON.md).

### 4. 📚 Knowledge Base (RAG)

Sistema de busca semântica:
- Criar bases de conhecimento
- Adicionar múltiplos documentos
- Consultas em linguagem natural
- Respostas contextualizadas
- Vector store com FAISS

### 5. 📄 Gerenciador de Documentos

Processamento de arquivos:
- Upload drag-and-drop
- Suporte: TXT, PDF, DOCX, CSV
- Chunking inteligente
- Processamento de texto direto
- Configuração de chunk size/overlap

### 6. 📊 Analytics

Métricas em tempo real:
- Total de chats
- Knowledge bases criadas
- Documentos processados
- Workflows salvos

### 7. ⚙️ Configurações

Personalize o sistema:
- Escolha do modelo (GPT-3.5, GPT-4)
- Ajuste de temperatura
- Configuração de tokens
- Gerenciamento de dados

---

## 🛠️ Tecnologias

### Backend
- **Django 3.2+** - Framework web
- **Python 3.8+** - Linguagem de programação
- **SQLite** - Banco de dados

### IA & LangChain
- **LangChain 1.1.0** - Framework de IA
- **OpenAI API** - Modelos GPT
- **FAISS** - Vector store
- **Tiktoken** - Tokenização

### Frontend
- **HTML5** - Estrutura
- **CSS3** - Estilos
- **JavaScript ES6+** - Interatividade
- **Bootstrap 3** - Framework CSS
- **Font Awesome** - Ícones

---

## 📁 Estrutura do Projeto

```
sistemaWeb/
├── app/
│   ├── controllers/          # Lógica de negócio
│   │   └── ai_controller.py
│   ├── services/             # Serviços LangChain
│   │   ├── langchain_service.py
│   │   └── document_service.py
│   ├── repositories/         # Acesso a dados
│   │   ├── chat_repository.py
│   │   └── knowledge_base_repository.py
│   ├── models.py            # Modelos Django
│   ├── views.py             # Views e APIs
│   ├── admin.py             # Admin Django
│   ├── static/              # Arquivos estáticos
│   │   ├── app/content/     # CSS
│   │   └── app/scripts/     # JavaScript
│   └── templates/           # Templates HTML
│       └── app/
│           ├── layout_sidebar.html
│           ├── index_sidebar.html
│           ├── ai_chat.html
│           ├── workflow_builder.html
│           ├── knowledge_base.html
│           ├── documents.html
│           ├── analytics.html
│           └── settings.html
├── sistemaWeb/
│   ├── settings.py          # Configurações Django
│   ├── urls.py              # Rotas
│   └── wsgi.py              # WSGI
├── requirements.txt         # Dependências
├── .env.example            # Exemplo de variáveis
├── manage.py               # Django CLI
└── README.md               # Este arquivo
```

---

## 🔌 APIs REST

### Chat
```http
POST /api/chat
Content-Type: application/json

{
  "message": "Olá, como você está?",
  "session_id": "session_123"
}
```

### Criar Knowledge Base
```http
POST /api/create-kb
Content-Type: application/json

{
  "documents": ["texto1", "texto2"],
  "kb_id": "kb_123"
}
```

### Consultar Knowledge Base
```http
POST /api/query-kb
Content-Type: application/json

{
  "query": "Sua pergunta aqui",
  "kb_id": "kb_123"
}
```

### Processar Documento
```http
POST /api/process-document
Content-Type: application/json

{
  "file_path": "C:\\docs\\arquivo.txt",
  "file_type": "txt"
}
```

---

## 📖 Documentação

### Documentos Disponíveis

- **[README_LANGCHAIN.md](README_LANGCHAIN.md)** - Documentação técnica completa
- **[GUIA_RAPIDO.md](GUIA_RAPIDO.md)** - Guia de início rápido
- **[INSTALACAO.md](INSTALACAO.md)** - Guia de instalação detalhado
- **[DASHBOARD_NOCODE.md](DASHBOARD_NOCODE.md)** - Documentação do dashboard
- **[WORKFLOW_BUILDER.md](WORKFLOW_BUILDER.md)** - Guia do workflow builder
- **[docs/N8N_COMPARISON.md](docs/N8N_COMPARISON.md)** - Comparação com N8N
- **[MENU_LATERAL.md](MENU_LATERAL.md)** - Documentação do menu
- **[VIEWS_IMPLEMENTADAS.md](VIEWS_IMPLEMENTADAS.md)** - Todas as views

### Tutoriais

#### Criar um Chatbot Simples
```python
from app.controllers.ai_controller import AIController

controller = AIController()
result = controller.process_chat_message("Olá!", "session_1")
print(result['response'])
```

#### Criar uma Knowledge Base
```python
docs = [
    "Python é uma linguagem de programação.",
    "Django é um framework web.",
    "LangChain facilita IA."
]
controller.create_knowledge_base(docs, "kb_tech")
```

#### Consultar Knowledge Base
```python
result = controller.query_knowledge_base(
    "O que é Python?",
    "kb_tech"
)
print(result['answer'])
```

---

## 🎓 Casos de Uso

### 1. Atendimento ao Cliente
- Crie KB com FAQs
- Configure chat para responder dúvidas
- Automatize respostas comuns

### 2. Análise de Documentos
- Processe PDFs de contratos
- Crie KB com documentos legais
- Faça perguntas sobre cláusulas

### 3. Assistente Pessoal
- Chat para tarefas gerais
- KB com informações pessoais
- Consultas rápidas sobre dados

### 4. Automação de Processos
- Crie workflows complexos
- Integre com APIs externas
- Automatize tarefas repetitivas

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Diretrizes

- Siga o padrão de código existente
- Adicione testes para novas funcionalidades
- Atualize a documentação
- Descreva suas mudanças claramente

---

## 🐛 Reportar Bugs

Encontrou um bug? Abra uma [issue](https://github.com/seu-usuario/langchain-ai-system/issues) com:

- Descrição clara do problema
- Passos para reproduzir
- Comportamento esperado vs atual
- Screenshots (se aplicável)
- Ambiente (OS, Python version, etc.)

---

## 📝 Roadmap

### Em Desenvolvimento
- [ ] Suporte a mais modelos de IA (Anthropic, Cohere)
- [ ] Gráficos interativos no Analytics
- [ ] Upload de arquivos via interface
- [ ] Streaming de respostas
- [ ] Testes unitários completos

### Planejado
- [ ] Autenticação multi-usuário
- [ ] Permissões e roles
- [ ] API GraphQL
- [ ] Deploy em Docker
- [ ] Integração com mais serviços
- [ ] Mobile app

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👥 Autores

- **Seu Nome** - *Desenvolvimento inicial* - [GitHub](https://github.com/seu-usuario)

---

## 🙏 Agradecimentos

- [N8N](https://n8n.io/) - Inspiração para o Workflow Builder
- [LangChain](https://python.langchain.com/) - Framework de IA
- [OpenAI](https://openai.com/) - Modelos GPT
- [Django](https://www.djangoproject.com/) - Framework web
- [Bootstrap](https://getbootstrap.com/) - Framework CSS
- [Font Awesome](https://fontawesome.com/) - Ícones

---

## 📞 Suporte

- 📧 Email: contato@langchain-ai.com
- 💬 Discord: [Link do servidor]
- 🐦 Twitter: [@langchain_ai]
- 📖 Documentação: [docs.langchain-ai.com]

---

## ⭐ Star History

Se este projeto foi útil para você, considere dar uma estrela! ⭐

---

<div align="center">

**Desenvolvido com ❤️ usando Django e LangChain**

[⬆ Voltar ao topo](#-langchain-ai-system---sistema-mvc-escalável-com-ia)

</div>
