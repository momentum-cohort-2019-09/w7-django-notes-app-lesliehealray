import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from notes.models import Note, Comment
from notes.forms import NoteForm, CommentForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q



# Create your views here.
def note_list(request):
    notes = Note.objects.all()
    return render(request, "notes/note_list.html", {
        "notes": notes,
    })


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_item = comment_form.save(commit=False)
            new_item.note = note
            if note.comments.all():
                last_item = note.comments.order_by('-order')[0]
                new_item.order = last_item.order + 1

            new_item.save()

            return redirect(to='note_detail', pk=pk)
    else:
       comment_form = CommentForm()

    return render(request, "notes/note_detail.html", {
        "comment_form": comment_form,
        "note": note,
    })


def note_create(request):
    if request.method == "POST":  # form was submitted
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect(to=note)
    else:
        form = NoteForm()

    return render(request, "notes/note_create.html", {"form": form})


def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            note = form.save()
            return redirect(to=note)
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note_edit.html', {
        "note": note,
        "form": form,
    })


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect(to='note_list')

    return render(request, 'notes/note_delete.html',
                  {"note": note})


def note_comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    new_body = request.POST.get('body')
    if new_body:
        comment.body = new_body
        comment.save()
    return redirect(to='note_detail', pk=comment.note.pk)

@csrf_exempt
def notes_reorder(request, pk):
    note = get_object_or_404(Note, pk=pk)

    body = request.body.decode("UTF-8")
    ids = json.loads(body)
    for order, pk in enumerate(ids):
        item = note.comments.get(pk=int(pk))
        item.order = order
        item.save()

    return JsonResponse({"ok": True})


class SearchResultsView(ListView):
    model = Note
    template_name = 'notes/search_results.html'

    def get_queryset(self):
        import ipdb;ipdb.set_trace()
        query = self.request.GET.get('q')
        object_list = Note.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return object_list
    