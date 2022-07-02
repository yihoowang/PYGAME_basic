import pygame

pygame.init()
WINDOW_WINTH,WINDOW_HIGHT=800,600
display=pygame.display.set_mode((WINDOW_WINTH,WINDOW_HIGHT))
pygame.display.set_caption("Blitting image")

brid_topleft=pygame.image.load("angrybird.png")#載圖
brid_topleft_rect=brid_topleft.get_rect()#取得圖案大小放變數中
brid_topleft_rect.topleft=(0,0)#設定圖案出現位置
#載入圖片物件與設定位置
brid_topright=pygame.image.load("angrybird.png")#載圖
brid_topright_rect=brid_topright.get_rect()#取得圖案大小放變數中
brid_topright_rect.topright=(WINDOW_WINTH,0)#設定圖案出現位置

WHITE=(255,255,255)
GREEN=(0,255,0)
DARKGREEN=(10,50,10)

#fonts=pygame.font.get_font()//取得所有pygame內建字型
system_font=pygame.font.SysFont("centry",64)
costom_font=pygame.font.Font("Attack.ttf",50)#載入外部下載字型

#define text:
show_text_1=system_font.render("andry bird game:",True,GREEN,DARKGREEN)
show_text_1_rect=show_text_1.get_rect()#產方塊
show_text_1_rect.center=(WINDOW_WINTH//2, 30)

show_text_2=costom_font.render("move angry brid soon!",True,GREEN)
show_text_2_rect=show_text_2.get_rect()#產方塊
show_text_2_rect.center=(WINDOW_WINTH//2,WINDOW_HIGHT//2+100)
#音效
sound_1=pygame.mixer.Sound("sound_1.wav")
sound_2=pygame.mixer.Sound("sound_2.wav")

sound_1.play()
pygame.time.delay(2000)#毫秒
sound_1.play()
pygame.time.delay(2000)

sound_2.set_volume(1.0)#設音量
sound_2.play()#播放

#背景音:
pygame.mixer.music.load("music.wav")#-1重複播放，從頭
pygame.mixer.music.play(-1,0.0)      #-1重複播放，從頭
pygame.time.delay(10000)
pygame.mixer.music.stop()
running=True
while running:
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            running=False
    pygame.draw.line(display,WHITE,(0,75),(WINDOW_WINTH,75),5)
    display.blit(brid_topleft,brid_topleft_rect)
    display.blit(brid_topright,brid_topright_rect)
    display.blit(show_text_1,show_text_1_rect)
    display.blit(show_text_2,show_text_2_rect)
    pygame.display.update()
pygame.quit()