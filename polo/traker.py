from .models import PoloBrand , Polo_Id
from sittengs.models import Sittenge_data
import requests
from bs4 import BeautifulSoup as BS


def catch_data():
    sittengs_d = Sittenge_data.objects.all()[0]
    res = PoloBrand.objects.all().filter(has_variations='Yes')
    list_yes = []
    list_no = []
    for item in res:
        list = {item.main_sku:{
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
    res2 = PoloBrand.objects.all().filter(has_variations='No')
    for i in res2:
        list_no.append(i.main_sku)

    polo_ids = Polo_Id.objects.all()
    all_id = {}
    for item in polo_ids:
        all_id[item.sku] = item.polo_id
    return list_yes , list_no , all_id , sittengs_d.access_token , sittengs_d.STORE_ID

def get_content(url):
    '''
    use url and return with html content 
    '''
    page = requests.get(url)
    html = BS(page.content, 'html.parser')
    return html

def search_sku(sku):
    '''
    search with sku and return with item link or None if it cant catch product 
    in this case the product well be remove from polo site 
    '''
    url = 'https://tr.uspoloassn.com/list/?search_text='
    url = url + sku
    html = get_content(url)
    try:
        product_link = html.find('span',class_='product__name').find('a').get('href')
        return "https://tr.uspoloassn.com/" + product_link
    except:
        return None
        
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

def exctract_variants(url): 
    disable_variant = []
    enable_variants = []
    html = get_content(url)
    try:
        all_variants = html.find_all('ul',class_='product__variant--variables cf')[1]
    except:
        all_variants = html.find_all('ul',class_='product__variant--variables cf')[0]
    list = []
    for i in all_variants:  
        list.append(i.find('a'))
    for i in list:                     
        try:                    
            enable_variants.append(i.text.strip())
        except:
            pass
        try:
            if i.get('class')[1] == 'disabled':
                disable_variant.append(i.text.strip())
        except:
                pass
    for i in disable_variant:
        enable_variants.remove(i)
    return disable_variant , enable_variants    

def start_no():
    list_yes , list_no , all_id , access_token , STORE_ID = catch_data()
    for item in list_no:
        try:
            str = item.split('.')[2]+'.'+item.split('.')[3]
            str.strip()
        except:
            str = item
        if search_sku(str) == None:
            change_value(all_id[item],False,access_token , STORE_ID)
        else:
            change_value(all_id[item],True,access_token , STORE_ID)

def start_yes():
    list_yes , list_no , all_id , access_token , STORE_ID = catch_data()
    for item in list_yes:
        result = search_sku(list(item.keys())[0])
        if result == None:
            for j in item:
                for s in item[j]:
                    try:
                        change_value(all_id[item[j][s]],False,access_token , STORE_ID)
                    except:
                        pass
        else:
            disable_variant , enable_variants = exctract_variants(result)
            for z in item:
                for dis in disable_variant:
                    try:
                        change_value(all_id[item[z][dis]],False,access_token , STORE_ID)
                    except:
                        pass
                for ena in enable_variants:
                    try:
                        change_value(all_id[item[z][ena]],True,access_token , STORE_ID)
                    except:
                        pass

def run_tracker():
    start_no()    
    start_yes()


