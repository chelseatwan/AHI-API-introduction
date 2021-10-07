#this API has data on COVID cases by country
#data on total confirmed cases, new deaths, total deaths, new recovered, total recovered, etc.
#does not require authorization

import requests

url = "https://api.covid19api.com/summary"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)