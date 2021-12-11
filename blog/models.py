from django.conf import settings
from django.db import models


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.comment_text


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    post = models.ForeignKey(Post, models.CASCADE)

    def __str__(self):
        return self.post.title


