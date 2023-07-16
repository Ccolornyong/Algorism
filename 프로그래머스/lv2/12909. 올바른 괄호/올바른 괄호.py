def solution(s):
    answer = False
    ans = []
    
    for i in s:
        if i == ")":
            if ans==[]:
                ans=[-1]
                break
            else:
                ans.pop()
        else:
            ans.append("(")
            
    if ans==[]:
        answer = True

    return answer