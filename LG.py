from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def CornCounter(): 
    counter = 1
    Brand = "LG Seeds"
    SeedType = "Corn"
    while counter < 105:
        try: 
            productName = driver.find_element_by_css_selector('tr.ng-scope:nth-child(% s) > td:nth-child(2) > a:nth-child(1)'% counter)
            #print(productName.text)
            traits = driver.find_element_by_css_selector('tr.ng-scope:nth-child(% s) > td:nth-child(5) '% counter)
            if "Conventional" in traits.text:
                traits = "CONV"
            elif "DroughtGard" in traits.text:
                traits = "DROUGHTGARD VT2PRO RIB"
            elif "VT Double Pro" in traits.text and "RIB" in traits.text:
                traits = "VT2PRO RIB"
            elif "Roundup Ready" in traits.text:
                traits = "RR"
            elif "3120" in traits.text:
                traits = "3120 E-Z"
            elif "SmartStax" in traits.text and "RIB" in traits.text:
                traits = "SSTX RIB"
            elif "3220 E-Z" in traits.text:
                traits = "3220 E-Z REFUGE"
            elif "3220A E-Z" in traits.text:
                traits = "3220A E-Z REFUGE"
            elif "5222 E-Z" in traits.text:
                traits = "5222 E-Z REFUGE"
            elif "3111" in traits.text:
                traits = "3111"
            elif "Trecepta" in traits.text and "RIB" in traits.text:
                traits = "TRECEPTA RIB"
            elif "Trecepta" in traits.text:
                traits = "Trecepta"
            elif  "SmartStax" in traits.text:
                traits = "SSTX"
            elif "3110" in traits.text:
                traits = "3110"
            elif "VT Double Pro" in traits.text:
                traits = "VT2PRO"
            elif "5222" in traits.text:
                traits = "5222"
            else:
                print("*************Missing")
            #print(traits)
            relativeMaturity = driver.find_element_by_css_selector('tr.ng-scope:nth-child(% s) > td:nth-child(3)'% counter)
            #print(relativeMaturity)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break

def SoybeanCounter(): 
    counter = 1
    Brand = "LG Seeds"
    SeedType = "Soybeans"
    while counter < 50:
        try: 
            productName = driver.find_element_by_css_selector('tr.ng-scope:nth-child(% s) > td:nth-child(2) > a:nth-child(1)'% counter)
            #print(productName.text)
            traits = driver.find_element_by_css_selector('tr.ng-scope:nth-child(% s) > td:nth-child(5) '% counter)
            if "Conventional" in traits.text:
                traits = "CONV"
            elif "Roundup Ready 2 Xtend" in traits.text:
                traits = "RR2X"
            elif "Enlist E3" in traits.text:
                traits = "E3"
            else:
                print("*************Missing")
            #print(traits)
            relativeMaturity = driver.find_element_by_css_selector('tr.ng-scope:nth-child(% s) > td:nth-child(3)'% counter)
            #print(relativeMaturity)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break


driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.lgseeds.com/products/corn')
time.sleep(5)

sbtn = driver.find_element_by_css_selector('#tt1-button')
driver.execute_script("arguments[0].click();", sbtn)
time.sleep(5)

CornCounter()

driver.get('https://www.lgseeds.com/products/soybeans')
time.sleep(5)

SoybeanCounter()


print("LG Seeds is scraped.")