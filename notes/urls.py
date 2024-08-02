from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_notes, name='list_notes'),
    path('<str:category>/<str:filename>/', views.note_detail, name='note_detail'),
]
