from rest_framework import routers
from notes.viewsets import NoteViewSet

router = routers.DefaultRouter()

router.register(r'note', NoteViewSet)