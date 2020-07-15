from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def CornCounterPageOne(): 
    counter = 0
    Brand = "Hefty"
    SeedType = "Corn"
    while counter < 21:
        try: 
            productName = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(2)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(3)'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break
def CornCounterPageTwo(): 
    counter = 20
    Brand = "Hefty"
    SeedType = "Corn"
    while counter < 40:
        try: 
            productName = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(2)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(3)'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break

def CornCounterPageThree(): 
    counter = 40
    Brand = "Hefty"
    SeedType = "Corn"
    while counter < 60:
        try: 
            productName = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(2)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(3)'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break

def CornCounterPageFour(): 
    counter = 60
    Brand = "Hefty"
    SeedType = "Corn"
    while counter < 80:
        try: 
            productName = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(2)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(3)'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break

def CornCounterPageFive(): 
    counter = 80
    Brand = "Hefty"
    SeedType = "Corn"
    while counter < 100:
        try: 
            productName = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(2)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(3)'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break

def SoybeanCounterPageOne(): 
    counter = 0
    Brand = "Hefty"
    SeedType = "Soybeans"
    while counter < 21:
        try: 
            productName = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(2)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(3)'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break
def SoybeanCounterPageTwo(): 
    counter = 20
    Brand = "Hefty"
    SeedType = "Soybeans"
    while counter < 40:
        try: 
            productName = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(2)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(3)'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break

def SoybeanCounterPageThree(): 
    counter = 40
    Brand = "Hefty"
    SeedType = "Soybeans"
    while counter < 60:
        try: 
            productName = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(2)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(3)'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break

def SoybeanCounterPageFour(): 
    counter = 60
    Brand = "Hefty"
    SeedType = "Soybeans"
    while counter < 80:
        try: 
            productName = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(1)'% counter)
            print(productName.text)
            traits = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(2)'% counter)
            relativeMaturity = driver.find_element_by_css_selector('.ninja_table_row_%s > td:nth-child(3)'% counter)
            counter += 1
            with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv", 'a') as f1:
                f1.write(Brand + "\t" + productName.text  + "\t" + traits.text + "\t" + "None" + "\t" + relativeMaturity.text + "\t" + SeedType + "\n")      
        except: 
            break


def NextPageCorn():
    time.sleep(5)
    sbtn = driver.find_element_by_css_selector('li.footable-page-nav:nth-child(8) > a:nth-child(1)')
    driver.execute_script("arguments[0].click();", sbtn)
    time.sleep(5)

def NextPageSoybean():
    time.sleep(5)
    sbtn = driver.find_element_by_css_selector('li.footable-page-nav:nth-child(7) > a:nth-child(1)')
    driver.execute_script("arguments[0].click();", sbtn)
    time.sleep(5)


driver = webdriver.Chrome(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\chromedriver_win32\chromedriver.exe')
driver.get('https://heftyseed.com/corn/selection-tool')
time.sleep(5)

print("Page 1-Corn")
CornCounterPageOne()

NextPageCorn()
print("Page 2-Corn")
CornCounterPageTwo()

NextPageCorn()
print("Page 3-Corn")
CornCounterPageThree()

NextPageCorn()
print("Page 4-Corn")
CornCounterPageFour()

NextPageCorn()
print("Page 5-Corn")
CornCounterPageFive()


driver.get('https://heftyseed.com/soybeans/soybean-selection-tool')
time.sleep(5)
#sorting by Trait like Corn page automatically is. Then Indexes for first column match up.
sbtn = driver.find_element_by_css_selector('.tableFloatingHeaderOriginal > tr:nth-child(2) > th:nth-child(2)')
driver.execute_script("arguments[0].click();", sbtn)

time.sleep(5)

print("Page 1-Soybeans")
SoybeanCounterPageOne()

NextPageSoybean()
print("Page 2-Soybeans")
SoybeanCounterPageTwo()

NextPageSoybean()
print("Page 3-Soybeans")
SoybeanCounterPageThree()

NextPageSoybean()
print("Page 4-Soybeans")
SoybeanCounterPageFour()

print("Hefty is done scraping")
