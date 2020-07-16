from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def CornCounter(): 
    counter = 1
    Brand = "Legend"
    SeedType = "Corn"
    while counter < 150:
        #if counter is even number, tr.even path for ProductName
        try:
            if counter % 2 == 0:
                productName = driver.find_element_by_css_selector('tr.even:nth-child(% s) > td:nth-child(4)'% counter)
                #print(productName.text)
                if "CONV" in productName.text:
                    traits = "CONV"
                elif "VT2PRIB" in productName.text:
                    traits = "VT2PRIB"
                elif "RR" in productName.text:
                    traits = "RR"
                elif  "GT" in productName.text:
                    traits = "GT"
                elif "VIP3220EZREF" in productName.text:
                    traits = "VIP3220EZREF"
                elif "VT2P" in productName.text:
                    traits = "VT2P"
                elif "DC5122EZREF" in productName.text:
                    traits = "DC5122EZREF"
                elif "GENSSRIB" in productName.text:
                    traits = "GENSSRIB"
                elif "3122EZREF" in productName.text:
                    traits = "3122EZREF"
                elif "3010A" in productName.text:
                    traits = "3010A"
                elif "VIP3110" in productName.text:
                    traits = "VIP3110"
                elif "3011A" in productName.text:
                    traits = "3011A"
                elif "3120EZREF" in productName.text:
                    traits = "3120EZREF"
                elif "DC5222AEZREF" in productName.text:
                    traits = "DC5222AEZREF"
                elif "VIP3220AEZREF" in productName.text:
                    traits = "VIP3220AEZREF"
                elif "VIP3330EZREF" in productName.text:
                    traits = "VIP3330EZREF"
                else:
                    traits = "None"
                relativeMaturity = driver.find_element_by_css_selector('tr.even:nth-child(% s) > td:nth-child(5)'% counter)
                counter += 1
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")    
        #else: tr.odd path
            else:
                productName = driver.find_element_by_css_selector('tr.odd:nth-child(% s) > td:nth-child(4)'% counter)
                #print(productName.text)
                if "CONV" in productName.text:
                    traits = "CONV"
                elif "VT2PRIB" in productName.text:
                    traits = "VT2PRIB"
                elif "RR" in productName.text:
                    traits = "RR"
                elif  "GT" in productName.text:
                    traits = "GT"
                elif "VIP3220EZREF" in productName.text:
                    traits = "VIP3220EZREF"
                elif "VT2P" in productName.text:
                    traits = "VT2P"
                elif "DC5122EZREF" in productName.text:
                    traits = "DC5122EZREF"
                elif "GENSSRIB" in productName.text:
                    traits = "GENSSRIB"
                elif "3122EZREF" in productName.text:
                    traits = "3122EZREF"
                elif "3010A" in productName.text:
                    traits = "3010A"
                elif "VIP3110" in productName.text:
                    traits = "VIP3110"
                elif "3011A" in productName.text:
                    traits = "3011A"
                elif "3120EZREF" in productName.text:
                    traits = "3120EZREF"
                elif "DC5222AEZREF" in productName.text:
                    traits = "DC5222AEZREF"
                elif "VIP3220AEZREF" in productName.text:
                    traits = "VIP3220AEZREF"
                elif "VIP3330EZREF" in productName.text:
                    traits = "VIP3330EZREF"
                else:
                    traits = "None"
                #print(productName.text + "\t" + traits)
                relativeMaturity = driver.find_element_by_css_selector('tr.odd:nth-child(% s) > td:nth-child(5)'% counter)
                counter += 1
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName.text  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")        
        except: 
            break

def SoybeanCounter(): 
    counter = 1
    Brand = "Legend"
    SeedType = "Soybeans"
    while counter < 150:
        #if counter is even number, tr.even path for ProductName
        try:
            if counter % 2 == 0:
                productName = driver.find_element_by_css_selector('tr.even:nth-child(% s) > td:nth-child(3)'% counter)
                #print(productName.text)
                traits = driver.find_element_by_css_selector('tr.even:nth-child(% s) > td:nth-child(4)'% counter)
                relativeMaturity = driver.find_element_by_css_selector('tr.even:nth-child(% s) > td:nth-child(5)'% counter)
                counter += 1
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")    
        #else: tr.odd path
            else:
                productName = driver.find_element_by_css_selector('tr.odd:nth-child(% s) > td:nth-child(3)'% counter)
                #print(productName.text)
                #print(productName.text + "\t" + traits)
                traits = driver.find_element_by_css_selector('tr.odd:nth-child(% s) > td:nth-child(4)'% counter)
                relativeMaturity = driver.find_element_by_css_selector('tr.odd:nth-child(% s) > td:nth-child(5)'% counter)
                counter += 1
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")        
        except: 
            break

driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://legendseeds.net/products/corn')
time.sleep(5)
#Selecting all products from corn page
driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/div/div[3]/div/div[2]/div/div[2]/div[3]/label/select/option[text()='All']").click()

time.sleep(7)

CornCounter()

driver.get('https://legendseeds.net/products/soybeans')
time.sleep(5)
#Selecting all products from corn page
driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/div/div[3]/div/div[2]/div/div[2]/div[3]/label/select/option[text()='All']").click()

time.sleep(5)

SoybeanCounter()