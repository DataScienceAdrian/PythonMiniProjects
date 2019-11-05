import re

import requests
import bs4 as bs

response = requests.get("https://en.wikipedia.org/wiki/Rutland_Boughton").text
response2 = requests.get("https://www.python.org/dev/peps/").text

#Zad 1
def main_func():
    connection_check()
    data_scrap()


def connection_check():
    if response:
        print('Page was successfully connected!\n')
    elif response2:
        print('Page was successfully connected!\n')
    else:
        print("Page Not found!\n")


def data_scrap():
    soup = bs.BeautifulSoup(response, 'lxml')

    head_tags = soup.find_all('h1')
    author_name = head_tags[0].text

    text_with_tag = soup.find_all('p')

    author_information = text_with_tag[1].text

    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]

    print('name:', author_name, '\n', 'description:', author_information, 'images:')

    for url in urls:
        print("https:", url)


#main_func()

#Zad2

def data_scrap2():
    soup = bs.BeautifulSoup(response2, 'lxml')
    td_tags = soup.find_all('td')

    pep_number1 = td_tags[8].text
    print(pep_number1)

    pep_title1 = td_tags[9].text
    print(pep_title1)

    pep_authors1 = td_tags[10].text
    print(pep_authors1)

    links = []

    url_tags = soup.find_all('a')
    #print(url_tags)

    myclasses = soup.findAll("a", {"class": "reference external"})
    #print(myclasses)

    pep_url = myclasses[1]
    pep_string = myclasses[1]
    print(pep_string)

    print(pep_url)
    #//*[@id="meta-peps-peps-about-peps-or-processes"]/table/tbody/tr[1]/td[2]/a



def main_func2():
    connection_check()
    data_scrap2()

main_func2()
