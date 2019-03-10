from blog.models import Article
from django import forms
from django.core.exceptions import ValidationError

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'body', 'draft', 'published_date', 'author']

    def clean(self):
        super().clean()
        description = self.cleaned_data.get('description')
        if len(description) < 10 or len(description) > 500:
            raise ValidationError('The body must be between 10-500 characters')
