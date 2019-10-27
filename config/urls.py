"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from notes import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('notes/<int:pk>/', views.note_detail, name="note_detail"),
    path('notes/<int:pk>/edit/', views.note_edit, name="note_edit"),
    path('notes/<int:pk>/delete/',
         views.note_delete,
         name="note_delete"),
    path('notes/<int:pk>/reorder/', 
        views.notes_reorder, 
        name="notes_reorder"),
    path('notes/new/', views.note_create, name='note_create'),
    path('notes/comment/<int:pk>/edit/',
         views.note_comment_edit,
         name="note_comment_edit"),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns