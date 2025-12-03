// Workflow Builder - N8N Style
// Complete drag-and-drop workflow automation builder

class WorkflowBuilder {
    constructor() {
        this.nodes = [];
        this.connections = [];
        this.selectedNode = null;
        this.draggedNode = null;
        this.nodeCounter = 0;
        this.isDraggingConnection = false;
        this.connectionStart = null;
        
        this.init();
    }

    init() {
        this.setupDragAndDrop();
        this.setupCanvas();
        this.loadSavedWorkflow();
    }

    setupDragAndDrop() {
        const nodeItems = document.querySelectorAll('.node-item');
        
        nodeItems.forEach(item => {
            item.addEventListener('dragstart', (e) => {
                e.dataTransfer.setData('nodeType', item.dataset.type);
                e.dataTransfer.effectAllowed = 'copy';
            });
        });

        const canvas = document.getElementById('canvas');
        
        canvas.addEventListener('dragover', (e) => {
            e.preventDefault();
            e.dataTransfer.dropEffect = 'copy';
        });

        canvas.addEventListener('drop', (e) => {
            e.preventDefault();
            const nodeType = e.dataTransfer.getData('nodeType');
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left + canvas.scrollLeft;
            const y = e.clientY - rect.top + canvas.scrollTop;
            
            this.createNode(nodeType, x, y);
        });
    }

    setupCanvas() {
        const canvas = document.getElementById('canvas');
        
        canvas.addEventListener('click', (e) => {
            if (e.target === canvas) {
                this.deselectAllNodes();
            }
        });
    }

    createNode(type, x, y) {
        const nodeId = `node-${++this.nodeCounter}`;
        const nodeConfig = this.getNodeConfig(type);
        
        const node = {
            id: nodeId,
            type: type,
            x: x,
            y: y,
            config: nodeConfig
        };

        this.nodes.push(node);
        this.renderNode(node);
        this.hideEmptyState();
        this.markUnsaved();
    }

    getNodeConfig(type) {
        const configs = {
            'trigger-manual': {
                icon: '▶️',
                title: 'Manual Trigger',
                description: 'Inicia o workflow manualmente',
                fields: {}
            },
            'trigger-schedule': {
                icon: '⏰',
                title: 'Schedule',
                description: 'Executa em horários programados',
                fields: {
                    schedule: { type: 'text', label: 'Cron Expression', value: '0 9 * * *' }
                }
            },
            'trigger-webhook': {
                icon: '🔗',
                title: 'Webhook',
                description: 'Recebe dados via HTTP',
                fields: {
                    path: { type: 'text', label: 'Path', value: '/webhook' }
                }
            },
            'ai-chat': {
                icon: '💬',
                title: 'Chat GPT',
                description: 'Conversa com IA',
                fields: {
                    prompt: { type: 'textarea', label: 'Prompt', value: '' },
                    model: { type: 'select', label: 'Model', value: 'gpt-3.5-turbo', options: ['gpt-3.5-turbo', 'gpt-4', 'gpt-4-turbo'] },
                    temperature: { type: 'number', label: 'Temperature', value: 0.7 }
                }
            },
            'ai-embedding': {
                icon: '🧠',
                title: 'Embeddings',
                description: 'Gera embeddings de texto',
                fields: {
                    text: { type: 'textarea', label: 'Text', value: '' }
                }
            },
            'ai-rag': {
                icon: '📚',
                title: 'RAG Query',
                description: 'Consulta knowledge base',
                fields: {
                    query: { type: 'textarea', label: 'Query', value: '' },
                    kb_id: { type: 'text', label: 'KB ID', value: '' }
                }
            },
            'ai-summarize': {
                icon: '📝',
                title: 'Summarize',
                description: 'Resume textos',
                fields: {
                    text: { type: 'textarea', label: 'Text', value: '' },
                    max_length: { type: 'number', label: 'Max Length', value: 200 }
                }
            },
            'ai-translate': {
                icon: '🌐',
                title: 'Translate',
                description: 'Traduz textos',
                fields: {
                    text: { type: 'textarea', label: 'Text', value: '' },
                    target_lang: { type: 'select', label: 'Target Language', value: 'pt', options: ['pt', 'en', 'es', 'fr', 'de'] }
                }
            },
            'doc-load': {
                icon: '📄',
                title: 'Load Document',
                description: 'Carrega documento',
                fields: {
                    path: { type: 'text', label: 'File Path', value: '' },
                    type: { type: 'select', label: 'Type', value: 'txt', options: ['txt', 'pdf', 'docx'] }
                }
            },
            'doc-split': {
                icon: '✂️',
                title: 'Text Splitter',
                description: 'Divide texto em chunks',
                fields: {
                    chunk_size: { type: 'number', label: 'Chunk Size', value: 1000 },
                    overlap: { type: 'number', label: 'Overlap', value: 200 }
                }
            },
            'doc-extract': {
                icon: '🔍',
                title: 'Extract Text',
                description: 'Extrai texto de documentos',
                fields: {
                    pattern: { type: 'text', label: 'Pattern (regex)', value: '' }
                }
            },
            'data-input': {
                icon: '📥',
                title: 'Input Data',
                description: 'Entrada de dados',
                fields: {
                    data: { type: 'textarea', label: 'Data (JSON)', value: '{}' }
                }
            },
            'data-output': {
                icon: '📤',
                title: 'Output Data',
                description: 'Saída de dados',
                fields: {
                    format: { type: 'select', label: 'Format', value: 'json', options: ['json', 'text', 'csv'] }
                }
            },
            'data-transform': {
                icon: '🔄',
                title: 'Transform',
                description: 'Transforma dados',
                fields: {
                    operation: { type: 'select', label: 'Operation', value: 'map', options: ['map', 'filter', 'reduce'] },
                    expression: { type: 'textarea', label: 'Expression', value: '' }
                }
            },
            'data-filter': {
                icon: '🔎',
                title: 'Filter',
                description: 'Filtra dados',
                fields: {
                    condition: { type: 'textarea', label: 'Condition', value: '' }
                }
            },
            'logic-if': {
                icon: '❓',
                title: 'IF Condition',
                description: 'Condição IF/ELSE',
                fields: {
                    condition: { type: 'textarea', label: 'Condition', value: '' }
                }
            },
            'logic-switch': {
                icon: '🔀',
                title: 'Switch',
                description: 'Múltiplas condições',
                fields: {
                    cases: { type: 'textarea', label: 'Cases (JSON)', value: '[]' }
                }
            },
            'logic-loop': {
                icon: '🔁',
                title: 'Loop',
                description: 'Repete operações',
                fields: {
                    iterations: { type: 'number', label: 'Iterations', value: 10 }
                }
            },
            'http-request': {
                icon: '🌐',
                title: 'HTTP Request',
                description: 'Faz requisição HTTP',
                fields: {
                    url: { type: 'text', label: 'URL', value: '' },
                    method: { type: 'select', label: 'Method', value: 'GET', options: ['GET', 'POST', 'PUT', 'DELETE'] },
                    body: { type: 'textarea', label: 'Body (JSON)', value: '{}' }
                }
            },
            'email-send': {
                icon: '📧',
                title: 'Send Email',
                description: 'Envia email',
                fields: {
                    to: { type: 'text', label: 'To', value: '' },
                    subject: { type: 'text', label: 'Subject', value: '' },
                    body: { type: 'textarea', label: 'Body', value: '' }
                }
            },
            'db-query': {
                icon: '💾',
                title: 'Database',
                description: 'Consulta banco de dados',
                fields: {
                    query: { type: 'textarea', label: 'SQL Query', value: '' }
                }
            }
        };

        return configs[type] || configs['data-input'];
    }

    renderNode(node) {
        const canvas = document.getElementById('canvas');
        const nodeEl = document.createElement('div');
        nodeEl.className = 'workflow-node';
        nodeEl.id = node.id;
        nodeEl.style.left = `${node.x}px`;
        nodeEl.style.top = `${node.y}px`;

        const config = node.config;
        
        nodeEl.innerHTML = `
            <div class="connection-point input" data-node="${node.id}" data-type="input"></div>
            <div class="connection-point output" data-node="${node.id}" data-type="output"></div>
            <div class="node-header">
                <span class="icon">${config.icon}</span>
                <span class="title">${config.title}</span>
                <button class="delete-btn" onclick="workflowBuilder.deleteNode('${node.id}')">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            <div class="node-content">
                ${config.description}
            </div>
        `;

        canvas.appendChild(nodeEl);
        this.setupNodeEvents(nodeEl, node);
        this.setupConnectionPoints(nodeEl, node);
    }

    setupNodeEvents(nodeEl, node) {
        let isDragging = false;
        let startX, startY, initialX, initialY;

        nodeEl.addEventListener('mousedown', (e) => {
            if (e.target.closest('.delete-btn') || e.target.closest('.connection-point')) {
                return;
            }

            isDragging = true;
            nodeEl.classList.add('dragging');
            
            startX = e.clientX;
            startY = e.clientY;
            initialX = node.x;
            initialY = node.y;

            this.selectNode(node.id);
            e.preventDefault();
        });

        document.addEventListener('mousemove', (e) => {
            if (!isDragging) return;

            const dx = e.clientX - startX;
            const dy = e.clientY - startY;

            node.x = initialX + dx;
            node.y = initialY + dy;

            nodeEl.style.left = `${node.x}px`;
            nodeEl.style.top = `${node.y}px`;

            this.updateConnections();
        });

        document.addEventListener('mouseup', () => {
            if (isDragging) {
                isDragging = false;
                nodeEl.classList.remove('dragging');
                this.markUnsaved();
            }
        });
    }

    setupConnectionPoints(nodeEl, node) {
        const points = nodeEl.querySelectorAll('.connection-point');
        
        points.forEach(point => {
            point.addEventListener('mousedown', (e) => {
                e.stopPropagation();
                this.startConnection(node.id, point.dataset.type);
            });

            point.addEventListener('mouseup', (e) => {
                e.stopPropagation();
                this.endConnection(node.id, point.dataset.type);
            });
        });
    }

    startConnection(nodeId, type) {
        if (type === 'output') {
            this.isDraggingConnection = true;
            this.connectionStart = { nodeId, type };
        }
    }

    endConnection(nodeId, type) {
        if (this.isDraggingConnection && type === 'input' && this.connectionStart) {
            if (this.connectionStart.nodeId !== nodeId) {
                this.createConnection(this.connectionStart.nodeId, nodeId);
            }
        }
        this.isDraggingConnection = false;
        this.connectionStart = null;
    }

    createConnection(fromNodeId, toNodeId) {
        // Check if connection already exists
        const exists = this.connections.some(c => 
            c.from === fromNodeId && c.to === toNodeId
        );

        if (!exists) {
            this.connections.push({ from: fromNodeId, to: toNodeId });
            this.updateConnections();
            this.markUnsaved();
        }
    }

    updateConnections() {
        const svg = document.getElementById('connections-svg');
        svg.innerHTML = '';

        this.connections.forEach(conn => {
            const fromNode = document.getElementById(conn.from);
            const toNode = document.getElementById(conn.to);

            if (fromNode && toNode) {
                const fromPoint = fromNode.querySelector('.connection-point.output');
                const toPoint = toNode.querySelector('.connection-point.input');

                const fromRect = fromPoint.getBoundingClientRect();
                const toRect = toPoint.getBoundingClientRect();
                const svgRect = svg.getBoundingClientRect();

                const x1 = fromRect.left + fromRect.width / 2 - svgRect.left;
                const y1 = fromRect.top + fromRect.height / 2 - svgRect.top;
                const x2 = toRect.left + toRect.width / 2 - svgRect.left;
                const y2 = toRect.top + toRect.height / 2 - svgRect.top;

                const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                const d = this.createCurvePath(x1, y1, x2, y2);
                path.setAttribute('d', d);
                path.setAttribute('class', 'connection-line');
                svg.appendChild(path);
            }
        });
    }

    createCurvePath(x1, y1, x2, y2) {
        const dx = x2 - x1;
        const dy = y2 - y1;
        const cx1 = x1 + dx * 0.5;
        const cy1 = y1;
        const cx2 = x2 - dx * 0.5;
        const cy2 = y2;

        return `M ${x1} ${y1} C ${cx1} ${cy1}, ${cx2} ${cy2}, ${x2} ${y2}`;
    }

    selectNode(nodeId) {
        this.deselectAllNodes();
        
        const nodeEl = document.getElementById(nodeId);
        if (nodeEl) {
            nodeEl.classList.add('selected');
            this.selectedNode = this.nodes.find(n => n.id === nodeId);
            this.showProperties(this.selectedNode);
        }
    }

    deselectAllNodes() {
        document.querySelectorAll('.workflow-node').forEach(node => {
            node.classList.remove('selected');
        });
        this.selectedNode = null;
        this.hideProperties();
    }

    showProperties(node) {
        const panel = document.getElementById('properties-panel');
        const config = node.config;
        
        let html = `<h3><i class="fas fa-cog"></i> ${config.title}</h3>`;
        html += `<p style="color: #666; margin-bottom: 20px;">${config.description}</p>`;

        Object.keys(config.fields).forEach(key => {
            const field = config.fields[key];
            html += `<div class="property-group">`;
            html += `<label>${field.label}</label>`;

            if (field.type === 'text' || field.type === 'number') {
                html += `<input type="${field.type}" class="node-input" value="${field.value}" 
                         onchange="workflowBuilder.updateNodeField('${node.id}', '${key}', this.value)">`;
            } else if (field.type === 'textarea') {
                html += `<textarea class="node-textarea" 
                         onchange="workflowBuilder.updateNodeField('${node.id}', '${key}', this.value)">${field.value}</textarea>`;
            } else if (field.type === 'select') {
                html += `<select class="node-select" 
                         onchange="workflowBuilder.updateNodeField('${node.id}', '${key}', this.value)">`;
                field.options.forEach(opt => {
                    html += `<option value="${opt}" ${opt === field.value ? 'selected' : ''}>${opt}</option>`;
                });
                html += `</select>`;
            }

            html += `</div>`;
        });

        panel.innerHTML = html;
    }

    hideProperties() {
        const panel = document.getElementById('properties-panel');
        panel.innerHTML = `
            <h3><i class="fas fa-cog"></i> Propriedades</h3>
            <p style="color: #999;">Selecione um nó para editar suas propriedades</p>
        `;
    }

    updateNodeField(nodeId, fieldKey, value) {
        const node = this.nodes.find(n => n.id === nodeId);
        if (node && node.config.fields[fieldKey]) {
            node.config.fields[fieldKey].value = value;
            this.markUnsaved();
        }
    }

    deleteNode(nodeId) {
        // Remove connections
        this.connections = this.connections.filter(c => 
            c.from !== nodeId && c.to !== nodeId
        );

        // Remove node
        this.nodes = this.nodes.filter(n => n.id !== nodeId);

        // Remove from DOM
        const nodeEl = document.getElementById(nodeId);
        if (nodeEl) {
            nodeEl.remove();
        }

        this.updateConnections();
        this.hideProperties();
        this.markUnsaved();

        if (this.nodes.length === 0) {
            this.showEmptyState();
        }
    }

    hideEmptyState() {
        const emptyState = document.querySelector('.empty-state');
        if (emptyState) {
            emptyState.style.display = 'none';
        }
    }

    showEmptyState() {
        const canvas = document.getElementById('canvas');
        const emptyState = document.querySelector('.empty-state');
        if (emptyState) {
            emptyState.style.display = 'block';
        } else {
            canvas.innerHTML = `
                <div class="empty-state">
                    <div class="icon">🎨</div>
                    <h3>Canvas Vazio</h3>
                    <p>Arraste nós da paleta para começar</p>
                </div>
            `;
        }
    }

    markUnsaved() {
        const badge = document.querySelector('.status-badge');
        badge.textContent = 'Não salvo';
        badge.className = 'status-badge unsaved';
    }

    markSaved() {
        const badge = document.querySelector('.status-badge');
        badge.textContent = 'Salvo';
        badge.className = 'status-badge saved';
    }

    saveWorkflow() {
        const workflow = {
            nodes: this.nodes,
            connections: this.connections
        };

        localStorage.setItem('workflow', JSON.stringify(workflow));
        this.markSaved();
        alert('✅ Workflow salvo com sucesso!');
    }

    loadSavedWorkflow() {
        const saved = localStorage.getItem('workflow');
        if (saved) {
            const workflow = JSON.parse(saved);
            this.loadWorkflow(workflow);
        }
    }

    loadWorkflow(workflow = null) {
        if (!workflow) {
            const saved = localStorage.getItem('workflow');
            if (!saved) {
                alert('Nenhum workflow salvo encontrado');
                return;
            }
            workflow = JSON.parse(saved);
        }

        this.clearCanvas(false);
        
        workflow.nodes.forEach(node => {
            this.nodes.push(node);
            this.renderNode(node);
        });

        this.connections = workflow.connections;
        this.updateConnections();
        this.hideEmptyState();
        this.markSaved();
    }

    clearCanvas(confirm = true) {
        if (confirm && !window.confirm('Deseja limpar o canvas? Esta ação não pode ser desfeita.')) {
            return;
        }

        this.nodes = [];
        this.connections = [];
        this.selectedNode = null;
        this.nodeCounter = 0;

        const canvas = document.getElementById('canvas');
        canvas.innerHTML = '';
        
        const svg = document.getElementById('connections-svg');
        svg.innerHTML = '';

        this.showEmptyState();
        this.hideProperties();
        this.markUnsaved();
    }

    exportWorkflow() {
        const workflow = {
            nodes: this.nodes,
            connections: this.connections
        };

        const dataStr = JSON.stringify(workflow, null, 2);
        const dataBlob = new Blob([dataStr], { type: 'application/json' });
        const url = URL.createObjectURL(dataBlob);
        
        const link = document.createElement('a');
        link.href = url;
        link.download = 'workflow.json';
        link.click();
        
        URL.revokeObjectURL(url);
    }

    async executeWorkflow() {
        if (this.nodes.length === 0) {
            alert('⚠️ Adicione nós ao workflow antes de executar');
            return;
        }

        const modal = document.getElementById('execution-modal');
        const resultDiv = document.getElementById('execution-result');
        
        resultDiv.innerHTML = '<p>⏳ Executando workflow...</p>';
        modal.classList.add('active');

        try {
            // Simulate execution
            await new Promise(resolve => setTimeout(resolve, 2000));
            
            let result = '<div style="line-height: 2;">';
            result += '<p><strong>✅ Workflow executado com sucesso!</strong></p>';
            result += `<p>Nós processados: ${this.nodes.length}</p>`;
            result += `<p>Conexões: ${this.connections.length}</p>`;
            result += '<hr>';
            result += '<p><strong>Ordem de execução:</strong></p>';
            result += '<ol>';
            
            this.nodes.forEach(node => {
                result += `<li>${node.config.icon} ${node.config.title}</li>`;
            });
            
            result += '</ol>';
            result += '</div>';
            
            resultDiv.innerHTML = result;
        } catch (error) {
            resultDiv.innerHTML = `<p style="color: #ff5722;">❌ Erro: ${error.message}</p>`;
        }
    }
}

// Initialize
let workflowBuilder;

document.addEventListener('DOMContentLoaded', () => {
    workflowBuilder = new WorkflowBuilder();
});

// Global functions
function executeWorkflow() {
    workflowBuilder.executeWorkflow();
}

function saveWorkflow() {
    workflowBuilder.saveWorkflow();
}

function loadWorkflow() {
    workflowBuilder.loadWorkflow();
}

function clearCanvas() {
    workflowBuilder.clearCanvas();
}

function exportWorkflow() {
    workflowBuilder.exportWorkflow();
}

function closeModal() {
    document.getElementById('execution-modal').classList.remove('active');
}
