from bs4 import BeautifulSoup
import requests 
link = input("Please enter a link")
source = requests.get(link).text
soup = BeautifulSoup(source, "lxml")
#"https://www.nike.com/ca/w/womens-running-shoes-37v7jz5e1x6zy7ok"
#print(soup.prettify)
section = soup.find('section')
#shoes = listing.product-grid__items
#print(section.prettify())
#listing = section.find("div", class_ = "product_msg_info").text
#product-card__title
# x = soup.find("div", class_= "product-card__title").text
# print(x)
#link = input("Please enter a link")
ShoesArray=[]
for shoes in section.find_all(class_="product-card__info"):
    shoeType = shoes.find("div", class_= "product-card__title").text
    #parsing through all the shoe names
    print(shoeType)
    #for prices in section.find_all(class_="product-card__price-wrapper"):
    shoePrice = shoes.find("div", class_= "product-price__wrapper").text
    print(shoePrice)
    print("======================")
print("Provided Link Was : " + link)
