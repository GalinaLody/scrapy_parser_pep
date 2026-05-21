from pep_parse.constants import NAME_RESULTS_DIR, SPIDERS_MODULE

BOT_NAME = 'pep_parse'

SPIDER_MODULES = [SPIDERS_MODULE]
NEWSPIDER_MODULE = SPIDERS_MODULE

ROBOTSTXT_OBEY = True

FEED_EXPORT_ENCODING = 'utf-8'
FEEDS = {
    NAME_RESULTS_DIR+'/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
