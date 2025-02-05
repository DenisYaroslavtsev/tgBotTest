from bs4 import BeautifulSoup
from pars_site.pars import get_html


def extract_car_models(soup) -> dict:
    results = {}
    model_links = soup.find_all('a', class_='c-search-column__item')

    for model in model_links:
        href = model['href']
        if 'mercedes-benz' in href:
            model_name = model.get_text(strip=True)
            model_name = model_name.replace("Mercedes-Benz", "").strip()
            if model_name:
                results[model_name] = results.get(model_name, 0)

    return results


def extract_generations(soup):
    results = []
    span_tags = soup.find_all('span', class_='l-flex--middle')

    for span in span_tags:
        generation_info = span.get_text(strip=True)
        results.append(generation_info)

    return results


def main():
    url = 'https://atcmoment.ru/mercedes-benz/'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    return extract_car_models(soup)


def models_generations() -> dict:
    model_ms_benz = main()
    for generation in model_ms_benz.keys():
        url = f"https://atcmoment.ru/mercedes-benz/{generation.lower()}"
        html = get_html(url)
        soup = BeautifulSoup(html, 'lxml')
        generations = extract_generations(soup)
        model_ms_benz[generation] = generations
    return model_ms_benz

