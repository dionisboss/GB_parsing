# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from jobparser2.items import Jobparser2Item

class SjSpider(scrapy.Spider):
    name = 'sj'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://russia.superjob.ru/vacancy/search/?keywords=python']

    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//a[@class = 'icMQ_ _1_Cht _3ze9n f-test-button-dalshe f-test-link-Dalshe']//@href").extract_first()

        #next_page = response.css("a.HH-Pager-Controls-Next::attr(href)").extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacansy_links = response.xpath("//a[contains(@class,'_2JivQ ')]/@href").extract()

        for link in vacansy_links:
            yield response.follow(link, callback=self.vacancy_parse)
    def vacancy_parse(self, response:HtmlResponse):
        name = response.xpath("//h1[@class = '_3mfro rFbjy s1nFK _2JVkc']").extract_first()
        salary = response.xpath("//span[@class = '_3mfro _2Wp8I ZON4b PlM3e _2JVkc']").extract()
        company = response.xpath("//div[contains(@class ,'_3zucV ')]//h2[@class = '_3mfro PlM3e _2JVkc _2VHxz _3LJqf _15msI']//text()").extract_first()
        experience = response.xpath("//span[@class = '_3mfro _1hP6a _2JVkc']//text()")[2].extract()
        type_of_work = response.xpath("//span[@class = '_3mfro _1hP6a _2JVkc']//text()")[3].extract()
        vac_text = response.xpath("//span[@class = '_3mfro _2LeqZ _1hP6a _2JVkc _2VHxz _15msI']//text()").extract()
        key_skills = None
        ##print(name,salary)
        yield Jobparser2Item(name = name, salary = salary, experience = experience,type_of_work = type_of_work,
                             vac_text = vac_text,key_skills = key_skills, company = company)



