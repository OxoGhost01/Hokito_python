import pygame


class Menu:
    def __init__(self, screen):
        self.screen = screen

    def view(self, active):
        if active == 0:
            self.opening()
        if active == 1:
            self.level_choice()

    def opening(self):
        home = pygame.image.load("homepage.png")
        self.screen.fill((179, 255, 204))
        self.screen.blit(home, (173, 200))
        font = pygame.sysfont.SysFont("None", 60)
        font2 = pygame.sysfont.SysFont("None", 30)
        solo = font.render("Solo", 0, (191, 191, 99))
        duo = font.render("Duo", 0, (191, 191, 99))
        escape = font.render("Exit", 0, (191, 191, 99))
        by = font2.render("By OxoGhost", 0, (191, 191, 99))
        pygame.draw.line(self.screen, (0, 255, 0), (120, 420), (120, 520), 5)
        self.screen.blit(solo, (170, 450))
        pygame.draw.line(self.screen, (0, 255, 0), (320, 420), (320, 520), 5)
        self.screen.blit(duo, (370, 450))
        pygame.draw.line(self.screen, (0, 255, 0), (510, 420), (510, 520), 5)
        self.screen.blit(escape, (570, 450))
        pygame.draw.line(self.screen, (0, 255, 0), (710, 420), (710, 520), 5)
        self.screen.blit(by, (700, 815))

    def level_choice(self):
        home = pygame.image.load("homepage.png")
        self.screen.fill((179, 255, 204))
        self.screen.blit(home, (173, 200))
        font = pygame.sysfont.SysFont("None", 60)
        font2 = pygame.sysfont.SysFont("None", 30)
        easy = font.render("Easy", 0, (191, 191, 99))
        medium = font.render("Medium", 0, (191, 191, 99))
        retour = font.render("Return", 0, (191, 191, 99))
        by = font2.render("By OxoGhost", 0, (191, 191, 99))
        pygame.draw.line(self.screen, (0, 255, 0), (120, 420), (120, 520), 5)
        self.screen.blit(easy, (170, 450))
        pygame.draw.line(self.screen, (0, 255, 0), (320, 420), (320, 520), 5)
        self.screen.blit(medium, (338, 450))
        pygame.draw.line(self.screen, (0, 255, 0), (510, 420), (510, 520), 5)
        self.screen.blit(retour, (540, 450))
        pygame.draw.line(self.screen, (0, 255, 0), (710, 420), (710, 520), 5)
        self.screen.blit(by, (700, 815))

    def cursor(self, coord, mode):
        if mode == 0:
            if 120 <= coord[0] < 320 and 420 <= coord[1] <= 520:
                pygame.draw.line(self.screen, (0, 255, 0), (170, 490), (255, 490), 5)
                return 1
            if 320 <= coord[0] < 510 and 420 <= coord[1] <= 520:
                pygame.draw.line(self.screen, (0, 255, 0), (370, 490), (450, 490), 5)
                return 4
            if 510 <= coord[0] < 710 and 420 <= coord[1] <= 520:
                pygame.draw.line(self.screen, (0, 255, 0), (570, 490), (650, 490), 5)
                return 5
        if mode == 1:
            if 120 <= coord[0] < 320 and 420 <= coord[1] <= 520:
                pygame.draw.line(self.screen, (0, 255, 0), (170, 490), (260, 490), 5)
                return 2
            if 320 <= coord[0] < 510 and 420 <= coord[1] <= 520:
                pygame.draw.line(self.screen, (0, 255, 0), (338, 490), (495, 490), 5)
                return 3
            if 510 <= coord[0] < 710 and 420 <= coord[1] <= 520:
                pygame.draw.line(self.screen, (0, 255, 0), (540, 490), (675, 490), 5)
                return 0
        return 0
