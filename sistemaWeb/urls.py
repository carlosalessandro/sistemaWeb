"""
Definition of urls for sistemaWeb.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('ai-chat/', views.ai_chat, name='ai_chat'),
    path('dashboard/', views.nocode_dashboard, name='nocode_dashboard'),
    path('workflow/', views.workflow_builder, name='workflow_builder'),
    path('knowledge-base/', views.knowledge_base, name='knowledge_base'),
    path('documents/', views.documents, name='documents'),
    path('analytics/', views.analytics, name='analytics'),
    path('settings/', views.settings, name='settings'),
    
    # API endpoints
    path('api/chat', views.api_chat, name='api_chat'),
    path('api/create-kb', views.api_create_kb, name='api_create_kb'),
    path('api/query-kb', views.api_query_kb, name='api_query_kb'),
    path('api/process-document', views.api_process_document, name='api_process_document'),
    
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
