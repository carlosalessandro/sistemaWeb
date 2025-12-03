# 📡 API Reference

Documentação completa das APIs REST do sistema.

## Base URL

```
http://localhost:8000/api
```

## Autenticação

Atualmente não requer autenticação. Em produção, use tokens JWT.

---

## Endpoints

### 1. Chat com IA

Envia mensagem para o modelo de IA.

**Endpoint:** `POST /api/chat`

**Request:**
```json
{
  "message": "Olá, como você está?",
  "session_id": "session_123"
}
```

**Response (Success):**
```json
{
  "success": true,
  "response": "Olá! Estou bem, obrigado por perguntar...",
  "session_id": "session_123"
}
```

**Response (Error):**
```json
{
  "success": false,
  "error": "Mensagem de erro",
  "session_id": "session_123"
}
```

**Exemplo cURL:**
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Olá!", "session_id": "test"}'
```

---

### 2. Criar Knowledge Base

Cria uma nova base de conhecimento.

**Endpoint:** `POST /api/create-kb`

**Request:**
```json
{
  "documents": [
    "Python é uma linguagem de programação.",
    "Django é um framework web.",
    "LangChain facilita IA."
  ],
  "kb_id": "kb_tech"
}
```

**Response (Success):**
```json
{
  "success": true,
  "message": "Knowledge base 'kb_tech' created successfully",
  "kb_id": "kb_tech"
}
```

**Response (Error):**
```json
{
  "success": false,
  "error": "Mensagem de erro"
}
```

**Exemplo cURL:**
```bash
curl -X POST http://localhost:8000/api/create-kb \
  -H "Content-Type: application/json" \
  -d '{"documents": ["doc1", "doc2"], "kb_id": "kb_test"}'
```

---

### 3. Consultar Knowledge Base

Faz uma consulta em uma knowledge base existente.

**Endpoint:** `POST /api/query-kb`

**Request:**
```json
{
  "query": "O que é Python?",
  "kb_id": "kb_tech"
}
```

**Response (Success):**
```json
{
  "success": true,
  "answer": "Python é uma linguagem de programação de alto nível...",
  "sources": [
    "Python é uma linguagem de programação.",
    "Django é um framework web."
  ]
}
```

**Response (Error):**
```json
{
  "success": false,
  "error": "Knowledge base 'kb_tech' not found"
}
```

**Exemplo cURL:**
```bash
curl -X POST http://localhost:8000/api/query-kb \
  -H "Content-Type: application/json" \
  -d '{"query": "O que é Python?", "kb_id": "kb_tech"}'
```

---

### 4. Processar Documento

Processa um arquivo de documento.

**Endpoint:** `POST /api/process-document`

**Request:**
```json
{
  "file_path": "C:\\docs\\arquivo.txt",
  "file_type": "txt"
}
```

**Response (Success):**
```json
{
  "success": true,
  "documents": [...],
  "count": 15
}
```

**Response (Error):**
```json
{
  "success": false,
  "error": "Unsupported file type: xyz"
}
```

**Tipos de arquivo suportados:**
- `txt` - Arquivos de texto
- `pdf` - Documentos PDF

**Exemplo cURL:**
```bash
curl -X POST http://localhost:8000/api/process-document \
  -H "Content-Type: application/json" \
  -d '{"file_path": "C:\\docs\\test.txt", "file_type": "txt"}'
```

---

## Códigos de Status HTTP

- `200 OK` - Requisição bem-sucedida
- `400 Bad Request` - Dados inválidos
- `404 Not Found` - Recurso não encontrado
- `500 Internal Server Error` - Erro no servidor

---

## Rate Limiting

Atualmente não há rate limiting. Em produção, considere:
- 100 requisições por minuto por IP
- 1000 requisições por hora por usuário

---

## Exemplos em Diferentes Linguagens

### Python
```python
import requests

response = requests.post(
    'http://localhost:8000/api/chat',
    json={
        'message': 'Olá!',
        'session_id': 'test'
    }
)
print(response.json())
```

### JavaScript
```javascript
fetch('http://localhost:8000/api/chat', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    message: 'Olá!',
    session_id: 'test'
  })
})
.then(res => res.json())
.then(data => console.log(data));
```

### PowerShell
```powershell
$body = @{
    message = "Olá!"
    session_id = "test"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/chat" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

---

## Webhooks (Futuro)

Em desenvolvimento:
- Notificações de eventos
- Callbacks assíncronos
- Integração com serviços externos

---

## Versionamento

Versão atual: `v1`

Futuras versões usarão prefixo:
- `/api/v1/chat`
- `/api/v2/chat`

---

## Suporte

Dúvidas sobre a API?
- 📧 Email: api@langchain-ai.com
- 📖 Docs: https://docs.langchain-ai.com
- 💬 Discord: [Link do servidor]
