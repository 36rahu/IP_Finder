import requests
from termcolor import colored
from bs4 import BeautifulSoup

url = "http://whatismyip.org"
r = requests.get(url)
soup = BeautifulSoup(r.text)
data = soup.find_all("span")
IP = str(data[0].text)

print colored("Your IP address :"+IP, 'green')

