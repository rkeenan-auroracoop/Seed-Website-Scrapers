from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def CornCounter(): 
    counter = 2
    #Brand = "Brevant"
    SeedType = "Corn"
    while counter < 63:
        try: 
            brand = driver.find_element_by_css_selector('.seeds_list > tbody:nth-child(1) > tr:nth-child(%s) > td:nth-child(1)'% counter)
            productName = driver.find_element_by_css_selector('.seeds_list > tbody:nth-child(1) > tr:nth-child(%s) > td:nth-child(2) > a:nth-child(1)'% counter)
            #traits = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(2)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('.seeds_list > tbody:nth-child(1) > tr:nth-child(%s) > td:nth-child(3)'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(brand.text + "\t" + productName.text  + "\t" + "None" + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break

def SoybeanCounter(): 
    counter = 2
    #Brand = "Brevant"
    SeedType = "Soybeans"
    while counter < 63:
        try: 
            brand = driver.find_element_by_css_selector('.seeds_list > tbody:nth-child(1) > tr:nth-child(%s) > td:nth-child(1)'% counter)
            productName = driver.find_element_by_css_selector('.seeds_list > tbody:nth-child(1) > tr:nth-child(%s) > td:nth-child(2) > a:nth-child(1)'% counter)
            #traits = driver.find_element_by_css_selector('div.product-results__result:nth-child(% s) > div:nth-child(2)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('.seeds_list > tbody:nth-child(1) > tr:nth-child(%s) > td:nth-child(3)'% counter)
            counter += 1

            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(brand.text + "\t" + productName.text  + "\t" + "None" + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break

driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.robseeco.com/products/?seed_category=corn&seed_tag=western-nebraska-eastern-wyoming-western-kansas-colorado')
time.sleep(5)

CornCounter()

driver.get('https://www.robseeco.com/products/?seed_category=soybeans&seed_tag=central-eastern-nebraska')
time.sleep(5)

print("\n" + "\n" + "SOYBEANS" + "\n" + "\n")

SoybeanCounter()