import pygame
from src.Player import Player

all_sprites = pygame.sprite.Group()


class GameView:

    def __init__(self, is_running: bool, width: int, height: int, FPS: int):
        self.is_running = is_running
        self.width = width
        self.height = height
        self.FPS = FPS

    def update_game(self):
        pygame.init()
        window = pygame.display.set_mode((self.width, self.height))

        player1 = Player(10, 10, "Gabe")
        all_sprites.add(player1)
        all_sprites.draw(window)
        while (self.is_running):
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.is_running = False

            window.fill((0, 225, 0))
            pygame.display.update()

            pygame.time.Clock().tick(self.FPS)
