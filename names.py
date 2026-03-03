import pygame
 
pygame.init()


WIDTH,HEIGTH= 800,600
WHITE=(225,255,255)
BLACK=(0,0,0)
FONT_SIZE=32

screen= pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption(("Bissekie Ndongo Andre marie's screen"))
font= pygame.font.SysFont('Arial',FONT_SIZE)
clock=pygame.time.Clock()

text_surface= font.render("Bissekie Ndongo Andre Marie",True,BLACK)

text_rect= text_surface.get_rect(center=(WIDTH//2,HEIGTH//2))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(WHITE)
    screen.blit(text_surface,text_rect)
    
    pygame.display.flip()
    clock.tick(60)
