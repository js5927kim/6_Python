


# 모듈 import
#   현재 파일에서 다른 파일(.py)에 정의된 변수/함수/클래스 등을 가져옴

# 모듈 전체를 가져오기
import module_util

print(f"3,000원 ---> {module_util.clean_price('3,000원')}")

# 특정 항목만 가져오기
from module_util import BASE_URL, to_code

print(f"to_code --> {to_code(7979)}")
print(f"BASE_URL --> {BASE_URL}")

# 별칭 부여
from module_util import clean_price