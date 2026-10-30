import requests
from bs4 import BeautifulSoup
import csv

# 1. Target website ka URL
url = 'http://quotes.toscrape.com/'

# 2. Website ko request bhejna
response = requests.get(url)

if response.status_code == 200:
    # 3. BeautifulSoup ke zariye HTML parse karna
    soup = BeautifulSoup(response.text, 'html.parser')
    
    quotes_data = []
    
    # Website par har quote ek 'div' class 'quote' ke andar hai
    items = soup.find_all('div', class_='quote')
    
    for item in items:
        quote = item.find('span', class_='text').text
        author = item.find('small', class_='author').text
        
        quotes_data.append([quote, author])
        print(f"Author: {author} \nQuote: {quote}\n")

    # 4. Scraped data ko CSV file mein save karna
    with open('scraped_quotes.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Quote', 'Author']) # Table Headers
        writer.writerows(quotes_data)
        
    print("Mubarak ho! Data successfully scrape hokar 'scraped_quotes.csv' file mein save ho gaya hai.")
else:
    print("Website load nahi ho payi. Status code:", response.status_code)