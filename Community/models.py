from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse


class User(AbstractUser):
    introduction = models.TextField(max_length=100)
    age = models.IntegerField(null=True)
    gender = models.BooleanField(null=True)
    email = models.EmailField()
    user_type = models.BooleanField(default=False)
    

# 博客文章数据模型
class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    total_views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('community:article_detail', args=[self.id])


# 博文的评论
class Comment(models.Model):
    article = models.ForeignKey(
        ArticlePost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments'
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]