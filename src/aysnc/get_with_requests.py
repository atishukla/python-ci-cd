import requests
import asyncio
from aiohttp import ClientSession


async def get_post(url):
    async with ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
    return data


async def get_posts(urls):
    tasks = [asyncio.create_task(get_post(url)) for url in urls]  # asyncio is included in python
    return await asyncio.gather(*tasks)


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
    base_url = 'https://jsonplaceholder.typicode.com/posts'
    urls = [base_url + f'/{i}' for i in range(1, 100)]
    # responses = with_requests(urls)
    # responses = without_session_with_requests(urls)
    responses = asyncio.run(get_posts(urls))
    print(responses[:2])


if __name__ == '__main__':
    import time

    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"Completed in {elapsed:0.2f} seconds")
