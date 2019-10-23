from django.conf import settings
from django.db import models
from django.utils import timezone


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(
        help_text="Put the details of your note here.",
        blank=True,
        null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# class Comment(models.Model):
#     comment = models.ForeignKey(to=Note,
#                                   on_delete=models.CASCADE,
#                                   related_name='items')
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.comment