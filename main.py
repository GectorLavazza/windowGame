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

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
