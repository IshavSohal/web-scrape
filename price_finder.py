from bs4 import BeautifulSoup
import requests

product = input("What are you searching for?: ")
product = product.replace(" ", "+") # A URL has + instead of a space

sort = input("Lowest price (ls), Best selling (bs), Best rated (br): ")

if sort == "ls":
    sort = 1
elif sort == "bs":
    sort = 3
else:  # sort == "br"
    sort = 4

url = f"https://www.newegg.ca/p/pl?d={product}&Order={sort}"

#To-do: Add more tech websites to scrape
#url2 = f"https://www.bestbuy.ca/en-ca/category/cpu-computer-processors/29080"

html = requests.get(url).text

# Contains entire html file as one object that we can search through
soup = BeautifulSoup(html, "lxml")

# When finding this div tag, note that it does not matter what layer it is in,
# and how nested is in within the other tags. It will still be found
products = soup.find("div", class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")

# Obtains very first div tag within the div section returned by products
# because when the sorting filter is applied, this product is the first
# one that will show up
target = products.div

title_tag_a = target.find("a", class_="item-title")

link = title_tag_a["href"]

title = title_tag_a.text

price_tag = target.find("li", class_="price-current")
price_dollar = price_tag.strong.text
price_cents = price_tag.sup.text


print("Heres the result")
print(f"name: {title}")
print(f"Price: ${price_dollar}{price_cents}")
print("link:", link)
