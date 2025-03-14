from django import forms

from .models import Categories


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='sarlavxa',widget=forms.TextInput(attrs={"class":"form-control"}))
    context = forms.CharField(label='Text',required=False,widget=forms.Textarea(attrs={"class":"form-control","rows":4}))
    is_bool = forms.BooleanField(label='Belgilash',initial=True)
    category = forms.ModelChoiceField(empty_label='Yonalish',label="Yo'nalishni tanlang",queryset=Categories.objects.all(),widget=forms.Select(attrs={"class":"form-control"}))
