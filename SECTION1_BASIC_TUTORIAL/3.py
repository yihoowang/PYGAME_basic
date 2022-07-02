
import random

import pygame

pygame.init()
WINDOW_WINTH,WINDOW_HIGHT=800,600
display=pygame.display.set_mode((WINDOW_WINTH,WINDOW_HIGHT))
pygame.display.set_caption("movent and collisions!")
BLACK=(0,0,0)
#set FPS(frequency per second)and clock(抓cpu的時序)
FPS=60
clock=pygame.time.Clock()
#set game values
velocity=5#速率
BLACK=(255,255,255)
angry_bird=pygame.image.load("angrybird.png")
angry_bird_rect=angry_bird.get_rect()
angry_bird_rect.center=(WINDOW_WINTH//2,WINDOW_HIGHT//2)

coin=pygame.image.load("coin.png")
coin_rect=coin.get_rect()
coin_rect.center=(100,100)
running=True
while running:
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            running=False
    display.blit(angry_bird,angry_bird_rect)
    keys=pygame.key.get_pressed()#側有哪個鍵被按下
    if keys[pygame.K_LEFT]or keys[pygame.K_a]and angry_bird_rect.left>0:
        angry_bird_rect.x-=velocity
    if keys[pygame.K_RIGHT]or keys[pygame.K_d]and angry_bird_rect.right<WINDOW_WINTH:
        angry_bird_rect.x+=velocity
    if keys[pygame.K_UP]or keys[pygame.K_w]and angry_bird_rect.top>0:
        angry_bird_rect.y-=velocity
    if keys[pygame.K_DOWN]or keys[pygame.K_s]and angry_bird_rect.bottom<WINDOW_HIGHT:
        angry_bird_rect.y+=velocity
    if angry_bird_rect.colliderect(coin_rect):
        print("hit")
        coin_rect.x=random.randint(0,WINDOW_WINTH-50)
        coin_rect.y=random.randint(0,WINDOW_HIGHT-50)
    display.fill(BLACK)
    display.blit(coin,coin_rect)
    display.blit(angry_bird,angry_bird_rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()