import requests
from decouple import config
from urllib.parse import urlparse


def is_bitlink(headers, url):
    parser = urlparse(url)
    bitlink = f"{parser.netloc}{parser.path}"
    bitly_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"
    response = requests.get(bitly_url, headers=headers)
    return response.ok


def shorten_link(headers, url):
    bitly_url = "https://api-ssl.bitly.com/v4/shorten"
    payload = {'long_url': url}
    response = requests.post(bitly_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(header, url):
    parser = urlparse(url)
    bitlink = f"{parser.netloc}{parser.path}"
    bitly_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    response = requests.get(bitly_url, headers=header)
    response.raise_for_status()
    return response.json()['total_clicks']


def main():
    user_input = input("Я могу сократить ссылку или показать сколько было кликов\nДавай ссылку: ")

    token = config('BITLY_API_TOKEN')
    headers = {'Authorization': f"Bearer {token}"}

    try:
        if is_bitlink(headers, user_input):
            clicks = count_clicks(headers, user_input)
            print(f"Всего кликов: {clicks}")
        else:
            short_url = shorten_link(headers, user_input)
            print(f"Битлинк: {short_url}")
    except requests.exceptions.HTTPError as e:
        print(f"Ошибочка получается: {e}")


if __name__ == '__main__':
    main()
