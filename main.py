import time

import pygame

from screen import Screen

pygame.init()
clock = pygame.time.Clock()
fps = 30
screen = Screen((600, 400))

last_time = time.time()

running = True

particles = pygame.sprite.Group()

# define ball
ball_obj = pygame.draw.circle(
    surface=screen.surface, color='red', center=[100, 100], radius=20)
# define speed of ball
# speed = [X direction speed, Y direction speed]
speed = [5, 5]


# define colors
red = (255, 0, 0)
black = (0, 0, 0)

while running:

    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                screen.dy = -1
            if event.key == pygame.K_s:
                screen.dy = 1
            if event.key == pygame.K_a:
                screen.dx = -1
            if event.key == pygame.K_d:
                screen.dx = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                screen.dy = 0
            if event.key == pygame.K_s:
                screen.dy = 0
            if event.key == pygame.K_a:
                screen.dx = 0
            if event.key == pygame.K_d:
                screen.dx = 0

    screen.update(dt)

    ball_obj = ball_obj.move(speed)

    if ball_obj.left <= 0 or ball_obj.right >= screen.width:
        speed[0] = -speed[0]
    if ball_obj.top <= 0 or ball_obj.bottom >= screen.height:
        speed[1] = -speed[1]

    pygame.draw.circle(screen.surface, color=red,
                       center=ball_obj.center, radius=20)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
