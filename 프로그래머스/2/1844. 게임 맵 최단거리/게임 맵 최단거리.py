from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    rx = [1,-1,0,0]
    ry = [0,0,1,-1]
    
    queue = deque([(0,0)])
    
    while queue:
        x, y = queue.pop()
        
        for i in range(4):
            nx = rx[i] + x
            ny = ry[i] + y
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                queue.appendleft((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
                
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1