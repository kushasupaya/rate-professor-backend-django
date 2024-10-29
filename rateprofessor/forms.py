from django import forms

class ProfessorDataForm(forms.Form):
    url = forms.URLField(label="URL", required=True)

    def clean_url(self):
        url = self.cleaned_data['url']
        return url
