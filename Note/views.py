from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import note
from .forms import noteForm

# Create your views here.
def home(request):
    return render(request, "Note/index.html")

class noteCreate(CreateView):
    model = note
    form_class = noteForm
    template_name = 'Note/note_edit.html'

class noteList(ListView):
    model = note
    template_name = 'Note/note.html'

class noteUpdate(UpdateView):
    model = note
    form_class = noteForm
    template_name = 'Note/note_edit.html'

class noteDelete(DeleteView):
    model = note
    success_url = '/notes/list'
    template_name = 'Note/note_edit.html'