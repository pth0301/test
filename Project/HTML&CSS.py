# HTML: trích xuất các phần tử HTML chứa dữ liệu cần 
import requests
import json
from bs4 import BeautifulSoup
url = "https://www.blockchain.com/"
response = requests.get(url)
data = response.json()
# parse data collection 