def solution(s):
    answer = ''
    
    s=s.split(" ")
    
    for i in s:
        for l in range(len(i)):
            if l%2==0:
                answer+=i[l].upper()
            else:
                answer+=i[l].lower()
        answer+=" "
    answer=answer[:-1]
    return answer