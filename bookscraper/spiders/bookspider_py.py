import scrapy
import random
from bookscraper.items import BookItem

class BookspiderPySpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    ####    Custom save

    custom_settings = {
        'FEEDS':{'book.json': {'format': 'json', 'overwrite':True}}
    }


    def parse(self, response):# Loop through books to get the link to each book

        books = response.css('article.product_pod')

        for book in books: 
            relativeUrl = book.css('h3 a ::attr(href)').get()

            if 'catalogue/' in relativeUrl:
                book_url = 'https://books.toscrape.com/' + relativeUrl

            else:
                book_url = 'https://books.toscrape.com/catalogue/' + relativeUrl 

            yield response.follow(book_url, callback=self.parse_book_page)

        next_page = response.css('li.next a').attrib['href']
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page

            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page  

            yield response.follow(next_page_url, callback=self.parse)


    def parse_book_page(self, response):
        lst = response.css('table td::text').getall()
        book_item = BookItem()
        book_item['url']            = response.url
        book_item['title']          = response.css('div.col-sm-6.product_main h1::text').get()
        book_item['category']       =response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get()
        book_item['price']          = lst[2]
        book_item['price_w_tax']    = lst[3]
        book_item['stock']          = lst[-2]
        book_item['description']    = response.xpath("//article[@class='product_page']/p/text()").get()
        book_item['ratings']        = response.css('.product_main p.star-rating').attrib['class'].split(' ')[-1]
        
        yield book_item

