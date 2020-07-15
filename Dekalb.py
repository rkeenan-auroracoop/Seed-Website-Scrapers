from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def CornCounter(): 
    counter = 2
    Brand = "Dekalb"
    SeedType = "Corn"
    while counter < 52:
        try: 
            productName = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(2) > span:nth-child(2)'% counter)
            traits = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(10) > p:nth-child(1)'% counter)
            traits = traits.text.replace("TRAIT: ", "")
            relativeMaturity = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1)'% counter)
            relativeMaturity = relativeMaturity.text.replace("RELATIVE MATURITY: ","")
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")      
        except: 
            break

def SoybeanCounter(): 
    counter = 2
    Brand = "Dekalb"
    SeedType = "Soybean"
    while counter < 32:
        try: 
            productName = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(2) > span:nth-child(2)'% counter)
            traits = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(10) > p:nth-child(1)'% counter)
            traits = traits.text.replace("TRAIT: ", "")
            relativeMaturity = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1)'% counter)
            relativeMaturity = relativeMaturity.text.replace("RELATIVE MATURITY: ","")
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")      
        except: 
            break

driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.dekalbasgrowdeltapine.com/en-us/seed-finder/corn.html#plid=9LN5233A6&crop=corn&territory=J6D&view=local')
time.sleep(5)

CornCounter()

driver.get('https://www.dekalbasgrowdeltapine.com/en-us/seed-finder/soybeans.html#territory=J6D&plid=9LN5233A6&view=local')
time.sleep(5)

SoybeanCounter()