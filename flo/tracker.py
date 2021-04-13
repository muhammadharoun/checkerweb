# https://www.flo.com.tr/tum-kategoriler

from .models import FloBrand , Flo_Id
from sittengs.models import Sittenge_data
import requests
from bs4 import BeautifulSoup as BS


def catch_data():
    sittengs_d = Sittenge_data.objects.all()[0]
    res = FLoBrand.objects.all().filter(has_variations='Yes')
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
    res2 = FloBrand.objects.all().filter(has_variations='No')
    for i in res2:
        list_no.append([i.main_sku,item.url])

    flo_ids = flo_Id.objects.all()
    all_id = {}
    for item in flo_ids:
        all_id[item.sku] = item.flo_id
    return list_yes , list_no , all_id , sittengs_d.access_token , sittengs_d.STORE_ID

def get_content(url):
    '''
    use url and return with html content 
    '''
    page = requests.get(url)
    html = BS(page.content, 'html.parser')
    return html

def change_value(item_id,value,access_token,STORE_ID): 
        url = 'https://api.zid.sa/v1/products/{0}/'.format(item_id)
        if value == True:
            payload = "{\n    \"quantity\": 0,\n    \"is_infinite\": true\n}"
        elif value == False:
            payload = "{\n    \"quantity\": 0,\n    \"is_infinite\": false\n}"
        else:
            payload = " "
        payload = payload.encode('utf-8')
        headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI4OCIsImp0aSI6IjRlNDA2ZjgwZjNkN2M0MTU4MWI3MGI4NTE3MzY5ZDc3ZmJiNTgyYWQxMmE0YWQ0YmY5YzgyZGQ3ODViMzNkNDBjOTI0NjA5MDk0YzI5YjJkIiwiaWF0IjoiMTYwODcyMTAwNy45NzU5MjQiLCJuYmYiOiIxNjA4NzIxMDA3Ljk3NTkyOCIsImV4cCI6IjE2NDAyNTcwMDcuOTY3MTQ1Iiwic3ViIjoiNTAiLCJzY29wZXMiOlsidGhpcmQtcGFydGllcy1hcGlzIl19.Zw1nElivrORpTcsKqZP55HFpxSKVo_6CSvdc_xZCuA-pGUt2dQDolrn0tGUAg61PRS9hiSVw33rbOa3jYnyBn4-TFCOtomgZMhfNUBto9jEHz8DI5eg3dwYt9MFhZzAYRULE2YKHakLImwLQQvN9h2y9Oo3hST0jbI39nVCOZnmIFRE--fC9BD_O6u3K4p6XUTWFgVUIAQJRrXFdxyI78IXKrA0_7hn_rk82itDwZJHui-WQB5SzNg5CvHr6g-hlTsCOPanFTQ8yLI61JK953YsCczQlkh8_cMc33uAeB9KN3YoPaiyyCutpwNeqafs8a3oQ14p7i98maeeru8SeB4bywDEqxLoGjDhukoYHKGhMD5xf52vccg_MvgUsxvWLEwrOWqYYNhqXFA44zoDzqhAFbi-qPTj7H2PKSXIbwRuZ2VpA0cOpgbzmshg3tCHeB5oH3t3Tlzvm9ZThGgVywg1A-HAiCkjPI5a1kBOOHOwwU78UpCAXZAu-0jQdg4jvjiheMQz4nece1Tm-SZpEmwqo5vuOkFgrNGqasxi0FwFrIpVPEtK-oHOjK8dQHTHi0H1QkQX7ISmuYPzwDr8ASjJDxrar5euqUzTVnRqSUfK8VGUOqgpzWYwoQOIlOoyGUeAt3chp34WMFa8nQwmtE2qHuL05rLcpp-32sgeUmYk',
        'STORE-ID': '{0}'.format(STORE_ID),
        'ROLE': 'Manager',
        'Content-Type': 'application/json',
        'access-token':'{0}'.format(access_token), 
        }
        requests.request("PATCH", url, headers=headers, data = payload)      

def search(url):
    html = get_content(url)
    if  html.find('div',class_= 'error-page-wrapper') == None:
        return True
    else:
        return False

def exctract_variants(url): 
    disable_variant = []
    enable_variants = []
    html = get_content(url)
    all_variants = list(html.find('select',class_='js-select-size-options'))
    for i in all_variants[1::]:
        if 'Stok Yok' in i.text.strip():
            disable_variant.append(i.text.replace('(Stok Yok)','').strip())
        else:
            enable_variants.append(i.text.strip())

    return disable_variant , enable_variants    

def start_yes():
    list_yes , list_no , all_id , access_token , STORE_ID = catch_data()


    for item in list_yes:
        if search(item[list(item.keys())[0]]['link']) == False:
            for z in item[list(item.keys())[0]]:
                if z == 'link' or z == None:
                    pass
                else:
                    change_value(all_id[item[list(item.keys())[0]][z]],False,access_token , STORE_ID)

        else:
            # link >>  item[list(item.keys())[0]]['link']
            disable_variant , enable_variants = exctract_variants(item[list(item.keys())[0]]['link'])
            for dis in disable_variant:
                try:
                    change_value(all_id[item[list(item.keys())[0]][dis]],False,access_token , STORE_ID)
                except:
                    pass
            for ena in enable_variants:
                change_value(all_id[item[list(item.keys())[0]][ena]],True,access_token , STORE_ID)


def start_no():
    list_yes , list_no , all_id , access_token , STORE_ID = catch_data()
    for item in list_no:
        if search(item[1]) == False:
            change_value(all_id[item[0]],False,access_token , STORE_ID)
        else:
            change_value(all_id[item[0]],True,access_token , STORE_ID)


def run_tracker():
    start_no()    
    start_yes()
