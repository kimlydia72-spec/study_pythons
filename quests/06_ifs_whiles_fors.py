# 문제 1 — 문자열 포맷 오류 수정하기

# second = "Programming"
# first = "Welcome to Python Strings" + second   # 오류 발생

# print(first)

# 문제 2 — while 조건 오류 찾기

# first = "Hello Python"

# while len(first) > 0:
#     print(first)
#     first = first[:-1]

#   오류 설명 : 
#   TypeError가 발생합니다. **문자열("Hello Python")**과 정수(0 또는 1) 간의 
#   크기 비교(>)나 뺄셈(-) 연산을 직접 수행할 수 없기 때문입니다.

#   해결 방법 : 
    # while 조건문에서 문자열 first 대신 길이를 확인하는 len(first) > 0을 사용합니다. 
    # 반복문 내부에서는 뺄셈 대신 문자열 슬라이싱(first = first[:-1])을 사용해 
    # 마지막 글자를 제거합니다.
                                                                    
# 문제 3 — 리스트 누적 합 오류 찾기

# kor = [70, 80, 90, 40, 50]
# eng = [90, 80, 70, 70, 60]
# sum_all = 0

# sum_all = sum(kor) + sum(eng)
# print(f'전체 합계 : {sum_all}')

# 문제 4 — for-range 인덱스 문제 해결

# kor = [70, 80, 90, 40, 50]
# eng = [90, 80, 70, 70, 60]

# sum_total = 0

# for i in range(0, 10):    # 오류 발생
#     sum_total = sum_total + kor[i] + eng[i]
