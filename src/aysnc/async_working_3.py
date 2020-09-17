import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        if response.status != 200:
            response.raise_for_status()
        return await response.json()


async def fetch_all(urls):
    async with aiohttp.ClientSession(loop=loop) as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    return results


async def main():
    base_url = 'https://jsonplaceholder.typicode.com/photos'
    urls = [base_url + f'/{i}' for i in range(1, 2000)]
    results = await fetch_all(urls)
    print(len(results))
    print(results[:2])


if __name__ == '__main__':
    import time

    s = time.perf_counter()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())  # change for 3.6 and below

    elapsed = time.perf_counter() - s
    print(f"Completed in {elapsed:0.2f} seconds")
