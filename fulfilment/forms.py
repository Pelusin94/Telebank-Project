from django import forms
from . import models


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = models.UploadFile
        fields = ('file_path',)