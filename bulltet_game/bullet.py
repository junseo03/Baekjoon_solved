import pygame

#총알 클래스
class Bullet:

    def __init__(self, x, y, to_x, to_y,type):
        self.type = type                        #총알 종류 설정
        
        if self.type ==1:                       #빨간 총알 
            self.pos =[x,y]                     #빨간 총알 위치
            self.to =[to_x,to_y]                #빨간 총알 방향
            self.radius = 7                     #빨간 총알 반지름
            self.color = (190,0,0)              #빨간색

        if self.type ==2:                       #초록 총알
            self.pos =[x,y]                     #초록 총알 위치
            self.to =[to_x,to_y]                #초록 총알 방향
            self.radius = 10                    #초록 총알 반지름
            self.color = (0,190,0)              #초록색
        
        if self.type ==3:                       #파란 총알
            self.pos =[x,y]                     #파란 총알 위치
            self.to =[to_x,to_y]                #파란 총알 방향
            self.radius = 13                    #파란 총알 반지름
            self.color = (0,0,190)              #파란색

    #총알 그리는 함수            
    def update_and_draw(self,dt,screen):
        width, height =screen.get_size()                                #화면 가로세로 길이를 가져온다.
        self.pos[0] = (self.pos[0]+dt*self.to[0]) %width                #총알이 계속 돌아다니기 위한 위치 설정
        self.pos[1] = (self.pos[1]+dt*self.to[1]) %height               #총알리 계속 돌아다니기 위한 위치 설정
        pygame.draw.circle(screen,self.color,self.pos, self.radius)     #총알을 그린다.