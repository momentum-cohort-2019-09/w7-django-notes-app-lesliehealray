from django.db import models
from django.urls import reverse


class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(
        help_text="Be sure to click add item to save.",
        blank=True,
        null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def comment_count(self):
        return self.comments.count()

    def get_absolute_url(self):
        return reverse("note_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):

    class Meta:
        ordering = ['order']

    body = models.CharField(max_length=255)
    note = models.ForeignKey(to=Note,
                                  on_delete=models.CASCADE,
                                  related_name='comments')
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
