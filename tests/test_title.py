import re, sys
from playwright.sync_api import Page, expect
sys.stdout.reconfigure(encoding='utf-8')
     # додав кодування sys дві строчки вище
def test_title_main_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/")
    # Перевірка title головна
    expect(page).to_have_title(re.compile("Oiler - технічне обслуговування та ремонт автомобілів."))

def test_title_carservice_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/sto/sto-obolon/")
    expect(page).to_have_title(re.compile("СТО на Оболоні: вул. Бережанська, 15"))

def test_title_masla_list_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/avtotovary/masla/motornye-masla/")
    expect(page).to_have_title(re.compile("Моторне масло, купити краще автомобільне моторне масло в Києві"))

def test_title_masla_card_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/motul-6100-synergie-10w-40/")
    expect(page).to_have_title(re.compile("Моторне масло Motul 6100 Synergie+ 10w-40 - Купити Моторне масло Motul 6100 Synergie+ 10w-40 | Oiler.pro"))

def test_title_posluga_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/sto/zamena-masla/")
    expect(page).to_have_title(re.compile("Заміна масла в двигуні в Києві - доступна ціна на послуги | СТО OILER"))

def test_title_akum_list_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/avtotovary/akkumulyatory/")
    expect(page).to_have_title(re.compile("Авто акумулятори"))

def test_title_amort_list_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/zapchasti/category-amortizator-1/")
    expect(page).to_have_title(re.compile("Амортизатор - Купити за вигідною ціною в Києві - Oiler.pro"))

def test_title_filtrmasla_card_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/zapchasti/masljanyj-fil-tr-mann-filter-hu-820-2-x/")
    expect(page).to_have_title(re.compile("Фільтр масляний MANN-FILTER HU 820/2 x"))

def test_title_shiny_list_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/shiny/")
    expect(page).to_have_title(re.compile("Шини - Купити шини для авто за вигідною ціною в Києві - oiler.pro"))

def test_title_shina_card_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/zapchasti/shini-rosava-bc-54-185-75-r16-92q/")
    expect(page).to_have_title(re.compile("Купити Шини Rosava BC-54 185/75 R16 92Q"))

def test_title_kontakty_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/kontakty/")
    expect(page).to_have_title(re.compile("Контакти - oiler.pro"))

def test_title_onas_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/o-nas/")
    expect(page).to_have_title(re.compile("Про нас - oiler.pro"))

def test_title_sto_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/sto/")
    expect(page).to_have_title(re.compile("СТО в Києві, Ремонт автомобіля за доступними цінами в Автосервісі OILER"))

def test_title_blog_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/blog/")
    expect(page).to_have_title(re.compile("Корисні статті та поради щодо ремонту та обслуговування автомобілів"))

def test_title_zapchasti_bmw_5_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/zapchasti/bmw/5-touring-g31/category-podveska---amortizacija_1/filter/brand-sachs/")
    expect(page).to_have_title(re.compile("Підвіска / амортизація SACHS для BMW 5 Touring"))

def test_title_maslo_3filtra_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/avtotovary/masla/motornye-masla/filter/brand-motul/viscosity-5w-40/specification-acea-b4/")
    expect(page).to_have_title(re.compile("Моторні масла Motul 5w-40 B4 - Купити за вигідною ціною в Києві - Oiler.pro"))

def test_title_maslo_2filtra_ua(page: Page):
    page.goto("https://oiler.pro/ua-ua/avtotovary/masla/motornye-masla/motornye-masla-vo-lvove/filter/brand-motul/")
    expect(page).to_have_title(re.compile("Моторні масла у Львові Motul"))

# Перевірка тайтлів для російськомовної версії сайту

def test_title_main_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/")
    # Перевірка title.
    expect(page).to_have_title(re.compile("Oiler - техническое обслуживание и ремонт автомобилей."))

def test_title_carservice_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/sto/sto-obolon/")
    expect(page).to_have_title(re.compile("СТО на Оболони: ул. Бережанская, 15 | Автосервис OILER"))

def test_title_masla_list_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/avtotovary/masla/motornye-masla/")
    expect(page).to_have_title(re.compile("Моторное масло, купить лучшее автомобильное моторное масло в Киеве"))

def test_title_masla_card_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/motul-6100-synergie-10w-40/")
    expect(page).to_have_title(re.compile("Купить Моторное масло Motul 6100 Synergie"))

def test_title_posluga_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/sto/zamena-masla/")
    expect(page).to_have_title(re.compile("Замена масла в двигателе в Киеве - доступная цена на услуги | СТО OILER"))

def test_title_akum_list_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/avtotovary/akkumulyatory/")
    expect(page).to_have_title(re.compile("Авто аккумуляторы. Купить автомобильный аккумулятор в Киеве в интернет магазине Oiler.pro"))

def test_title_amort_list_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/zapchasti/category-amortizator-1/")
    expect(page).to_have_title(re.compile("Амортизатор - Купить по выгодной цене в Киеве - Oiler.pro"))

def test_title_filtrmasla_card_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/zapchasti/masljanyj-fil-tr-mann-filter-hu-820-2-x/")
    expect(page).to_have_title(re.compile("Купить Масляный фильтр MANN-FILTER HU 820/2 x"))

def test_title_shiny_list_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/shiny/")
    expect(page).to_have_title(re.compile("Шины - Купить шины для авто по выгодной цене в Киеве - oiler.pro"))

def test_title_shina_card_ru(page: Page):
    page.goto("https://oiler.pro/ua-ua/zapchasti/shiny-michelin-pilot-sport-3-mo-acoustic-255-40-r20-101y-xl/")
    expect(page).to_have_title(re.compile("Купити Шини Michelin Pilot Sport 3"))

def test_title_kontakty_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/kontakty/")
    expect(page).to_have_title(re.compile("Контакты - oiler.pro"))

def test_title_onas_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/o-nas/")
    expect(page).to_have_title(re.compile("О нас - oiler.pro"))

def test_title_sto_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/sto/")
    expect(page).to_have_title(re.compile("СТО в Киеве, Ремонт автомобиля по доступным ценам в Автосервисе OILER"))

def test_title_blog_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/blog/")
    expect(page).to_have_title(re.compile("Полезные статьи и советы по ремонту и обслуживанию автомобилей"))


def test_title_zapchasti_bmw_5_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/zapchasti/bmw/5-touring-g31/category-podveska---amortizacija_1/filter/brand-sachs/")
    expect(page).to_have_title(re.compile("Подвеска / амортизация SACHS для BMW 5 Touring"))

def test_title_maslo_3filtra_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/avtotovary/masla/motornye-masla/filter/brand-motul/viscosity-5w-40/specification-acea-b4/")
    expect(page).to_have_title(re.compile("Моторные масла Motul 5w-40 B4"))

def test_title_maslo_2filtra_ru(page: Page):
    page.goto("https://oiler.pro/ua-ru/avtotovary/masla/motornye-masla/motornye-masla-vo-lvove/filter/brand-motul/")
    expect(page).to_have_title(re.compile("Моторные масла во Львове Motul"))
