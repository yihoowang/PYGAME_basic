from tkinter import W
import pygame#載載入遊戲模組

pygame.init()#遊戲模組啟動
WINDOW_WINTH,WINDOW_HIGHT=800,600
display=pygame.display.set_mode((WINDOW_WINTH,WINDOW_HIGHT))#產生畫布
pygame.display.set_caption("my first pygame!")

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
CYAN=(0,255,255)
MEG=(255,0,255)
gray=(192,192,192)
display.fill(gray)#填滿畫布背景
#pygame.draw.line(畫布名稱，color,start,end,thickness)
pygame.draw.line(display,GREEN,(0,WINDOW_HIGHT//2),(WINDOW_WINTH,WINDOW_HIGHT//2),5)
pygame.draw.line(display,RED,  (WINDOW_WINTH//2,0),(WINDOW_WINTH//2,WINDOW_HIGHT),5)
pygame.draw.line(display,GREEN,(0,0),(WINDOW_WINTH,WINDOW_HIGHT),5)

#pygame.draw.circle(畫布名稱，color,中心點,半徑,thickness)thickness=0(填滿),1,2...10:線條寬度
pygame.draw.circle(display,CYAN,(WINDOW_WINTH//2,WINDOW_HIGHT//2),200,6)
pygame.draw.circle(display,CYAN,(WINDOW_WINTH//2,WINDOW_HIGHT//2),180,0)

#pygame.draw.rect(畫布名稱，color,(topleft-x,topleft-y,width,height))
pygame.draw.rect(display,BLUE,(0,0,WINDOW_WINTH,100),0)
running=True
while running:
    for event in pygame.event.get():#抓取畫布所有物件
        #print(event)
        if event.type==pygame.QUIT:#事件的type==quit(案結束建)
            running=False
    pygame.display.update()#畫布更新
pygame.quit()#遊戲模組結束