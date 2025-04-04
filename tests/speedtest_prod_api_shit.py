from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
import requests

# === Настройки Google Sheets ===
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1ncsEErmO-Uejzdxx3rjdbG7R3dU6VM5c2C_To-bKrJY"
SHEET_NAME = "Лист1"

# === Авторизация в Google Sheets ===
creds = Credentials.from_service_account_file("C:/pythonPRO/oilerAQA/tests/credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

# === Получение PageSpeed метрик ===
def get_page_metrics(url, api_key):
    api_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = {
        'url': url,
        'key': api_key,
        'strategy': 'mobile',
        'category': ['performance', 'accessibility', 'best-practices', 'seo']
    }

    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'performance': data['lighthouseResult']['categories']['performance']['score'] * 100,
            'accessibility': data['lighthouseResult']['categories']['accessibility']['score'] * 100,
            'best_practices': data['lighthouseResult']['categories']['best-practices']['score'] * 100,
            'seo': data['lighthouseResult']['categories']['seo']['score'] * 100
        }
    else:
        print(f"Error fetching data for {url}: {response.status_code}")
        return None

# === Запись метрик в таблицу в формате C1: дата, C2: perf, C3: access и т.д. ===
def write_metrics_to_sheet(urls, api_key):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    existing_data = sheet.get_all_values()
    col_index = max(len(existing_data[0]), 2) + 1 if existing_data else 3

    sheet.update_cell(1, col_index, timestamp)

    row = 2
    for url in urls:
        metrics = get_page_metrics(url, api_key)
        if metrics:
            sheet.update_cell(row, col_index, round(metrics['performance']))
            sheet.update_cell(row + 1, col_index, round(metrics['accessibility']))
            sheet.update_cell(row + 2, col_index, round(metrics['best_practices']))
            sheet.update_cell(row + 3, col_index, round(metrics['seo']))
            row += 4

# === Запуск ===
api_key = "AIzaSyCxh5G_ODaZS8gDH2cVuS5roosCRda6SjI"
urls = [
    "https://oiler.pro/ua-ua/",
    "https://oiler.pro/ua-ua/sto/",
    "https://oiler.pro/ua-ua/shiny/filter/brand-continental/",
    "https://oiler.pro/ua-ua/zapchasti/shiny-continental-contipremiumcontact-6-fr-235-40-r18-91y/",
    "https://oiler.pro/ua-ua/sto/predprodajnaya-diagnostika-avto/",
    "https://oiler.pro/ua-ua/sto/sto-lukyanovka/",
    "https://oiler.pro/ua-ua/avtotovary/masla/motornye-masla/filter/brand-motul/",
    "https://oiler.pro/ua-ua/motul-6100-syn-nergy-5w-40/",
    "https://oiler.pro/ua-ua/blog/",
    "https://oiler.pro/ua-ua/blog/oshibka-epc-prichiny-poyavleniya-i-sposoby-ustraneniya/",
    "https://oiler.pro/ua-ua/zapchasti/category-amortizator-1/filter/brand-kyb/",
    "https://oiler.pro/ua-ua/zapchasti/amortizator-kyb-334254/"
]

write_metrics_to_sheet(urls, api_key)
