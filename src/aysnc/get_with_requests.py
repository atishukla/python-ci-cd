from concurrent.futures import as_completed

import requests
from requests_futures.sessions import FuturesSession


def with_future_session(urls):
    responses = []
    with FuturesSession() as session:
        futures = [session.get(url) for url in urls]
        for future in as_completed(futures):
            response = future.result()
            responses.append(response.json())
    return responses


def without_session_with_requests(urls):
    responses = []
    for url in urls:
        response = requests.get(url)
        responses.append(response.json())
    return responses


def with_requests(urls):
    responses = []
    with requests.session() as session:
        for url in urls:
            response = session.get(url)
            responses.append(response.json())
    return responses


def main():
    base_url = 'https://jsonplaceholder.typicode.com/photos'
    urls = [base_url + f'/{i}' for i in range(1, 2000)]
    # responses = with_requests(urls)
    # responses = without_session_with_requests(urls)
    responses = with_future_session(urls)

    print(len(responses))
    print(responses[:2])


if __name__ == '__main__':
    import time

    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"Completed in {elapsed:0.2f} seconds")
