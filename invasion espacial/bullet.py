import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Manage the bullets of the Alien I. Game'''
    def __init__(self, game_instance):     #Nuevamente, requerimos acceso a las propiedades de la partida
        super().__init__()
        self.screen = game_instance.screen
        self.settings = game_instance.settings
        self.color = game_instance.settings.bullet_color

        #Made the bullet a rectangle
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game_instance.ship.rect.midtop     #Posición en la que debe aparecer la bala

        self.y = float(self.rect.y)

    
    def update(self):
        self.y -= self.settings.bullet_speed

        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)    #Espacio en el que se debe dibujar, su color y sus propiedades.