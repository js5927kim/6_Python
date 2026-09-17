"""
    넘파이 배열 - 검색, 정렬

    - where : 조건에 맞는 요소의 인덱스 반환 / 값 치환
    - argmax / argmin : 최댓값/최솟값이 있는 인덱스를 반환
    - sort : 정렬
"""
import numpy as np

arr = np.array([10 ,5, 22, 15, 8, 20])
print(f"arr : {arr}")

# 15보다 큰 값을 찾기
np.where(arr > 15)  # np.where(조건) => 조건에 해당하는 인덱스들을 반환


# 10보다 큰 값은 99로 변경
#           아닌 값은 0으로 변경
arr2 = np.where(arr > 10 ,99, 0)
print("== 10보다 크면 99, 아니면 0으로 변경 ==")
print(f"arr2 : {arr2}")
# np.where(조건, 조건에 해당하면_변경할 값)
#               , 조건에 해당하지 않으면_변경할 값)

# => 조건에 따라 변경된 값으로 배열 반환
sorted_arr = np.sort(arr)
print(f"정렬된 배열 : {sorted_arr}")