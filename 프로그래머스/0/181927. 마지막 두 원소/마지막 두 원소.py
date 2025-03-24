def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num = num_list[-1]-num_list[-2]
        num_list.append(num)
        return num_list
    else:
        num = num_list[-1]*2
        num_list.append(num)
        return num_list