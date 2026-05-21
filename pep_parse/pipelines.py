import csv
import datetime as dt
from collections import defaultdict

from pep_parse.constants import RESULTS_DIR


DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def open_spider(self, spider):
        RESULTS_DIR.mkdir(exist_ok=True)
        self.status_counter = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = RESULTS_DIR / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows([
                ('Статус', 'Количество'),
                *self.status_counter.items(),
                ('Всего', sum(self.status_counter.values()))
            ])
