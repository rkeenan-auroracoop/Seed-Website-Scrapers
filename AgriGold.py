from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def CornCounter(): 
    counter = 1
    Brand = "Agrigold"
    SeedType = "Corn"
    while counter < 112:
        try: 
            productName = driver.find_element_by_css_selector('div.snapshotHolder:nth-child(% s) > div:nth-child(1) > div:nth-child(1) > h2:nth-child(2)'% counter)
            traits = driver.find_element_by_css_selector('div.snapshotHolder:nth-child(% s) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('div.snapshotHolder:nth-child(% s) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)'% counter)
            counter += 1
            #Need to write these into JSON file as key/value pairs
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                #f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text.replace(' DAYS','') + "\t" + SeedType + "\n")
                      
        except: 
            break

def SoybeanCounter(): 
    counter = 1
    Brand = "Agrigold"
    SeedType = "Soybeans"
    while counter < 53:
        try: 
            productName = driver.find_element_by_css_selector('div.snapshotHolder:nth-child(% s) > div:nth-child(1) > div:nth-child(1) > h2:nth-child(2)'% counter)
            traits = driver.find_element_by_css_selector('div.snapshotHolder:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('div.snapshotHolder:nth-child(% s) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)'% counter)
            counter += 1
            #Need to write these into JSON file as key/value pairs
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                #f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text.replace("RELATIVE MATURITY ", "") + "\t" + SeedType + "\n")
                      
        except: 
            break

driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://agrigold.com/corn-hybrids/')
time.sleep(5)

CornCounter()

driver.get('https://agrigold.com/soybeans/')
time.sleep(5)
SoybeanCounter()

driver.close()