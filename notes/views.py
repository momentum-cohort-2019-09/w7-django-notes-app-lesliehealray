from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

def note_list(request):
    return render(request, "notes/note_list.html", {
        "notes": Note.objects.all()
    })

def note_detail(request, id):
    return render(request, "notes/note_detail.html", {
        "note": Note.objects.get(id=id)
    })