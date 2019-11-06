import requests
import bs4 as bs

response = requests.get("https://en.wikipedia.org/wiki/Rutland_Boughton").text
response2 = requests.get("https://www.python.org/dev/peps/").text


# Zad 1
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


# Zad2

def data_scrap2():
    soup = bs.BeautifulSoup(response2, 'lxml')
    td_tags = soup.find_all('td')

    pep_number1 = td_tags[8].text
    pep_title1 = td_tags[9].text
    pep_authors1 = td_tags[10].text
    pep_class_type = soup.findAll("a", {"class": "reference external"})
    pep_url1 = pep_class_type[1].get('href')

    pep_number2 = td_tags[12].text
    pep_title2 = td_tags[13].text
    pep_authors2 = td_tags[14].text
    pep_class_type2 = soup.findAll("a", {"class": "reference external"})
    pep_url2 = pep_class_type2[2].get('href')

    print('pep_number:', pep_number1, '\n', 'pep_title:', pep_title1, '\n', 'pep_authors:', pep_authors1, '\n'
                                                                                                          'pep_url:',
          pep_url1)
    print('\n\n')
    print('pep_number:', pep_number2, '\n', 'pep_title:', pep_title2, '\n', 'pep_authors:', pep_authors2, '\n'
                                                                                                          'pep_url:',
          pep_url2)


def main_func2():
    connection_check()
    data_scrap2()


# main_func()
main_func2()
