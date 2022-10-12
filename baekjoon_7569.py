from collections import deque
import sys

check = False
cnt = 0
q = deque()
x = []
y = []
z = []
M,N,H = map(int,sys.stdin.readline().split())
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
box = [[[] for _ in range(N)] for _ in range(H)]
for k in range(H):
    for i in range(N):
        box[k][i] = input().split()
        for j in range(M):
            if box[k][i][j] == '1':
                q.append((j,i,k))
while q:
    for _ in range(len(q)):
        tmpx,tmpy,tmpz = q.popleft()
        if not visited[tmpz][tmpy][tmpx]:
            visited[tmpz][tmpy][tmpx] = True
            x.append(tmpx)
            y.append(tmpy)
            z.append(tmpz)
    for i in range(len(x)):
        if y[i] != 0:
            if box[z[i]][y[i]-1][x[i]] == '0':
                box[z[i]][y[i]-1][x[i]] = '1'
                q.append((x[i],y[i]-1,z[i]))
        if y[i] != N-1:
            if box[z[i]][y[i]+1][x[i]] == '0':
                box[z[i]][y[i]+1][x[i]] = '1'
                q.append((x[i],y[i]+1,z[i]))
        if x[i] != 0:
            if box[z[i]][y[i]][x[i]-1] == '0':
                box[z[i]][y[i]][x[i]-1] = '1'
                q.append((x[i]-1,y[i],z[i]))
        if x[i] != M-1:
            if box[z[i]][y[i]][x[i]+1] == '0':
                box[z[i]][y[i]][x[i]+1] = '1'
                q.append((x[i]+1,y[i],z[i]))
        if z[i] != 0:
            if box[z[i]-1][y[i]][x[i]] == '0':
                box[z[i]-1][y[i]][x[i]] = '1'
                q.append((x[i],y[i],z[i]-1))
        if z[i] != H-1:
            if box[z[i]+1][y[i]][x[i]] == '0':
                box[z[i]+1][y[i]][x[i]] = '1'
                q.append((x[i],y[i],z[i]+1))
    x.clear()
    y.clear()
    z.clear()
    cnt +=1
for i in range(H):
    for j in range(N):
        if '0' in box[i][j]:
            check =True
if check:
    print(-1)
else:
    print(cnt-1)
    