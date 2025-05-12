import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_website(url):
    try:
        response = requests.get(url,timeout=5)
        response.raise_for_status()
    except Exception as e:
        return [f"Error: {e}"]

    soup = BeautifulSoup(response.text, 'html.parser')
    links = set()

    for tag in soup.find_all('a', href=True):
        full_url = urljoin(url, tag['href'])
        links.add(full_url)

    return sorted(links)
