from django.shortcuts import render
from django.http import HttpResponse
from .models import PoloBrand , Reverse_check , Polo_Id
from django.core import serializers
import json
from sittengs.models import Sittenge_data
from polo.models import PoloBrand
# from flo.models import Flo_Brand


def test(request):
    # list_yes , list_no , all_id , access_token , STORE_ID = catch_data()

    print(list_yes)
    return render(request, 'index.html', context={'result':list_yes})
