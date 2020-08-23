import requests

url = "http://192.168.199.9:8081/service/rest/v1/components?repository=personal"

payload = {'maven2.groupId': 'com.atishay.test',
           'artifactId': 'someartifact',
           'version': '2.0.0',
           'generate-pom': 'false',
           'packaging': 'zip',
           'asset1.extension': 'pdf'}
files = [
    ('asset1', open(
        r'C:/Users/atishayshukla/Documents/Air Ticket Booking _ Book Flight Tickets _ Cheap Air Fare _ LTC Fare_ IRCTC AIR.pdf',
        'rb'))
]
headers = {
    'Authorization': 'Basic YWRtaW46cGFzc3dvcmQ='
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text.encode('utf8'))
