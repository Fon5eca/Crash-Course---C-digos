import sys
import pygame
from ship import Ship

class GameSettings():
    def __init__(self):
        '''Create the game settings.'''
        self.width = 1000
        self.height = 800
        self.screen_color = (75, 34, 171)     #Screen colors in RGB
        self.ship_speed = 0.4


class AlienInvasion():
    def __init__(self):
        '''Cuando se crea una instancia (partida), que se guarden estos ajustes y se inicialice pygame.'''
        pygame.init()
        self.settings = GameSettings()
        self.ship_speed = self.settings.ship_speed
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))     #Creates a window
        pygame.display.set_caption("Alien Invasion")     #Name of the window
        self.ship = Ship(self)     #Esto se hace para dar acceso de una clase a otra y viceversa.


    #Eto es lo que quiero que esté constantemente corriendo
    def run_game(self):
        '''Iniciar el juego'''
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()


    def _check_events(self):
        #Ver acciones
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            elif e.type == pygame.KEYDOWN:
                self._check_downkeys(e)

            elif e.type == pygame.KEYUP:
                self._check_upkeys(e)

    
    #Refactorizar la revisión de eventos
    def _check_downkeys(self, event):
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = True

    def _check_upkeys(self, event):
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
    

    #Todo lo que implica actualizar la pantalla
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