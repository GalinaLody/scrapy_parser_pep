import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import RESULTS_DIR


DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counter = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_name = 'status_summary_{}.csv'.format(
            dt.datetime.now().strftime(DATETIME_FORMAT)
        )
        # Не могу перенести file_path из-за тестов Практикума.
        # На сколько я поняла, если выносить file_path,
        # то неучитывается подмена директорий в тестах,
        # файл записывается в реальную директорию results и потом тесты
        # не могут наийти второй файл в подменной директори и падают.
        file_path = RESULTS_DIR / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows((
                ('Статус', 'Количество'),
                *self.status_counter.items(),
                ('Всего', sum(self.status_counter.values()))
            ))
