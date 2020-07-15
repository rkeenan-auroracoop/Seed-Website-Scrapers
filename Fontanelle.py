from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def CornCounter(): 
    counter = 2
    Brand = "Fontanelle"
    SeedType = "Corn"
    while counter < 65:
        try: 
            productName = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(2) > span:nth-child(2)'% counter)
            traits = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(10)'% counter)
            traits = traits.text.replace("TRAIT: ","")
            relativeMaturity = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(2) '% counter)
            relativeMaturity = relativeMaturity.text.replace("RELATIVE MATURITY: ", "")
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")               
        except: 
            print("Corn is done.")
            break

def SoybeanCounter(): 
    counter = 2
    Brand = "Fontanelle"
    SeedType = "Soybeans"
    while counter < 65:
        try: 
            productName = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(2) > span:nth-child(2)'% counter)
            traits = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(10)'% counter)
            traits = traits.text.replace("TRAIT: ","")
            relativeMaturity = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(2) '% counter)
            relativeMaturity = relativeMaturity.text.replace("RELATIVE MATURITY: ", "")
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")               
        except: 
            print("Corn is done.")
            break

driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.fontanelle.com/en-us/products/corn.html')
time.sleep(10)

#input text into box with CSS Selector: #zipcode
zipCodeInput = driver.find_element_by_css_selector('#zipcode')
zipCodeInput.send_keys("68365")
#wait 5 seconds
time.sleep(10)

#then click button Search button. 
sbtn = driver.find_element_by_css_selector('#entry-form > div.mdc-layout-grid__inner.horizontal-search.show-search > div.mdc-layout-grid__cell.mdc-layout-grid__cell--span-4-desktop.mdc-layout-grid__cell--span-2-tablet.no-location.search-seed-list > button > span')
driver.execute_script("arguments[0].click();", sbtn)

time.sleep(10)

CornCounter()

driver.get('https://www.fontanelle.com/en-us/products/soybeans.html#view=national')
time.sleep(10)

SoybeanCounter()