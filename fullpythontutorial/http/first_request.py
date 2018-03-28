import requests
url = "https://google.com"
response = requests.get(url)
print("The request to {} came back with code {}".format(url, response.status_code))
