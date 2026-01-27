import pygame
from pygame.sprite import Sprite     #Para trabajar con varios elementos del juego a la vez

class Alien(Sprite):
    def __init__(self, game_instance):
        super().__init__()
        self.screen = game_instance.screen

        self.image = pygame.image.load("/home/fon5eca/Programación/CrashCourse/invasion espacial/Images/alien.png")
        self.image_rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)