import requests, pyautogui 
from bs4 import BeautifulSoup

search_key = pyautogui.prompt("뉴스 검색어를 입력하세요.")
print(f'search_key: {search_key}')
response = requests.get("https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query="+search_key)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.select("ul.list_news > li .news_tit")
    for i, element in enumerate(elements):
        print(
            f'{i} 번째, 제목: {element.text} / 링크: {element.attrs["href"]}'
        )