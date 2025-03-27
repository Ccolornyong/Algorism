def solution(start_num, end_num):
    answer = []
    i = start_num
    while True:
        answer.append(i)
        i+=1
        if i > end_num:
            break
    return answer