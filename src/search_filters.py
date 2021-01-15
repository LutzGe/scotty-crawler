from selenium import webdriver

from time import sleep


def search(driver, filters: dict, calls_only=False, screenshot=False):
    """Procura pelos chamados da área e retorna o arquivo onde o texto foi salvo\n
    driver: selenium webdriver\n
    areaid: área do scotty à buscar"""

    # abre o menu de filtros
    driver.execute_script('mostraFiltros()')
    
    # lugar aleatório que precisa ser clicado após o send_keys (às vezes)
    _empty_space = driver.find_element_by_id('areaid_lookupDescription')

    for key in filters.keys():
        print("Adicionando o filtro " + key)

        ## insere os filtros
        elem = driver.find_element_by_id(key)
        elem.clear()
        elem.send_keys(filters[key])

        # o tal do click extra
        _empty_space.click()

    # busca e espera
    search_elem = driver.find_element_by_id('search')
    search_elem.click()
    sleep(5)

    if screenshot:
        driver.save_screenshot('screenshots/screenshot' + _count_files('dist/') + '.png')

    # tabela de chamados
    table_elem = driver.find_element_by_id('GrdCallUser')
    
    ## Retorna a página inteira ou apenas a tabela de chamados
    if calls_only:
        page = table_elem
    else:
        page = driver

    return page
