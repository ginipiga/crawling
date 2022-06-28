import requests
from bs4 import BeautifulSoup
a = input()
response = requests.get(
    "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+a)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")
for link in links:
    title = link.text  # 태크안에 텍스트요소를 가져온다.
    url = link.attrs['href']  # href의 속성값을 가져온다.
    print(title, url)
