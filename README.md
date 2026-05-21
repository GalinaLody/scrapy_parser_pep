# Описание проекта
scrapy_parser_pep - это парсер документации PEP. Парсер делает следующее:
- собирает ссылки на документации PEP, переходить по ним и записывает в файл номер PEP, наименгование PEP, статус PEP;
- собирает и записывает в отдельный файл информацию о количестве PEP в каждом статусе и общее количество PEP.


## Технологический стек проекта.
- Python 3.9
- Scrapy 2.5.1

### Как запустить проект Yacut:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:GalinaLody/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
## Примеры запуска парсера
Для запуска парсера введите команду:

```
scrapy crawl pep
```

## Автор.

[Галина Лодыгина](Zolotova-87-gali@yandex.ru)