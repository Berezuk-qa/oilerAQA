import requests

def get_page_metrics(url, api_key):
    api_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = {
        'url': url,
        'key': api_key,
        'strategy': 'mobile',  # можно изменить на 'desktop' для десктопной версии
        'category': ['performance', 'accessibility', 'best-practices', 'seo']
    }

    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        # Извлечение нужных категорий и конвертация в проценты (от 0 до 100)
        performance = data['lighthouseResult']['categories']['performance']['score'] * 100
        accessibility = data['lighthouseResult']['categories']['accessibility']['score'] * 100
        best_practices = data['lighthouseResult']['categories']['best-practices']['score'] * 100
        seo = data['lighthouseResult']['categories']['seo']['score'] * 100

        return {
            'url': url,
            'performance': performance,
            'accessibility': accessibility,
            'best_practices': best_practices,
            'seo': seo
        }
    else:
        print(f"Error fetching data for {url}: {response.status_code}")
        return None

def analyze_pages(urls, api_key):
    results = []
    for url in urls:
        metrics = get_page_metrics(url, api_key)
        if metrics:
            results.append(metrics)
            print(f"Metrics for {url}:\n {metrics}\n")
    return results

# Пример использования функции
api_key = "AIzaSyCxh5G_ODaZS8gDH2cVuS5roosCRda6SjI"
urls = ["https://dev.oiler.ua/ua-ua/", "https://dev.oiler.ua/ua-ua/sto/", "https://dev.oiler.ua/ua-ua/shiny/filter/brand-continental/",
"https://dev.oiler.ua/ua-ua/shiny-continental-wintercontact-ts-870-195-55-r16-87h/"]
analyze_pages(urls, api_key)