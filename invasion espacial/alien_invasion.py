import sys
import pygame
from ship import Ship

class GameSettings():
    def __init__(self):
        '''Create the game settings.'''
        self.width = 1600
        self.height = 900
        self.screen_color = (75, 34, 171)     #Screen colors in RGB


class AlienInvasion():
    def __init__(self):
        '''Cuando se crea una instancia (partida), que se guarden estos ajustes y se inicialice pygame.'''
        pygame.init()
        self.settings = GameSettings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))     #Creates a window
        pygame.display.set_caption("Alien Invasion")     #Name of the window
        self.ship = Ship(self)     #Esto se hace para dar acceso de una clase a otra y viceversa.

    def run_game(self):
        '''Iniciar el juego'''
        while True:
            # Siempre esté viendo las acciones con el teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Actualizar el color de fondo
            self.screen.fill(self.settings.screen_color)
            
            self.ship.blitme()

            #Actualizar el frame (para los fps)
            pygame.display.flip()


if __name__ == '__main__':
    partida = AlienInvasion()
    partida.run_game()