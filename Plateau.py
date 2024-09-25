import random
from Pion import *


class Jeu:
    def __init__(self, screen, mode):
        self.screen = screen
        self.mode = mode
        self.pions = []
        self.cases_vides = []
        self.dep = []
        self.select = None
        self.joueur = 0
        self.bot = random.randint(0, 1)
        self.jeu_bot = None
        self.creer_pions()

    def dessin_plateau(self):
        vert = (0, 255, 0)
        for y in range(140, 841, 140):
            pygame.draw.line(self.screen, vert, (0, y), (840, y))
        for x in range(140, 841, 140):
            pygame.draw.line(self.screen, vert, (x, 0), (x, 840))
        for y in range(70, 841, 140):
            for x in range(70, 841, 140):
                pygame.draw.circle(self.screen, vert, (x, y), 2)
        for pion in self.pions:
            pion.draw_pawn()
        if self.jeu_bot:
            pygame.draw.circle(self.screen, (0, 0, 200), (self.jeu_bot[0][0] * 140 + 70,
                                                          self.jeu_bot[0][1] * 140 + 70), 50, 4)
            pygame.draw.circle(self.screen, (0, 0, 200), (self.jeu_bot[1][0] * 140 + 70,
                                                          self.jeu_bot[1][1] * 140 + 70), 50, 4)
        if self.select:
            pygame.draw.circle(self.screen, (0, 255, 0), (self.select[0] * 140 + 70, self.select[1] * 140 + 70), 50, 4)
            for i in self.dep:
                pygame.draw.circle(self.screen, (255, 0, 0), (i[0] * 140 + 70, i[1] * 140 + 70), 50, 4)

    def creer_pions(self):
        done = []
        for pts in range(1, 4):
            for i in range(6):
                coord = (random.randint(0, 5), random.randint(0, 2))
                while coord in done:
                    coord = (random.randint(0, 5), random.randint(0, 2))
                self.pions.append(Pion(coord, 0, pts, 1, self.screen))
                done.append(coord)
        for pts in range(1, 4):
            for i in range(6):
                coord = (random.randint(0, 5), random.randint(3, 5))
                while coord in done:
                    coord = (random.randint(0, 5), random.randint(3, 5))
                self.pions.append(Pion(coord, 1, pts, 1, self.screen))
                done.append(coord)

    def update_cases_vides(self):
        self.cases_vides = []
        for y in range(6):
            for x in range(6):
                if self.find_pawn((x, y)) is None:
                    self.cases_vides.append((x, y))

    def changer_joueur(self):
        self.joueur = 0 if self.joueur else 1

    def find_pawn(self, coord):
        for i in range(len(self.pions)):
            if self.pions[i].coord() == coord:
                return i
        return None

    @staticmethod
    def mouse(coord):
        for y in range(0, 6):
            for x in range(0, 6):
                if x * 140 <= coord[0] < (x + 1) * 140 and y * 140 <= coord[1] < (y + 1) * 140:
                    print(x, y)
                    return x, y

    def click(self, coord, bot=False):
        if not bot:
            coord = self.mouse(coord)
        ipion = self.find_pawn(coord)
        if ipion is not None and self.pions[ipion].color == self.joueur and not self.select:
            self.dep = []
            self.select = coord
            pts = self.pions[ipion].pts
            x, y = self.pions[ipion].coord()
            pile = False if self.pions[ipion].pile == 1 else True
            self.calcul_dep(pts, x, y, pile)
            while coord in self.dep:
                self.dep.remove(coord)
        elif coord in self.dep and self.select:
            victime = self.find_pawn(coord)
            pile_v = self.pions[victime].pile
            self.pions.remove(self.pions[victime])
            self.pions[self.find_pawn(self.select)].move(coord)
            self.pions[self.find_pawn(coord)].pile += pile_v
            self.reset()
            self.update_cases_vides()
            self.changer_joueur()
        else:
            self.reset()

    def calcul_dep(self, pts, x, y, pile, direc=None):
        if 0 <= x <= 5 and 0 <= y <= 5:
            if pts == 0:
                pion = self.pions[self.find_pawn((x, y))].pile
                if pion > 1 and pile or pion == 1 and not pile:
                    self.dep.append((x, y))
            else:
                if direc != "l":
                    i = 1
                    while x + i <= 5:
                        if self.find_pawn((x + i, y)) is not None:
                            self.calcul_dep(pts - 1, x + i, y, pile, "r")
                            break
                        i += 1
                if direc != "r":
                    i = 1
                    while x - i >= 0:
                        if self.find_pawn((x - i, y)) is not None:
                            self.calcul_dep(pts - 1, x - i, y, pile, "l")
                            break
                        i += 1
                if direc != "u":
                    i = 1
                    while y + i <= 5:
                        if self.find_pawn((x, y + i)) is not None:
                            self.calcul_dep(pts - 1, x, y + i, pile, "d")
                            break
                        i += 1
                if direc != "d":
                    i = 1
                    while y - i >= 0:
                        if self.find_pawn((x, y - i)) is not None:
                            self.calcul_dep(pts - 1, x, y - i, pile, "u")
                            break
                        i += 1

    def reset(self):
        self.select = None
        self.dep = []

    def end(self):
        booolb = True
        boooln = True
        for pion in self.pions:
            if pion.color:
                boooln = False
            else:
                booolb = False
        if booolb or boooln:
            return self.points()
        return 0

    def points(self):
        pts = 0
        for pion in self.pions:
            if pion.color == self.joueur:
                pts += pion.pile * pion.pts
        return pts

    def easy(self):
        pion = self.pions[random.randint(0, len(self.pions) - 1)]
        while not self.dep:
            pion = self.pions[random.randint(0, len(self.pions) - 1)]
            self.click(pion.coord(), True)
        coord = pion.coord()
        move = self.dep[random.randint(0, len(self.dep) - 1)]
        self.click(move, True)
        self.jeu_bot = (coord, move)

    def medium(self):
        coups = {}
        i = 0
        while i > len(self.pions):
            if self.pions[i].color == self.joueur:
                coups[self.pions[i].coord()] = self.test(self.pions[i])
            i += 1
        maxi = 0
        coup = None
        for i in coups.keys():
            if coups[i][1] > maxi:
                maxi = coups[i][1]
                coup = i
        self.click(coup, True)
        self.click(coups[coup][0], True)

    def test(self, pion):
        pts = pion.pts
        x = pion.x
        y = pion.y
        pile = pion.pile
        self.calcul_dep(pts, x, y, pile)
        coup = None
        maxi = 0
        for dep in self.dep:
            victime = self.find_pawn(dep)
            pile_v = self.pions[victime].pile
            old_pawn = self.pions.pop(self.pions[victime])
            self.pions[self.find_pawn((x, y))].move(dep)
            self.pions[self.find_pawn(dep)].pile += pile_v
            pts = self.points()
            if pts > maxi:
                coup = (dep, pts)
                maxi = pts
            self.pions[self.find_pawn(dep)].move((x, y))
            self.pions[self.find_pawn((x, y))].pile -= pile_v
            self.pions.append(old_pawn)
        return coup

    def play_bot(self, mode):
        if self.bot == self.joueur:
            if mode == 2:
                self.easy()
            elif mode == 3:
                self.medium()
