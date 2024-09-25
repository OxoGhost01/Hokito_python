import pygame


class Pion:
    def __init__(self, coord, color, points, pile, screen):
        self.x = coord[0]
        self.y = coord[1]
        self.color = color
        self.pts = points
        self.pile = pile
        self.screen = screen

    def coord(self):
        return self.x, self.y

    def move(self, new):
        self.x, self.y = new[0], new[1]

    def draw_pawn(self):
        noir = (0, 0, 0)
        blanc = (255, 255, 255)
        dore = (230, 191, 0)
        pygame.draw.circle(self.screen, noir if self.color else blanc, (self.x * 140 + 70, self.y * 140 + 70), 50)
        sysfont = pygame.font.SysFont("None", 30)
        pts = sysfont.render(f"{self.pile}", 0, blanc if self.color else noir)
        pygame.draw.circle(self.screen, noir if self.color else blanc, (self.x * 140 + 20, self.y * 140 + 20), 15)
        self.screen.blit(pts, (self.x * 140 + 14, self.y * 140 + 10))
        if self.pts == 1:
            pygame.draw.rect(self.screen, dore, (self.x * 140 + 65, self.y * 140 + 30, 10, 80))

        if self.pts == 2:
            pygame.draw.rect(self.screen, dore, (self.x * 140 + 45, self.y * 140 + 40, 20, 10))
            pygame.draw.rect(self.screen, dore, (self.x * 140 + 55, self.y * 140 + 40, 10, 60))
            pygame.draw.rect(self.screen, dore, (self.x * 140 + 45, self.y * 140 + 90, 20, 10))

            pygame.draw.rect(self.screen, dore, (self.x * 140 + 75, self.y * 140 + 40, 20, 10))
            pygame.draw.rect(self.screen, dore, (self.x * 140 + 75, self.y * 140 + 40, 10, 60))
            pygame.draw.rect(self.screen, dore, (self.x * 140 + 75, self.y * 140 + 90, 20, 10))

        if self.pts == 3:
            pygame.draw.rect(self.screen, dore, (self.x * 140 + 40, self.y * 140 + 40, 20, 10))
            pygame.draw.rect(self.screen, dore, (self.x * 140 + 50, self.y * 140 + 40, 10, 60))
            pygame.draw.rect(self.screen, dore, (self.x * 140 + 40, self.y * 140 + 90, 20, 10))

            pygame.draw.rect(self.screen, dore, (self.x * 140 + 65, self.y * 140 + 35, 10, 70))

            pygame.draw.rect(self.screen, dore, (self.x * 140 + 80, self.y * 140 + 40, 20, 10))
            pygame.draw.rect(self.screen, dore, (self.x * 140 + 80, self.y * 140 + 40, 10, 60))
            pygame.draw.rect(self.screen, dore, (self.x * 140 + 80, self.y * 140 + 90, 20, 10))
