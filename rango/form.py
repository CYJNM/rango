from django import forms
from rango.models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter Category name.")
    views = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    slug = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter Page title.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput, initial=0)

    class Meta:
        model = Page
        exclude = ('category',)

    def clean(self):
        cleand_data = self.cleaned_data
        url = cleand_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleand_data['url'] = url

        return cleand_data
