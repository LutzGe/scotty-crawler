from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup
from time import sleep

# set headless (não abre o navegador)
options = Options()
options.headless = True

# Abre a página de login do scotty, e espera carregar
print("Abrindo o browser...")

driver = webdriver.Firefox(options=options)
driver.get('https://www.univates.br/scotty2/')
sleep(5)

print("Página: " + driver.title)
print("Logando no sistema...")

# uid
id_elem = driver.find_element_by_id('uid')
id_elem.clear()
id_elem.send_keys("626442")

# pwd
pwd_elem = driver.find_element_by_id('pwd')
pwd_elem.clear()

with open('./.pwd') as pwd:
    pwd_elem.send_keys(pwd.read())

# 'dá enter' no login e espera carregar (de novo)
pwd_elem.send_keys(Keys.RETURN)
sleep(5)

print("Logado.")

areaid = '52'
print("Buscando chamados da área "+areaid)

driver.execute_script('mostraFiltros()')
## filtros
# abre os filtros
filtros_elem = driver.find_element_by_id('mlabel47')
filtros_elem.click()

# insere os dados
areaid_elem = driver.find_element_by_id('areaid')
areaid_elem.clear()
areaid_elem.send_keys(areaid)

# click extra por que precisa computar o valor inserido anteriormente
area_desc_elem = driver.find_element_by_id('areaid_lookupDescription')
area_desc_elem.click()

# busca e espera
search_elem = driver.find_element_by_id('search')
search_elem.click()
sleep(5)

# tabela de chamados
table_elem = driver.find_element_by_id('GrdCallUser')


with open('scraped.html', 'w') as out:
    out.write(table_elem.text)

# driver.save_screenshot('filtradoxxx.png')






# quit
driver.quit()