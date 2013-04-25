from Dots import *
from Cursor import *
import sys, pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

menu_img = "menu.jpg"
instructions_img = "instructions.jpg"
game_back_img = "Stock.jpg"
correct_sound_file = "correct_sound_effect.wav"
wrong_sound_file = "wrong_sound_effect.wav"

screen = pygame.display.set_mode((1018,516),0,32)
pygame.display.set_caption('Purple Hammer')
game_back = pygame.image.load(game_back_img).convert()
menu = pygame.image.load(menu_img).convert_alpha()
instructions = pygame.image.load(instructions_img).convert_alpha()
correct_sound = pygame.mixer.Sound(correct_sound_file)
wrong_sound = pygame.mixer.Sound(wrong_sound_file)

cursor = Cursor()
dots = Dots()

cursor.move_cursor(menu, screen, 1, cursor.start_pos_1)

cursor.NavigateOptions(Dots, menu, screen, instructions)
cursor.redraw(dots, screen, game_back, False, "None", True)

count = 0
done = False
first = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if cursor.game_start == True:
        dots.generate_dots(screen)
        dots.random_remove()
        if first:
            dots.question()
            first = False
        
        cursor.redraw(dots, screen, game_back, False, "Dots", True)
                
        if count == dots.answer_question - dots.level_num - dots.stage_num:
            dots.answer = dots.dots[:]
        
        pygame.display.flip()
        pygame.time.delay(3000)
        
        if count == dots.level_num:
            pygame.display.flip()
            if dots.answer_yes:
                cursor.redraw(dots, screen, game_back, True, "Answer", True)
                cursor.BreakWhenAnswer(dots, screen, game_back, "Answer")
                if cursor.outcome == "Yes":
                    correct_sound.play()
                    dots.wins += 1
                    done = True
                elif cursor.outcome == "No":
                    wrong_sound.play()
                    done = True
                elif cursor.outcome == "Time":
                    wrong_sound.play()
                    done = True

            else:
                while True:
                    dots.dots[:] = []
                    dots.generate_dots(screen)
                    dots.random_remove()
                    pygame.display.flip()
                    if dots.dots != dots.answer:
                        break
                cursor.redraw(dots, screen, game_back, True, "Dots", True)
                cursor.BreakWhenAnswer(dots, screen, game_back, "Dots")
                if cursor.outcome == "No":
                    correct_sound.play()
                    dots.wins += 1
                    done = True
                elif cursor.outcome == "Yes":
                    wrong_sound.play()
                    done = True
                elif cursor.outcome == "Time":
                    wrong_sound.play()
                    done = True
        
        dots.dots[:] = []
        
        count += 1
        
        if done:
            count = 0
            done = False
            first = True
        
        dots.stage()
        dots.level()
            
        pygame.display.flip()