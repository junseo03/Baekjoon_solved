N = int(input())

def hanoi(N, form_pos, aux_pos, to_pos):
    if N == 1:
        print(form_pos, to_pos)
    else:
        hanoi(N-1, form_pos,to_pos,aux_pos)
        hanoi(1,form_pos,aux_pos,to_pos)
        hanoi(N-1, aux_pos, form_pos, to_pos)

print(2**N-1)
if N < 21:
    hanoi(N ,1,2,3)