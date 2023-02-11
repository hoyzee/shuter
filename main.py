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


class Gamesprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img, speed):
        super().__init__()
        self.image = pygame.image.load(file_path(img))
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def __init__(self, x, y, width, height, img, speed):
        super().__init__(x, y, width, height, img, speed)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def fire(self):
        pass

player = Player(300, 400, 70, 70, "player.jfif", 5)







game = True
play = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if play == True:
        window.blit(image_background,(0, 0))

        player.reset()
        player.update()

    clock.tick(FPS)
    pygame.display.update()
