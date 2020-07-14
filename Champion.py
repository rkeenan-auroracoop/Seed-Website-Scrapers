from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.parse

def CornCounterPageOne(): 
    counter = 1
    Brand = "Champion"
    SeedType = "Corn"
    urlBase = "https://www.plantchampion.com/product"
    while counter < 17:
        try:
            if counter == 1:
                productNames = driver.find_element_by_css_selector('li.has-post-thumbnail:nth-child(% s) > h4:nth-child(2) > a:nth-child(1)'% counter)
                #print(productName.text)
                productName = productNames.text[0:5]
                urlSuffix = "/product/" + productNames.text
                productPage = urllib.parse.urljoin(urlBase, urlSuffix)
                print("productPage = " + str(productPage))
                driver.get(productPage)
                time.sleep(5)
                #print(productName)
                traits = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[2]/td')
                #print(traits.text)
                relativeMaturity = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[1]/td')
                #print(relativeMaturity.text)
                #THEN GO BACK TO ORIGINAL PAGE
                time.sleep(3)
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")
                counter += 1
            else:
                driver.get('https://www.plantchampion.com/product-category/corn')
                time.sleep(3)
                productNames = driver.find_element_by_css_selector('li.has-post-thumbnail:nth-child(% s) > h4:nth-child(2) > a:nth-child(1)'% counter)
                productName = productNames.text[0:5]
                if counter == 4 or counter == 6:
                    urlSuffix = "/product/" + productNames.text[0:5] + "-2"
                elif counter == 7:
                    urlSuffix = "/product/" + productNames.text[0:5] + "-3"
                elif counter == 11 or counter == 16:
                    urlSuffix = "/product/" + productNames.text[0:5] + "-1"
                elif counter == 13:
                    urlSuffix = "/product/" + productNames.text[0:5] + "-vt2-pro-rib"
                else: 
                    urlSuffix = "/product/" + productNames.text[0:5]
                productPage = urllib.parse.urljoin(urlBase, urlSuffix)
                print("productPage = " + str(productPage))
                #print(productName.text)
                driver.get(productPage)
                time.sleep(5)
                #print("productPage = " + str(productPage))
               
                #PULL RELATIVE MATURIYT AND TRAIT FROM THIS PAGE
                traits = driver.find_element_by_css_selector('tr.woocommerce-product-attributes-item:nth-child(2) > td:nth-child(2)')
                #print(traits.text)
                relativeMaturity = driver.find_element_by_css_selector('tr.woocommerce-product-attributes-item:nth-child(1) > td:nth-child(2)')
                #print(relativeMaturity.text)
                #THEN GO BACK TO ORIGINAL PAGE
                time.sleep(3)
                counter += 1
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")             
        except: 
            break

def CornCounterPageTwo(): 
    counter = 1
    Brand = "Champion"
    SeedType = "Corn"
    urlBase = "https://www.plantchampion.com/product"
    while counter < 17:
        try:
                productNames = driver.find_element_by_css_selector('li.has-post-thumbnail:nth-child(% s) > h4:nth-child(2) > a:nth-child(1)'% counter)
                #print(productName.text)
                productName = productNames.text[0:5]
                if counter == 5 or counter == 7 or counter == 10 or counter == 14 or counter == 12:
                    urlSuffix = "/product/" + productNames.text[0:5] + "-ss-rib"
                elif counter == 4 or counter == 1 or counter == 6 or counter == 8 or counter == 11 or counter == 13 or counter == 15:
                    urlSuffix = "/product/" + productNames.text[0:5] + "-vt2-pro-rib"
                else: 
                    urlSuffix = "/product/" + productNames.text[0:5] 
                productPage = urllib.parse.urljoin(urlBase, urlSuffix)
                print("productPage = " + str(productPage))
                driver.get(productPage)
                time.sleep(5)
                #print(productName)
                traits = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[2]/td')
                #print(traits.text)
                relativeMaturity = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[1]/td')
                #print(relativeMaturity.text)
                #THEN GO BACK TO ORIGINAL PAGE
                time.sleep(3)
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")
                counter += 1
                driver.get('https://www.plantchampion.com/product-category/corn/?paged=2')
      
        except: 
            break

def CornCounterPageThree(): 
    counter = 1
    Brand = "Champion"
    SeedType = "Corn"
    urlBase = "https://www.plantchampion.com/product"
    while counter < 17:
        try:
                productNames = driver.find_element_by_css_selector('li.has-post-thumbnail:nth-child(% s) > h4:nth-child(2) > a:nth-child(1)'% counter)
                #print(productName.text)
                productName = productNames.text[0:5]
                if counter == 4 or counter == 8 or counter == 13:
                    urlSuffix = "/product/" + productNames.text[0:5] + "-ss-rib"
                elif counter == 5 or counter == 6 or counter == 9 or counter == 12 or counter == 14:
                    urlSuffix = "/product/" + productNames.text[0:5] + "-vt2-pro-rib"
                elif counter == 16:
                    urlSuffix = "/product/" + productNames.text[0:5] + "-dg-vt2-pro-rib"
                elif counter == 1:
                    urlSuffix = "/product/" + productNames.text[0:5] + "-3220-ez"
                elif counter == 10:
                    urlSuffix = "/product/" + productNames.text[0:5] + "-3330-ez"
                else: 
                    urlSuffix = "/product/" + productNames.text[0:5] 
                productPage = urllib.parse.urljoin(urlBase, urlSuffix)
                print("productPage = " + str(productPage))
                driver.get(productPage)
                time.sleep(5)
                #print(productName)
                traits = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[2]/td')
                #print(traits.text)
                relativeMaturity = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[1]/td')
                #print(relativeMaturity.text)
                #THEN GO BACK TO ORIGINAL PAGE
                time.sleep(3)
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")
                counter += 1
                driver.get('https://www.plantchampion.com/product-category/corn/?paged=3')
      
        except: 
            break

def CornCounterPageFour(): 
    counter = 1
    Brand = "Champion"
    SeedType = "Corn"
    urlBase = "https://www.plantchampion.com/product"
    while counter < 17:
        try:
                productNames = driver.find_element_by_css_selector('li.has-post-thumbnail:nth-child(% s) > h4:nth-child(2) > a:nth-child(1)'% counter)
                #print(productName.text)
                if counter < 14:                    
                    productName = productNames.text[0:5]
                else:
                    productName = productNames.text[0:9]
                if counter ==  1 or counter == 3 or counter == 8 or counter == 10 or counter == 12:
                    urlSuffix = "/product/" + productNames.text[0:5] + "-ss-rib"
                elif counter == 2 or counter == 4 or counter == 5 or counter == 9 or counter == 11 or counter == 13:
                    urlSuffix = "/product/" + productNames.text[0:5] + "-vt2-pro-rib"
                elif counter == 7:
                    urlSuffix = "/product/" + productNames.text[0:5] + "-dg-vt2-pro-rib"
                elif counter == 14 or counter == 15:
                    urlSuffix = "/product/" + productNames.text[0:9] + "-RR"
                elif counter == 16:
                    urlSuffix = "/product/" + productNames.text[0:9] + "-Conv"
                else: 
                    urlSuffix = "/product/" + productNames.text[0:5] 
                productPage = urllib.parse.urljoin(urlBase, urlSuffix)
                print("productPage = " + str(productPage))
                driver.get(productPage)
                time.sleep(5)
                #print(productName)
                traits = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[2]/td')
                #print(traits.text)
                relativeMaturity = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[1]/td')
                #print(relativeMaturity.text)
                #THEN GO BACK TO ORIGINAL PAGE
                time.sleep(3)
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")
                counter += 1
                driver.get('https://www.plantchampion.com/product-category/corn/?paged=4')
      
        except: 
            break

def SoybeanCounterPageOne(): 
    counter = 1
    Brand = "Champion"
    SeedType = "Soybeans"
    urlBase = "https://www.plantchampion.com/product/"
    while counter < 17:
        try:
                productNames = driver.find_element_by_css_selector('li.has-post-thumbnail:nth-child(% s) > h4:nth-child(2) > a:nth-child(1)'% counter)
                #print(productName.text)
                productName = productNames.text
                urlSuffix = "/product/" + productNames.text
                productPage = urllib.parse.urljoin(urlBase, urlSuffix)
                print("productPage = " + str(productPage))
                driver.get(productPage)
                time.sleep(5)
                #print(productName)
                traits = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[2]/td')
                #print(traits.text)
                relativeMaturity = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[1]/td')
                #print(relativeMaturity.text)
                #THEN GO BACK TO ORIGINAL PAGE
                time.sleep(3)
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")
                counter += 1
                driver.get('https://www.plantchampion.com/product-category/soybean')
      
        except: 
            break

def SoybeanCounterPageTwo(): 
    counter = 1
    Brand = "Champion"
    SeedType = "Soybeans"
    urlBase = "https://www.plantchampion.com/product/"
    while counter < 17:
        try:
                productNames = driver.find_element_by_css_selector('li.has-post-thumbnail:nth-child(% s) > h4:nth-child(2) > a:nth-child(1)'% counter)
                #print(productName.text)
                productName = productNames.text
                if counter == 8:
                    urlSuffix = "/product/" + "200e" 
                else:
                    urlSuffix = "/product/" + productNames.text
                productPage = urllib.parse.urljoin(urlBase, urlSuffix)
                print("productPage = " + str(productPage))
                driver.get(productPage)
                time.sleep(5)
                #print(productName)
                traits = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[2]/td')
                #print(traits.text)
                relativeMaturity = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[1]/td')
                #print(relativeMaturity.text)
                #THEN GO BACK TO ORIGINAL PAGE
                time.sleep(3)
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")
                counter += 1
                driver.get('https://www.plantchampion.com/product-category/soybean/?paged=2')
      
        except: 
            print("*****************Error: " + productName)
            break

def SoybeanCounterPageThree(): 
    counter = 1
    Brand = "Champion"
    SeedType = "Soybeans"
    urlBase = "https://www.plantchampion.com/product/"
    while counter < 17:
        try:
                productNames = driver.find_element_by_css_selector('li.has-post-thumbnail:nth-child(% s) > h4:nth-child(2) > a:nth-child(1)'% counter)
                #print(productName.text)
                productName = productNames.text
                if counter == 8:
                    urlSuffix = "/product/" + "2259cn-2"
                else: 
                    urlSuffix = "/product/" + productNames.text
                productPage = urllib.parse.urljoin(urlBase, urlSuffix)
                print("productPage = " + str(productPage))
                driver.get(productPage)
                time.sleep(5)
                #print(productName)
                traits = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[2]/td')
                #print(traits.text)
                relativeMaturity = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[1]/td')
                #print(relativeMaturity.text)
                #THEN GO BACK TO ORIGINAL PAGE
                time.sleep(3)
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")
                counter += 1
                driver.get('https://www.plantchampion.com/product-category/soybean/?paged=3')
      
        except:
            print("*****************Error: " + productName) 
            break

def SoybeanCounterPageFour(): 
    counter = 1
    Brand = "Champion"
    SeedType = "Soybeans"
    urlBase = "https://www.plantchampion.com/product/"
    while counter < 17:
        try:
                productNames = driver.find_element_by_css_selector('li.has-post-thumbnail:nth-child(% s) > h4:nth-child(2) > a:nth-child(1)'% counter)
                #print(productName.text)
                productName = productNames.text
                urlSuffix = "/product/" + productNames.text
                productPage = urllib.parse.urljoin(urlBase, urlSuffix)
                print("productPage = " + str(productPage))
                driver.get(productPage)
                time.sleep(5)
                #print(productName)
                traits = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[2]/td')
                #print(traits.text)
                relativeMaturity = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[1]/td')
                #print(relativeMaturity.text)
                #THEN GO BACK TO ORIGINAL PAGE
                time.sleep(3)
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")
                counter += 1
                driver.get('https://www.plantchampion.com/product-category/soybean/?paged=4')
      
        except: 
            print("*****************Error: " + productName)
            break

def SoybeanCounterPageFive(): 
    counter = 1
    Brand = "Champion"
    SeedType = "Soybeans"
    urlBase = "https://www.plantchampion.com/product/"
    while counter < 6:
        try:
                productNames = driver.find_element_by_css_selector('li.has-post-thumbnail:nth-child(% s) > h4:nth-child(2) > a:nth-child(1)'% counter)
                #print(productName.text)
                productName = productNames.text
                urlSuffix = "/product/" + productNames.text
                productPage = urllib.parse.urljoin(urlBase, urlSuffix)
                print("productPage = " + str(productPage))
                driver.get(productPage)
                time.sleep(5)
                #print(productName)
                traits = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[2]/td')
                #print(traits.text)
                relativeMaturity = driver.find_element_by_xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[1]/td')
                #print(relativeMaturity.text)
                #THEN GO BACK TO ORIGINAL PAGE
                time.sleep(3)
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")
                counter += 1
                driver.get('https://www.plantchampion.com/product-category/soybean/?paged=5')
      
        except: 
            print("*****************Error: " + productName)
            break

def CornPage2():
    time.sleep(3)
    driver.get('https://www.plantchampion.com/product-category/corn/?paged=2')
    time.sleep(3)

def CornPage3():
    time.sleep(3)
    driver.get('https://www.plantchampion.com/product-category/corn/?paged=3')
    time.sleep(3)

def CornPage4():
    time.sleep(3)
    driver.get('https://www.plantchampion.com/product-category/corn/?paged=4')
    time.sleep(3)

def SoybeanPage2():
    time.sleep(3)
    driver.get('https://www.plantchampion.com/product-category/soybean/?paged=2')
    time.sleep(3)

def SoybeanPage3():
    time.sleep(3)
    driver.get('https://www.plantchampion.com/product-category/soybean/?paged=3')
    time.sleep(3)

def SoybeanPage4():
    time.sleep(3)
    driver.get('https://www.plantchampion.com/product-category/soybean/?paged=4')
    time.sleep(3)

def SoybeanPage5():
    time.sleep(3)
    driver.get('https://www.plantchampion.com/product-category/soybean/?paged=5')
    time.sleep(3)

driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.plantchampion.com/product-category/corn')
time.sleep(5)

CornCounterPageOne()

CornPage2()
CornCounterPageTwo()

CornPage3()
CornCounterPageThree()

CornPage4()
CornCounterPageFour()

driver.get('https://www.plantchampion.com/product-category/soybean')
time.sleep(3)
SoybeanCounterPageOne()

SoybeanPage2()
SoybeanCounterPageTwo()

SoybeanPage3()
SoybeanCounterPageThree()

SoybeanPage4()
SoybeanCounterPageFour()

SoybeanPage5()
SoybeanCounterPageFive()

print("Scraping for Champion is done. Closing down the browser.")

driver.close()