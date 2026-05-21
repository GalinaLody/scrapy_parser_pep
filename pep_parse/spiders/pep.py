import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_pep_links = response.css('a.pep.reference.internal[href^="pep"]')
        for pep_link in all_pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number_name_pep = response.css('h1.page-title::text')
        data = {
            'number': int(number_name_pep.re_first(r"PEP\s*(\d+)")),
            'name': number_name_pep.re_first(r"PEP\s*\d+\s*–\s*(.*)"),
            'status': response.css('dt:contains("Status") + dd abbr::text').get(),
        }
        yield PepParseItem(data)
