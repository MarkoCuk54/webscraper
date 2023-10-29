import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

url = input("\nEnter the URL of the website you want to scrape: ")

# Ask the user to choose a User-Agent or skip
print("\nChoose a User-Agent: \n")
print("\t1. Googlebot")
print("\t2. Bingbot")
print("\tPress Enter to skip\n")
choice = input("Enter your choice (1,2): ")

parsed_url = urlparse(url)
if not parsed_url.scheme:
    url = "https://" + url


if choice == "1":
    user_agent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
elif choice == "2":
    user_agent = 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)'
else:
    user_agent = ''

headers = {'User-Agent': user_agent} if user_agent else {}

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
