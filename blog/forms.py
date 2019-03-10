from blog.models import Article
from django import forms
from django.core.exceptions import ValidationError
import datetime


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'body', 'draft', 'published_date', 'author']

    def clean(self):
        super().clean()
        description = self.cleaned_data.get('body')
        draft = self.cleaned_data.get('draft')
        published = self.cleaned_data.get('published_date')
        today = datetime.date.today()
        if len(description) <= 1:
            raise ValidationError('The body must contain more then 1 character.')
        if draft == True and published < today:
            raise ValidationError('If draft is selected the published date must be in the future.')
        if draft == False and published >= today:
            raise ValidationError('Published date cannot be a future date.')
