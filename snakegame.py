# import pygame
# pygame.init()
# dis=pygame.display.set_mode((400,380))
# pygame.display.update()
# pygame.quit()
# quit()
# pygame
#to open contineous  screen
import pygame
pygame.init()
dis=pygame.display.set_mode((400,380))
pygame.display.update()
pygame.display.set_caption('snake game')
blue=(0,0,255)
white=(255,255,255)
red=(255,0,0)
game_over=False #we can also use true and delete not in while loop
x1=300
y1=300
x1_change=0
y1_change=0
clock=pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():    #captures the event ex pressing buttons
        if event.type==pygame.QUIT:
            game_over=True   #this will end the game
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x1_change=-10
                y1_change=0
            if event.key==pygame.K_RIGHT:
                x1_change=10
                y1_change=0
            if event.key==pygame.K_UP:
                x1_change=0
                y1_change=-10
            if event.key==pygame.K_LEFT:
                x1_change=0
                y1_change=10
    x1+=x1_change
    y1+=y1_change
    dis.fill(white)
    pygame.draw.rect(dis,blue,[x1,y1,10,10])
    pygame.display.update()
    clock.tick(3)
pygame.quit()
quit()
