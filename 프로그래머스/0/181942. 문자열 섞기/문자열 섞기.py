def solution(str1, str2):
    # answer = [i for i,j in str1, str2]
    answer = ""
    for i, j in zip(str1, str2):
        answer+=i
        answer+=j
    return answer