import pygame, random
from pygame.locals import *

class Dots(object):
    def __init__(self):
        self.level_num = 2
        self.stage_num = 1
        self.answer_question = 3
        self.wins = 0
        self.dots = []
        self.dot = pygame.image.load("url_18x18.png").convert_alpha()
        self.x_pos = 100
        self.y_pos = 100
        self.percent_yes = 62
        self.answer_yes = True
        self.answer = list
        self.meter_0 = pygame.image.load("8.png").convert_alpha()
        self.meter_1 = pygame.image.load("1.png").convert_alpha()
        self.meter_2 = pygame.image.load("2.png").convert_alpha()
        self.meter_3 = pygame.image.load("3.png").convert_alpha()
        self.meter_4 = pygame.image.load("4.png").convert_alpha()
        self.meter_5 = pygame.image.load("5.png").convert_alpha()
        self.meter_6 = pygame.image.load("6.png").convert_alpha()
        self.meter_7 = pygame.image.load("7.png").convert_alpha()
        self.meter_8 = pygame.image.load("80.png").convert_alpha()
        self.current_meter = pygame.image.load("8.png").convert_alpha()
        self.meter_num = 0
        self.meter_pos = (9,368)
        self.question_2 = pygame.image.load("2_ago_question.png").convert_alpha()
        self.question_3 = pygame.image.load("3_ago_question.png").convert_alpha()
        self.current_question = pygame.image.load("2_ago_question.png").convert_alpha()
        self.question_pos = (4,463)
    def generate_dots(self,screen):
        count = 0
        for i in range(self.level_num**2):
            self.dots.append((self.dot,(self.x_pos,self.y_pos)))
            self.x_pos += 100
            count += 1
            if count == self.level_num:
                self.y_pos += 100
                self.x_pos = 100
                count = 0
        self.y_pos = 100
    def random_remove(self):
        random.seed()
        rand_dot = random.randint(0,(len(self.dots)-1))
        self.dots.pop(rand_dot)
    def stage(self):
        meters = [self.meter_0, self.meter_1, self.meter_2, self.meter_3, self.meter_4, self.meter_5, self.meter_6, self.meter_7, self.meter_8]
        if self.wins == 3:
            self.stage_num += 1
            self.meter_num += 1
            self.current_meter = meters[self.meter_num]
            self.wins = 0
            self.answer_question += 1
    def level(self):
        if self.stage_num == 8:
            self.level_num += 1
            self.stage_num = 1
            self.answer_question = 1
    def question(self):
        score = random.randint(0,100)
        if score < self.percent_yes:
            self.answer_yes = True
        else:
            self.answer_yes = False