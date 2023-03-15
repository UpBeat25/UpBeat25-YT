import pygame
from pygame.locals import *
import math
import sys

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Rotate Object with Mouse")

object_image = pygame.image.load("Images//dirt.png")
object_pos = (250, 250)
rotated_image = pygame.image.load("Images//dirt.png")
rotated_rect = rotated_image.get_rect(center=object_pos)
def get_angle(object_pos, mouse_pos):
    dx = mouse_pos[0] - object_pos[0]
    dy = mouse_pos[1] - object_pos[1]
    radians = math.atan2(-dy, dx)
    angle = math.degrees(radians)
    return angle

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            angle = get_angle(object_pos, mouse_pos)
            rotated_image = pygame.transform.rotate(object_image, angle)
            rotated_rect = rotated_image.get_rect(center=object_pos)

    screen.fill((255, 255, 255))
    screen.blit(rotated_image, rotated_rect)
    pygame.display.update()
