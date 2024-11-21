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

        # Создание URL-отчета
        report_url = f"https://developers.google.com/speed/pagespeed/insights/?url={url}&tab=mobile"

        return {
            'url': url,
            'performance': performance,
            'accessibility': accessibility,
            'best_practices': best_practices,
            'seo': seo,
            'report_url': report_url  # Ссылка на отчет
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
urls = ["https://oiler.pro/ua-ua/", "https://oiler.pro/ua-ua/sto/", "https://oiler.pro/ua-ua/shiny/filter/brand-continental/",
"https://oiler.pro/ua-ua/zapchasti/shiny-continental-contipremiumcontact-6-fr-235-40-r18-91y/", "https://oiler.pro/ua-ua/sto/predprodajnaya-diagnostika-avto/",
"https://oiler.pro/ua-ua/sto/sto-lukyanovka/", "https://oiler.pro/ua-ua/avtotovary/masla/motornye-masla/filter/brand-motul/",
"https://oiler.pro/ua-ua/motul-6100-syn-nergy-5w-40/", "https://oiler.pro/ua-ua/blog/", "https://oiler.pro/ua-ua/zapchasti/category-amortizator-1/filter/brand-kyb/",
"https://oiler.pro/ua-ua/zapchasti/amortizator-kyb-334254/"]
analyze_pages(urls, api_key)

