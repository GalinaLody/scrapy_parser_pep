import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counter = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        print('НАЧАЛО')
        results = [
            ('Статус', 'Количество'),
            *self.status_counter.items(),
            ('Всего', sum(self.status_counter.values()))
        ]
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        print(f'ЗАПИСЬ {file_path}')
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(f, dialect=csv.unix_dialect).writerows(results)
