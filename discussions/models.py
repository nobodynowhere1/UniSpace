from django.conf import settings
from django.db import models


class DiscussionPost(models.Model):
    class Category(models.TextChoices):
        PROGRAMMING = 'programming', 'Programming'
        STUDY = 'study', 'Study / University'
        CAREER = 'career', 'Career / Internships'
        PROJECTS = 'projects', 'Projects'
        OFFTOPIC = 'offtopic', 'Offtopic'

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='discussions/images/', blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='discussion_posts'
    )
    category = models.CharField(max_length=20, choices=Category.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(DiscussionPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='discussion_comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self) -> str:
        return f'Comment by {self.author} on {self.post}'

# Create your models here.
