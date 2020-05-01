# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from jobparser2.items import Jobparser2Item

class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&text=python&page=0']

    def parse(self, response:HtmlResponse):
        # next_page = response.xpath("//a[@class='bloko-button HH-Pager-Controls-Next HH-Pager-Control']/@href")
        next_page = response.css("a.HH-Pager-Controls-Next::attr(href)").extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacansy_links = response.xpath("//a[@class='bloko-link HH-LinkModifier']/@href").extract()

        for link in vacansy_links:
            yield response.follow(link, callback=self.vacancy_parse)
    def vacancy_parse(self, response:HtmlResponse):
        name = response.css('div.vacancy-title h1::text').extract_first()
        salary = response.xpath("//p[@class='vacancy-salary']/span/text()").extract()
        company = response.xpath("//span[@class = 'bloko-section-header-2 bloko-section-header-2_lite']//text()").extract()
        experience = response.xpath("//span[@data-qa = 'vacancy-experience']//text()").extract_first()
        type_of_work = response.xpath("//p[@data-qa = 'vacancy-view-employment-mode']//text()").extract()
        vac_text = response.xpath("//div[@class = 'g-user-content']//text()").extract()
        key_skills = response.xpath("//div[@data-qa = 'bloko-tag bloko-tag_inline skills-element']//text()").extract()
        ##print(name,salary)
        yield Jobparser2Item(name = name, salary = salary, experience = experience,type_of_work = type_of_work,
                             vac_text = vac_text,key_skills = key_skills, company = company)


    
