lists = [{'item.main_sku':{
    'item.variation1':'item.sku1',
    'item.variation2':'item.sku2',
    'item.variation3':'item.sku3',
    }}]

for item in lists:
    for j in item:
        print(item[j]['item.variation2'])