from requests_html import HTMLSession
from string import Template

session = HTMLSession()

url = 'https://brevant.com/products/#/'

r = session.get(url)

r.html.render(sleep=2, keep_page=True, scrolldown=1)

products = r.html.find('.product-results__result')

attributes = r.html.find('html body.products-page div.content div.products section div.content__inner div div div.product-list div.product-list__results div div.product-results div.product-results__result div div.attribute-value span')


counter = 2


'''while counter < 22:
    productName = r.html.find('div.product-results__result:nth-child(% s) > div:nth-child(1) > a:nth-child(1)'% counter)
    for item in productName:
        products = {
            'Product Name': item.text,
        }
    print(products)
    traits = r.html.find('div.product-results__result:nth-child(% s) > div:nth-child(2)'% counter)    
    for trait in traits:
        trait = {
            'Trait' : trait.text[8:],
        }
        print(trait)
    relativeMaturity = r.html.find('div.product-results__result:nth-child(% s) > div:nth-child(3) > div:nth-child(2) > span:nth-child(1)'% counter)
    for RM in relativeMaturity:
        RM = {
            'Relative Maturity' : RM.text,
        }
        print(RM)
    silkGDUs = r.html.find('div.product-results__result:nth-child(% s) > div:nth-child(4) > div:nth-child(2) > span:nth-child(1)'% counter)
    counter += 1
    for sGDU in silkGDUs:
        sGDU = {
            'Silk GDUs' : sGDU.text,
        }
        print(sGDU)'''

while counter < 22:
    productName = r.html.find('div.product-results__result:nth-child(% s) > div:nth-child(1) > a:nth-child(1)'% counter)
    traits = r.html.find('div.product-results__result:nth-child(% s) > div:nth-child(2)'% counter) 
    relativeMaturity = r.html.find('div.product-results__result:nth-child(% s) > div:nth-child(3) > div:nth-child(2) > span:nth-child(1)'% counter)
    silkGDUs = r.html.find('div.product-results__result:nth-child(% s) > div:nth-child(4) > div:nth-child(2) > span:nth-child(1)'% counter)
    counter += 1
    for item in productName:
        for trait in traits:
            for RM in relativeMaturity:
                for sGDU in silkGDUs:
                    Product = {
                        'Product Name': item.text,
                        'Trait' : trait.text[8:],
                        'Relative Maturity' : RM.text,
                        'Silk GDUs' : sGDU.text,
                    }
                    print(Product)


#Click "Page 2" button.pager__button:nth-child(3) or button.pager__button:nth-child(8)