import pygame


class BankNumButton:
    def __init__(self, image, bound_rect: pygame.rect, digit: int):
        self.image = image
        self.digit = digit
        self.bound_rect = bound_rect

    def handle_event(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.bound_rect.collidepoint(event.pos):
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
                print(f"BankNumButton with digit: {self.digit} clicked")
                return True

        return False
