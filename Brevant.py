from requests_html import HTMLSession
from string import Template

session = HTMLSession()

url = 'https://brevant.com/products/#/'

r = session.get(url)

r.html.render(sleep=2, keep_page=True, scrolldown=1)

products = r.html.find('.product-results__result')

attributes = r.html.find('html body.products-page div.content div.products section div.content__inner div div div.product-list div.product-list__results div div.product-results div.product-results__result div div.attribute-value span')
counter = 2
#productCounter = 2


while counter < 22:
    productName = r.html.find('div.product-results__result:nth-child(% s) > div:nth-child(1) > a:nth-child(1)'% counter)
    for item in productName:
        products = {
            'productName': item.text,
        }
    print(products)
    #while traitCounter < 30:
            #print(count)
    traits = r.html.find('div.product-results__result:nth-child(% s) > div:nth-child(2)'% counter)
    counter += 1
            
            #print(traits)
    for trait in traits:
        trait = {
            'trait' : trait.text[8:],
        }
                #print(products)
        print(trait)
    #print(attributes)
    #print(attributes)
    #print(product.attrs)