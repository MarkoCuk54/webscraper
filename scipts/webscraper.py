import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

url = input("Enter the URL of the website you want to scrape: ")

parsed_url = urlparse(url)
if not parsed_url.scheme:
    url = "https://" + url

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        a_tags = soup.find_all('a')
        
        for tag in a_tags:
            print(f'Text: {tag.get_text()}')
            print(f'Href: {tag.get("href")} \n')
    else:
        print(f'Failed to retrieve the web page. Status Code: {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'An error occurred while making the request (possible thaht the Host is unreachable. Did you use format : www.xyz.com ?): {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
