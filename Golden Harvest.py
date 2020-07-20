from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup as soup

def CornCounter(): 
    counter = 0
    elseCounter = counter + 1
    Brand = "Golden Harvest"
    SeedType = "Corn"
    while counter < 67:
        #try:      
            if counter == 0:
                productName = driver.find_elements_by_class_name('product')[counter]
                productName = productName.text
                relativeMaturity = driver.find_elements_by_class_name('rm')[counter+1]
                relativeMaturity = relativeMaturity.text.replace("RM", "")
                traits = driver.find_element_by_css_selector('div.col-md-6:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(4)')
                traits = traits.text[7:]
                if '|' in traits:
                    traits = traits.split('|')
                    if len(traits) == 2:
                        traits1 = traits[0]
                        traits1 = traits1.strip()
                        traits2 = traits[1]
                        traits2 = traits2.strip()
                            #print(productName)
                            #print(relativeMaturity)
                            #print(traits1)
                            #print(counter)
                        counter += 1   
                        with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                            f1.write(Brand + "\t" + productName  + "\t" + traits1 + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")
                        with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                            f1.write(Brand + "\t" + productName  + "\t" + traits2 + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")  
                    elif len(traits) == 3:
                        traits1 = traits[0]
                        traits2 = traits[1]
                        traits3 = traits[2]
                        counter += 1 
                        with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                            f1.write(Brand + "\t" + productName  + "\t" + traits1 + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")
                        with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                            f1.write(Brand + "\t" + productName  + "\t" + traits2 + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")
                        with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                            f1.write(Brand + "\t" + productName  + "\t" + traits3 + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")                                 
                    elif len(traits) == 4:
                        traits1 = traits[0]
                        traits2 = traits[1]
                        traits3 = traits[2]
                        traits4 = traits[3]
                        counter += 1 
                        with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                            f1.write(Brand + "\t" + productName  + "\t" + traits1 + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")
                        with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                            f1.write(Brand + "\t" + productName  + "\t" + traits2 + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")
                        with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                            f1.write(Brand + "\t" + productName  + "\t" + traits3 + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")
                        with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                            f1.write(Brand + "\t" + productName  + "\t" + traits4 + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")
                            counter += 1
                    else: 
                        print("more than four items.")
                        counter += 1
                        break      
                else:
                    counter += 1 
                    traits = traits
                    with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                        f1.write(Brand + "\t" + productName  + "\t" + traits + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")
                          
            else:
                print(counter)
                productName = driver.find_elements_by_class_name('product')[counter]
                productName = productName.text
                relativeMaturity = driver.find_elements_by_class_name('rm')[counter+1]
                relativeMaturity = relativeMaturity.text.replace("RM", "")
                traits = driver.find_element_by_css_selector('div.col-xs-12:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(4)'% elseCounter)
                traits = traits.text[7:]
                if '|' in traits:
                    traits = traits.split('|')
                    if len(traits) == 2:
                        traits1 = traits[0]
                        traits2 = traits[1]
                        counter += 1   
                        with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                            f1.write(Brand + "\t" + productName  + "\t" + traits1 + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")
                            f1.write(Brand + "\t" + productName  + "\t" + traits2 + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")
                    elif len(traits) == 3:
                        traits1 = traits[0]
                        traits2 = traits[1]
                        traits3 = traits[2]
                        counter += 1  
                        with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                            f1.write(Brand + "\t" + productName  + "\t" + traits1 + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")
                            f1.write(Brand + "\t" + productName  + "\t" + traits2 + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")
                            f1.write(Brand + "\t" + productName  + "\t" + traits3 + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")                                   
                    elif len(traits) == 4:
                        traits1 = traits[0]
                        traits2 = traits[1]
                        traits3 = traits[2]
                        traits4 = traits[3]
                        counter += 1
                        with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                            f1.write(Brand + "\t" + productName  + "\t" + traits1 + "\t" + "None" + "\t" +relativeMaturity + "\t" + SeedType + "\n")
                            f1.write(Brand + "\t" + productName  + "\t" + traits2 + "\t" + "None" + "\t" +relativeMaturity + "\t" + SeedType + "\n")
                            f1.write(Brand + "\t" + productName  + "\t" + traits3 + "\t" + "None" + "\t" +relativeMaturity + "\t" + SeedType + "\n")
                            f1.write(Brand + "\t" + productName  + "\t" + traits4 + "\t" + "None" + "\t" +relativeMaturity + "\t" + SeedType + "\n")
                    else:
                        print("Trait items are more than 4.")
                        counter +=1
                        continue
        #except:
        #    print("Breaking out of Golden Harvest corn loop")
        #   break

def SoybeanCounter(): 
    counter = 0
    elseCounter = counter + 1
    Brand = "Golden Harvest"
    SeedType = "Soybean"
    while counter <= 90:
        #try:      
            if counter == 0:
                productName = driver.find_elements_by_class_name('product')[counter]
                productName = productName.text
                print(productName)
                relativeMaturity = driver.find_elements_by_class_name('rm')[counter+1]
                relativeMaturity = relativeMaturity.text.replace("RM", "")
                print(relativeMaturity)
                traits = driver.find_element_by_css_selector('div.col-md-6:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(4)')
                #traits = traits.text[7:]
                print(traits.text)
                counter += 1   
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")
                          
            else:
                print(counter)
                productName = driver.find_elements_by_class_name('product')[counter]
                productName = productName.text
                print(productName)
                relativeMaturity = driver.find_elements_by_class_name('rm')[counter+1]
                relativeMaturity = relativeMaturity.text.replace("RM", "")
                print(relativeMaturity)
                traits = driver.find_element_by_css_selector('div.col-xs-12:nth-child(% s) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(4)'% elseCounter)
                #traits = traits.text[7:]
                print(traits.text)
                counter += 1   
                with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                    f1.write(Brand + "\t" + productName  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity + "\t" + SeedType + "\n")
        #except:
        #    print("Breaking out of Golden Harvest corn loop")
        #   break

def MoreResults():
    time.sleep(10)
    sbtn = driver.find_element_by_css_selector('.load-more')
    driver.execute_script("arguments[0].click();", sbtn)
    time.sleep(10)


driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.goldenharvestseeds.com/corn/product-finder')
time.sleep(10)
#Need to first fill out the Relative maturity boxes

leftEntry = driver.find_element_by_css_selector('#txtRmFrom')
leftEntry.clear()
leftEntry.send_keys("1")
rightEntry = driver.find_element_by_css_selector('#txtRmTo')
rightEntry.clear()
rightEntry.send_keys("200")

#Then click "Update Relative Maturity"

sbtn = driver.find_element_by_css_selector('#updateRM')
driver.execute_script("arguments[0].click();", sbtn)

#This clicks the more results button enough times where all corn products are shown



MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()

time.sleep(10)

CornCounter()

driver.get('https://www.goldenharvestseeds.com/soybean/product-finder')
time.sleep(5)

leftEntry = driver.find_element_by_css_selector('#mainBody_txtRmFrom')
leftEntry.clear()
leftEntry.send_keys("0.0")
rightEntry = driver.find_element_by_css_selector('#mainBody_txtRmTo')
rightEntry.clear()
rightEntry.send_keys("9.9")

time.sleep(3)

sbtn = driver.find_element_by_css_selector('#updateRM')
driver.execute_script("arguments[0].click();", sbtn)


MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()
MoreResults()

time.sleep(5)

SoybeanCounter()

print("Scraping is done!")

