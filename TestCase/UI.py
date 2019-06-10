from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

def input_demo(a):
    input_el = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/input')
    input_el.send_keys('亚索你是智障')
    time.sleep(2)
    input_el.clear()
    time.sleep(2)

def file_demo(a):
    file_el = driver.find_element_by_id('file1')
    file_el.send_keys('C:/Users/Administrator/Desktop/timg.jpg')
    time.sleep(2)

def radio_demo(a):
    radio_el = driver.find_elements_by_name('radio')
    radio_el[0].click()
    time.sleep(2)
    radio_el[1].click()
    time.sleep(2)

def check_demo(a):
    checkbox_els = driver.find_elements_by_class_name('checkbox')
    checkbox_els[0].click()
    time.sleep(2)
    checkbox_els[1].click()
    time.sleep(2)
    checkbox_els[2].click()
    time.sleep(2)

def button_demo(a):
    button_el = driver.find_element_by_xpath('//input[@value="普通按钮"]')
    time.sleep(1)
    button_el.click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    # driver.switch_to.alert.dismiss()

def input_demo1(a):
    input_el = driver.find_element_by_xpath('//input[@type="password"]')
    input_el.send_keys('wjs351')
    time.sleep(2)

def select_demo(a):
    select_el=driver.find_element_by_css_selector('body > table > tbody > tr:nth-child(12) > td:nth-child(2) > select')
    s = Select(select_el)
    s.select_by_index(2)
    s.select_by_value('z1')
    s.select_by_visible_text('周龙2')
    time.sleep(1)

def a_demo(a):
    driver.find_element_by_link_text('问问度娘').click()
    time.sleep(2)
    driver.back()
    time.sleep(1)
    driver.find_element_by_partial_link_text('京').click()
    time.sleep(2)
    driver.back()
    time.sleep(1)
    driver.forward()
    time.sleep(1)
    driver.refresh()
    time.sleep(1)

if __name__ == '__main__':
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    driver.get('http://192.168.60.146:8080/demo1.html')
    # time.sleep(2)
    # input_demo(driver)
    # file_demo(driver)
    # radio_demo(driver)
    # check_demo(driver)
    driver.quit()
    pass
