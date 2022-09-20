N = int(input())
M = N % 1500000
def Fabo(n,a,b,k):
        if n == 1:
            print(0)
            return 0
        elif n == 2:
            print(1)
            return 0
        elif k == n:
            print(b%1000000)
        else:
            Fabo(n,b%1500000,(a+b)%1500000,k+1)

Fabo(N,0,1,2)