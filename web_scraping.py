import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?d=graphics+card'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close() 

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
cells = page_soup.findAll("div", {"class": "item-cell" })

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product name, shipping\n" 

f.write(headers)

index = 1
for cell in cells:
	brand = ""
	product_name = ""
	shipping = ""
 
	try: 
		brand = cell.findAll("div", {"class": "item-branding"})[0].a.img["title"]
	except:
		pass


	try: 
		product_name = cell.findAll("a", {"class": "item-title" })[0].text
	except:
		pass

	try: 
		shipping = cell.findAll("li", {"class": "price-ship"})[0].text.strip()
	except:
		pass

	print("brand: " + brand)
	print("product name: " + product_name)
	print("shipping: " + shipping)
	print(index)
	index += 1

	f.write(brand + "," + product_name.replace(",", " ") + "," + shipping + "\n")

f.close()




