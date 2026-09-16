"""
    실습용 사이트에서 
        종목 메뉴 페이지(SSR)의 섹터를 "IT 서비스"로 검색한 결과 데이터를 추출

    - 요청 주소: ??
"""

import requests
from config import BASE, HEADERS, TIMEOUT
from parsers import parse_stocks


resp = requests.get(f"{BASE}/stocks?sector=S08", headers=HEADERS, timeout=TIMEOUT)
resp.raise_for_status()

html = resp.text

stocks = parse_stocks(html)

for s in stocks:
    print(f"{s}")