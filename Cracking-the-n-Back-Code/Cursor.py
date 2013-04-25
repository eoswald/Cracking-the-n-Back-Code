import pygame, sys
from pygame.locals import *

class Cursor(object):
    def __init__(self):
        self.img = "cursor.png"
        self.start_pos_1 = (422,299)
        self.start_pos_2 = (370,360)
        self.ans_pos_1 = (670,460)
        self.ans_pos_2 = (899,460)
        self.cursor = pygame.image.load(self.img).convert_alpha()
        self.cursorpos = 1
        self.game_start = False
        self.outcome = str
        self.no = pygame.image.load("realred_50x50.png").convert_alpha()
        self.no_pos = (948,450)
        self.yes = pygame.image.load("yes_50x50.png").convert_alpha()
        self.yes_pos = (718,450)
        self.selection_sound = pygame.mixer.Sound("Select_Sound_Effect.wav")
    def move_cursor(self, menu, screen, cursorpos, pos):
        self.cursorpos = cursorpos
        screen.blit(menu, (0,0))
        screen.blit(self.cursor, pos)
    def NavigateOptions(self, other, menu, screen, instructions):
        _pass = False
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_DOWN and self.cursorpos == 1:
                        self.move_cursor(menu, screen, 2, self.start_pos_2)
                    elif event.key == K_DOWN and self.cursorpos == 2:
                        self.move_cursor(menu, screen, 1, self.start_pos_1)
                    elif event.key == K_UP and self.cursorpos == 1:
                        self.move_cursor(menu, screen, 2, self.start_pos_2)
                    elif event.key == K_UP and self.cursorpos == 2:
                        self.move_cursor(menu, screen, 1, self.start_pos_1)
                    if event.key == K_SPACE and self.cursorpos == 1:
                        _pass = True
                    elif event.key == K_SPACE and self.cursorpos == 2:
                        _pass_i = False
                        screen.blit(instructions, (0, 0))
                        pygame.display.update()
                        while True:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == KEYDOWN:
                                    if event.key == K_SPACE:
                                        _pass_i = True
                            if _pass_i == True:
                                screen.blit(menu, (0,0))
                                screen.blit(self.cursor, self.start_pos_2)
                                break
            if _pass == True:
                self.game_start = True
                break
            pygame.display.update()
    def redraw(self, other, screen, background, boolean, answer, pause):
        screen.blit(background, (0,0))
        screen.blit(other.current_meter, other.meter_pos)
        screen.blit(self.no, self.no_pos)
        screen.blit(self.yes, self.yes_pos)
        if boolean:
            screen.blit(other.current_question, other.question_pos)
        if self.cursorpos == 1:
            screen.blit(self.cursor, self.ans_pos_1)
        else:
            screen.blit(self.cursor, self.ans_pos_2)
        if pause:
            pygame.display.flip()
            pygame.time.delay(1000)
        if answer == "Answer":
            for i in other.answer:
                screen.blit(*i)
        elif answer == "Dots":
            for i in other.dots:
                screen.blit(*i)
        pygame.display.flip()
    def BreakWhenAnswer(self,other, screen, background, answer):
        clock = pygame.time.Clock()
        duration = 0
        _pass = False
        self.cursorpos = 1
        screen.blit(self.cursor, self.ans_pos_1)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT and self.cursorpos == 1:
                        self.cursorpos = 2
                        self.redraw(other, screen, background, True, answer, False)
                    elif event.key == K_RIGHT and self.cursorpos == 2:
                        self.cursorpos = 1
                        self.redraw(other, screen, background, True, answer, False)
                    elif event.key == K_LEFT and self.cursorpos == 1:
                        self.cursorpos = 2
                        self.redraw(other, screen, background, True, answer, False)
                    elif event.key == K_LEFT and self.cursorpos == 2:
                        self.cursorpos = 1
                        self.redraw(other, screen, background, True, answer, False)
                    if event.key == K_SPACE and self.cursorpos == 1:
                        self.outcome = "Yes"
                        _pass = True
                    elif event.key == K_SPACE and self.cursorpos == 2:
                        self.outcome = "No"
                        _pass = True
            if duration > 10 and not _pass:
                self.outcome = "Time"
                break
            if _pass:
                break
            milli = clock.tick()
            seconds = milli/1000.
            duration += seconds