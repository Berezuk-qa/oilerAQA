import requests


def get_page_metrics(url, api_key):
    api_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = {
        'url': url,
        'key': api_key,
        'strategy': 'mobile',  # можно изменить на 'desktop'
    }

    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()

        # Извлечение значений метрик с проверкой на наличие ключей
        performance = data['lighthouseResult']['categories'].get('performance', {}).get('score', 0) * 100
        accessibility = data['lighthouseResult']['categories'].get('accessibility', {}).get('score', 0) * 100
        best_practices = data['lighthouseResult']['categories'].get('best-practices', {}).get('score', 0) * 100
        seo = data['lighthouseResult']['categories'].get('seo', {}).get('score', 0) * 100

        # Ссылка на отчет с конкретным замером
        report_url = f"https://developers.google.com/speed/pagespeed/insights/?url={url}&tab=mobile"

        return {
            'url': url,
            'performance': performance,
            'accessibility': accessibility,
            'best_practices': best_practices,
            'seo': seo,
            'report_url': report_url
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
urls = ["https://oiler.pro/ua-ua/", "https://oiler.pro/ua-ua/sto/",
"https://oiler.pro/ua-ua/shiny/filter/brand-continental/"]
analyze_pages(urls, api_key)
