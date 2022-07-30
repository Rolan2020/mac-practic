from xml.sax.xmlreader import Locator
from playwright.sync_api import Page, expect
# Declarar el fixture Page en el test function de pytest

# busar 'panda' en https://duckduckgo.com/
def test_research_duckduckgo(page: Page) -> None:
    # con page tenemos autocompletado

    page.goto("https://duckduckgo.com/")
    # con fill completamos ese campo
    page.locator('id=search_form_input_homepage').fill('panda')
    page.locator('id=search_button_homepage').click()
    # validamos que contenga el valor
    expect(page.locator('id=search_form_input_homepage')).to_have_value('panda')
    expect(page).to_have_title('DuckDuckGo — La privacidad, simplificada.')
    expect(page.locator('a[data-testid="result-title-a"]')).to_have_count(10)

