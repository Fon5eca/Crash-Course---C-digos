import sys
import pygame
from ship import Ship
from bullet import Bullet

class GameSettings():
    def __init__(self):
        '''Create the game settings.'''
        self.width = 0     #Pongo 0 para poder ponerlo en pantalla grande
        self.height = 0
        self.screen_color = (75, 34, 171)     #Screen colors in RGB
        self.ship_speed = 10

        #Bullet settings
        self.bullet_speed = 15.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)



class AlienInvasion():
    def __init__(self):
        '''Cuando se crea una instancia (partida), que se guarden estos ajustes y se inicialice pygame.'''
        pygame.init()
        self.settings = GameSettings()
        self.ship_speed = self.settings.ship_speed
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height), pygame.FULLSCREEN)     #Creates a window
        self.settings.width = self.screen.get_rect().width
        self.settings.height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")     #Name of the window
        self.ship = Ship(self)     #Esto se hace para dar acceso de una clase a otra y viceversa.
        self.bullet = pygame.sprite.Group()


    #Eto es lo que quiero que esté constantemente corriendo
    def run_game(self):
        '''Iniciar el juego'''
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.bullet.update()


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
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_upkeys(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullet.add(new_bullet)     #Agregar al grupo de sprites
    

    #Todo lo que implica actualizar la pantalla
    def _update_screen(self):
        #Actualizar el color de fondo
        self.screen.fill(self.settings.screen_color)
        
        #Pegar la imagen en la pestaña
        self.ship.blitme()

        #Dibujar cada bala
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()

        #Actualizar el frame (para los fps)
        pygame.display.flip()

if __name__ == '__main__':
    partida = AlienInvasion()
    partida.run_game()