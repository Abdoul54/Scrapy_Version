import scrapy
from pymongo import MongoClient

class AvitoscrapeSpider(scrapy.Spider):
    name = "avitoScrape"


    def __init__(self, *args, **kwargs):
        super(AvitoscrapeSpider, self).__init__(*args, **kwargs)
        self.client = MongoClient('mongodb://localhost:27017/mydb?directConnection=true')
        self.db = self.client['Scrape']
        self.collection = self.db['Posts']

    def start_requests(self):
        cities = ['agadir',
                  'bouznika',
                  'béni mellal',
                  'el jadida',
                  'fès',
                  'khouribga',
                  'kénitra',
                  'marrakech',
                  'meknès',
                  'mohammedia',
                  'nador',
                  'oujda',
                  'rabat',
                  'safi',
                  'salé',
                  'settat',
                  'tanger',
                  'temara',
                  'tétouan']

        for city in cities:
            link = f'https://www.avito.ma/fr/{city}/voitures-à_vendre'
            yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        data = []
        for i in range(1, 30):
            title = response.xpath(
                f'//*[@id="__next"]/div/main/div/div[6]/div[1]/div/div[2]/div[{i}]/a/div[2]/div[1]/h3/span/text()').get()
            link = response.xpath(
                f'//*[@id="__next"]/div/main/div/div[6]/div[1]/div/div[2]/div[{i}]/a/@href').get()
            img = response.xpath(
                f'//*[@id="__next"]/div/main/div/div[6]/div[1]/div/div[2]/div[{i}]/a/div[1]/div/div/img/@src').get()
            price = response.xpath(
                f'//*[@id="__next"]/div/main/div/div[6]/div[1]/div/div[2]/div[{i}]/a/div[2]/div[1]/div/span/div/span[1]/text()').get()
            Type = response.xpath(
                f'//*[@id="__next"]/div/main/div/div[6]/div[1]/div/div[2]/div[{i}]/a/div[2]/div[2]/p/text()').get()
            localisation = response.xpath(
                f'//*[@id="__next"]/div/main/div/div[6]/div[1]/div/div[2]/div[{i}]/a/div[2]/div[2]/div/div[2]/span/text()').get()
            if price is None:
                price = 0
            else:
                price = price.replace(',', '')
            data.append({"Category": "Vehicle",'Title': title, 'Link': link, 'Image': img, 'Price': int(price), 'Type': Type, 'Localisation': localisation,"Platform": "www.avito.ma"})
        self.collection.insert_many(data)

