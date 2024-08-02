import os
from django.shortcuts import render
from django.core.paginator import Paginator
import markdown

def list_notes(request):
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'notes_data')
    categories = [name for name in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, name))]

    selected_category = request.GET.get('category', 'All Notes')
    query = request.GET.get('q', '')

    notes = []
    all_notes = []

    for category in categories:
        category_dir = os.path.join(base_dir, category)
        if os.path.exists(category_dir):
            for filename in os.listdir(category_dir):
                note = {
                    'id': len(all_notes) + 1,
                    'title': filename,
                    'category': category,
                    'path': os.path.join(category, filename)
                }
                all_notes.append(note)
                if selected_category == 'All Notes' or category == selected_category:
                    notes.append(note)

    if query:
        notes = [note for note in notes if query.lower() in note['title'].lower()]

    paginator = Paginator(notes, 5)  # Show 5 notes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'notes': page_obj,
        'selected_category': selected_category,
        'query': query,
    }
    return render(request, 'notes/notes.html', context)

def note_detail(request, category, filename):
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'notes_data')
    file_path = os.path.join(base_dir, category, filename)

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            if filename.endswith('.md'):
                content = markdown.markdown(content)

        note = {
            'title': filename,
            'content': content,
            'category': category
        }

        context = {
            'note': note,
        }
        return render(request, 'notes/note_detail.html', context)
    else:
        return render(request, 'notes/note_not_found.html', {'filename': filename})
