def calculate_all(num1, num2):
    # 덧셈
    add_result = num1 + num2
    # 뺄셈
    subtract_result = num1 - num2
    # 곱셈
    multiply_result = num1 * num2
    
    # 나눗셈: num2가 0인 경우를 처리합니다.
    if num2 == 0:
        division_result = "division_error"
    else:
        # 일반적인 나눗셈 (실수형 결과)
        division_result = num1 / num2
        
    # 요구사항에 따라 (덧셈, 뺄셈, 곱셈, 나눗셈) 순서의 튜플을 반환합니다.
    return (add_result, subtract_result, multiply_result, division_result)


# 테스트 리스트 (10개)
test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

# 테스트 실행 코드는 수정하지 마세요.
for i in range(10):
    a = test_a[i]
    b = test_b[i]
    result = calculate_all(a, b)
    print(f"{a}, {b} => {result}")