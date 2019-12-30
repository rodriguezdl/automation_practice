from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

driver.get('https://blackboard.vcu.edu/webapps/login/?action=relogin')
login_usr = driver.find_element_by_name('user_id')
agree_btn = driver.find_element_by_name('agree_button')
login_usr.send_keys('rodriguezdl')
login_password = driver.find_element_by_name('password')
login_btn = driver.find_element_by_name('entry-login')
login_btn.click()
