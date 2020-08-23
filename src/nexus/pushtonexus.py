import requests
import json
from requests.auth import HTTPBasicAuth

NEXUS_BASE_URL = "http://192.168.199.9:8081/service/rest/v1/components"
USERNAME = 'admin'
PASSWORD = 'password'
REPOSITORY = 'personal'


def delete():
    params = (
        ('repository', REPOSITORY),
    )

    response = requests.get(NEXUS_BASE_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD), params=params).json()
    components = response['items']

    filtered = [component for component in components if component['group'] == 'com.atishay.test']
    for component in filtered:
        response = requests.delete(f'{NEXUS_BASE_URL}/{component["id"]}', auth=(USERNAME, PASSWORD))
        print(response.status_code)


def upload():
    filename = r'C:\Users\atishayshukla\Desktop\demo-wordpress\wordpress-data.tar.gz'
    for i in range(3, 20):
        payload = {
            'maven2.groupId': (None, 'com.atishay.test'),
            'artifactId': (None, 'someartifact'),
            'version': (None, f'{i}.0.0'),
            'generate-pom': (None, 'false'),
            'packaging': (None, 'zip'),
            'asset1': (filename, open(filename, 'rb')),
            'asset1.extension': (None, 'zip'),
        }
        params = (
            ('repository', REPOSITORY),
        )

        response = requests.post(NEXUS_BASE_URL,
                                 allow_redirects=False,
                                 auth=HTTPBasicAuth(USERNAME, PASSWORD),
                                 params=params,
                                 files=payload,
                                 timeout=20,
                                 )
        print(response.status_code)
        break


if __name__ == '__main__':
    import time

    s = time.perf_counter()
    delete()
    elapsed = time.perf_counter() - s
    print(f"Completed in {elapsed:0.2f} seconds")
