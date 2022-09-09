#괄호 쪼개서 입력받기
bracket = list(input())
#스택을 위한 리스트
stack=[]
#결과값 
answer=0
#임시 변수
tmp=1

#입력된 괄호 수만큼 반복
for i in range(len(bracket)):

#"("라면 스택추가하고 2배
    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3
    
    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer=0
            break
        if bracket[i-1] == '(':
            answer += tmp
        stack.pop()
        tmp //= 2
    elif bracket[i] == "]":
        if not stack or stack[-1] == "(":
            answer=0
            break
        if bracket[i-1] == '[':
            answer += tmp
        stack.pop()
        tmp //= 3
    
if stack:
    print(0)
else:
    print(answer)
