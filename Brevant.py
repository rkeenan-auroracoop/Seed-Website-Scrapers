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
            #silkGDUs = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(4) > div:nth-child(2) > span:nth-child(1)'% counter)
            counter += 1
            #Need to write these into JSON file as key/value pairs
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break

def SilageCornCounter(): 
    time.sleep(5)
    counter = 2
    Brand = "Brevant"
    SeedType = "Silage Corn"
    while counter < 22:
        try: 
            productName = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(1) > a:nth-child(1)'% counter)
            traits = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(2)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(3) > div:nth-child(2) > span:nth-child(1)'% counter)
            counter += 1
            print(Brand + "\t" + productName.text + "\t" + traits.text + "\t" + SeedType + "\t" + relativeMaturity.text +  "\t" + "")
        
        except: 
            break

def SoybeansCounter(): 
    time.sleep(5)
    counter = 2
    Brand = "Brevant"
    SeedType = "Soybeans"
    while counter < 22:
        try: 
            productName = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(1) > a:nth-child(1)'% counter)
            traits = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(2)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(3) > div:nth-child(2) > span:nth-child(1)'% counter)
            #canopyType = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(4) > div:nth-child(2) > span:nth-child(1)'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")
        
        except: 
            break

'''def SunflowersCounter(): 
    time.sleep(5)
    counter = 2
    Brand = "Brevant"
    SeedType = "Sunflowers"
    while counter < 22:
        try: 
            productName = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(1) > a:nth-child(1)'% counter)
            traits = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(2)'% counter)
            daysToFlowering = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(3) > div:nth-child(2) > span:nth-child(1)'% counter)
            #oilContent = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(4) > div:nth-child(2) > span:nth-child(1) > title'% counter)
            counter += 1
            print(Brand + "\t" + productName.text + "\t" + traits.text + "\t" + SeedType + "\t" + daysToFlowering.text +  "\t" + "")
        
        except: 
            break

def ConolaCounter(): 
    time.sleep(5)
    counter = 2
    Brand = "Brevant"
    SeedType = "Conola"
    while counter < 22:
        try: 
            productName = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(1) > a:nth-child(1)'% counter)
            traits = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(2)'% counter)
            counter += 1
            print(Brand + "\t" + productName.text + "\t" + traits.text + "\t" + SeedType + "\t" +  "")
        
        except: 
            break

def AlfalfaCounter(): 
    time.sleep(5)
    counter = 2
    Brand = "Brevant"
    SeedType = "Alfala"
    while counter < 22:
        try: 
            productName = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(1) > a:nth-child(1)'% counter)
            traits = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(2)'% counter)
            winterHardiness = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(3) > div:nth-child(2) > span:nth-child(1)'% counter)
            fallDormancy = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(4) > div:nth-child(2) > span:nth-child(1)'% counter)
            counter += 1
            print(Brand + "\t" + productName.text + "\t" + traits.text + "\t" + SeedType+ "\t" + winterHardiness.text +  "\t" + fallDormancy.text)
        
        except: 
            break'''



def CornNextPage():
    sbtn = driver.find_element_by_css_selector('button.pager__button:nth-child(8)')
    driver.execute_script("arguments[0].click();", sbtn)
    time.sleep(5)

def SilageCornNextPage():
    sbtn = driver.find_element_by_css_selector('button.pager__button:nth-child(5)')
    driver.execute_script("arguments[0].click();", sbtn)
    time.sleep(5)

def SoybeansNextPage():
    sbtn = driver.find_element_by_css_selector('button.pager__button:nth-child(5)')
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

'''def SelectSunflowers():
    time.sleep(3)
    driver.find_element_by_css_selector('select.crop-select:nth-child(1) > option:nth-child(4)').click()

def SelectConola():
    time.sleep(3)
    driver.find_element_by_css_selector('select.crop-select:nth-child(1) > option:nth-child(5)').click()

def SelectAlfalfa():
    time.sleep(3)
    driver.find_element_by_css_selector('select.crop-select:nth-child(1) > option:nth-child(6)').click()'''



driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://brevant.com/products/')
time.sleep(5)


print("Page 1-Corn")
CornCounter()
CornNextPage()

print('Page 2-Corn')
CornCounter()
CornNextPage()

print('Page 3-Corn')
CornCounter()
CornNextPage()

print('Page 4-Corn')
CornCounter()
CornNextPage()

print('Page 5-Corn')
CornCounter()
CornNextPage()

print('Page 6-Corn')
CornCounter()

BackToPageOne()
#SelectSilageCorn()

#print("Page 1-Silage Corn")
#SilageCornCounter()
#SilageCornNextPage()

#print("Page 2-Silage Corn")
#SilageCornCounter()
#SilageCornNextPage()

#print("Page 3-Silage Corn")
#SilageCornCounter()

#ackToPageOne()


SelectSoybeans()

print("Page 1-Soybeans")
SoybeansCounter()
SoybeansNextPage()

print("Page 2-Soybeans")
SoybeansCounter()
SoybeansNextPage()

print("Page 3-Soybeans")
SoybeansCounter()

#BackToPageOne()

#SelectSunflowers()

#print("Page 1-Sunflowers")
#SunflowersCounter()

#SelectConola()

#print("Page 1-Conola")
#ConolaCounter()


#SelectAlfalfa()
#print("Page 1-Conola")
#AlfalfaCounter()

print("Scraping is done. Closing browser.")

driver.quit()
