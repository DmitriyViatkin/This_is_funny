import requests
from bs4 import BeautifulSoup


def parser(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    anekdots = soup.find_all(
        "div",
        class_="text",
    )

    return [c.text for c in anekdots]
