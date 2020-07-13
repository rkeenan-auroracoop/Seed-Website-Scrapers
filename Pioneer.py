from requests_html import HTMLSession
from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json


driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.pioneer.com/us/products/corn/corn-seed-finder.html')
time.sleep(5)

with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
    f1.write("Brand" + "\t" + "ProductName"  + "\t" + "TechnologySegment" + "\t" + "HybridFamily" + "\t" + "RelativeMaturity" + "\t" + "SeedType" + "\n")

def CornCounter():
    time.sleep(10)
    counter = 1
    Brand = "Pioneer"
    SeedType = "Corn"
    while counter < 11:
        try:          
            productName = driver.find_element_by_css_selector('.DTFC_LeftBodyLiner > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(% s) > td:nth-child(2) '% counter)
            crm = driver.find_element_by_css_selector('#seedGuideTable > tbody:nth-child(2) > tr:nth-child(% s) > td:nth-child(3)'% counter)
            technologySegment = driver.find_element_by_css_selector('#seedGuideTable > tbody:nth-child(2) > tr:nth-child(% s) > td:nth-child(4)'% counter)
            hybridFamily = driver.find_element_by_css_selector('#seedGuideTable > tbody:nth-child(2) > tr:nth-child(% s) > td:nth-child(5)'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text + "\t" + technologySegment.text + "\t" + hybridFamily.text + "\t" + crm.text + "\t" + SeedType + "\n")
        except:
            break

def GoToNextPage():
    time.sleep(10)
    counter = 2
    print("Page 1-Corn")
    while counter < 5:
        CornCounter()
        sbtn = driver.find_element_by_css_selector('a.fg-button:nth-child(% s)'% counter).click()
        print("Page " + str(counter) + "-Corn")
        counter += 1

def goToPageFive():
    time.sleep(10)
    CornCounter()
    sbtn = driver.find_element_by_css_selector('a.fg-button:nth-child(5)').click()
    print("Page " + str(5) + "-Corn")

def goToPageSix():
    time.sleep(10)
    CornCounter()
    sbtn = driver.find_element_by_css_selector('a.fg-button:nth-child(5)').click()
    print("Page " + str(6) + "-Corn")

def GoToPageSevenAndEight():
    time.sleep(10)
    counter = 6
    while counter < 9:   
        CornCounter()
        if counter == 6:
            sbtn = driver.find_element_by_css_selector('a.fg-button:nth-child(% s)'% counter).click()
            counter += 1
            print("Page " + str(counter) + "-Corn")
        elif counter == 7: 
            sbtn = driver.find_element_by_css_selector('a.fg-button:nth-child(% s)'% counter).click()
            counter += 1
            print("Page " + str(counter) + "-Corn")
        else:
            break
#CornCounter()
GoToNextPage()
goToPageFive()
goToPageSix()
GoToPageSevenAndEight()

print("Corn website has finished scraping.")


driver.get('https://www.pioneer.com/us/products/soybeans/soybean-seed-finder.html')
time.sleep(5)

def SoybeanCounter():
    time.sleep(10)
    counter = 1
    Brand = "Pioneer"
    SeedType = "Soybeans"
    while counter < 11:
        try:           
            productName = driver.find_element_by_css_selector('.DTFC_LeftBodyLiner > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(% s) > td:nth-child(2)'% counter)
            technologySegment = driver.find_element_by_css_selector('#seedGuideTable > tbody > tr:nth-child(% s) > td:nth-child(4)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('#seedGuideTable > tbody > tr:nth-child(% s) > td.textNowrap.sorting_1'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + technologySegment.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")
        except:
            break

def SelectPage2():
    time.sleep(10)
    counter = 2
    print("Page 1-Soybeans")
    while counter < 8:
        try:
            SoybeanCounter()
            sbtn = driver.find_element_by_css_selector('#seedGuideTable_paginate > span > a:nth-child(% s)'% counter).click()
            print("Page " + str(counter) + "-Soybeans")
            counter += 1
        except:
            break

SelectPage2()

print("Web scraping is done. Closing browser now...")

time.sleep(10)

driver.close()