import asyncio

import aiohttp
from aiohttp import FormData

NEXUS_BASE_URL = "http://192.168.199.9:8081/service/rest/v1/components"
USERNAME = 'admin'
PASSWORD = 'password'
REPOSITORY = 'personal'


async def main():
    params = {'repository': 'personal'}
    file = r'C:\Users\atishayshukla\Desktop\demo-wordpress\wordpress-data.tar.gz'
    data = FormData()
    headers = {
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQ='
    }

    data.add_fields(
        ('maven2.groupId', 'com.atishay.test'),
        ('artifactId', 'someartifact'),
        ('version', '1.0.0'),
        ('generate-pom', 'false'),
        ('packaging', 'zip'),
        ('asset1', open(file, 'rb')),
        ('asset1.extension', 'zip')
    )

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(NEXUS_BASE_URL, params=params, data=data) as r:
            print(r.status)
            resp = await r.text()
            print(resp)


if __name__ == '__main__':
    asyncio.run(main())
