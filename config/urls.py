from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.note_list, name='note_list'),
    path('notes/<id>/', views.note_detail, name="note_detail"),
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns