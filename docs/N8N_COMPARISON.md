# 🔄 Workflow Builder - Comparação com N8N

## Inspiração no N8N

O **Workflow Builder** deste projeto foi **inspirado no N8N**, uma das melhores ferramentas de automação no-code do mercado. Implementamos conceitos similares adaptados para automação de IA com LangChain.

---

## 🎯 Conceitos do N8N Implementados

### 1. Interface Visual Drag-and-Drop

**N8N:**
- Arraste nós da paleta lateral
- Solte no canvas
- Interface intuitiva

**Nossa Implementação:**
```javascript
// Drag-and-drop completo
- Paleta de nós à esquerda (280px)
- Canvas infinito com grid
- 21 tipos de nós disponíveis
- Feedback visual em tempo real
```

### 2. Conexões Visuais

**N8N:**
- Linhas conectando nós
- Curvas suaves
- Indicadores de fluxo

**Nossa Implementação:**
```javascript
// Conexões SVG com Bezier
- Curvas suaves entre nós
- Pontos de conexão (input/output)
- Atualização automática ao mover nós
- Validação de conexões
```

### 3. Painel de Propriedades

**N8N:**
- Painel lateral direito
- Edição de parâmetros
- Campos dinâmicos

**Nossa Implementação:**
```javascript
// Painel dinâmico (320px)
- Propriedades por tipo de nó
- Campos editáveis (text, textarea, select, number)
- Atualização em tempo real
- Validação de entrada
```

### 4. Tipos de Nós

**N8N:**
- Triggers
- Actions
- Transformações
- Integrações

**Nossa Implementação:**
```javascript
// 21 tipos organizados em 6 categorias
▶️ Triggers (3)
🤖 IA & LangChain (5)
📄 Documentos (3)
💾 Dados (4)
🔀 Lógica (3)
🔌 Integrações (3)
```

### 5. Salvar e Executar

**N8N:**
- Salvar workflows
- Executar manualmente
- Histórico de execuções

**Nossa Implementação:**
```javascript
// Funcionalidades completas
- Salvar no localStorage
- Carregar workflows salvos
- Executar workflows
- Exportar para JSON
- Modal com resultados
```

---

## 📊 Comparação Detalhada

| Funcionalidade | N8N | Nossa Implementação | Status |
|----------------|-----|---------------------|--------|
| Drag-and-Drop | ✅ | ✅ | Implementado |
| Canvas Infinito | ✅ | ✅ | Implementado |
| Conexões Visuais | ✅ | ✅ | Implementado |
| Painel de Propriedades | ✅ | ✅ | Implementado |
| Salvar Workflows | ✅ | ✅ | Implementado |
| Executar Workflows | ✅ | ✅ | Implementado |
| Triggers | ✅ | ✅ | 3 tipos |
| Integrações HTTP | ✅ | ✅ | Implementado |
| Lógica Condicional | ✅ | ✅ | IF, Switch, Loop |
| Transformação de Dados | ✅ | ✅ | Transform, Filter |
| Webhooks | ✅ | ✅ | Implementado |
| Schedule/Cron | ✅ | ✅ | Implementado |
| Versionamento | ✅ | ⏳ | Planejado |
| Colaboração | ✅ | ⏳ | Planejado |
| Execução em Background | ✅ | ⏳ | Planejado |
| Logs Detalhados | ✅ | ⏳ | Planejado |

---

## 🎨 Design Inspirado no N8N

### Layout
```
┌──────────┬──────────────────────────────┬───────────────┐
│          │                              │               │
│  PALETA  │         CANVAS               │  PROPRIEDADES │
│  DE NÓS  │      (Drag & Drop)           │               │
│          │                              │               │
│ ▶️ Trig  │  ┌────┐      ┌────┐          │  Nó: Chat GPT │
│ 🤖 IA    │  │ N1 │─────→│ N2 │          │               │
│ 📄 Docs  │  └────┘      └────┘          │  Prompt:      │
│ 💾 Data  │                              │  [________]   │
│ 🔀 Logic │  ┌────┐                      │               │
│ 🔌 Integ │  │ N3 │                      │  Model:       │
│          │  └────┘                      │  [GPT-3.5▼]   │
└──────────┴──────────────────────────────┴───────────────┘
```

### Cores e Estilo
- **Azul Piscina (#00bcd4)** - Cor principal
- **Gradientes** nos nós
- **Sombras suaves** para profundidade
- **Animações** em hover e drag
- **Grid de fundo** para organização

---

## 🚀 Diferenciais da Nossa Implementação

### 1. Foco em IA e LangChain

**Nós Específicos de IA:**
```javascript
- Chat GPT (GPT-3.5, GPT-4)
- Embeddings (OpenAI)
- RAG Query (Knowledge Base)
- Summarize (Resumo de textos)
- Translate (Tradução)
```

### 2. Integração com Sistema

**Conectado ao Ecossistema:**
```javascript
- Usa mesmas APIs do sistema
- Compartilha Knowledge Bases
- Acessa documentos processados
- Integrado com chat
```

### 3. Sem Dependências Externas

**Vanilla JavaScript:**
```javascript
- Sem React, Vue ou Angular
- Sem bibliotecas de drag-and-drop
- SVG nativo para conexões
- LocalStorage para persistência
```

### 4. Código Aberto e Customizável

**Fácil de Modificar:**
```javascript
- Adicionar novos tipos de nós
- Customizar propriedades
- Alterar cores e estilos
- Estender funcionalidades
```

---

## 📝 Exemplo de Workflow N8N-Style

### Workflow: Análise de Documentos com IA

```
┌─────────────┐
│   Manual    │
│   Trigger   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Load     │
│  Document   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Text     │
│   Splitter  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Embeddings  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ RAG Query   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Summarize   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Output    │
└─────────────┘
```

**Implementação:**
1. Arraste "Manual Trigger" para o canvas
2. Arraste "Load Document" e conecte
3. Continue adicionando nós
4. Configure propriedades de cada nó
5. Clique em "Executar"

---

## 🎓 Aprendizados do N8N

### 1. UX/UI
- Interface intuitiva é crucial
- Feedback visual em tempo real
- Drag-and-drop deve ser suave
- Propriedades devem ser claras

### 2. Arquitetura
- Nós devem ser independentes
- Conexões devem ser validadas
- Estado deve ser persistente
- Execução deve ser rastreável

### 3. Extensibilidade
- Fácil adicionar novos nós
- Propriedades configuráveis
- Integrações modulares
- Código bem organizado

---

## 🔮 Roadmap Inspirado no N8N

### Curto Prazo
- [ ] Zoom e pan no canvas
- [ ] Undo/Redo
- [ ] Copiar/Colar nós
- [ ] Grupos de nós

### Médio Prazo
- [ ] Execução real com backend
- [ ] Logs de execução
- [ ] Debugging visual
- [ ] Templates de workflows

### Longo Prazo
- [ ] Versionamento de workflows
- [ ] Colaboração em tempo real
- [ ] Marketplace de nós
- [ ] Execução agendada

---

## 💡 Como Adicionar Novos Nós (N8N-Style)

### 1. Definir Configuração

```javascript
'seu-tipo': {
    icon: '🎯',
    title: 'Seu Nó',
    description: 'Descrição do nó',
    fields: {
        campo1: { 
            type: 'text', 
            label: 'Campo 1', 
            value: '' 
        },
        campo2: { 
            type: 'select', 
            label: 'Campo 2', 
            value: 'opcao1',
            options: ['opcao1', 'opcao2']
        }
    }
}
```

### 2. Adicionar na Paleta

```html
<div class="node-item" draggable="true" data-type="seu-tipo">
    <span class="icon">🎯</span>
    <span class="label">Seu Nó</span>
</div>
```

### 3. Implementar Lógica

```javascript
async function executeSeuTipo(node) {
    const campo1 = node.config.fields.campo1.value;
    const campo2 = node.config.fields.campo2.value;
    
    // Sua lógica aqui
    const result = await processarDados(campo1, campo2);
    
    return result;
}
```

---

## 🌟 Créditos

**N8N** - [n8n.io](https://n8n.io/)
- Inspiração para interface
- Conceitos de workflow
- Padrões de UX/UI
- Arquitetura de nós

**Nossa Implementação:**
- Código 100% original
- Focado em IA e LangChain
- Integrado com Django
- Sem dependências do N8N

---

## 📚 Recursos

### N8N
- [Documentação N8N](https://docs.n8n.io/)
- [GitHub N8N](https://github.com/n8n-io/n8n)
- [Comunidade N8N](https://community.n8n.io/)

### Nossa Implementação
- [Workflow Builder Docs](../WORKFLOW_BUILDER.md)
- [Código Fonte](../app/static/app/scripts/workflow-builder.js)
- [Template HTML](../app/templates/app/workflow_builder.html)

---

## 🙏 Agradecimentos

Agradecemos ao time do **N8N** por criar uma ferramenta incrível que serviu de inspiração para nosso Workflow Builder. O conceito de automação visual no-code é revolucionário e estamos orgulhosos de trazer essa experiência para o mundo da IA com LangChain.

---

**Workflow Builder - Powered by N8N Concepts** 🔄✨
