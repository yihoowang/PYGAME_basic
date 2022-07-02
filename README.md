# python_game:自己創造的小遊戲

 1. **參考資料**
   1. pygame page http://pygame.org
   2. documentation:http://pygame.org/docs/ref/
   3. Icon Archive:https://iconarchive.com/(下載角色)
   4. leshy SFMaker:https://www.leshylabs.com/apps/sfMaker/(載音效)
   5. ~~xxxxxxxx 忘了~~<br><br>
  ------
**_2.What is pygame_**:
  * pygame提供display,sound,image,text,event幫助製作遊戲
  * pygame可做出2-d小遊戲
  * pygame偵測使用者用keyboard,joystick,mouse控制遊戲
  * pygame提供許多內建的game object來製遊戲<br><br>
  
**_3.pygame basic_**:
  |name|description|
  |:-----:|:-----:|
  | _1.py_ |create my game surfance，game loop and darwing.|
  | _2.py_ |blit text,font,sound,and,image objects.     |  
  | _3.py_ |getting user keyboard and collision dection.|
  
**_4.code snipped_**
```python
#create game display
WINDOW_WINTH,WINDOW_HIGHT=1000,600
display1=pygame.display.set_mode((WINDOW_WINTH,WINDOW_HIGHT))
pygame.display.set_caption("movent and collisions!")

```
```python
#blit image object and setting its rec.
player_image=pygame.image.load("angry_bird.png")
player_rect=player_image.get_rect()
player_rect.left=32
player_rect.centery=WINDOW_HIGHT//2
 display1.blit(player_image,player_rect)
 ```
 **_5.game assets:_**
 .[icon archive:](https://iconarchive.com/)網站提供角色下載<br>
 .[leshy SFMaker:](https://www.leshylabs.com/apps/sfMaker/)網站可以載遊戲特效，也可以簡單自己製音效
 <img src="
