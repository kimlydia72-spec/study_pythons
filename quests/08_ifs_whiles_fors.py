# 문제 1 — return 누락 오류

# def to_celsius(temp):
#     celsius = (temp - 32) * 5 / 9
#     # return 문이 없음
#     return celsius

# result = to_celsius(77)
# print(result)

# 문제 2 — 매개변수 이름 오류

# def convert(temp):
#     return (temp - 32) * 5 / 9

# print(convert(95))

# 문제 3 — 함수 호출 인자 오류

# def to_celsius(temp):
#     return (temp - 32) * 5 / 9

# value = to_celsius(77)
# print(value)

# 문제 4 — 타입 오류(TypeError)

# def to_celsius(temp):
#     return (int(temp) - 32) * 5 / 9

# print(to_celsius("77"))

# 문제 5 — 반복 구조 + 함수 사용 오류

# def to_celsius(temp):
#     return (temp - 32) * 5 / 9

# def convert_temps_list_comprehension(temps_list):
#     return [to_celsius(t) for t in temps_list]

# temps = [77, 95, 50]
# results = convert_temps_list_comprehension(temps)
# print(results)

