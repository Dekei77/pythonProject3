import os

import pygame
import sys

from button import ImageButton
from Bankbuttons import Numbutton
from utils import generate_num_buttons, gen_accept_reject_buttons, generate_receipt

MAX_FPS = 60
WIDTH = 1280
HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bank game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

# Load images
bg = pygame.image.load('images/Bankicon.png')
Bankomat = pygame.image.load('images/Bankomatik.png')
Bankomat = pygame.transform.scale(Bankomat, (450, 800))
card = pygame.image.load('images/card.png')
card = pygame.transform.scale(card, (60, 60))
numbutton = pygame.image.load('images/buttons.png')
numbutton = pygame.transform.scale(numbutton, (300, 300))
tap = pygame.image.load('images/tap_here.png')
tap = pygame.transform.scale(tap,(150,100))


bg_sound = pygame.mixer.Sound('sounds/Bs.mp3')
bg_sound.play()
money = pygame.mixer.Sound('sounds/money.mp3')

# Clock
clock = pygame.time.Clock()

# Cursor
cursor = pygame.image.load("images/cursor.png")
cursor = pygame.transform.scale(cursor, (30, 30))
hand = pygame.image.load("images/hand.png")
hand = pygame.transform.scale(hand, (30, 30))
pygame.mouse.set_visible(False)


def main_menu():
    start_button = ImageButton(800, 352, 74, "Start", "images/button.png", "images/hbutton.png", "sounds/button.mp3")
    settings_button = ImageButton(800, 452, 10, "Settings", "images/button.png", "images/hbutton.png", "sounds/button.mp3")
    exit_button = ImageButton(800, 552, 10, "Quit", "images/button.png", "images/hbutton.png", "sounds/button.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(event.pos):
                    print("Start button clicked!")
                    fade()
                    start_menu()
                elif settings_button.rect.collidepoint(event.pos):
                    print("Settings button clicked!")
                    fade()
                    settings_menu()
                elif exit_button.rect.collidepoint(event.pos):
                    running = False
                    pygame.quit()
                    sys.exit()
            for btn in [start_button,settings_button,exit_button]:
                btn.handle_event(event)

        for btn in [start_button, settings_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))

        pygame.display.flip()


def settings_menu():
    audio_button = ImageButton(800, 352, 74, "audio", "images/button.png", "images/button.png", "sounds/button.mp3")
    video_button = ImageButton(800, 452, 10, "video", "images/button.png", "images/button.png", "sounds/button.mp3")
    back_button = ImageButton(800, 552, 10, "back", "images/button.png", "images/button.png", "sounds/button.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if audio_button.rect.collidepoint(event.pos):
                    fade()
                elif video_button.rect.collidepoint(event.pos):
                    fade()
                    videosettings_menu()
                elif back_button.rect.collidepoint(event.pos):
                    fade()
                    running = False
            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))
        pygame.display.flip()


def change_videomode(w, h, fullscreen=0):
    global WIDTH, HEIGHT, screen, bg
    WIDTH, HEIGHT = w, h
    screen = pygame.display.set_mode((WIDTH, HEIGHT), fullscreen)
    bg = pygame.image.load('images/Bankicon.png')


def videosettings_menu():
    video_button = ImageButton(800, 252, 74, "1280-720", "images/button.png", "images/button.png", "sounds/button.mp3")
    video1_button = ImageButton(800, 352, 10, "1280-800", "images/button.png", "images/button.png", "sounds/button.mp3")
    video2_button = ImageButton(800, 452, 10, "FULL HD", "images/button.png", "images/button.png", "sounds/button.mp3")
    back_button = ImageButton(800, 552, 10, "back", "images/button.png", "images/button.png", "sounds/button.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if video_button.rect.collidepoint(event.pos):
                    WIDTH = 1280
                    HEIGHT = 720
                    fade()
                    running = False
                elif video1_button.rect.collidepoint(event.pos):
                    change_videomode(1600, 720)
                    WIDTH = 1600
                    HEIGHT = 720
                    fade()
                    running = False
                elif video2_button.rect.collidepoint(event.pos):
                    change_videomode(1920, 1080, pygame.FULLSCREEN)
                    fade()
                    running = False
                elif back_button.rect.collidepoint(event.pos):
                    fade()
                    running = False

        for btn in [video_button, video1_button, video2_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))
        pygame.display.flip()


def start_menu():
    bankomat_button = ImageButton(500, 452, 74, "Bankomat", "images/button.png", "sounds/button.mp3")
    back_button = ImageButton(500, 552, 74, "Back", "images/button.png", "sounds/button.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bankomat_button.rect.collidepoint(event.pos):
                    print("Bankomat button clicked")
                    fade()
                    running = False
                    bankomat1()
                elif back_button.rect.collidepoint(event.pos):
                    fade()
                    running = False

        for btn in [back_button, bankomat_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))
        pygame.display.flip()


def bankomat1():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(Bankomat, (430, -40))
        screen.blit(tap,(800,250))
        card_button = Numbutton(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if card_button.rect.collidepoint(event.pos):
                    print("OK")
                    fade()
                    bank_buttons_pincode()  ####
            for btn in [card_button]:
                btn.handle_event(event)

        x, y = pygame.mouse.get_pos()
        screen.blit(hand, (x - 2, y - 2))
        pygame.display.flip()


def bank_buttons_pincode():
    running = True

    # Generate button objects
    num_buttons = generate_num_buttons(numbutton)
    accept_button, reject_button = gen_accept_reject_buttons(numbutton)

    # Entered digits
    entered_pincode = ""
    any_button_clicked = False

    while running:
        screen.fill((0, 0, 0))
        screen.blit(Bankomat, (430, -40))
        screen.blit(card, (772, 327))
        screen.blit(numbutton, (500, 200))

        if not any_button_clicked:
            font = pygame.font.SysFont(None, 34)
            text = font.render("Enter pincode: ", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2 + 10, 150))
            screen.blit(text, text_rect)
        else:
            font = pygame.font.SysFont(None, 36)
            text = font.render("*" * len(entered_pincode), True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2 + 10, 150))
            screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                any_button_clicked = True
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in range(pygame.K_0, pygame.K_9 + 1) and len(entered_pincode) < 4:
                    entered_pincode += str(event.unicode)
                elif event.key == pygame.K_BACKSPACE:
                    entered_pincode = entered_pincode[:-1]
                elif event.key == pygame.K_RETURN and len(entered_pincode) == 4:
                    bank_buttons_entered()  ####
            else:
                for button in num_buttons:
                    is_event_completed = button.handle_event(event)
                    any_button_clicked |= is_event_completed
                    if len(entered_pincode) < 4 and is_event_completed:
                        entered_pincode += str(button.digit)
                is_event_completed = accept_button.handle_event(event)
                if is_event_completed and len(entered_pincode) == 4:
                    any_button_clicked = True
                    bank_buttons_entered()  ####
                is_event_completed = reject_button.handle_event(event)
                if is_event_completed:
                    any_button_clicked = True
                    entered_pincode = entered_pincode[:-1]

        x, y = pygame.mouse.get_pos()
        screen.blit(hand, (x - 2, y - 2))
        pygame.display.flip()


def bank_buttons_entered():
    running = True

    # Generate button objects
    num_buttons = generate_num_buttons(numbutton)
    accept_button, reject_button = gen_accept_reject_buttons(numbutton)

    # Entered digits
    entered_number = 0

    while running:
        screen.fill((0, 0, 0))
        screen.blit(Bankomat, (430, -40))
        screen.blit(card, (772, 327))
        screen.blit(numbutton, (500, 200))

        # Render entered digits as text on the screen
        font = pygame.font.SysFont(None, 36)
        text = font.render(str(entered_number) + " $", True, (0, 100, 0))
        text_rect = text.get_rect(center=(WIDTH // 2 + 10, 150))
        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    entered_number *= 10
                    entered_number += int(event.unicode)
                elif event.key == pygame.K_BACKSPACE:
                    entered_number //= 10
                elif event.key == pygame.K_RETURN:
                    receipt_scene("ATM", entered_number)
            else:
                for button in num_buttons:
                    is_event_completed = button.handle_event(event)
                    if is_event_completed:
                        entered_number *= 10
                        entered_number += int(button.digit)
                is_event_completed = accept_button.handle_event(event)
                if is_event_completed:
                    receipt_scene("ATM", entered_number)
                is_event_completed = reject_button.handle_event(event)
                if is_event_completed:
                    entered_number //= 10

        x, y = pygame.mouse.get_pos()
        screen.blit(hand, (x - 2, y - 2))
        pygame.display.flip()


def receipt_scene(service_name: str, value: int):
    loading_scene()
    fade()
    running = True

    back_button = ImageButton(460, 530, 74, "Back", "images/button.png", "sounds/button.mp3")
    receipt = generate_receipt(service_name, value)
    while running:
        screen.fill((0, 0, 0))
        screen.blit(Bankomat, (430, -40))

        # Receipt blit
        receipt_width, receipt_height = receipt.get_size()
        screen_width, screen_height = screen.get_size()
        receipt_x = (screen_width - receipt_width) // 2
        receipt_y = (screen_height - receipt_height) // 2
        screen.blit(receipt, (receipt_x + 12, receipt_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    fade()
                    main_menu()  # recursion bruh
                    running = False
        for btn in [back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(hand, (x - 2, y - 2))
        pygame.display.flip()


def loading_scene():
    running = True

    player_images = [pygame.image.load(os.path.join('Player_right', f'p{i}.png')) for i in range(1, 5)]

    # Set up variables for animation
    frame_index = 0
    frame_count = len(player_images)
    animation_speed = 0.1
    animation_timer = 0.0

    # fill color
    line_color = (0, 255, 0)
    line_length = 400
    line_thickness = 10
    fill_percent = 0.0
    fill_speed = 0.01

    scale_factor = 2
    while running:
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 255, 255), (430, -40, 450, 800))

        # center
        scene_center_x = WIDTH // 2 - 80
        scene_center_y = HEIGHT // 2

        # Draw gradually filling line
        shrunk_line_length = line_length * fill_percent / 2
        pygame.draw.line(screen, line_color, (scene_center_x, scene_center_y),
                         (scene_center_x + shrunk_line_length, scene_center_y),
                         line_thickness)

        # character pos
        character_x = scene_center_x - 16 * scale_factor - shrunk_line_length - 10
        character_y = scene_center_y - 80  # Move character 80 pixels up
        if fill_percent > 0:
            character_x += shrunk_line_length * 2

        # running character
        player_image = pygame.transform.scale(player_images[frame_index], (32 * scale_factor, 32 * scale_factor))
        screen.blit(player_image, (character_x, character_y))

        # update animation
        animation_timer += pygame.time.Clock().tick_busy_loop(30) / 1000.0
        if animation_timer >= animation_speed:
            frame_index = (frame_index + 1) % frame_count
            animation_timer = 0.0

        font = pygame.font.SysFont(None, 45)
        text = font.render("Loading" + ("." * (int(fill_percent / 0.1) % 4)), True, (0, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2 + 10, 450))
        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        fill_percent = min(fill_percent + fill_speed, 1.0)

        if fill_percent == 1.0:
            running = False

        x, y = pygame.mouse.get_pos()
        screen.blit(hand, (x - 2, y - 2))

        pygame.display.flip()


def fade():
    running = True
    fade_alpha = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        fade_surface = pygame.Surface((1280, 720))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(MAX_FPS)


def Pos(pos, xy):
    """Position function."""
    pos_x, pos_y = "", ""
    bool_x, bool_y = False, False
    for i in range(len(pos)):
        if pos[i] == "(" and xy == "x":
            bool_x = True
        elif bool_x == True and pos[i] != "," and xy == "x":
            pos_x += pos[i]
        elif pos[i] == "," and xy == "x":
            bool_x = False
        elif pos[i] == " " and xy == "y":
            bool_y = True
        elif bool_y == True and pos[i] != ")" and xy == "y":
            pos_y += pos[i]
        elif pos[i] == ")" and xy == "y":
            bool_y = False
    if xy == "x":
        return int(pos_x)
    elif xy == "y":
        return int(pos_y)


if __name__ == "__main__":
    main_menu()
