from bs4 import BeautifulSoup
import requests

url = "https://remoteok.com/remote-dev-jobs"
headers = {'User-Agent': 'Mozilla/5.0'} 

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')  

print(soup.prettify())  
