from selene import browser, have, by
import time

# уберу тесты с гуглом, чтобы не извращаться с капчей. Выполню задание для других поисковиков

# def test_google_should_find_selene(google):
#     browser.open('')
#     browser.element('[name="q"]').type('yashaka/selene').press_enter()
#     # Капча автоматически не проходится, поэтому костыль. Я за 5с мосты и светофоры нахожу, но возьмем с запасом
#     print('HUMAN, YOU HAVE 15s TO HELP ME')
#     time.sleep(15)
#     browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

#
#
# def test_google_should_show_captcha(google):
#     browser.open('')
#     browser.element('[name="q"]').type('yashaka/selene').press_enter()
#     browser.element('html').should(have.text('Об этой странице'))



def test_yandex_should_find_selene(yandex):
    browser.open('')
    browser.element(by.xpath("//input[@placeholder='Найдётся всё']")).type('yashaka/selene').press_enter()
    browser.element(by.xpath("//ul[@id='search-result']")).should(have.text('yashaka/selene'))




def test_duck_should_find_selene(duck):
    browser.open('')
    browser.element(by.xpath("//input[@placeholder='Поиск без отслеживания']")).type('yashaka/selene').press_enter()
    browser.element(by.xpath("//ol[@class='react-results--main']")).should(have.text('yashaka/selene'))



def test_yandeex_should_not_find_roll_head_on_keyboard(yandex):
    browser.open('')
    browser.element(by.xpath("//input[@placeholder='Найдётся всё']")).type('xLNJKFCddlkfjdklflkefu').press_enter()
    # a в консоли, если ткнуть на элемент, можно скопировать к нему селектор или х-пасс автоматически
    browser.element(EmptySearchResults__bmhicayzpyswl134xq-PRxbHrb > div > div.EmptySearchResults-Title).should(have.text("Ничего не нашли"))

# def test_duck_should_not_find_roll_head_on_keyboard(duck)
# а он любую фигню находит, сколько головой по клавиатуре не катайся