
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US'
browser.get(url)

# 모니터(해상도) 높이로 세로 방향 스크롤 내리기
# 바탕화면 > 마우스 우클릭 > 디스플레이 설정 > 메뉴에서 PC 해상도 확인 가능
browser.execute_script('window.scrollTo(0,2080)')

