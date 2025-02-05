import requests
from bs4 import BeautifulSoup


def get_html(url) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36'
    }

    r = requests.get(url, headers=headers)
    return r.text


def extract_car_brands(soup):
    results = []
    car_brands = soup.find_all('div', class_='c-search-panel-container__car-brands')
    for brand in car_brands:
        brands_list = brand.text.strip().split('\n')
        for brand_name in brands_list:
            if brand_name.strip():
                results.append(brand_name.strip())
    return results


def main() -> list:
    url = 'https://atcmoment.ru/'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    return extract_car_brands(soup)