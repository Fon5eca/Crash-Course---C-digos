import pygame

class Ship():
    '''Class to manage the ship.'''
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("/home/fon5eca/Programación/CrashCourse/invasion espacial/Images/AI_Ship.png")
        self.rect = self.image.get_rect()     #ESto da las propiedades de la imagen, convirtiéndola a rectángulo
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.ship_speed = ai_game.ship_speed
        self.x = float(self.rect.x)     #HAbilitarla para poder sumarle numeros decimales

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        if self.moving_right:
            self.x += self.ship_speed     #Aumenta en 1 la posición en x de la nave (ahora es un rectángulo)

        if self.moving_left:
            self.x -= self.ship_speed
        
        self.rect.x = self.x