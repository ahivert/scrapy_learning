import scrapy
from cpasbien.items import CpasbienItem

class CpasbienSpider(scrapy.Spider):
    name = "cpb"
    allowed_domains = ["cpasbien.pw"]
    start_urls = [
        "http://www.cpasbien.pw/view_cat.php?categorie=films",
        "http://www.cpasbien.pw/view_cat.php?categorie=series"
    ]


    def parse(self, response):
        for lig in response.xpath('//div[@class="ligne1" or @class="ligne0"]'):
            item = CpasbienItem()
            item['name'] = lig.xpath('a/text()').extract()
            item['size'] = lig.xpath('div[@class="poid"]/text()').extract()
            item['seeders'] = lig.xpath('div[@class="up"]/span[@class="seed_nok" or @class="seed_ok"]/text()').extract()
            item['leechers'] = lig.xpath('div[@class="down"]/text()').extract()
            link = lig.xpath('a/@href').extract()[0]
            request = scrapy.Request(link, callback=self.get_link_torrent)
            request.meta['item'] = item
            return request


    def get_link_torrent(self, response):
        item = response.meta['item']
        item['link'] = response.xpath('//a[@id="telecharger"]/@href').extract()
        return item

