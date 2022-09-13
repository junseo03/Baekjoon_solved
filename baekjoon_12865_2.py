N, K = map(int,input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(N+1):
    for j in range(1,K+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        
        elif j == weight:
            knapsack[i][j] = max(knapsack[i-1][j] , value)

        else:
            knapsack[i][j] = max(knapsack[i-1][j] , value + knapsack[i-1][j-weight])

print(knapsack[N][K])





