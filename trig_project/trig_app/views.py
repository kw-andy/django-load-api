import csv, io
from django.shortcuts import render
from django.contrib import messages
from .models import Denomination,Retailer
from django.views import generic

from rest_framework import viewsets
from .serializers import *
# Create your views here.

def profile_upload(request):
    # declaring template
    template = "profile_upload.html"
    #data = Profile.objects.all()
# prompt is a context variable that can have different values      depending on their context

    prompt = {'order': 'Order of the CSV should be name denom and that s all'}
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)

    #next(io_string) #if you have headers in your file

    for column in csv.reader(io_string):
        _, created = Denomination.objects.update_or_create(
            denom_name=column[0],
            retailer_id = 2
        )
    context = {}
    return render(request, template, context)

def denom_list(request):
    template='home.html'

    all_denom_names = Denomination.objects.values_list("denom_name", flat=True)

    list_trig = []
    for denom_name in all_denom_names:
        if denom_name:
            list_trig.append(denom_name[:3])


    return render(request, template, {'all_denom': list_trig})


class DenominationViewSet(viewsets.ModelViewSet):

    queryset = Denomination.objects.all()
    serializer_class = DenominationSerializer


class RetailerViewSet(viewsets.ModelViewSet):

    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer