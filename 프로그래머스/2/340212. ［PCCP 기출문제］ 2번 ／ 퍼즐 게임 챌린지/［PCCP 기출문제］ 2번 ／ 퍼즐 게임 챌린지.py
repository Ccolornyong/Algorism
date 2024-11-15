def solution(diffs, times, limit):
    result = 0
    left = 1
    right = max(diffs)
    
    while left <= right:
        mid = (left+right)//2
        answer = 0
        
        for i in range(len(diffs)):
            if diffs[i]<=mid:
                answer += times[i]
            else:
                answer += (times[i-1]+times[i])*(diffs[i]-mid)+times[i]

        if answer <= limit:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return result