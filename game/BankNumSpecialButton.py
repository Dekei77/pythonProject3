import pygame


class BankNumSpecialButton:
    def __init__(self, image, bound_rect: pygame.rect, action: str):
        self.image = image
        self.action = action
        self.bound_rect = bound_rect

    def handle_event(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.bound_rect.collidepoint(event.pos):
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
                print(f"BankNumSpecialButton with action: {self.action} clicked")
                return True

        return False
