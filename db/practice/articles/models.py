from django.db import models
from django.conf import settings


# Create your models here.

# 게시글 table schema
class Article(models.Model): # Model 상속
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # AUTH_USER_MODEL : 유저를 불러올 때 사용 (only models.py에서)
    # on_delete=models.CASCADE : 부모키가 삭제될 때 자녀키도 삭제
    title = models.CharField(max_length=10)
    # CharField : TEXT 길이제한
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# 댓글 table schema
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content