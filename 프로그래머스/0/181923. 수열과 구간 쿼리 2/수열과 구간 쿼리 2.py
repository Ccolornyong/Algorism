def solution(arr, queries):
    answer = []
    new_arr = []
    for s,e,k in queries:
        new_arr = arr[s:e+1]
        new_arr.sort()
        for i in new_arr:
            if i>k:
                answer.append(i)
                break
        if new_arr[-1]<=k:
            answer.append(-1)
                
    return answer