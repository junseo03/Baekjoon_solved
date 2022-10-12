from collections import deque
import sys

check = False
cnt = 0
q = deque()
x = []
y = []
M,N = map(int,sys.stdin.readline().split())
visited = [[False for _ in range(M)] for _ in range(N)]
box = [[] for _ in range(N)]
for i in range(N):
    box[i] = input().split()
    for j in range(M):
        if box[i][j] == '1':
            q.append((j,i))
while q:
    for _ in range(len(q)):
        tmpx,tmpy = q.popleft()
        if not visited[tmpy][tmpx]:
            visited[tmpy][tmpx] = True
            x.append(tmpx)
            y.append(tmpy)
    for i in range(len(x)):
        if y[i] != 0:
            if box[y[i]-1][x[i]] == '0':
                box[y[i]-1][x[i]] = '1'
                q.append((x[i],y[i]-1))
        if y[i] != N-1:
            if box[y[i]+1][x[i]] == '0':
                box[y[i]+1][x[i]] = '1'
                q.append((x[i],y[i]+1))
        if x[i] != 0:
            if box[y[i]][x[i]-1] == '0':
                box[y[i]][x[i]-1] = '1'
                q.append((x[i]-1,y[i]))
        if x[i] != M-1:
            if box[y[i]][x[i]+1] == '0':
                box[y[i]][x[i]+1] = '1'
                q.append((x[i]+1,y[i]))
    x.clear()
    y.clear()
    cnt +=1
for i in range(N):
    if '0' in box[i]:
        check =True
if check:
    print(-1)
else:
    print(cnt-1)
    