from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def CornCounterSetOne(): 
    counter = 1
    Brand = "Croplan"
    SeedType = "Corn"
    while counter < 19:
        try: 
            productName = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(2) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(2) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)'% counter)
            traits = traits.text[6:]
            relativeMaturity = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(2) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)'% counter)
            relativeMaturity = relativeMaturity.text.replace(" day", "")
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                print(Brand + "\t" + productName.text[0:30]  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")      
        except: 
            break

def CornCounterSetTwo(): 
    counter = 1
    Brand = "Croplan"
    SeedType = "Corn"
    while counter < 19:
        try: 
            productName = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(3) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(3) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)'% counter)
            traits = traits.text[6:]
            relativeMaturity = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(3) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)'% counter)
            relativeMaturity = relativeMaturity.text.replace(" day", "")
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                print(Brand + "\t" + productName.text[0:30]  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")      
        except: 
            break

def CornCounterSetThree(): 
    counter = 1
    Brand = "Croplan"
    SeedType = "Corn"
    while counter < 19:
        try: 
            productName = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(4) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(4) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)'% counter)
            traits = traits.text[6:]
            relativeMaturity = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(4) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)'% counter)
            relativeMaturity = relativeMaturity.text.replace(" day", "")
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                print(Brand + "\t" + productName.text[0:30]  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")      
        except: 
            break

def CornCounterSetFour(): 
    counter = 1
    Brand = "Croplan"
    SeedType = "Corn"
    while counter < 19:
        try: 
            productName = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(5) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(5) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)'% counter)
            traits = traits.text[6:]
            relativeMaturity = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(5) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)'% counter)
            relativeMaturity = relativeMaturity.text.replace(" day", "")
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                print(Brand + "\t" + productName.text[0:30]  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")      
        except: 
            break

def CornCounterSetFive(): 
    counter = 1
    Brand = "Croplan"
    SeedType = "Corn"
    while counter < 19:
        try: 
            productName = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(6) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(6) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)'% counter)
            traits = traits.text[6:]
            relativeMaturity = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(6) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)'% counter)
            relativeMaturity = relativeMaturity.text.replace(" day", "")
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                print(Brand + "\t" + productName.text[0:30]  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")      
        except: 
            break

def CornCounterSetSix(): 
    counter = 1
    Brand = "Croplan"
    SeedType = "Corn"
    while counter < 19:
        try: 
            productName = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(7) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(7) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)'% counter)
            traits = traits.text[6:]
            relativeMaturity = driver.find_element_by_css_selector('.seeds-grid-wrapper > div:nth-child(7) > div:nth-child(% s) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)'% counter)
            relativeMaturity = relativeMaturity.text.replace(" day", "")
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                print(Brand + "\t" + productName.text[0:30]  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")      
        except: 
            break





driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.winfieldunited.com/product/croplan-seed/crops/corn/seeds')
time.sleep(7)

driver.find_element_by_css_selector('#cookie-msg > div.medium-4.columns > a').click()
time.sleep(10)

# would not work with just a click method. Had to go JS route.
sbtn = driver.find_element_by_css_selector('span.page-number-by-page:nth-child(4)')
driver.execute_script("arguments[0].click();", sbtn)

print("Page 1-Corn")
time.sleep(5)

CornCounterSetOne()
CornCounterSetTwo()
CornCounterSetThree()
CornCounterSetFour()
CornCounterSetFive()
CornCounterSetSix()

sbtn = driver.find_element_by_css_selector('span.page-number:nth-child(2)')
driver.execute_script("arguments[0].click();", sbtn)

print("Page 2-Corn")
time.sleep(5)

CornCounterSetOne()
CornCounterSetTwo()
CornCounterSetThree()
CornCounterSetFour()
CornCounterSetFive()
CornCounterSetSix()

sbtn = driver.find_element_by_css_selector('span.page-number:nth-child(3)')
driver.execute_script("arguments[0].click();", sbtn)

print("Page 3-Corn")
time.sleep(5)

CornCounterSetOne()
CornCounterSetTwo()
CornCounterSetThree()
CornCounterSetFour()
CornCounterSetFive()
CornCounterSetSix()

sbtn = driver.find_element_by_css_selector('span.page-number:nth-child(4)')
driver.execute_script("arguments[0].click();", sbtn)

print("Page 4-Corn")
time.sleep(5)

CornCounterSetOne()
CornCounterSetTwo()
CornCounterSetThree()
CornCounterSetFour()
CornCounterSetFive()
CornCounterSetSix()