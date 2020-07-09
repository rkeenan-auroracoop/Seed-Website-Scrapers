from requests_html import HTMLSession
from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def CornCounter(): 
    counter = 2
    Brand = "Brevant"
    SeedType = "Corn"
    while counter < 22:
        try: 
            productName = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(1) > a:nth-child(1)'% counter)
            traits = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(2)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(3) > div:nth-child(2) > span:nth-child(1)'% counter)
            silkGDUs = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(4) > div:nth-child(2) > span:nth-child(1)'% counter)
            counter += 1
            print(Brand + "\t" + productName.text + "\t" + traits.text + "\t" + SeedType + "\t" + relativeMaturity.text +  "\t" + silkGDUs.text)
        
        except: 
            break

def NextPage():
    sbtn = driver.find_element_by_css_selector('button.pager__button:nth-child(8)')
    driver.execute_script("arguments[0].click();", sbtn)
    time.sleep(5)

def BackToPageOne():
    sbtn = driver.find_element_by_css_selector('button.pager__button:nth-child(2)')
    driver.execute_script("arguments[0].click();", sbtn)
    time.sleep(5)

def SelectSilageCorn():
    time.sleep(3)
    driver.find_element_by_css_selector('select.crop-select:nth-child(1) > option:nth-child(2)').click()

def SelectSoybeans():
    time.sleep(3)
    driver.find_element_by_css_selector('select.crop-select:nth-child(1) > option:nth-child(3)').click()

def SelectSunflowers():
    time.sleep(3)
    driver.find_element_by_css_selector('select.crop-select:nth-child(1) > option:nth-child(4)').click()

def SelectConola():
    time.sleep(3)
    driver.find_element_by_css_selector('select.crop-select:nth-child(1) > option:nth-child(5)').click()

def SelectAlfalfa():
    time.sleep(3)
    driver.find_element_by_css_selector('select.crop-select:nth-child(1) > option:nth-child(6)').click()

session = HTMLSession()

url = 'https://brevant.com/products/'

r = session.get(url)

r.html.render(sleep=2, keep_page=True, scrolldown=1)


driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://brevant.com/products/')
time.sleep(5)


print("Page 1-Corn")
CornCounter()
NextPage()

print('Page 2-Corn')
CornCounter()
NextPage()

print('Page 3-Corn')
CornCounter()
NextPage()

print('Page 4-Corn')
CornCounter()
NextPage()

print('Page 5-Corn')
CornCounter()
NextPage()

print('Page 6-Corn')
CornCounter()

BackToPageOne()





SelectSilageCorn()

SelectSoybeans()

SelectSunflowers()

SelectConola()

SelectAlfalfa()

#access next seed type from dropdown

#driver.quit()
