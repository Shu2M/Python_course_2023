import requests


response = requests.get('https://roadmap.sh/python')

print(response.status_code)
print(response.ok)

print(response.text)