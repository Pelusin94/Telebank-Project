from django.shortcuts import render
from django.http import HttpResponse
from . import forms


def fulfilment_view(request):
    template = 'fulfilment/main.html'
    upload_form = forms.UploadFileForm()
    context = {'form': upload_form}

    # if request.method == 'POST':
    #
    #     if request.POST.get('uploaddata'):
    #         upload_form = forms.UploadFileForm(request.POST, request.FILES)
    #         if upload_form.is_valid():









    return render(request, template, context)
