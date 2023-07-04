def solution(price, money, count):
    answer = 0
    sum = 0
    
    for i in range(1,count+1):
        sum+=price*i
        print(sum)
    
    if(sum>=money):
        answer=sum-money
    else:
        answer=0

    return answer