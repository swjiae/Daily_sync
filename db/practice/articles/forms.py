from django import forms
from .models import Article

# 게시글 model참조 form
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('user',)
        # FK 입력 제외시키기
        # fields = '__all__' : model과 완전히 같음

# 댓글 model참조 form
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('article', 'user',)