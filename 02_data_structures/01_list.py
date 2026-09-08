"""
    리스트 (list)
"""

# 리스트 데이터 표현 : 대괄호 []
colors = ["red", "green", "blue"]

print(f"colors -> {colors}")
# 첫 번째 요소 출력
print(f"첫번째 : {colors[0]}")
# 마지막 요소 출력
print(f"마지막 : {colors[-1]}")
print(f"마지막 다른 방식 : {colors[len(colors)-1]}")

print(f"{colors[0:2]}")
print(f"{colors[-2]}")

# 다양한 타입의 데이터를 담을 수 있음
mixed = [100, "Hello", True, [1,2,3]]
print(f"{mixed}")
print(f"{mixed[3][0]}")

temp = []
print(f"mixed -> {bool(mixed)}")
print(f"temp --> {bool(temp)}")


print("=" * 60)
items = ["포카칩", "썬칩", "치토스"]

print(f"items -> {items}")

# 데이터 추가 : append(), insert(), extend()
items.append("콘칩")
print(f"맨 뒤에 추가 : {items}")

items.insert(2,"쿠쿠다스")
print(f"지정된 위치에 추가 : {items}")

items.extend(["홈런볼", "허니버터칩"])
print(f"여러개 데이터를 list형태로 추가 : {items}")

# 수정, 삭제
print("=" * 60)
items[0] = "오감자"
print(f"특정 인덱스를 지정하여 값을 변경 : {items}")

items.remove("쿠쿠다스")    # 값으로 삭제
print(f"쿠쿠다스 삭제 : {items}")
# remove 사용 시 해당 데이터가 없을 경우 ValueError 발생

snack = items.pop()
print(f"pop - 결과 : {snack}")  # 맨 뒤 데이터를 삭제 후 반환
print(f"pop 다음 items 값 : {items}")

del items[0]
print(f"del - 인덱스로 삭제 : {items}")


