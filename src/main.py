from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from time import sleep, time

from os import listdir

# own
from search_filters import search
from login import login
from calls_parser import CallsParser

def main():
    try:
        if USE_LOG:
            with open('dist/'+ filename, 'r') as file:
                filtered_page = file.read()
        
        else:
            # set headless (não abre o navegador)
            options = Options()
            options.headless = True
            # Abre a página de login do scotty, e espera carregar
            print("Abrindo o browser...")
            driver = webdriver.Firefox(options=options)
            driver.get('https://www.univates.br/scotty2/')
            sleep(3)

            print("Página: " + driver.title)

            ## Login
            uid = 626442
            with open('./.pwd') as pwd:
                login(driver, uid, pwd.read())    
            
            sleep(5)

            ## Search
            filters = {
                'areaid':'52'
            }
            filtered_page = search(driver, filters)
            filtered_page = filtered_page.find_element_by_tag_name('html')
            filtered_page = filtered_page.get_attribute('outerHTML')
        # ## Parse
        parser = CallsParser(filtered_page)

        print(parser.get_total_calls())
        
        
    
    finally:
        if not USE_LOG:
            ## não remover
            driver.quit()
            ##

if __name__ == '__main__':

    USE_LOG = 0
    tempo_agora = time()
    keyword = 'parsed'
    files = listdir('dist/')
    file_time = 0

    for file in files:

        if (keyword in file) and '.html' in file:
            tmp_time = int(file[len(keyword):file.index('.html')])

            if tmp_time > file_time:
                file_time = tmp_time
        
    if (file_time != 0) and (tempo_agora - file_time) < 300:
        USE_LOG = 1
        filename = file
    print('USE_LOG: ' + str(USE_LOG))

    main()