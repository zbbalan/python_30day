import webbrowser # web browser module to open websites
import requests
# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
'''for url in url_lists:
    webbrowser.open_new_tab(url)'''
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page


url1 = 'https://developer.aliyun.com/mirror/all'
response = requests.get(url1)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries

