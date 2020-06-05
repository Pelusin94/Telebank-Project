from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models
import csv


def fulfilment_view(request):
    template = 'fulfilment/main.html'
    upload_form = forms.UploadFileForm()
    context = {'form': upload_form}

    if request.method == 'POST':

        if request.POST.get('uploaddata'):
            upload_form = forms.UploadFileForm(request.POST, request.FILES)
            if upload_form.is_valid():
                model = models.FulfilmentFilesData.objects.all()
                file = upload_form.cleaned_data['file_path']
                data = file.read().decode('utf-8').splitlines()
                dic_data = csv.DictReader(data)

                for row in dic_data:
                    print(row)









    return render(request, template, context)
