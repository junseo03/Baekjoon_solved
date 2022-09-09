#높이,넓이 입력
H , W = map(int,(input().split()))
#블록 리스트 입력
block = list(map(int,(input().split())))
#마지막 j의 에러 방지를 위한 0 추가
block.append(0)
#check 된 지점
tmp = 0
#결과값
rst = 0
#물이 가둬지는지 체크
check = False
#높이만큼 반복
for i in range(H,0,-1):
    for j in range(W):
        #현재 위치가 검은색으로 칠해진 부분이라면
        if block[j] >= i:
            #이전에 체크되지 않았다면 체크하고 현재위치를 저장            
            if check == False and block[j+1] <i: 
                check = True
                tmp = j
            #이전에 체크되었다면 물이 고인양 결과값에 더하기
            elif check == True:
                rst += j - tmp - 1
                #뒤에 막힌부분이 또 있을 경우를 대비해 현재위치 저장
                tmp = j
                #다음칸이 막혀있다면 다음칸을 체크하게 하기 위함
                if block[j+1] >= i:
                    check = False
    #고정위치 초기화
    tmp = 0
    #체크 초기화
    check = False
#결과값 출력
print(rst)