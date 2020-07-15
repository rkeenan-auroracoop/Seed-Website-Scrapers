from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def CornCounter(): 
    counter = 1
    Brand = "Hoegemeyer"
    SeedType = "Corn"
    while counter < 22:
        try: 
            productName = driver.find_element_by_css_selector('div.content-segment--step-down-1:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(% s) > td:nth-child(2)'% counter)
            print(productName.text)
            productName = productName.text.replace("NEW - ", "")
            traits = driver.find_element_by_css_selector('div.content-segment--step-down-1:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(% s) > td:nth-child(4)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('div.content-segment--step-down-1:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(% s) > td:nth-child(3)'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break

def SoybeanCounter(): 
    counter = 1
    Brand = "Hoegemeyer"
    SeedType = "Soybeans"
    while counter < 22:
        try: 
            productName = driver.find_element_by_css_selector('div.content-segment--step-down-1:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(% s) > td:nth-child(2)'% counter)
            print(productName.text)
            productName = productName.text.replace("NEW - ", "")
            traits = driver.find_element_by_css_selector('div.content-segment--step-down-1:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(% s) > td:nth-child(4)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('div.content-segment--step-down-1:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(% s) > td:nth-child(3)'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break


def NextPage():
    sbtn = driver.find_element_by_css_selector('.pager__link--next')
    driver.execute_script("arguments[0].click();", sbtn)
    time.sleep(5)

driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.therightseed.com/products/corn')
time.sleep(10)

print("Page 1-Corn")
CornCounter()
NextPage()

print("Page 2-Corn")
CornCounter()
NextPage()

print("Page 3-Corn")
CornCounter()
NextPage()

print("Page 4-Corn")
CornCounter()
NextPage()

print("Page 5-Corn")
CornCounter()
NextPage()

print("Page 6-Corn")
CornCounter()
NextPage()

print("Page 7-Corn")
CornCounter()
NextPage()

print("Page 8-Corn")
CornCounter()
NextPage()

print("Page 9-Corn")
CornCounter()
NextPage()

print("Page 10-Corn")
CornCounter()
NextPage()

print("Page 11-Corn")
CornCounter()

driver.get('https://www.therightseed.com/products/soybeans')
time.sleep(10)

print("Page 1-Corn")
SoybeanCounter()
NextPage()

print("Page 2-Corn")
SoybeanCounter()
NextPage()

print("Page 3-Corn")
SoybeanCounter()
NextPage()

print("Page 4-Corn")
SoybeanCounter()
NextPage()

print("Page 5-Corn")
SoybeanCounter()
NextPage()

print("Page 6-Corn")
SoybeanCounter()
NextPage()

print("Page 7-Corn")
SoybeanCounter()

print("Hoeyemeyer is done.")