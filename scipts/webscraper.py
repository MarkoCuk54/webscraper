import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

url = input("Enter the URL of the website you want to scrape: ")

parsed_url = urlparse(url)
if not parsed_url.scheme:
    url = "https://" + url

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    a_tags = soup.find_all('a')
    
    for tag in a_tags:
        print(f'Text: {tag.get_text()}')
        print(f'Href: {tag.get("href")}')
else:
    print('Failed to retrieve the web page.')
