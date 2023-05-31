import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('window-size=1900,1000')

navegador = webdriver.Chrome(options=options)

navegador.get('https://documentacao.mksolutions.com.br/')

sleep(2)

button_stay = navegador.find_element(By.ID, 'plusminus10158626-0')
button_stay.click()

site = BeautifulSoup(navegador.page_source, 'html.parser')
print(site.prettify())
