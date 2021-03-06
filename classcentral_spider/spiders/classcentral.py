# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class ClasscentralSpider(Spider):
    name = 'classcentral'
    allowed_domains = ['classcentral.com']
    start_urls = ['https://www.classcentral.com/subjects']

    def __init__(self, subject=None):
        self.subject = subject

    def parse(self, response):
        if self.subject:
            subject_url = response.xpath('//a[contains(@title, "Programming")]/@href').extract_first()
            absolute_subject_url = response.urljoin(subject_url)
            yield Request(absolute_subject_url,
                          callback=self.parse_subject)
        else:
            self.log('Scraping all subjects.')
            subjects = response.xpath('//h3/a[1]/@href').extract()
            for subject in subjects:
                absolute_subject_url = response.urljoin(subject)
                yield Request(absolute_subject_url,
                              callback=self.parse_subject)

    def parse_subject(self, response):
        pass
