from requests_html import HTMLSession
from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#session = HTMLSession()

#url = 'https://www.pioneer.com/us/products/corn/corn-seed-finder.html'

#r = session.get(url)

#r.html.render(sleep=2, keep_page=True, scrolldown=1)

driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.pioneer.com/us/products/corn/corn-seed-finder.html')
time.sleep(5)

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
            print(Brand + "\t" + productName.text + "\t" + technologySegment.text + "\t" + hybridFamily.text + "\t" + crm.text + "\t" + SeedType)
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

print("Website is scraped. Closing browser.")




