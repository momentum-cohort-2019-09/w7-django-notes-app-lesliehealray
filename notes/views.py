from django.shortcuts import render, redirect
from notes.forms import NoteForm
from .models import Note


def note_list(request):
    notes = Note.objects.all()
    return render(request, "notes/note_list.html", {
        "notes": notes,
    })

def note_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, "notes/note_detail.html", {
        "note": note,
    })

def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = note.save()
            return redirect(to='note_list')
    else:
        form = NoteForm()

    return render(request, "notes/note_create.html", {"form":form})