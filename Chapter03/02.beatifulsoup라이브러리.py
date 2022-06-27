import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.naver.com")
html = response.text
# response.text 안에 get링크의 소스코드가 담겨있다.
soup = BeautifulSoup(html, 'html.parser')
# Beautifulsoup(html 코드, html 번역선생님) <- 이런 형태
word = soup.select_one('#NM_set_home_btn')
# soup.select는 여러개의 태그를 선택하고 싶을때
# soup.select_one은 1개의 태그를 선택하고 싶을때
# id를 찾을때는 앞에 #을 붙인다.
print(word.text)
