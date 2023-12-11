# urlshortner v.0.5

Простой скрипт Python для взаимодействия с Bitly API для сокращения длинных URL-адресов или получения статистики кликов
для Bitlinks.

http://loooooooooooooooooooooooooong.url >> http://short.url

### Environment

Python 3.x

### Requirements

- requests~=2.31.0
- python-decouple==3.8

Установка зависимостей

```shell
pip install -r requirements.txt
```

### Environments variables

- Bitly API Token. Получить [тут](https://dev.bitly.com/docs/getting-started/authentication/)

### Run

1. Клонировать репозиторий
2. Создать в проекте `.env` файл и добавить Bitly API токен

```dotenv
BITLY_API_TOKEN=<token>
```

3. Запустить скрипт

```shell
python app.py
```

