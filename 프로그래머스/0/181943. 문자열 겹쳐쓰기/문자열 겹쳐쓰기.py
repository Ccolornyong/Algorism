def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string
    if len(answer) <= len(my_string):
        add_len = len(answer)
        answer += my_string[add_len:]
    return answer