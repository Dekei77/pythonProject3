import io
import random
from datetime import datetime

import pygame

from BankNumButton import BankNumButton
from BankNumSpecialButton import BankNumSpecialButton
from receiptGenerator import ReceiptGenerator


def generate_num_buttons(numbutton):
    # Define rectangles for each digit
    scaling = 300 / 626
    offset = (500, 200)
    y_delta = 100 * scaling
    x_delta = 115 * scaling
    button_x_size = 85 * scaling
    button_y_size = 70 * scaling
    start_pt = (152 * scaling + offset[0], 125 * scaling + offset[1])
    digit_top_left_rect_points = [
        (start_pt[0] + 1 * x_delta, start_pt[1] + 3 * y_delta),  # 0
        (start_pt[0] + 0 * x_delta, start_pt[1] + 0 * y_delta),  # 1
        (start_pt[0] + 1 * x_delta, start_pt[1] + 0 * y_delta),  # 2
        (start_pt[0] + 2 * x_delta, start_pt[1] + 0 * y_delta),  # 3
        (start_pt[0] + 0 * x_delta, start_pt[1] + 1 * y_delta),  # 4
        (start_pt[0] + 1 * x_delta, start_pt[1] + 1 * y_delta),  # 5
        (start_pt[0] + 2 * x_delta, start_pt[1] + 1 * y_delta),  # 6
        (start_pt[0] + 0 * x_delta, start_pt[1] + 2 * y_delta),  # 7
        (start_pt[0] + 1 * x_delta, start_pt[1] + 2 * y_delta),  # 8
        (start_pt[0] + 2 * x_delta, start_pt[1] + 2 * y_delta),  # 9

    ]
    num_buttons = []
    for idx in range(len(digit_top_left_rect_points)):
        p = digit_top_left_rect_points[idx]
        digit_rect = pygame.Rect(*p, button_x_size, button_y_size)
        digit_button = BankNumButton(numbutton, digit_rect, idx)
        num_buttons.append(digit_button)
    return num_buttons


def gen_accept_reject_buttons(numbutton):
    # Define rectangles for each digit
    scaling = 300 / 626
    offset = (500, 200)
    y_delta = 100 * scaling
    x_delta = 115 * scaling
    button_x_size = 85 * scaling
    button_y_size = 70 * scaling
    start_pt = (152 * scaling + offset[0], 125 * scaling + offset[1])
    special_rect = pygame.Rect(start_pt[0] + 2 * x_delta, start_pt[1] + 3 * y_delta
                               , button_x_size, button_y_size)
    accept_button = BankNumSpecialButton(numbutton, special_rect, action="accept")
    special_rect = pygame.Rect(start_pt[0] + 0 * x_delta, start_pt[1] + 3 * y_delta
                               , button_x_size, button_y_size)
    reject_button = BankNumSpecialButton(numbutton, special_rect, action="reject")
    return accept_button, reject_button


def _generate_receipt(header_text_data, body_text_data, footer_text_data):
    receipt_generator = ReceiptGenerator()
    receipt_generator.generate_header(header_text_data)
    receipt_generator.generate_header(body_text_data)
    receipt_generator.generate_header(footer_text_data)
    receipt_image = receipt_generator.generate_resulted_image()

    image_data = receipt_image.tobytes()
    width, height = receipt_image.size
    pygame_receipt_image = pygame.image.frombuffer(image_data, (width, height), 'RGB')
    return pygame_receipt_image


def generate_receipt(service_name: str, value: int, size=(320, 480)):
    header_text_data = [
        'ATM',
        '654 Maple Boulevard, Metropolis, USA',
        '727-345-727',
        f'Receipt: {random.randint(10, 100)}',
        f'Date: {datetime.now().strftime("%m/%d/%Y")}'
    ]
    body_text_data = [
        ('A.No', 'Service Description', 'Value', '    '),
        ('1', service_name, f"{value} $", '    ')
    ]
    footer_text_data = [
        ('      Service Tax:', f'   3.0'),
        ('           FT Tax:', f'   1.0'),
        ('Total Tax:', f'{value * 0.04} $')
    ]
    receipt_generator = ReceiptGenerator(size)
    receipt_generator.generate_header(header_text_data)
    receipt_generator.generate_body(body_text_data)
    receipt_generator.generate_footer(footer_text_data)
    receipt_image = receipt_generator.generate_resulted_image()

    buffer = io.BytesIO()
    receipt_image.save(buffer, format='PNG')
    image_data = buffer.getvalue()
    pygame_receipt_image = pygame.image.load(io.BytesIO(image_data))
    return pygame_receipt_image
