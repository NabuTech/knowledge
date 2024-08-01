from django.shortcuts import render
from django.core.paginator import Paginator

def home(request):
    return render(request, 'dashboard/home.html')

def notes(request):
    categories = ["Course Name 1", "Course Name 2", "Evernote Notebook 1", "Topic 1"]
    all_notes = [
        {"id": 1, "title": "Note 1", "content": "Content of note 1", "category": "Course Name 1"},
        {"id": 2, "title": "Note 2", "content": "Content of note 2", "category": "Evernote Notebook 1"},
        {"id": 3, "title": "Note 3", "content": "Content of note 3", "category": "Course Name 2"},
        {"id": 4, "title": "Note 4", "content": "Content of note 4", "category": "Topic 1"},
        # Add more notes for demonstration
    ]
    
    selected_category = request.GET.get('category', 'All Notes')
    query = request.GET.get('q', '')

    if selected_category != 'All Notes':
        notes = [note for note in all_notes if note['category'] == selected_category]
    else:
        notes = all_notes

    if query:
        notes = [note for note in notes if query.lower() in note['title'].lower() or query.lower() in note['content'].lower()]
    
    paginator = Paginator(notes, 5)  # Show 5 notes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'categories': categories,
        'notes': page_obj,
        'selected_category': selected_category,
        'query': query,
    }
    return render(request, 'dashboard/notes.html', context)

def articles(request):
    return render(request, 'dashboard/articles.html')

def recent_documents(request):
    return render(request, 'dashboard/recent_documents.html')

def category(request, category_name):
    context = {'category_name': category_name}
    return render(request, 'dashboard/category.html', context)

def help_support(request):
    return render(request, 'dashboard/help_support.html')

def note_detail(request, note_id):
    all_notes = [
        {"id": 1, "title": "Note 1", "content": "Content of note 1", "category": "Course Name 1"},
        {"id": 2, "title": "Note 2", "content": "Content of note 2", "category": "Evernote Notebook 1"},
        {"id": 3, "title": "Note 3", "content": "Content of note 3", "category": "Course Name 2"},
        {"id": 4, "title": "Note 4", "content": "Content of note 4", "category": "Topic 1"},
    ]
    note = next((note for note in all_notes if note["id"] == note_id), None)
    
    context = {
        'note': note,
    }
    return render(request, 'dashboard/note_detail.html', context)
