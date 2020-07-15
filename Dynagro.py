from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def CornCounter(): 
    counter = 1
    Brand = "Dynagro"
    SeedType = "Corn"
    while counter < 187:
        try: 
            productName = driver.find_element_by_css_selector('a.crop-search-products-result:nth-child(% s) > div:nth-child(1) > div:nth-child(1)'% counter)
            traits = driver.find_element_by_css_selector('a.crop-search-products-result:nth-child(% s) > div:nth-child(2) > div:nth-child(3)'% counter)
            traits = traits.text.replace("Trait: ", "")
            relativeMaturity = driver.find_element_by_css_selector('a.crop-search-products-result:nth-child(% s) > div:nth-child(2) > div:nth-child(1)'% counter)
            relativeMaturity = relativeMaturity.text.replace("RM: ", "")
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")               
        except: 
            break

def SoybeanCounter(): 
    counter = 1
    Brand = "Dynagro"
    SeedType = "Soybeans"
    while counter < 150:
        try: 
            productName = driver.find_element_by_css_selector('a.crop-search-products-result:nth-child(% s) > div:nth-child(1) > div:nth-child(1)'% counter)
            traits = driver.find_element_by_css_selector('a.crop-search-products-result:nth-child(% s) > div:nth-child(2) > div:nth-child(2)'% counter)
            traits = traits.text.replace("Trait: ", "")
            relativeMaturity = driver.find_element_by_css_selector('a.crop-search-products-result:nth-child(% s) > div:nth-child(2) > div:nth-child(1)'% counter)
            relativeMaturity = relativeMaturity.text.replace("RM: ", "")
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")               
        except: 
            break


driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.dynagroseed.com/products/corn/')
time.sleep(10)

CornCounter()

driver.get('https://www.dynagroseed.com/products/soybean/')
time.sleep(10)

SoybeanCounter()