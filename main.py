import pygame
import os
pygame.init()

def file_path (file_name):
    folder = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder, file_name)
    return path


WIN_WIDTH, WIN_HEIGHT = 700, 500
FPS = 40

image_background = pygame.image.load(file_path("images (1).jfif"))
image_background = pygame.transform.scale(image_background, (WIN_WIDTH, WIN_HEIGHT))

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Шутер")
clock = pygame.time.Clock()

game = True
play = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if play == True:
        window.blit(image_background,(0, 0))

    clock.tick(FPS)
    pygame.display.update()
