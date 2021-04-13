from .models import FloBrand , Reverse_check
import requests
from bs4 import BeautifulSoup as BS
import math

def get_page_numbers():
    url = 'https://www.flo.com.tr/tum-kategoriler'
    response = requests.get(url)
    result = BS(response.content,'lxml')
    product = int(result.find_all('li',{'class':'page-item'})[-2].text)
    return product

def get_product_sku(pages_number):
    all_product_sku = []
    for number in range(pages_number):
        if number == 0:
            pass
        else: 
            url = 'https://www.flo.com.tr/tum-kategoriler?page={0}'.format(number)
            response = requests.get(url)
            result = BS(response.content,'lxml')
            product = result.find_all('div',{'class':'js-product-vertical col-6 col-lg-4 listing__col-product'})
            for i in product:
                sku = i.find('div').get('data-gtm-product-id')
                all_product_sku.append(sku)            
    return all_product_sku



def run_code():
    page_number = int(get_page_numbers())
    all_product_sku = get_product_sku(page_number)
    return all_product_sku


def final_task():
    result = FloBrand.objects.all()
    old = [str(x.main_sku) for x in result]
    res = Reverse_check.objects.all()
    new = [str(x.sku) for x in res]
    final_list = new + old
    site_sku_list = run_code()
    for i in site_sku_list:
        if i in final_list:
            pass
        else:
            Reverse_check.objects.create(sku=i)
