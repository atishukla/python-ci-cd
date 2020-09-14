import time
from io import StringIO

import requests
from lxml import etree
from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession


def main():
    urls = [
        'http://www.heroku.com',
        'http://httpbin.org',
        'http://python-requests.org',
        'http://imdb.com',
        'http://bbc.com',
        'http://orange.com',
        'http://compusearch.be',
        'http://linkedin.com',
        'https://www.belgiantrain.be',
        'http://netflix.com',
        'http://facebook.com',
        'http://bol.com',
        'http://buzzfeed.com',
        'http://stackoverflow.com',
        'http://quora.com',
        'https://www.ansible.com/',
        'http://emirates.com',
    ]

    # del_urls = []
    # for i in range(50):
    #     del_urls.append('https://httpbin.org/delete')

    print(with_future_requests(urls))
    # status = with_future_requests(del_urls)
    # print(status)


def with_future_requests(urls):
    titles = []
    with FuturesSession() as session:
        futures = [session.get(url) for url in urls]
        for future in as_completed(futures):
            response = future.result()
            title = get_title(response)
            titles.append(title.text)
            # titles.append(response.status_code)
    return titles


def with_requests_session(urls):
    status_codes = []
    with requests.session() as session:
        for url in urls:
            response = session.delete(url)
            status_codes.append(response.status_code)
    return status_codes


def get_title(response):
    parser = etree.HTMLParser()
    html = response.text
    tree = etree.parse(StringIO(html), parser=parser)
    site_title = tree.xpath('.//title')
    return site_title[0]


def with_requests_no_session(urls):
    for url in urls:
        response = requests.get(url)
        site_title = get_title(response)
        print(site_title[0].text)


if __name__ == '__main__':
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"executed in {elapsed:0.2f} seconds.")
