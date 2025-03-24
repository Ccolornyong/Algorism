def solution(numLog):
    key = {1:'w', -1:'s', 10:'d', -10:'a'}
    answer = ""
    for i in range(len(numLog)-1):
        for l in key:
            if numLog[i]+l == numLog[i+1]:
                answer+=key[l]
    return answer