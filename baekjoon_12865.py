#변수 입력받기
N, K = map(int,input().split())
#딕녀너리와 리스트 선언
things ={}
answer=[]
#무게와 가치를 딕셔너리에 저장
for i in range(N):
    W, V = map(int,input().split())
    things[W] = V
Weight = list(things.keys())
Min = min(Weight)

def add(K , i , cur_Weight, Weight, answer_weight, answer_value,things ):
    if i <= N-1:
        tmp_weight = cur_Weight + Weight[i]
        tmp_value = answer_value + things[Weight[i]]
        if tmp_weight > K:
            answer.append(answer_value)
            add(K,i+1, cur_Weight, Weight, answer_weight, answer_value,things)
        elif tmp_weight == K:
            answer.append(tmp_value) 
        else:
            add(K, i,  tmp_weight, Weight, tmp_weight, tmp_value,things)
            add(K, i+1,  tmp_weight, Weight, tmp_weight, tmp_value,things)            

    else:
        return(0)

#1차 가능한 가치 값 리스트 저장
for i in range(N):
    answer.append(things[Weight[i]] * (K//Weight[i]) )

#things_sorted = sorted(things.items())
Weight.sort(reverse=True)
#2차 가능한 가치값 리스트 저장
for i in range(N-1):
    add(K,i, 0, Weight, 0, 0 ,things)
                
print(max(answer))
