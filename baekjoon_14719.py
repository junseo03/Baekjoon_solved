#fkndndf
H , W = map(int,(input().split()))
block = list(map(int,(input().split())))
check = False
tmp = 0
rst = 0

for i in range(H,0,-1):
    for j in range(W):
        if block[j] >= i:
            if not check:
                tmp = j
                check = True
                #print(j)
            elif check:
                rst += j - tmp - 1
                check = False
    check = False

print(rst)