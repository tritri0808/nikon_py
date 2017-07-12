from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('D:\project\chromedriver.exe')

def login_method():
    delay = 15 # seconds
    wait = WebDriverWait(driver, delay)
    # get login
    driver.get("https://cms.nkisc.eu/iw-cc/command/iw.ccpro.filesys")
    assert "Login" in driver.title
    # fill user
    username = driver.find_element_by_id("iw_user")
    username.clear()
    username.send_keys("t.tran.eu")
    # username.send_keys(Keys.RETURN)
    # fill pass
    password = driver.find_element_by_id("iw_password")
    password.clear()
    password.send_keys("ThS7&Wf9bF")
    # password.send_keys(Keys.RETURN)
    # select by value
    select = Select(driver.find_element_by_id('iw_domain'))
    select.select_by_value('NIKON-ISC')
    wait.until(EC.element_to_be_clickable((By.ID, "iw_domain")))
    # click login
    button = driver.find_element_by_xpath("//*[@href='javascript:iw_do_login()']")
    button.click()
    assert "No results found." not in driver.page_source
    # driver.close()
def submit_method():
    delay = 10 # seconds
    wait = WebDriverWait(driver, delay)
    address='//nkbv-isc-04a/default/main/Nikon/EU/WORKAREA/main_wa/templatedata/en_EU/category_title_bar/data/'
    dcr='cutting_through_the_chaos'
    # input DCR
    inputDCR = wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='fs_location_external']")))
    inputDCR.clear()
    inputDCR.send_keys(address)
    inputDCR.send_keys(Keys.RETURN)
    # check DCR
    address_dcr=''.join((address,dcr))
    check_dcr="//input[@value='%s']" % address_dcr
    # switch iframe fs_content
    iframe_content = driver.find_element_by_name('fs_content')
    driver.switch_to.frame(iframe_content)
    # switch iframe fs_list
    driver.switch_to.frame(driver.find_element_by_xpath("//frame[@name='fs_list']")) 
    # click checkbox DCR
    check = driver.find_element_by_xpath(check_dcr)
    check.click()
    check = wait.until(EC.element_to_be_clickable((By.XPATH,check_dcr)))

if __name__ == '__main__':
    login_method()
    submit_method()