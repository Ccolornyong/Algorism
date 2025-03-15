def solution(a, b):
    result1 = int(str(a)+str(b))
    result2 = int(str(b)+str(a))
    return result1 if result1>= result2 else result2