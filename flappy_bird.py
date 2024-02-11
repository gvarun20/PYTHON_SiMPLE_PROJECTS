# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:07:57 2024

@author: varung
"""
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 60
GRAVITY = 0.5
BIRD_JUMP = 10
PIPE_SPEED = 5

# Colors
WHITE = (255, 255, 255)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_image = pygame.image.load("bird1.png")  # Replace with your bird image
pipe_image = pygame.image.load("pipe.png")  # Replace with your pipe image

# Bird class
class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.velocity = 0

    def jump(self):
        self.velocity = -BIRD_JUMP

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        screen.blit(bird_image, (self.x, int(self.y)))

# Pipe class
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.gap = 150
        self.height = random.randint(50, HEIGHT - 50 - self.gap)

    def move(self):
        self.x -= PIPE_SPEED

    def off_screen(self):
        return self.x + pipe_image.get_width() < 0

    def draw(self):
        screen.blit(pipe_image, (self.x, 0))
        screen.blit(pipe_image, (self.x, self.height + self.gap))

# Main game loop
clock = pygame.time.Clock()
bird = Bird()
pipes = []
exit_game = False  # Flag to indicate whether to exit the game

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Update
    bird.update()
    for pipe in pipes:
        pipe.move()

    # Generate new pipes
    if random.randint(1, 100) < 10:
        pipes.append(Pipe())

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if not pipe.off_screen()]

    # Check for collisions
    for pipe in pipes:
        if (
            bird.x < pipe.x + pipe_image.get_width()
            and bird.x + bird_image.get_width() > pipe.x
            and (bird.y < pipe.height or bird.y + bird_image.get_height() > pipe.height + pipe.gap)
        ):
            print("Collision detected!")
            exit_game = True
            break  # Exit the loop on collision

    # Draw
    screen.fill(WHITE)
    bird.draw()
    for pipe in pipes:
        pipe.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

