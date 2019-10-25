from rest_framework import viewsets, filters
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'title', 'text', 'name')
