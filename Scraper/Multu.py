import requests
import urllib
from bs4 import BeautifulSoup
from collections import Counter

lst_url = ["https://finance.yahoo.com/most-active/",
           "https://finance.yahoo.com/u/yahoo-finance/watchlists/most-active-penny-stocks"]

lst_Merge = []
set_Merge = []

for link in range(len(lst_url)):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0',
               "cookie": "CONSENT=YES+cb.20230531-04-p0.en+FX+908"}

    response = requests.get(lst_url[link], headers=headers)

    if response.status_code != 200:
        print("Error fetching page")
        exit()
    else:
        content = response.content

    soup = BeautifulSoup(response.content, 'html.parser')
    # All links in the page

    nb_links = len(soup.find_all('a'))
    print(f"There are {nb_links} links in this page")

    # GET ALL Text from the LINKS
    items = [item.text.strip() for item in soup.select('a')]
    # for i in items:
    # 	print(i)

    #   REMOVE NON LINK TEXT
    test_list = [item.text.strip() for item in soup.select('a')]
    # print(test_list)

    #  FILTER FOR CAPS ONLY
    for word in items:
        upperChars = True
        for letters in word:

            # checking for uppercase
            if not letters.isupper():
                upperChars = False
                break
        if upperChars:
            lst_Merge.append(word)

    # remove blanks
    lst_Merge = list(filter(None, lst_Merge))
    print('Merged List: ', lst_Merge)

    # Remove duplicates
    set_Merge = set(lst_Merge)
    print(len(lst_Merge))
    print(len(set_Merge))
    print(set_Merge)
