import pygame


class Numbutton:
    def __init__(self, screen):
        self.image = pygame.image.load('images/card.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(center=(772, 325))
        surface = self.image.get_rect(center=(772, 325))

        screen.blit(self.image, surface)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
