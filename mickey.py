import pygame
import sys
import time
from datetime import datetime
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")

clock = pygame.image.load("main-clock.png")
left = pygame.image.load("left-hand.png")
right = pygame.image.load("right-hand.png")

clock_rect = clock.get_rect(center=(WIDTH // 2, HEIGHT // 2))
left_rect = left.get_rect(center=(WIDTH // 2, HEIGHT // 2))
right_rect = right.get_rect(center=(WIDTH // 2, HEIGHT // 2))
while True:
    current_time = datetime.now()
    minute = current_time.minute
    second = current_time.second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    screen.blit(clock, clock_rect)
    rotated_left = pygame.transform.rotate(left, -4 * minute)
    rotated_right = pygame.transform.rotate(right, -6 * second)
    screen.blit(rotated_left, rotated_left.get_rect(center=left_rect.center))
    screen.blit(rotated_right, rotated_right.get_rect(center=right_rect.center))

    pygame.display.flip()
    time.sleep(1)
