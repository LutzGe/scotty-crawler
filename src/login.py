from selenium.webdriver.common.keys import Keys

def login(driver, uid, pwd):
    """Faz login no scotty. O driver precisa estar na página de login."""
    
    print("Logando no sistema...")
    
    # uid
    uid_elem = driver.find_element_by_id('uid')
    uid_elem.clear()
    uid_elem.send_keys(uid)

    # pwd
    pwd_elem = driver.find_element_by_id('pwd')
    pwd_elem.clear()
    pwd_elem.send_keys(pwd)

    # 'dá enter' no login e espera carregar (de novo)
    pwd_elem.send_keys(Keys.RETURN)
    
    
    print("Logado.")