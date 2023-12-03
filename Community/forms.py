from django import forms
from .models import Comment, ArticlePost

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArticlePost
        # 定义表单包含的字段
        fields = ('title', 'body')
