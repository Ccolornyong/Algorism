def solution(s):
    answer = ''
    s=s.lower()
    for i in s.split(" "):
        if i.isalpha():
            i = " " + i[0].upper() + i[1:]
            answer+=i
        else:
            i = " " + i
            answer+=i
            
    return answer[1:]