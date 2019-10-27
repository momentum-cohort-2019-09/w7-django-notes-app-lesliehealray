from django.contrib import admin

from notes.models import Note, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3


class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'comment_count',
        'updated_at',
    )

    inlines = [CommentInline]


admin.site.register(Note, NoteAdmin)
admin.site.register(Comment)
