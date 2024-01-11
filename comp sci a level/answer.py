import pygame
from pygame import *
import random

init()

width = 800
height = 1000

screen = display.set_mode((width, height))
boldgalde = font.SysFont('boldgalde', 100)

endProgram = False

word_list = ["HANDS", "ELBOW", "MOOSE", "IRONY", "CRATE", "BOARD", "BLAST"]
word_to_guess = random.choice(word_list).upper()
guessed_word = ['_' for _ in word_to_guess]

attempts = 0
max_attempts = 20
guessed_letters = set()

while not endProgram:
    for e in event.get():
        if e.type == QUIT:
            endProgram = True
        elif e.type == KEYDOWN:
            if e.key in range(K_a, K_z + 1):
                letter = chr(e.key).upper()
                if letter not in guessed_letters:
                    guessed_letters.add(letter)
                    if letter in word_to_guess:
                        for i, char in enumerate(word_to_guess):
                            if char == letter:
                                guessed_word[i] = letter
                    else:
                        attempts += 1

    screen.fill((0, 0, 0))
    draw.rect(screen, (255, 255, 255), (0, 0, width, height))

    messagepick = boldgalde.render("WORDLE", True, (0, 0, 0))
    screen.blit(messagepick, (220, 18))

    for i in range(1, 6):
        x = (i * 115) + 15
        for j in range(1, 7):
            y = (j * 105)
            draw.rect(screen, (220, 220, 220), (x, y, 80, 90), 4)
           

    for u in range(1, 11):
        x = (u * 60) + 34
        for s in range(1, 2):
            y = (s * 140) + 630
            draw.rect(screen, (224, 224, 224), (x, y, 55, 60))

    for u in range(1, 11):
        x = (u * 60) + 34
        for s in range(1, 2):
            y = (s * 140) + 630
            draw.rect(screen, (128, 128, 128), (x, y, 55, 60), 3)

    for l in range(1, 10):
        x = (l * 65) + 36
        for k in range(1, 2):
            y = (k * 190) + 650
            draw.rect(screen, (224, 224, 224), (x, y, 60, 60))

    for l in range(1, 10):
        x = (l * 65) + 36
        for k in range(1, 2):
            y = (k * 190) + 650
            draw.rect(screen, (128, 128, 128), (x, y, 60, 60), 3)
   
    for s in range(1, 10):
        x = (s * 65) + 36
        for o in range(1, 2):
            y = (o * 250) + 660
            draw.rect(screen, (224, 224, 224), (x, y, 60, 60))

    for s in range(1, 10):
        x = (s * 65) + 36
        for o in range(1, 3):
            y = (o * 250) + 660
            draw.rect(screen, (128, 128, 128), (x, y, 60, 60), 3)

    HelveticaNeue= font.SysFont('HelveticaNeue',45)
   
    first_letter = HelveticaNeue.render("Q", True, (0, 0, 0))
    screen.blit(first_letter, (105, 785))
    first_letter = HelveticaNeue.render("␡", True, (0, 0, 0))
    screen.blit(first_letter, (113, 918))
    first_letter = HelveticaNeue.render("W", True, (0, 0, 0))
    screen.blit(first_letter, (160, 785))
    first_letter = HelveticaNeue.render("Z", True, (0, 0, 0))
    screen.blit(first_letter, (180, 918))
    first_letter = HelveticaNeue.render("E", True, (0, 0, 0))
    screen.blit(first_letter, (228, 785))
    first_letter = HelveticaNeue.render("X", True, (0, 0, 0))
    screen.blit(first_letter, (245, 918))
    first_letter = HelveticaNeue.render("R", True, (0, 0, 0))
    screen.blit(first_letter, (285, 785))
    first_letter = HelveticaNeue.render("C", True, (0, 0, 0))
    screen.blit(first_letter, (310, 918))
    first_letter = HelveticaNeue.render("T", True, (0, 0, 0))
    screen.blit(first_letter, (350, 785))
    first_letter = HelveticaNeue.render("V", True, (0, 0, 0))
    screen.blit(first_letter, (375, 918))
    first_letter = HelveticaNeue.render("Y", True, (0, 0, 0))
    screen.blit(first_letter, (408, 785))
    first_letter = HelveticaNeue.render("B", True, (0, 0, 0))
    screen.blit(first_letter, (440, 918))
    first_letter = HelveticaNeue.render("U", True, (0, 0, 0))
    screen.blit(first_letter, (470, 785))
    first_letter = HelveticaNeue.render("I", True, (0, 0, 0))
    screen.blit(first_letter, (537, 785))
    first_letter = HelveticaNeue.render("N", True, (0, 0, 0))
    screen.blit(first_letter, (506, 918))
    first_letter = HelveticaNeue.render("O", True, (0, 0, 0))
    screen.blit(first_letter, (583, 785))
    first_letter = HelveticaNeue.render("M", True, (0, 0, 0))
    screen.blit(first_letter, (569, 918))
    first_letter = HelveticaNeue.render("P", True, (0, 0, 0))
    screen.blit(first_letter, (650, 785))
    first_letter = HelveticaNeue.render("✕", True, (0, 0, 0))
    screen.blit(first_letter, (640, 918))
    first_letter = HelveticaNeue.render("A", True, (0, 0, 0))
    screen.blit(first_letter, (113, 856))
    first_letter = HelveticaNeue.render("S", True, (0, 0, 0))
    screen.blit(first_letter, (180, 856))
    first_letter = HelveticaNeue.render("D", True, (0, 0, 0))
    screen.blit(first_letter, (245, 856))
    first_letter = HelveticaNeue.render("F", True, (0, 0, 0))
    screen.blit(first_letter, (310, 856))
    first_letter = HelveticaNeue.render("G", True, (0, 0, 0))
    screen.blit(first_letter, (375, 856))
    first_letter = HelveticaNeue.render("H", True, (0, 0, 0))
    screen.blit(first_letter, (440, 856))
    first_letter = HelveticaNeue.render("J", True, (0, 0, 0))
    screen.blit(first_letter, (510, 856))
    first_letter = HelveticaNeue.render("K", True, (0, 0, 0))
    screen.blit(first_letter, (572, 856))
    first_letter = HelveticaNeue.render("L", True, (0, 0, 0))
    screen.blit(first_letter, (640, 856))
   
    pygame.draw.line(screen, (0, 0, 0), (5, 20), (50, 20), 6)
    pygame.draw.line(screen, (0, 0, 0), (5, 30), (50, 30), 6)
    pygame.draw.line(screen, (0, 0, 0), (5, 40), (50, 40), 6)

    for i, letter in enumerate(guessed_word):
        if letter != '_':
            x = (i * 115) + 134
            y = 105
            letter_render = boldgalde.render(letter, True, (0, 0, 0))
            screen.blit(letter_render, (x + 5, y + 5))

    if '_' not in guessed_word:
        print("Congratulations! You guessed the word:", word_to_guess)
        endProgram = True
    elif attempts >= max_attempts:
        print("Sorry! You ran out of attempts. The word was:", word_to_guess)
        endProgram = True

    display.flip()
    time.delay(200)
