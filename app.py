import requests
from decouple import config
from urllib.parse import urlparse

BASEURL = 'https://api-ssl.bitly.com/v4'
HEADERS = {
    'Authorization': 'Bearer ' + config('BITLY_API_TOKEN'),
    'Content-Type': 'application/json'
}


def is_bitlink(headers, url):
    bitlink = urlparse(url)._replace(scheme='').geturl()[2:]
    bitly_url = f'{BASEURL}/bitlinks/{bitlink}'
    response = requests.get(bitly_url, headers=headers)
    return response.ok


def shorten_link(headers, url):
    bitly_url = f'{BASEURL}/shorten'
    payload = {'long_url': url}
    response = requests.post(bitly_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(header, url):
    bitlink = urlparse(url)._replace(scheme='').geturl()
    bitly_url = f'{BASEURL}/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(bitly_url, headers=header)
    response.raise_for_status()
    return response.json()['total_clicks']


def main():
    user_input = input("Я могу сократить ссылку или показать сколько было кликов\nДавай ссылку: ")
    try:
        if is_bitlink(HEADERS, user_input):
            clicks = count_clicks(HEADERS, user_input)
            print(f"Всего кликов: {clicks}")
        else:
            short_url = shorten_link(HEADERS, user_input)
            print(f"Битлинк: {short_url}")
    except requests.exceptions.HTTPError as e:
        exit(f"Ошибочка получается: {e}")


if __name__ == '__main__':
    main()
