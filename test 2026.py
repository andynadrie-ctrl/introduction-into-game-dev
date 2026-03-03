import pygame
pygame.init()

WIDTH,HEIGHT=800,600


screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("[2026 run]")
clock = pygame.time.Clock()



sky=pygame.transform.scale(pygame.image.load("Desktop/intro into/sky.JPG"),(WIDTH,HEIGHT))
ground=pygame.transform.scale(pygame.image.load("Desktop/intro into/ground.JPG"),(WIDTH,200))


# -------- PLAYER SETUP --------
run_frames = [
    pygame.image.load("Desktop/intro into/run/1.png").convert_alpha(),
    pygame.image.load("Desktop/intro into/run/2.png").convert_alpha(),
    pygame.image.load("Desktop/intro into/run/3.png").convert_alpha(),
    pygame.image.load("Desktop/intro into/run/4.png").convert_alpha(),
    pygame.image.load("Desktop/intro into/run/5.png").convert_alpha(),
    pygame.image.load("Desktop/intro into/run/6.png").convert_alpha(),
    pygame.image.load("Desktop/intro into/run/7.png").convert_alpha(),
    pygame.image.load("Desktop/intro into/run/8.png").convert_alpha(),
]

player_x = 100
player_y = 360   # on top of ground
speed = 5

frame_index = 0
animation_speed = 0.2
running = False

# ---------- MAIN LOOP ----------
while True:
    # ---------- EVENT HANDLING ----------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(sky,(0,0))
    screen.blit(ground,(0,400))


    keys = pygame.key.get_pressed()
    running = False

    if keys[pygame.K_RIGHT]:
        player_x += speed
        running = True

    if keys[pygame.K_LEFT]:
        player_x -= speed
        running = True

    # Animate
    if running:
        frame_index += animation_speed
        if frame_index >= len(run_frames):
            frame_index = 0
    else:
        frame_index = 0

    screen.blit(run_frames[int(frame_index)], (player_x, player_y))
    pygame.display.update()
    clock.tick(60)