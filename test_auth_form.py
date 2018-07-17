from selenium import webdriver
import sys,time
 
def test_auth_form(browser):

    "Test Авторизация maximonline"
 
    if browser.lower() == 'firefox':

            driver = webdriver.Firefox()

    elif browser.lower() == 'chrome':

            driver = webdriver.Chrome()

    pass_check_counter = 0
    total_checks = 0

    driver.get('https://www.maximonline.ru') 

  
    if(driver.title == "Мужской журнал MAXIM Online. Официальный сайт лучшего мужского журнала MAXIM."):

        print ("Success: Заголовок правильный")
        pass_check_counter += 1

    else:

        print ("Failed: Заголовок не корректный")

    total_checks += 1
 
    driver.find_element_by_link_text('Войти').click()  

    elem_login = driver.find_element_by_name("regauth_login")
    elem_login.send_keys("2135ytzu@2odem.com")
    elem_pass = driver.find_element_by_name("regauth_pass")
    elem_pass.send_keys("123456789")
    time.sleep(1)
    driver.find_element_by_css_selector('.standard-button-newdesign').click()
    time.sleep(1)
    driver.save_screenshot('screenshot_enter.png')
    time.sleep(1)
 
    auth_profile = driver.find_element_by_link_text('5ytzu').click()

    if(driver.title == 'Личный профиль'):

        print ("Success: Авторизация успешна")
        pass_check_counter += 1

    else:

        print ("Failed: Ошибка авторизации")

    total_checks += 1

    driver.get('https://www.maximonline.ru') 

    if(driver.title == "Мужской журнал MAXIM Online. Официальный сайт лучшего мужского журнала MAXIM."):

        print ("Success: Заголовок правильный")
        pass_check_counter += 1

    else:

        print ("Failed: Заголовок не корректный")

    total_checks += 1

    time.sleep(1)

    exit_login = driver.find_element_by_css_selector('.logout')
    exit_login.click()

    if(driver.find_element_by_link_text("Войти")):

        print ("Success: Разлогинивание выполнено")
        pass_check_counter += 1

    else:

        print ("Failed: Разлогинивание не выполнено")
    total_checks += 1

    assert total_checks == pass_check_counter 

    driver.quit() 

if __name__=='__main__':
    browser = sys.argv[1] 
    text_auth_form(browser)
