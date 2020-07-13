from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def CornCounter(): 
    counter = 1
    Brand = "Agventure"
    SeedType = "Corn"
    while counter < 187:
        try: 
            productName = driver.find_element_by_css_selector('.cols-6 > tbody:nth-child(3) > tr:nth-child(% s) > td:nth-child(1) > a:nth-child(1)'% counter)
            traits = driver.find_element_by_css_selector('.cols-6 > tbody:nth-child(3) > tr:nth-child(% s) > td:nth-child(3)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('.cols-6 > tbody:nth-child(3) > tr:nth-child(% s) > td:nth-child(2)'% counter)
            counter += 1
            #Need to write these into JSON file as key/value pairs
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")               
        except: 
            break

def SoybeanCounter(): 
    counter = 1
    Brand = "Agventure"
    SeedType = "Soybeans"
    while counter < 145:
        try: 
            productName = driver.find_element_by_css_selector('.cols-4 > tbody:nth-child(3) > tr:nth-child(% s) > td:nth-child(1) > a:nth-child(1)'% counter)
            traits = driver.find_element_by_css_selector('.cols-4 > tbody:nth-child(3) > tr:nth-child(% s) > td:nth-child(3)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('.cols-4 > tbody:nth-child(3) > tr:nth-child(% s) > td:nth-child(2)'% counter)
            counter += 1
            #Need to write these into JSON file as key/value pairs
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")               
        except: 
            break

driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.agventure.com/products-technology/corn')
time.sleep(5)

CornCounter()

driver.get('https://www.agventure.com/products-technology/soybean')
time.sleep(5)

SoybeanCounter()

driver.close()