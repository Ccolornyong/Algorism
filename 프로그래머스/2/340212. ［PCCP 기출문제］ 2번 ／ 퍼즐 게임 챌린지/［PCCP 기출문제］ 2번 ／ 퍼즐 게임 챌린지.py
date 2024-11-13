def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    answer = 0
    
    while left <= right:
        need_time = 0
        mid = (left+right)//2
        
        for i in range(len(diffs)):
            if diffs[i]<= mid:
                need_time += times[i]
            else:
                need_time += (times[i] + times[i-1])*(diffs[i]-mid) + times[i]
                
            if need_time > limit:
                break
            
        if need_time <= limit:
            answer = mid
            right = mid - 1
            
        else:
            left = mid + 1
            
    
    return answer