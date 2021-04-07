from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from pages.models import Note


class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class NoteListView(ListView):
    model = Note
    template_name='pages/note_list.html'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'pages/note_detail.html'
    slug_field = 'url'
