"""
    This file scrape the stock symbols from stockanalysis website.
"""
import json
import sys
import requests
from bs4 import BeautifulSoup


def html_parser(url_link):
    """
        Get the URL link and return the stock value from the parsed html.
    """
    try:
        page = requests.get(url_link, timeout=20)  # 20 seconds
        # parse all the content from the url with a time out of 20 seconds.
    except requests.exceptions.Timeout:
        # if the parse requires more than 20seconds, stop the execution.
        print("Timeout limit exceeded")
        sys.exit()
    else:
        # if no timeout error occure then find the class and value required.
        soup = BeautifulSoup(page.text, 'html.parser')
        stock_list = soup.find_all('td', class_='sym svelte-cod2gs')

        # we create a empty json file with initial dictionary contain empty list.
        with open('stocks.json', 'w', encoding='utf-8') as f:
            data = {
                "symbols": []
            }
            json.dump(data, f)
            f.close()

        # get all the symbol from the link tag and append to the dictionary
        for each in stock_list:
            symbol = each.find("a").contents[0]
            with open('stocks.json', 'w', encoding='utf-8') as f:
                data["symbols"].append(symbol)
                json.dump(data, f)


if __name__ == "__main__":
    # Pass the URL to the analyzer function
    URL = 'https://stockanalysis.com/list/nasdaq-stocks/'
    html_parser(URL)
