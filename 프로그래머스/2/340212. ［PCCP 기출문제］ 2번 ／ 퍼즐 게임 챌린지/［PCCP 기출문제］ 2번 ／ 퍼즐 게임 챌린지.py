def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        all_times = 0
        after_time = 0
        
        for i in range(len(diffs)):
            if i == 0:
                after_time = 0
            else:
                after_time = times[i-1]
            
            if mid >= diffs[i]:
                all_times += times[i]
            else:
                mistakes = diffs[i] - mid
                all_times += (times[i] + after_time) * mistakes + times[i]
                
            if all_times > limit:
                break
                
        if all_times <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer