# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        ## Uppercase to lowercase
        value = adapter.get('category')
        adapter['category'] = value.upper()



        ## Price to integer
        price_keys = ['price','price_w_tax'] 
        for price_key in price_keys:
                value = adapter.get(price_key)
                value = value.replace('£','')
                adapter[price_key] = float(value)



        ## Stock to float
        value = adapter.get('stock')
        if '(' not in value:
                value = 0
        else:               
                value = float(value.split(' ')[2][1:])
        adapter['stock'] = value



        ## Review into integer
        value = adapter.get('ratings')
        if value.upper() == 'ONE':
                value = 1
        elif value.upper() == 'TWO':
                value = 2
        elif value.upper() == 'THREE':
                value = 3
        elif value.upper() == 'FOUR':
                value = 4
        elif value.upper() == 'FIVE':
                value = 5
        
        adapter['ratings'] = value


        return item
