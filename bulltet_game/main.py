import pygame
import random as rnd
from bullet import Bullet
import math
import time
from player import Player


hp = 10
gameover = False
invincibility = False
score = 0
hp_bar = '//////////'
collision_time = 0
waiting_time =0
Red_bullets = []                            
Green_bullets = []
Blue_bullets = []
time_for_adding_bullets = 0
collision_check = False
scores = []
record = 0
start_time = time.time()

# txt를 화면에 쓰기위한 함수
def draw_text(txt, size, pos, color):
    font = pygame.font.Font('freesansbold.ttf', size)   #폰트 지정
    r = font.render(txt, True, color)                   #txt가 표시된 surface를 만듦
    screen.blit(r,pos)                                  #화면에 출력


pygame.init()  
WIDTH , HEIGHT = 1000,800                               #화면크기 설정
pygame.display.set_caption("총알 피하기")               #게임 제목
screen = pygame.display.set_mode((WIDTH,HEIGHT))        #화면 생성

clock = pygame.time.Clock()                 #pygame의 시간 관리
FPS = 60                                    #프레임 설정
bg_image = pygame.image.load('bg.jpg')      #배경화면 로드
bg_pos = [-500,-500]                        #배경화면 위치 지정
bg_to = [0,0]                               #배경화면 방향 지정

pygame.mixer.music.load('bgm.wav')          #배경음악 로드
pygame.mixer.music.play(-1)                 #배경음악 무한반복 재생

player = Player(WIDTH/2,HEIGHT/2)           #player를 player 클래스로 정의

#총알 생성
for i in range(10):                                                                                 #처음 10개의 총알 생성
    type = rnd.randrange(1,4)                                                                       #총알 종류를 랜덤으로 지정
    if type ==1:                            
        Red_bullets.append(Bullet(0, rnd.random()*HEIGHT, rnd.random()-0.5, rnd.random()-0.5,1))    #빨간 총알을 빨간 총알 리스트에 추가
    if type ==2:
        Green_bullets.append(Bullet(0, rnd.random()*HEIGHT,rnd.random()-0.5,rnd.random()-0.5,2))    #초록 총알을 초록 총알 리스트에 추가
    if type ==3:
        Blue_bullets.append(Bullet(0, rnd.random()*HEIGHT,rnd.random()-0.5,rnd.random()-0.5,3))     #파란 총알을 파란 총알 리스트에 추가

# 플레이어와 총알의 충돌을 감지하기 위한 함수
def collision(obj1,obj2):   
    if math.sqrt( (obj1.pos[0] -obj2.pos[0])**2 +
                 (obj1.pos[1]- obj2.pos[1])**2 )<20:        #플레이어와 총알이 충돌했다는 거리 지정
        if invincibility == False:                          #무적이 아닌 경우 충돌로 판단
            soundObj = pygame.mixer.Sound('boom.wav')       #boom.wav 사운드 로드   
            soundObj.play()                                 #충돌할 경우 boom.wav 재생           
            return True
    return False

#게임 시작
running = True  
while running:
    dt = clock.tick(FPS)                            #FPS설정
    time_for_adding_bullets +=dt                    #총알 추가시간 카운트
    
    # 키보드 입력을 받는 부분
    for event in pygame.event.get():                
        if event.type == pygame.QUIT:               #창닫기하면 게임 종료                  
            running = False
        if event.type == pygame.KEYDOWN:            #키보드를 누루면 누룬 키보드 화살표 방향으로 플레이어 방향 변경
            if event.key == pygame.K_LEFT:
                player.goto(-1,0)
            elif event.key == pygame.K_RIGHT:
                player.goto(1,0)
            elif event.key == pygame.K_DOWN:
                player.goto(0,1)
            elif event.key == pygame.K_UP:
                player.goto(0,-1)
        if event.type == pygame.KEYUP:              #키보드를 떼면 플레이어의 방향을 원래대로 되돌림
            if event.key == pygame.K_LEFT:
                player.goto(1,0)
            elif event.key == pygame.K_RIGHT:
                player.goto(-1,0)
            elif event.key == pygame.K_DOWN:
                player.goto(0,-1)
            elif event.key == pygame.K_UP:
                player.goto(0,1)
    
    #배경 위치와 방향 설정
    bg_goto = player.get_to()                                                                       #플레이어의 방향을 배경의 방향으로 정의
    bg_pos = (bg_pos[0] + bg_goto[0] * -0.1 * dt, bg_pos[1] + bg_goto[1] * -0.1 * dt)               #배경의 좌표를 방향에 따라 바꿈
    bg_pos = (max(min(bg_pos[0], 0), -2053 + WIDTH), max(min(bg_pos[1], 0), -1500 + HEIGHT))        #배경이 최대한 움직일 수 있는 좌표 설정
    screen.blit(bg_image, bg_pos)                                                                   #배경 그리기
    
    #플레이어 정보 업데이트와 플레이어 화면에 그리기
    player.update(dt, screen , collision_check)                                                     #플레이어 위치 지정, 플레이어 터지는 그림효과으로 변할 필요성 확인
    player.draw(screen,invincibility)                                             #플레이어를 화면에 출력,무적 상태라면 무적 지속시간동안 반짝거림

    collision_check = False                                                                         #다시 비행기 그림을 보이고 다음번 확인을 위해 다시 False로 설정
    
    #총알과 부딪혔는지 확인하는 부분
    if not gameover:                                                                                
        for b in Red_bullets:                           #빨간 총알의 개수만큼 부딪혔는지 확인
            if collision(player,b):                     
                invincibility = True                    #무적 활성화
                collision_time = time.time() - start_time        #무적 시간 카운트 시작
                collision_check = True                  #폭발 그림효과를 보이도록 설정
                hp -= 1                                 #HP 감소
                hp_bar = hp_bar[1:]                     #HP 막대기 감소
                                     
        for b in Green_bullets:                         #초록 총알의 개수만큼 부딪혔는지 확인
            if collision(player,b):                     
                invincibility = True                    #무적 활성화
                collision_time = time.time() - start_time        #무적 시간 카운트 시작
                collision_check = True                  #폭발 그림효과를 보이도록 설정
                hp -= 2                                 #HP 감소
                hp_bar = hp_bar[2:]                     #HP 막대기 감소

        for b in Blue_bullets:                          #파란 총알의 개수만큼 부딪혔는지 확인
            if collision(player,b):
                invincibility = True                    #무적 활성화
                collision_time = time.time() - start_time        #무적 시간 카운트 시작
                collision_check = True                  #폭발 그림효과를 보이도록 설정
                hp -= 3                                 #HP 감소
                hp_bar = hp_bar[3:]                     #HP 막대기 감소
    
    #HP가 없으면 gameover
    if hp <=0:                                          #HP가 0인지 확인하고 gameover 설정
        gameover = True
    
    #무적 상태 설정
    if (time.time() - start_time) - collision_time >5:           #무적시간 5초가 지나면 다시 무적이 아닌 상태로 설정
        invincibility = False
    
    #총알을 화면에 그림    
    for b in Red_bullets:
        b.update_and_draw(dt,screen)
    for b in Green_bullets:
        b.update_and_draw(dt,screen)
    for b in Blue_bullets:
        b.update_and_draw(dt,screen)
    
    #게임이 끝나면 기록 작성
    if record ==1:                                      #게임이 끝나고 한번만 기록을 수정하기 위한 설정
        record +=1                                      #게임이 끝나고 한번만 기록을 수정하기 위한 설정
        f = open("record.txt" , "r")                    #record.txt파일을 연다.
        for a in range(10):                             #record.txt.파일 줄읽기를 10번 반복  
            k = f.readline()                            #record.txt.파일 한줄을 읽는다.
            scores.append(float(k))                     ##record.txt.파일에서 읽은 내용을 float형태로 scores리스트에 추가한다.             
        f.close()                                       #파일을 닫는다.
        new_record = round(score,1)                     #현재까지 버틴 시간을 소수점 한자리수까지 new_record로 정의한다.
        scores.append(new_record)                       #현재까지 버틴 시간을 scores리스트에 추가한다.
        scores.sort(reverse=True)                       #scores리스트를 큰 숫자 순서대로 정리한다.
        del scores[10]                                  #리스트에서 가장 작은 숫자 삭제
        f =  open("record.txt", "w")                    #record.txt 파일을 연다.
        for s in scores:                                #record.txt에 scores리스트 원소들을 내림차순으로 저장한다.
            f.write(str(s) +"\n")                       #record.txt에 s번째 원소를 작성한다.
        f.close()                                       #record.txt 파일을 닫는다.
    
    #게임이 끝났을 때 현재까지 버틴 시간과 총알수, 기록을 보여주는 부분
    if gameover:
        if waiting_time ==0:                                                                                                  #현재까지 버틴 시간과 총알 수를 한번 보여주기 위한 설정
            waiting_time = time.time() - start_time                                                                           #타이머2 시작 시간 설정
        if (time.time() - start_time) - waiting_time < 3:                                                                      #현재 버틴 시간과 총알수를 3초동안 보여준다.
            draw_text("GAME OVER" , 100, (WIDTH/2 - 300, HEIGHT/2 - 50) , (255,255,255))                                #GAMEOVER를 지정한 위치 하얀색으로 화면에 출력
            txt = "Time:{:.1f} Bullet:{}".format(score, len(Red_bullets)+len(Green_bullets)+len(Blue_bullets))          #시간과 총알수를 txt로 정의
            draw_text(txt, 32, (WIDTH/2 - 150, HEIGHT/2 + 50) , (255,255,255))                                          #위 txt를 지정한 위치 하얀색으로 화면에 출력
            if record ==0:                                                                                              #게임이 끝남음으로 기록을 시작하기 위한 설정
                record = 1                                                                                              #기록 시작
        else:
            draw_text("RECORDS" , 100, (WIDTH/2 - 250, HEIGHT/2 - 350) , (255,255,255) )                                #3초후 RECORDS 화면 상단에 출력
            for n in range(10):                                                                                         #기록들 화면 출력을 10번 반복
                txt = "{}.  {}".format(n+1, scores[n])                                                                  #등수와 시간을 txt로 정의
                if scores[n] == new_record:                                                                             #지금 기록되는 버틴 시간이 이번 게임 기록인지 확인
                    draw_text(txt, 32, (WIDTH/2 - 250, HEIGHT/2 -(200-n*50)) , (255,0,0))                               #지금 기록되는 버틴 시간이 이번 게임의 기록이라면 글자를 빨간색으로 출력
                else:
                    draw_text(txt, 32, (WIDTH/2 - 250, HEIGHT/2 -(200-n*50)) , (255,255,255))                           #이번 게임 기록이 아니라면 하얀색으로 출력
            
    #게임이 끝나지 않았을 때 현재까지 버티고 있는 시간과 현재 총알수를 보여주는 부분
    else:                                                                                                               
        score = time.time() - start_time                                                                                                #현재까지 버틴 시간
        txt = "Time:{:.1f} Bullet:{} HP:{}  {} ".format(score, len(Red_bullets)+len(Green_bullets)+len(Blue_bullets),hp , hp_bar )      #현재 시간, 총알 수, HP 수, HP 수 막대기를 txt로 정의
        draw_text(txt, 32 ,(10,10), (255,255,255))                                                                                      #위 txt를 하얀색으로 화면에 출력
        
        #1초마다 총알을 추가하기 위한 부분
        if time_for_adding_bullets >1000:                                                                   #1초가 지나면 총알 추가
            type = rnd.randrange(1,4)                                                                       #총알 종류 랜덤으로 선택
            if type ==1:                                                                                    #빨간 총알 추가 생성
                Red_bullets.append(Bullet(0, rnd.random()*HEIGHT,rnd.random()-0.5,rnd.random()-0.5,1))
            if type ==2:                                                                                    #초록 총알 추가 생성
                Green_bullets.append(Bullet(0, rnd.random()*HEIGHT,rnd.random()-0.5,rnd.random()-0.5,2))
            if type ==3:                                                                                    #파란 총알 추가 생성
                Blue_bullets.append(Bullet(0, rnd.random()*HEIGHT,rnd.random()-0.5,rnd.random()-0.5,3))
            time_for_adding_bullets -=1000                                                                  #총알을 생성하고 다시 총알 생성 대기시간을 1초로 설정
    
    pygame.display.update()             #화면 업데이트

                                                                    