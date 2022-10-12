from collections import deque
import sys
q = deque()
Path = ""
for _ in range(int(sys.stdin.readline())):
    Visited = [ False for _ in range(10001)]
    q.clear()
    A,B = map(int,sys.stdin.readline().split()) 
    q.append((A,Path))

    while q:
        num, path = q.popleft()
        Visited[num] =True
        if num == B:
            print(path)
            break
        num1 = (num*2)%10000
        if Visited[num1] == False:
            Visited[num1] = True
            q.append((num1,path+"D"))
        num2 = (num+9999)%10000
        if Visited[num2] == False:
            Visited[num2] = True
            q.append((num2,path+"S"))
        
        num3 = int((num//1000+num*10)%10000)
        if Visited[num3] == False:
            Visited[num3] = True
            q.append((num3,path+"L"))
        num4 = num//10+(num%10*1000)
        if Visited[num4] == False:
            Visited[num4] = True
            q.append((num4,path+"R"))