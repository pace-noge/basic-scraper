from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from zomato.items import ZomatoItem

# scrapy crawl zomato -o deloitte_result.csv -t csv

URL = "https://www.zomato.com/id/bali/restoran?page=%d"
START_PAGE = 1
NUMBER_OF_PAGES = 101

class ZomatoSpider(Spider):
    name = "zomato"
    allowed_domains = ["zomato.com"]
    start_urls = [
        URL % START_PAGE
    ]

    def __init__(self):
        self.page_number = START_PAGE

    def start_requests(self):
        for i in range(self.page_number, NUMBER_OF_PAGES + 1):
            yield Request(url = URL % i, callback=self.parse)

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//*[@id="search-results-container"]/ol/li')

        items = []



        for site in sites:
            item = ZomatoItem()
            name = "".join(site.xpath('article/div/div/h3/a/text()').extract())
            area1 = ''.join(site.xpath('article/div[1]/div[3]/a/text()').extract())
            area2 = ''.join(site.xpath('article/div[1]/div[2]/a/text()').extract())
            address1 = ''.join(site.xpath('article/div[1]/div[3]/span/text()').extract())
            address2 = ''.join(site.xpath('article/div[1]/div[2]/span/text()').extract())
            cuisine_type = ''.join(site.xpath('article/div[3]/div[1]/div/a/text()').extract())
            cuisine_region = ''.join(site.xpath('article/div[3]/div[1]/div/text()').extract())
            price = ''.join(site.xpath('article/div[3]/div[2]/text()').extract())
            rating = ''.join(site.xpath('article/div[2]/div[1]/div/div[1]/text()').extract())

            address1 = address1.encode('ascii', errors='ignore').strip("\n")
            address2 = address2.encode('ascii', errors='ignore').strip("\n")
            area1 = area1.encode('ascii', errors='ignore').strip("\n")
            area2 = area2.encode('ascii', errors='ignore').strip("\n")

            if area1 == "":
                area = area2
            else:
                area = area1

            if address1 == "":
                address = address2
            else:
                address = address1

            item["name"] = name.encode('ascii', errors='ignore').strip("\n")
            item["area"] = area
            item["address"] = address
            item["cuisine_type"] = cuisine_type.encode('ascii', errors='ignore').strip("\n")
            item["cuisine_region"] = cuisine_region.encode('ascii', errors='ignore').strip("\n")
            item["price"] = price.encode('ascii', errors='ignore').strip("\n")
            item["rating"] = rating.encode('ascii', errors='ignore').strip("\n")

            items.append(item)
        return items