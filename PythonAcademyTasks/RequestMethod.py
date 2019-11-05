import requests
import bs4 as bs

response = requests.get("https://en.wikipedia.org/wiki/Rutland_Boughton").text


def main_func():
    connection_check()
    data_scrap()


def connection_check():
    if response:
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


main_func()
