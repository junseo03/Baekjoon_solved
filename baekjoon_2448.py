def DrawStar(N,i,j):
    if N == 3:
        bg[i][j] = '*'
        bg[i+1][j-1] = '*'
        bg[i+1][j+1] = '*'
        bg[i+2][j] = '*'
        bg[i+2][j-1] = '*'
        bg[i+2][j-2] = '*'
        bg[i+2][j+1] = '*'
        bg[i+2][j+2] = '*'
        return 0
    else:
        DrawStar(N//2,i,j)
        DrawStar(N//2,i+N//2,j+N//2)
        DrawStar(N//2,i+N//2,j-N//2)

N = int(input())
bg = [[' ' for _ in range(N*2)] for _ in range(N)]
cnt = 0
T = N/3
while T != 1:
    T /= 2
    cnt+=1
DrawStar(N, 0, N-1)
for i in range(N):
    print(''.join(bg[i]))