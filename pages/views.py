from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from pages.models import Note


class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class NoteListView(ListView):
    model = Note
    template_name='pages/list.html'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'pages/detail.html'
    #slug_field = 'slug'
