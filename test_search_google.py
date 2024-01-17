from selene import have, browser, be

def test_selene(setting_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_empty_google(setting_browser):
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').type('45eeeeddddggghh5664455').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print("В поиске нет результатов...")