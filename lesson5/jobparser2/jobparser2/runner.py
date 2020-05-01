from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from jobparser2 import settings
from jobparser2.spiders.hhru import  HhruSpider
from jobparser2.spiders.sj import SjSpider
# Get settings
if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
#tell what spider to start
    process = CrawlerProcess(settings = crawler_settings)
    process.crawl(HhruSpider)
    process.crawl(SjSpider)
#start process
    process.start()
