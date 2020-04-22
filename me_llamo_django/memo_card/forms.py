from .models import CategoryMemoCard, UserMemoCard
from django import forms


class CategoryCreationForm(forms.ModelForm):
    title = forms.CharField(label="",widget=forms.TextInput(attrs={"id":"input_text", "type":"text", "data-length":"50"}))
    description = forms.CharField(label="",widget=forms.Textarea(attrs={"id":"textarea2", "class":"materialize-textarea","data-length":"200"}))

    class Meta:
        model = CategoryMemoCard
        fields = ('title','description')


class CategoryUpdateForm(forms.ModelForm):
    title = forms.CharField(label="",widget=forms.TextInput(attrs={"id":"input_text", "type":"text", "data-length":"50"}))
    description = forms.CharField(label="",widget=forms.Textarea(attrs={"id":"textarea2", "class":"materialize-textarea","data-length":"200"}))

    class Meta:
        model = CategoryMemoCard
        fields = ('title','description')


class UserMemocardCreationForm(forms.ModelForm):
    title = forms.CharField(label="",widget=forms.TextInput(attrs={"id":"input_text", "type":"text", "data-length":"150"}))
    eg = forms.CharField(label="",widget=forms.Textarea(attrs={"id":"textarea2", "class":"materialize-textarea","data-length":"250"}))
    reverse_title = forms.CharField(label="",widget=forms.TextInput(attrs={"id":"input_text", "type":"text", "data-length":"150"}))
    reverse_eg = forms.CharField(label="",widget=forms.Textarea(attrs={"id":"textarea2", "class":"materialize-textarea","data-length":"250"}))

    class Meta:
        model = UserMemoCard
        fields = ('title','eg', 'reverse_title', 'reverse_eg')

