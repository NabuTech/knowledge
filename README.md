
# Knowledge Center

A Django-based intranet-style enterprise knowledge management system for personal use. This application allows you to manage notes organized by categories, view their content, and perform searches.

## Features

- Display notes categorized by folders
- Supports both HTML and Markdown note formats
- Pagination for easy navigation through notes
- Simple search functionality

## Setup

### Prerequisites

- Python 3.x
- Django 3.x or higher

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/knowledge-center.git
   cd knowledge-center
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the database migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```sh
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/`

## Directory Structure

```
knowledge-center/
├── dashboard/
│   ├── static/
│   ├── templates/
│   ├── views.py
│   ├── urls.py
│   ├── ...
├── myknowledgecenter/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── ...
├── notes/
│   ├── static/
│   ├── templates/
│   ├── views.py
│   ├── urls.py
│   ├── ...
├── notes_data/
│   ├── Web_Development/
│   ├── Data_Science/
│   ├── ...
└── manage.py
```

## Usage

- To view notes, go to `http://127.0.0.1:8000/notes/`
- Notes are categorized by folders within the `notes_data` directory.
- Supports both HTML and Markdown formats for notes.

## Future Updates

### Features to Add

1. **Note Creation**: Allow users to create new notes directly from the application.
2. **Edit Existing Notes**: Allow users to edit the content of existing notes.
3. **Delete Notes**: Allow users to delete notes.
4. **Tagging and Categorization**: Allow users to tag notes with multiple categories and filter by tags.
5. **Advanced Search**: Implement full-text search with advanced filtering options.
6. **User Authentication and Authorization**: Add user authentication to allow multiple users to manage their own notes.
7. **Note Versioning**: Keep track of changes to notes and allow users to revert to previous versions.
8. **Rich Text Editor**: Integrate a rich text editor for more formatting options in notes.
9. **Notifications**: Add a notification system for updates or changes to notes.
10. **File Uploads**: Allow users to upload and attach files to notes.

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
