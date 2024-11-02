import pygame


class Screen:
    def __init__(self, size):
        self.set_screen(size)

        self.dx, self.dy = 0, 0
        self.velocity = pygame.Vector2(0, 0)

        self.speed = 10

        self.acceleration = 0.1
        self.deceleration = 0.05

    def set_screen(self, size):
        self.screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)
        self.screen_rect = (0, 0, size[0], size[1])
        self.size = size

    def update(self, dt):
        pygame.display.set_caption(str(tuple(map(round, self.size))))
        self.screen.fill(pygame.Color('black'))
        self.move(dt)

    def move(self, dt):
        input_direction = pygame.Vector2(self.dx, self.dy)

        if input_direction.length() > 0:
            input_direction = input_direction.normalize()
            self.velocity.x += input_direction.x * self.acceleration * dt
            self.velocity.y += input_direction.y * self.acceleration * dt
        else:
            if self.velocity.length() > 0:
                self.velocity.x -= self.velocity.x * self.deceleration * dt
                self.velocity.y -= self.velocity.y * self.deceleration * dt

        if self.velocity.length() > self.speed:
            self.velocity = self.velocity.normalize() * self.speed

        new_size = (self.size[0] + self.velocity.x,
                    self.size[1] + self.velocity.y)

        if all(map(lambda n: n >= 200, new_size)):
            self.set_screen(new_size)
