import asyncio
import json
import pytest
from playwright.async_api import async_playwright

# Приклад із постмана https://prnt.sc/WBrdhDZIJqFd
API_URL = "https://api.binotel.com/api/4.0/stats/call-details.json"
HEADERS = {"Content-Type": "application/json"}
DATA = {
    "key": "b52431-0b58461",
    "secret": "8c7cb4-7dfb72-8afbf5-0cd2e6-77a8a471",
    "generalCallID": ["5692793452"]
}


@pytest.mark.asyncio
async def test_api_Binotel_call_details():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        request = await context.request.post(API_URL, headers=HEADERS, data=DATA)

        assert request.status == 200, f"Ошибка: {request.status}"
        response_data = await request.json()

        print("Ответ API:")
        print(json.dumps(response_data, indent=4, ensure_ascii=False))

        await browser.close()
