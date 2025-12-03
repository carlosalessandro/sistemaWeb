# 🤝 Guia de Contribuição

Obrigado por considerar contribuir com o LangChain AI System! 

## 📋 Código de Conduta

Este projeto adere a um código de conduta. Ao participar, você concorda em manter um ambiente respeitoso e inclusivo.

## 🚀 Como Contribuir

### Reportar Bugs

1. Verifique se o bug já não foi reportado nas [Issues](https://github.com/seu-usuario/langchain-ai-system/issues)
2. Abra uma nova issue com:
   - Título claro e descritivo
   - Descrição detalhada do problema
   - Passos para reproduzir
   - Comportamento esperado vs atual
   - Screenshots (se aplicável)
   - Informações do ambiente (OS, Python version, etc.)

### Sugerir Melhorias

1. Abra uma issue com a tag `enhancement`
2. Descreva a melhoria proposta
3. Explique por que seria útil
4. Forneça exemplos de uso

### Pull Requests

1. **Fork o projeto**
```bash
git clone https://github.com/seu-usuario/langchain-ai-system.git
cd langchain-ai-system
```

2. **Crie uma branch**
```bash
git checkout -b feature/MinhaFeature
```

3. **Faça suas alterações**
- Siga o padrão de código existente
- Adicione comentários quando necessário
- Mantenha o código limpo e legível

4. **Teste suas alterações**
```bash
python manage.py test
```

5. **Commit suas mudanças**
```bash
git commit -m "Add: Descrição clara da mudança"
```

Padrão de commits:
- `Add:` Nova funcionalidade
- `Fix:` Correção de bug
- `Update:` Atualização de código existente
- `Docs:` Mudanças na documentação
- `Style:` Formatação, sem mudança de código
- `Refactor:` Refatoração de código
- `Test:` Adição ou correção de testes

6. **Push para o GitHub**
```bash
git push origin feature/MinhaFeature
```

7. **Abra um Pull Request**
- Descreva suas mudanças claramente
- Referencie issues relacionadas
- Aguarde review

## 📝 Padrões de Código

### Python
- Siga PEP 8
- Use type hints quando possível
- Docstrings para funções e classes
- Máximo 100 caracteres por linha

```python
def process_document(file_path: str, file_type: str = "txt") -> Dict[str, Any]:
    """
    Process a document file.
    
    Args:
        file_path: Path to the document
        file_type: Type of file (txt, pdf, docx)
        
    Returns:
        Dictionary with processing results
    """
    pass
```

### JavaScript
- Use ES6+
- Const/let ao invés de var
- Arrow functions quando apropriado
- Comentários para lógica complexa

```javascript
const processData = (data) => {
    // Process the data
    return data.map(item => item.value);
};
```

### HTML/CSS
- Indentação de 4 espaços
- Classes descritivas
- Comentários para seções

```html
<!-- Main Content Section -->
<div class="main-content">
    <h1>Title</h1>
</div>
```

## 🧪 Testes

### Executar Testes
```bash
python manage.py test
```

### Adicionar Testes
- Crie testes para novas funcionalidades
- Mantenha cobertura acima de 80%
- Use nomes descritivos

```python
def test_create_knowledge_base():
    """Test knowledge base creation."""
    controller = AIController()
    result = controller.create_knowledge_base(["doc1"], "kb_test")
    assert result['success'] == True
```

## 📚 Documentação

### Atualizar Documentação
- Atualize README.md para novas features
- Adicione exemplos de uso
- Mantenha documentação sincronizada com código

### Criar Documentação
- Use Markdown
- Inclua exemplos práticos
- Adicione screenshots quando relevante

## 🎯 Áreas para Contribuir

### Funcionalidades
- [ ] Novos tipos de nós no Workflow Builder
- [ ] Suporte a mais formatos de documento
- [ ] Integração com mais APIs
- [ ] Melhorias na interface

### Documentação
- [ ] Tutoriais em vídeo
- [ ] Mais exemplos de uso
- [ ] Tradução para outros idiomas
- [ ] Guias de boas práticas

### Testes
- [ ] Aumentar cobertura de testes
- [ ] Testes de integração
- [ ] Testes de performance
- [ ] Testes E2E

### Performance
- [ ] Otimização de queries
- [ ] Cache de embeddings
- [ ] Lazy loading
- [ ] Compressão de assets

## 🔍 Review Process

1. **Automated Checks**
   - Linting
   - Tests
   - Coverage

2. **Code Review**
   - Pelo menos 1 aprovação
   - Sem conflitos
   - CI/CD passando

3. **Merge**
   - Squash commits
   - Mensagem clara
   - Delete branch após merge

## 💡 Dicas

- Comece com issues marcadas como `good first issue`
- Pergunte antes de fazer grandes mudanças
- Mantenha PRs pequenos e focados
- Seja paciente e respeitoso
- Aprenda com o feedback

## 📞 Contato

Dúvidas? Entre em contato:
- 📧 Email: contato@langchain-ai.com
- 💬 Discord: [Link do servidor]
- 🐦 Twitter: [@langchain_ai]

## 🙏 Agradecimentos

Obrigado por contribuir! Cada contribuição, por menor que seja, é valiosa.

---

**Happy Coding!** 🚀
