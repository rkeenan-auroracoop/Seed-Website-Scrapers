from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def CornCounterColumnOne(): 
    counter = 1
    Brand = "NC+"
    SeedType = "Corn"
    while counter < 27:
        try: 
            productName = driver.find_element_by_css_selector('div.sw-tab:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(% s) > h3:nth-child(1) > div:nth-child(1)'% counter)
            if "VT DOUBLE PRO" in productName.text:
                traits = "VT2PRO"
            elif "SMARTSTAX" in productName.text:
                traits = "SSTX"
            elif "CONV" in productName.text:
                traits = "CONV"
            elif " CON" in productName.text:
                traits = "CON"
            elif "DGVT DOUBLE PRO" in productName.text:
                traits = "DGVT2PRO"
            elif " RR" in productName.text:
                traits = "RR"
            elif "3111" in productName.text:
                traits = "VIP3111"
            else:
                traits = "***************Missing trait*******************"
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + "None"+ "\t" + SeedType + "\n")      
        except: 
            break

def CornCounterColumnTwo(): 
    counter = 1
    Brand = "NC+"
    SeedType = "Corn"
    while counter < 27:
        try: 
            productName = driver.find_element_by_css_selector('div.sw-tab:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(% s) > h3:nth-child(1) > div:nth-child(1)'% counter)
            if "VT DOUBLE PRO" in productName.text:
                traits = "VT2PRO"
            elif "SMARTSTAX" in productName.text:
                traits = "SSTX"
            elif "CONV" in productName.text:
                traits = "CONV"
            elif " CON" in productName.text:
                traits = "CON"
            elif "DGVT DOUBLE PRO" in productName.text:
                traits = "DGVT2PRO"
            elif " RR" in productName.text:
                traits = "RR"
            elif "3111" in productName.text:
                traits = "VIP3111"
            else:
                traits = "***************Missing trait*******************"
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + "None"+ "\t" + SeedType + "\n")      
        except: 
            break

def SoybeanCounterColumnOne(): 
    counter = 1
    Brand = "NC+"
    SeedType = "Soybeans"
    while counter < 27:
        try: 
            productName = driver.find_element_by_css_selector('div.sw-tab:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(% s) > h3:nth-child(1) > div:nth-child(1)'% counter)
            if "ENLIST E3" in productName.text:
                traits = "E3"
            elif "GT27" in productName.text:
                traits = "GT27"
            elif "ROUNDUP READY 2 XTEND" in productName.text:
                traits = "RR2X"
            else:
                traits = "None"
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + "None"+ "\t" + SeedType + "\n")      
        except: 
            break

def SoybeanCounterColumnTwo(): 
    counter = 1
    Brand = "NC+"
    SeedType = "Soybeans"
    while counter < 27:
        try: 
            productName = driver.find_element_by_css_selector('div.sw-tab:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(% s) > h3:nth-child(1) > div:nth-child(1)'% counter)
            if "ENLIST E3" in productName.text:
                traits = "E3"
            elif "GT27" in productName.text:
                traits = "GT27"
            elif "ROUNDUP READY 2 XTEND" in productName.text:
                traits = "RR2X"
            else:
                traits = "None"
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + "None"+ "\t" + SeedType + "\n")      
        except: 
            break


driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.nc-plus.com/our-products/')
time.sleep(5)

CornCounterColumnOne()

CornCounterColumnTwo()


sbtn = driver.find_element_by_css_selector('li.sw-tab:nth-child(2) > a:nth-child(1) > span:nth-child(1)')
driver.execute_script("arguments[0].click();", sbtn)
time.sleep(8)

SoybeanCounterColumnOne()

SoybeanCounterColumnTwo()

print("NC+ is finished scraping. ")