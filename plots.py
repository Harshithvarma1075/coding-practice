'''
import matplotlib.pyplot as plt
plt.bar([2024,2025,2026] , [67,89,50], color="yellow")
plt.title("car sales")
plt.xlabel("year")
plt.ylabel("sales")
plt.show()
'''
'''
import matplotlib.pyplot as plt
plt.scatter([1,2,3,4] ,[200,400,100,800],color="yellow",s=300)
plt.title("Swift car sales")
plt.xlabel("years")
plt.ylabel("Number of sales")
plt.show()
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

url="https://books.toscrape.com/"

try:
    response = requests.get(url)
    response.encoding ='utf-8'
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print("Error Fetching data:", e)
    exit()
soup=BeautifulSoup(response.text,"html.parser")
books =soup.find_all("article", class_="product_pod")

names = [ ]
prices = [ ]

for book in books:
    name = book.h3.a["title"]
    price_text = book.find("p", class_="price_color").text
    price = float(re.findall(r'\d+\.\d+' , price_text)[0])
    names.append(name)
    prices.append(price)

df = pd.DataFrame({
    "Book Name": names,
    "Price": prices
})

print("\n ⛔⛔⛔⛔Table Data:\n")
print(df.head())

df.to_csv("books_data.csv",index=False)
print("\n ✅ csv file created successfully!")
plt.figure()
plt.bar(names[:10],prices[:10])
plt.xticks(rotation=90)
plt.xlabel("Book Names")
plt.ylabel("Price")
plt.title("Book Prices(top 10)")
plt.tight_layout()
plt.show()
