def solution(s):
    answer = []
    num = 0
    count = 0
    countzore = 0
    
    while s!="1":
        for i in s: ## 1 세서 num에 숫자 저장
            if i=="1":
                num+=1
            else:
                countzore+=1
                
        s=""## s 초기화 후 2진법으로 변환한 num 저장공간으로 사용
    
        while num!=1: ##num을 2진법으로 변환
            result = str(num%2)
            num=num//2
            s+=result
        s+=str(num)
        s=s[::-1] ##거꾸로 출력해서 저장
        
        num = 0 ##숫자초기화
        count+=1 ##반복횟수 추가
        
    answer.append(count)
    answer.append(countzore)
        
    return answer