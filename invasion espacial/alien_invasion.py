import sys
import pygame
from ship import Ship

class GameSettings():
    def __init__(self):
        '''Create the game settings.'''
        self.width = 1000
        self.height = 800
        self.screen_color = (75, 34, 171)     #Screen colors in RGB
        self.ship_speed = 0.5


class AlienInvasion():
    def __init__(self):
        '''Cuando se crea una instancia (partida), que se guarden estos ajustes y se inicialice pygame.'''
        pygame.init()
        self.settings = GameSettings()
        self.ship_speed = self.settings.ship_speed
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))     #Creates a window
        pygame.display.set_caption("Alien Invasion")     #Name of the window
        self.ship = Ship(self)     #Esto se hace para dar acceso de una clase a otra y viceversa.

    def run_game(self):
        '''Iniciar el juego'''
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()

    def _check_events(self):
        #Siempre esté viendo las acciones con el teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            #Movernos a la derecha e izquierda
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    
    def _update_screen(self):
        #Actualizar el color de fondo
        self.screen.fill(self.settings.screen_color)
        
        #Pegar la imagen en la pestaña
        self.ship.blitme()

        #Actualizar el frame (para los fps)
        pygame.display.flip()

if __name__ == '__main__':
    partida = AlienInvasion()
    partida.run_game()