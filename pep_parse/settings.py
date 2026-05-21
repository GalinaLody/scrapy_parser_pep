from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
NAME_RESULTS_DIR = 'results'
RESULTS_DIR = BASE_DIR / NAME_RESULTS_DIR


BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]


ROBOTSTXT_OBEY = True

FEED_EXPORT_ENCODING = 'utf-8'
FEEDS = {
    f'{NAME_RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
