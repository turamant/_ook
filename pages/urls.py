from django.urls import path

from pages.views import AboutView, HomeView, NoteDetailView, NoteListView

urlpatterns = [
    path('about/',AboutView.as_view(), name='about'),
    path('',HomeView.as_view(), name='home'),
    path('notes/',NoteListView.as_view(), name='note_list'),
    path('notes/<int:pk>/',NoteDetailView.as_view(), name='note_detail'),

]