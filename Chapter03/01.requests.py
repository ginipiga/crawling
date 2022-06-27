import requests

response = requests.get("http://www.naver.com")
html = response.text
# response.text 안에 get링크의 소스코드가 담겨있다.
print(word.text)
