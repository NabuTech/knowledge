from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes, name='notes'),
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),
    path('articles/', views.articles, name='articles'),
    path('recent-documents/', views.recent_documents, name='recent_documents'),
    path('categories/<str:category_name>/', views.category, name='category'),
    path('help/', views.help_support, name='help_support'),
]
