from selene import browser, have, by
import time

YANDEX_URL = 'https://ya.ru/'
GOOGLE_URL = 'https://google.com/'
DUCK_URL = 'https://duckduckgo.com/'

# уберу тесты с гуглом, чтобы не извращаться с капчей. Выполню задание для других поисковиков


def test_yandex_should_find_selene():
    browser.open(YANDEX_URL)
    browser.element(by.xpath("//input[@placeholder='Найдётся всё']")).type('yashaka/selene').press_enter()
    browser.element(by.xpath("//ul[@id='search-result']")).should(have.text('yashaka/selene'))




def test_duck_should_find_selene():
    browser.open(DUCK_URL)
    browser.element(by.xpath("//input[@placeholder='Поиск без отслеживания']")).type('yashaka/selene').press_enter()
    browser.element(by.xpath("//ol[@class='react-results--main']")).should(have.text('yashaka/selene'))



def test_yandeex_should_not_find_roll_head_on_keyboard():
    browser.open(YANDEX_URL)
    browser.element(by.xpath("//input[@placeholder='Найдётся всё']")).type('xLNJKFCddlkfjdklflkefu').press_enter()
    browser.element('.EmptySearchResults > div.EmptySearchResults-Title').should(have.text("Ничего не нашли"))

# def test_duck_should_not_find_roll_head_on_keyboard(duck)
# а он любую фигню находит, сколько головой по клавиатуре не катайся