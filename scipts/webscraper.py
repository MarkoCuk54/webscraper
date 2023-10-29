import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from robots_checker import check_robots_txt

url = input("\nEnter the URL of the website you want to scrape: ")

check_robots = input("Do you want to check the robots.txt file? (Y/n): ").strip().lower()

if check_robots == "y":
    user_agent = input("\nChoose a User-Agent: \n1 for Googlebot\n2 for Bingbot\nor press Enter to skip:  ")
    if user_agent == "1":
        user_agent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    elif user_agent == "2":
        user_agent = 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)'
    else:
        user_agent = ''
else:
    user_agent = ''

parsed_url = urlparse(url)
if not parsed_url.scheme:
    url = "https://" + url


headers = {'User-Agent': user_agent} if user_agent else {}

try:
    # Check robots.txt
    if check_robots == "yes" and not check_robots_txt(url, user_agent):
        print(f'The User-Agent "{user_agent}" is not allowed to crawl this website according to robots.txt.')
        exit()
    
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
    print(f'An error occurred while making the request (possibly the host is unreachable. Did you use the format: www.xyz.com?): {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
