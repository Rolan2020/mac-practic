"""
https://www.youtube.com/watch?v=SjNpSGW4otM

pip install --upgrade pip
pip install playwright
playwright install

Instalar pytest-playwright
PARA MAC usas -> pip3 install pytest-playwright
"""
#  importamos para usar page y pytest
from playwright.sync_api import Page
import pytest

# Es importante que tanto Scripts como funciones tengan el prefijo "test" adelante -> test_ejem.py
# creamos funcion con def
# especificar el browser para un solo test
#@pytest.mark.only_browser('chromium')
def test_title(page: Page): # traemos el parametro Page
    #page.goto('https://www.saucedemo.com/') # redirecciona
    page.goto('/') # habilita usar path desde la consola
    # pytest --headed --base-url <URL>

    # asertion para validar nombre de titulo
    assert page.title()=='Swag Labs'

# skipear un browser
#@pytest.mark.skip_browser('chromium')
def test_inventory_page(page: Page):
    page.goto('/inventory.html')
    assert page.inner_text('h3')=="Epic sadface: You can only access '/inventory.html' when you are logged in."

"""
>pytest --headed --base-url https://www.saucedemo.com/ --browser webkit --browser chromium --slowmo 3000
como ejecutar solo chrome y no chromium -> --browser-channel chrome

Verificar la trasabilidad de los test
tener un logs de las ejecuciones para ver el paso a paso
trace de cada ejecucion --tracing on
trace solo cuando algo falla -- tracing retain-on-failure
Esto genera un folder -> test-results (genera zip. por test)
podemos ver el contenido con https://trace.playwright.dev/
"""