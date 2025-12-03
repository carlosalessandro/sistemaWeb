"""
Definition of views.
"""
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from app.controllers.ai_controller import AIController


# Initialize controller
ai_controller = AIController()


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index_sidebar.html',
        {
            'title': 'Home',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about_sidebar.html',
        {
            'title': 'Sobre',
            'message': 'Sistema MVC com LangChain',
            'year': datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact_sidebar.html',
        {
            'title': 'Contato',
            'message': 'Entre em contato conosco',
            'year': datetime.now().year,
        }
    )


def ai_chat(request):
    """Renders the AI chat page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/ai_chat.html',
        {
            'title': 'AI Chat',
            'year': datetime.now().year,
        }
    )


@csrf_exempt
@require_http_methods(["POST"])
def api_chat(request):
    """API endpoint for chat messages."""
    try:
        data = json.loads(request.body)
        message = data.get('message', '')
        session_id = data.get('session_id', 'default')
        
        if not message:
            return JsonResponse({'error': 'Message is required'}, status=400)
        
        result = ai_controller.process_chat_message(message, session_id)
        return JsonResponse(result)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def api_create_kb(request):
    """API endpoint for creating knowledge base."""
    try:
        data = json.loads(request.body)
        documents = data.get('documents', [])
        kb_id = data.get('kb_id', '')
        
        if not documents or not kb_id:
            return JsonResponse({'error': 'Documents and kb_id are required'}, status=400)
        
        result = ai_controller.create_knowledge_base(documents, kb_id)
        return JsonResponse(result)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def api_query_kb(request):
    """API endpoint for querying knowledge base."""
    try:
        data = json.loads(request.body)
        query = data.get('query', '')
        kb_id = data.get('kb_id', '')
        
        if not query or not kb_id:
            return JsonResponse({'error': 'Query and kb_id are required'}, status=400)
        
        result = ai_controller.query_knowledge_base(query, kb_id)
        return JsonResponse(result)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def api_process_document(request):
    """API endpoint for processing documents."""
    try:
        data = json.loads(request.body)
        file_path = data.get('file_path', '')
        file_type = data.get('file_type', 'txt')
        
        if not file_path:
            return JsonResponse({'error': 'File path is required'}, status=400)
        
        result = ai_controller.process_document(file_path, file_type)
        return JsonResponse(result)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def nocode_dashboard(request):
    """Renders the no-code dashboard page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/nocode_dashboard.html',
        {
            'title': 'Dashboard No-Code',
            'year': datetime.now().year,
        }
    )


def workflow_builder(request):
    """Renders the workflow builder page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/workflow_builder.html',
        {
            'title': 'Workflow Builder',
            'year': datetime.now().year,
        }
    )


def knowledge_base(request):
    """Renders the knowledge base page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/knowledge_base.html',
        {
            'title': 'Knowledge Base',
            'year': datetime.now().year,
        }
    )


def documents(request):
    """Renders the documents page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/documents.html',
        {
            'title': 'Documentos',
            'year': datetime.now().year,
        }
    )


def analytics(request):
    """Renders the analytics page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/analytics.html',
        {
            'title': 'Analytics',
            'year': datetime.now().year,
        }
    )


def settings(request):
    """Renders the settings page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/settings.html',
        {
            'title': 'Configurações',
            'year': datetime.now().year,
        }
    )
