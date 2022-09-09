import pygame 

#플레이어 클래스
class Player:
    
    def __init__(self,x,y):
        self.image = pygame.image.load('player.png')                            #비행기 그림 로드
        self.image = pygame.transform.scale(self.image, (64,64))                #비행기 크기 설정
        self.image2 = pygame.image.load('player2.png')                          #무적 상태시 반짝거림을 위한 다른색 비행기 그림 로드
        self.image2 = pygame.transform.scale(self.image2, (64,64))              #다른색 비행기 크기 설정
        self.boom_image =  pygame.image.load('boom.png')                        #터지는 그림 효과 로드
        self.boom_image = pygame.transform.scale(self.boom_image, (80,80))      #터지는 그림 효과 크기 설정
        self.pos = [x,y]                                                        #플레이어 위치 
        self.to = [0,0]                                                         #플레이어 방향
        self.acc = [0,0]                                                        #플레이어 각도
        self.boom = False                                                       #폭발 여부
        self.boom_time = 0                                                      #터지는 그림 효과 지속시간
        self.blink = 0                                                          #비행기 반짝거림을 위한 설정
    
    #플레이어 방향 변경
    def goto(self, x ,y):           #매개변수 x,y에 따라 방향 변경                                               
        self.to[0] += x             
        self.to[1] += y
    
    #플레이어 화면 출력
    def draw(self,screen,invincibility):                                    #screen 정보와 무적 여부를 매개변수로 받음       
        
        calib_pos = (self.pos[0] - self.image.get_width()/2,                #플레이어 위치 설정
                    self.pos[1] - self.image.get_height()/2)
        
        self.angle = 0                                                      #플레이어 초기 각도 설정
        
        #플레이어 방향에 따라 각도를 바꾸는 부분
        if self.to ==[-1,-1]: self.angle =45
        elif self.to ==[-1,0]: self.angle = 90
        elif self.to ==[-1,1]: self.angle = 135
        elif self.to == [0,1]: self.angle = 180
        elif self.to ==[1,1]: self.angle = -135
        elif self.to ==[1,0]: self.angle = -90
        elif self.to ==[1,-1]: self.angle = -45
        elif self.to ==[0,-1]: self.angle = 0

        #폭발 여부,무적여부에 따라 플레이어 그림을 바꾸는 부분

        #폭발한 상태라면 터지는 효과 그림을 플레이어 그림으로 설정한다.
        if self.boom:                                            
            rotated = pygame.transform.rotate(self.boom_image , self.angle)             
        
        #무적 상태라면 번갈아 가면서 파란 비행기와 노란 비행기를 플레이어 그림으로 설정한다.
        elif invincibility:                                                                
            if self.blink%2 ==0:                                                        
                    rotated = pygame.transform.rotate(self.image2 , self.angle)
                    self.blink +=1
            else:
                    rotated = pygame.transform.rotate(self.image , self.angle)
                    self.blink +=1
        #폭발 상태도 무적 상태도 아니라면 파란 비행기를 플레이어 그림으로 설정한다.
        else:    
            rotated = pygame.transform.rotate(self.image , self.angle)
        
        #플레이어 그림을 화면에 각도와 위치를 반영해 화면에 출력한다.
        screen.blit(rotated,calib_pos)

    #플레이어 위치 정보와 폭발 여부 업데이트    
    def update(self, dt, screen, collision):
        
        #플레이어 위치 설정
        width, height = screen.get_size()                           #화면 가로 세로 길이를 가져온다.
        self.pos[0] = self.pos[0] + dt*self.to[0]                   #플레이어 방향에 따라 플레이어 x좌표 위치 수정
        self.pos[1] = self.pos[1] + dt*self.to[1]                   #플레이어 방향에 따라 플레이어 y좌표 위치 수정
        self.pos[0] = min(max(self.pos[0], 32), width-32)           #플레이어가 화면밖으로 나가지 않기 위한 설정
        self.pos[1] = min(max(self.pos[1], 32), height-32)          #플레이어가 화면밖으로 나가지 않기 위한 설정

        #플레이어 폭발 여부 설정
        self.boom_time -= dt                #폭발 상태 지속시간을 카운트한다.
        if collision:                       #총알과 충돌 확인
            self.boom = True                #충돌했다면 폭발 상태로 설정
            self.boom_time = 1000           #폭발 상태 지속시간 1초
        if self.boom_time <0:               #폭발 상태 지속시간이 지났는지 확인
            self.boom = False               #폭발 상태 해제   

    #플레이어가 움직이는 방향에 맞춰 배경을 움직이기 위한 함수
    def get_to(self):
        return self.to          #플레이어의 방향을 리턴한다.
    