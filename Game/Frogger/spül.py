import pygame

class Settings():
    WINDOW = pygame.rect.Rect(0, 0, 400, 800)
    FPS = 60


class Background(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Frogger\images\Fortnite.png")
        self.image = pygame.transform.scale(self.image, (Settings.WINDOW.size))
        self.rect = self.image.get_rect()

class Frosch(pygame.sprite.Sprite):

    def init(self):
        super().__init__()

        self.image = pygame.image.load("Frogger\images\FROGGSY.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.startpos() 






    def startpos(self):
        self.rect.centerx = Settings.WINDOW.centerx
        self.rect.bottom = Settings.WINDOW.height

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Settings.WINDOW.size)
        self.background = pygame.sprite.GroupSingle(Background())
        self.frosch = pygame.sprite.GroupSingle(Frosch())

    def run(self):
        self.running = True
        while self.running:
            self.update()
            self.draw()

        pygame.quit

    def update(self):
        self.frosch.update()

    def draw (self):
        self.background.draw(self.screen)
        self.frosch.draw(self.screen)

        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()