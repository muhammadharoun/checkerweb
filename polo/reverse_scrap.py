from .models import PoloBrand , Reverse_check
import requests
from bs4 import BeautifulSoup as BS
import math


def get_page_numbers():
    url = 'https://tr.uspoloassn.com/list/?search_text='
    response = requests.get(url)
    result = BS(response.content,'lxml')
    pages_number = math.ceil(int(result.find('div',{'class':'entity__count'}).find('span').text.split(' ')[0])/24)
    return pages_number


def get_product(pages_number):
    all_product_links = []
    for number in range(pages_number):
        url = f'https://tr.uspoloassn.com/list/?search_text=&page={number}'
        response = requests.get(url)
        result = BS(response.content,'lxml')
        product = result.find_all('div',{'class':'product__listing--image'})
        for i in product:
            all_product_links.append('https://tr.uspoloassn.com'+i.find('figure').find('a').get('href'))            
    return all_product_links


def get_sku(products):
    all_sku = []
    for i in products:
        response = requests.get(i)
        result = BS(response.content,'lxml')
        content = str(result.find('div',{'class':'product__property--content'}).find('p').text).split('\n')
        sku = ' '.join(content).split()[0]
        all_sku.append(sku)
    return all_sku


def run_code():
    page_number = int(get_page_numbers())
    products = get_product(page_number)  
    return get_sku(products)              


def final_task():
    result = PoloBrand.objects.all()
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





# celery -A project worker -l info
# celery -A project beat -l info
# pip install celery==4.4.7