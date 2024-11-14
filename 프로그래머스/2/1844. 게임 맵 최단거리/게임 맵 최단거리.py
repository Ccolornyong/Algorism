from collections import deque

def solution(maps):
    n = len(maps) # 맵 끝의 x 좌표
    m = len(maps[0]) # 맵 끝의 y 좌표
    
    x, y = 0,0
    queue = deque([(x, y)])
    
    rx = [1, -1, 0, 0] # 좌,우,앞,뒤
    ry = [0, 0, 1, -1] # 좌,우,앞,뒤
    
    while queue:
        x, y = queue.pop() 
        for i in range(4):
            nx = x + rx[i]
            ny = y + ry[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                queue.appendleft((nx,ny))
                maps[nx][ny] = maps[x][y] + 1
    
    return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1