import requests
from requests.auth import HTTPBasicAuth

NEXUS_BASE_URL = "http://192.168.199.9:8081/service/rest/v1/components"
USERNAME = 'admin'
PASSWORD = 'password'
REPOSITORY = 'personal'

filename = r'C:\Users\atishayshukla\Desktop\demo-wordpress\wordpress-data.tar.gz'
params = (
    ('repository', REPOSITORY),
)


def delete():
    response = requests.get(NEXUS_BASE_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD), params=params).json()
    components = response['items']

    filtered = [component for component in components if component['group'] == 'com.atishay.test']
    for component in filtered:
        response = requests.delete(f'{NEXUS_BASE_URL}/{component["id"]}', auth=(USERNAME, PASSWORD))
        print(response.status_code)
        print(response.text)


def upload():
    for i in range(1, 40):
        payload = get_form_data(i)

        response = requests.post(NEXUS_BASE_URL,
                                 allow_redirects=False,
                                 auth=HTTPBasicAuth(USERNAME, PASSWORD),
                                 params=params,
                                 files=payload,
                                 timeout=20,
                                 )
        print(response.status_code)


def get_form_data(i):
    payload = {
        'maven2.groupId': (None, 'com.atishay.test'),
        'artifactId': (None, 'someartifact'),
        'version': (None, f'{i}.0.0'),
        'generate-pom': (None, 'false'),
        'packaging': (None, 'zip'),
        'asset1': (filename, open(filename, 'rb')),
        'asset1.extension': (None, 'zip'),
    }
    return payload


if __name__ == '__main__':
    import time

    s = time.perf_counter()
    delete()
    elapsed = time.perf_counter() - s
    print(f"Completed in {elapsed:0.2f} seconds")
