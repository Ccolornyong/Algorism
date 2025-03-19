def solution(a, b, c):
    answer = set([a,b,c])
    same = len(answer)
    one = a+b+c
    two = one*(a**2+b**2+c**2)
    three = two*(a**3+b**3+c**3)
    if same == 3:
        return one
    return two if same==2 else three