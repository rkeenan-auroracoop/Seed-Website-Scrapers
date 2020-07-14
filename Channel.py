from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def CornCounter(): 
    counter = 2
    Brand = "Channel"
    SeedType = "Corn"
    while counter < 77:
        try: 
            productName = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(2) > span:nth-child(2)'% counter)
            traits = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(10) > p:nth-child(1)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1)'% counter)
            counter += 1
            if "TRAIT: " in traits.text:
                traits = traits.text.replace("TRAIT:", "")
            else:
                traits = traits.text
            if "RELATIVE MATURITY: " in relativeMaturity.text:
                relativeMaturity = relativeMaturity.text.replace("RELATIVE MATURITY: ", "")
            else:
                relativeMaturity = relativeMaturity.text
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")      
        except: 
            break

def SoybeanCounter(): 
    counter = 2
    Brand = "Channel"
    SeedType = "Soybean"
    while counter < 18:
        try: 
            productName = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(2) > span:nth-child(2)'% counter)
            traits = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(10) > p:nth-child(1)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('div.product-card-cell:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1)'% counter)
            counter += 1
            if "TRAIT: " in traits.text:
                traits = traits.text.replace("TRAIT:", "")
            else:
                traits = traits.text
            if "RELATIVE MATURITY: " in relativeMaturity.text:
                relativeMaturity = relativeMaturity.text.replace("RELATIVE MATURITY: ", "")
            else:
                relativeMaturity = relativeMaturity.text
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")      
        except: 
            break

driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')

driver.get('https://www.channel.com/en-us/products/seed-finder/corn.html#territory=NMD&plid=1333&view=local')
time.sleep(7)

CornCounter()

driver.get('https://www.channel.com/en-us/products/seed-finder/soybeans.html#territory=NMD&plid=1333&view=local')
time.sleep(7)

SoybeanCounter()

driver.close()