import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for pep_link in response.css('a.pep.reference.internal[href^="pep"]'):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number_name_pep = response.css('h1.page-title::text')
        yield PepParseItem(dict(
            number=number_name_pep.re_first(r"PEP\s*(\d+)"),
            name=number_name_pep.re_first(r"PEP\s*\d+\s*–\s*(.*)"),
            status=response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get(),
        ))
