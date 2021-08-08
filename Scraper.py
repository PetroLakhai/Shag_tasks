# import requests
# import bs4
# import re
#
#
# def find_word_in_article_name():
#     # The website has 356 pages with articles, but I want to take only 10 pages. The reason is faster program usage.
#
#     all_pages = range(1, 11)
#     article_name = []
#     for page in all_pages:
#         url = f'https://texty.org.ua/articles/?page={page}'
#         result = requests.get(url)
#         soup = bs4.BeautifulSoup(result.text, 'lxml')
#
#         for item in soup.select('p'):
#             article_name.append(item.text)
#
#     rep_number = 0
#     reply = 'а'
#
#     for name in article_name:
#         rep_number += len(re.findall(reply, name.lower()))
#     print(article_name)
#     print(f'The number of articles` names is {len(article_name)}.')
#     print(f'The number of {reply} is {rep_number}.')
#
#
# find_word_in_article_name()


import requests
import bs4
import re


def find_word_in_article_name():
    # The last article has number 104144. I want to take body of last 20 articles. The number we can change.
    first_article_num = 104124
    last_article_num = 104144
    all_articles = range(first_article_num, last_article_num+1)
    article_body = []
    for article in all_articles:
        url = f'https://texty.org.ua/articles/{article}/'
        result = requests.get(url)
        soup = bs4.BeautifulSoup(result.text, 'lxml')

        for item in soup.select('p[data-block-key]'):
            article_body.append(item.text)

    rep_number = 0
    reply = 'наука'

    for name in article_body:
        rep_number += len(re.findall(reply, name.lower()))
    print(article_body)
    print(f'The number of {reply} is {rep_number} in last {last_article_num - first_article_num} articles` body.')


find_word_in_article_name()

