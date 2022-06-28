import requests
from bs4 import BeautifulSoup
import pyautogui
keyword = pyautogui.prompt("검색어를 입력하세요.")
response = requests.get(
    f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")
for link in links:
    title = link.text  # 태크안에 텍스트요소를 가져온다.
    url = link.attrs['href']  # href의 속성값을 가져온다.
    print(title, url)


# 팝업창을 띄우기 위해서 pip install pyautogui 로 라이브러리 설치 후 사용
