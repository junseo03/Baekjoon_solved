import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def destroy(left,stick):
    if left:
        for i in range(C):
            if cave[stick][i] == 'x':
                cave[stick][i] = '.'
                return (i,stick)
    else:
        for i in range(C-1,-1,-1):
            if cave[stick][i] == 'x':
                cave[stick][i] = '.'
                return (i,stick)
    return (-1,-1)

def search(x,y):
    falling = True
    q = deque()
    dq = deque()
    q.append((x,y))
    if 0<=x<C and 0<=y<R:
        if cave[y][x] =='x':
            dq.append((x,y))
    visit = [[0 for _ in range(C)] for _ in range(R)]
    while q:
        xx,yy  = q.popleft()
        for i in range(4):
            xxx = xx+dx[i]; yyy = yy+dy[i]
            if 0<=xxx<C and 0<=yyy<R:
                if not visit[yyy][xxx]:
                    visit[yyy][xxx]+=1
                    if cave[yyy][xxx] == 'x':
                        if yyy==R-1:
                            q.clear()
                            falling = False
                        else: 
                            q.append((xxx,yyy))
                            dq.append((xxx,yyy))
    if len(dq)-1<0:
        falling =False       
    return (falling,dq)

def fall(q):
    x,y = q
    q = deque()
    for i in range(4):
        xx = x+dx[i]; yy = y+dy[i]
        
        falling,dq = search(xx,yy)
        if falling:
            tmp = deque()
            while falling:
                tmp.clear()
                while dq:
                    xx,yy = dq.popleft()
                    q.append((xx,yy+1))
                    tmp.append((xx,yy+1))
                    cave[yy][xx] = '.'
                for qq in q:
                    dq.append(qq)
                while q:
                    xx,yy = q.popleft()
                    cave[yy][xx] = 'x'
                    if yy == R-1:
                        falling = False
                    elif cave[yy+1][xx] =='x' and (xx,yy+1) not in dq:
                        falling = False
            return 0
    return 0

R,C = map(int,sys.stdin.readline().split())

cave = [[] for _ in range(R)]

for i in range(R):
    line =  list(sys.stdin.readline()[:-1])
    cave[i] = line

N = int(sys.stdin.readline())
S = list(map(int,sys.stdin.readline().rstrip('\n').split()))

toggle = 0
for i in range(N):
    toggle+=1
    x,y = destroy((toggle)%2,R-S[i])    
    if y+x !=-2:
        fall((x,y))
for i in cave:
    for j in i:
        print(j, end='')
    print()
