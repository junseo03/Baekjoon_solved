import math

def DrawStar(i, N, space):
    if N == 3:
        A = '*'
        if i % N ==1:
            B = " "
        else:
            B = A
    else:
        j = round(math.log(N,3))
        A = DrawStar(i, N//3, space)
        if i % (3**(j)) in space[j-1]:
            B = " "*(N//3)
        else:
            B = A
    return A+B+A

N = int(input())
space = []
for i in range(round(math.log(N,3))):
    num = 3**(i+1)
    space.append(list(range(num)[int(num/3): int(num/3)*2]))
for i in range(N):
    ans = DrawStar(i, N, space)
    print(ans)