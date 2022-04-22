import pygame


def main():
    pygame.init()

    S_WIDTH = 1024
    S_HEIGHT = 768
    S_TITLE = "PONG"

    S = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    pygame.display.set_caption(S_TITLE)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    class Player:
        def __init__(self, x):
            self.width = 10
            self.height = 100

            self.x = x
            self.y = (S_HEIGHT / 2) - self.height

        def draw(self):
            pygame.draw.rect(S, WHITE, pygame.Rect(self.width, self.height, self.x, self.y))

    class Game:
        def __init__(self):
            self.running = True
            self.clock = pygame.time.Clock()
            self.plyr1 = Player(50)
            self.plyr2 = Player(S_WIDTH - 50)

        def event(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        def update(self):
            pass

        def render(self):
            self.plyr1.draw()
            self.plyr2.draw()

            pygame.display.flip()
            S.fill(BLACK)

        def loop(self):
            while self.running:
                self.clock.tick(120)
                self.render()
                self.event()
                self.update()

    game = Game()
    game.loop()


if __name__ == "__main__":
    main()
