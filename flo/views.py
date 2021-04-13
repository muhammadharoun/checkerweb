from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from sittengs.models import Sittenge_data
from .models import Flo_Brand , Flo_Id


def catch_data():
    sittengs_d = Sittenge_data.objects.all()[0]
    res = Flo_Brand.objects.all().filter(has_variations='Yes')
    list_yes = []
    list_no = []
    for item in res:
        list = {item.main_sku:{
            'link':item.url,
            item.variation1:item.sku1,
            item.variation2:item.sku2,
            item.variation3:item.sku3,
            item.variation4:item.sku4,
            item.variation5:item.sku5,
            item.variation6:item.sku6,
            item.variation7:item.sku7,
            item.variation8:item.sku8,
            item.variation9:item.sku9,
            item.variation10:item.sku10,
            item.variation11:item.sku11,
            item.variation12:item.sku12,
            item.variation13:item.sku13,
            item.variation14:item.sku14,
            item.variation15:item.sku15
            }}
        list_yes.append(list)
    res2 = Flo_Brand.objects.all().filter(has_variations='No')
    for i in res2:
        list_no.append([i.main_sku,i.url])

    flo_ids = Flo_Id.objects.all()
    all_id = {}
    for item in flo_ids:
        all_id[item.sku] = item.flo_id
    return list_yes , list_no , all_id , sittengs_d.access_token , sittengs_d.STORE_ID





def test(request):
    list_yes , list_no , all_id , access_token , STORE_ID = catch_data()

    # for i in list_no:
    #     print(i[list(i.keys())[0]])

    print(all_id)
    return render(request, 'index.html', context={'result':all_id})
