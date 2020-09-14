import asyncio

import aiohttp
from aiohttp import FormData

# https://number1.co.za/how-to-speed-up-http-calls-in-python-with-examples/

NEXUS_BASE_URL = "http://192.168.199.9:8081/service/rest/v1/components"
USERNAME = 'admin'
PASSWORD = 'password'
REPOSITORY = 'personal'
params = {'repository': 'personal'}
file = r'C:\Users\atishayshukla\Desktop\demo-wordpress\wordpress-data.tar.gz'
headers = {
    'Authorization': 'Basic YWRtaW46cGFzc3dvcmQ='
}


async def main():
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = []
        for i in range(1, 40):
            data = await get_form_data(i)
            tasks.append(upload_one(data, session))
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        return responses
        # await upload_one(data, session)


async def get_form_data(i):
    data = FormData()
    data.add_fields(
        ('maven2.groupId', 'com.atishay.test'),
        ('artifactId', 'someartifact'),
        ('version', f'{i}.0.0'),
        ('generate-pom', 'false'),
        ('packaging', 'zip'),
        ('asset1', open(file, 'rb')),
        ('asset1.extension', 'zip')
    )
    return data


async def upload_one(data, session):
    async with session.post(NEXUS_BASE_URL, params=params, data=data) as r:
        print(r.status)
        resp = await r.text()
        return resp


if __name__ == '__main__':
    import time

    s = time.perf_counter()
    responses = asyncio.run(main())
    print(responses)
    elapsed = time.perf_counter() - s
    print(f"Completed in {elapsed:0.2f} seconds")
