import pygame as pyg

class Buttons:
    def __init__(self, image, x, y, scale):
        width = int(image.get_width() * scale)
        height = int(image.get_height() * scale)

        self.image = pyg.transform.scale(image, width, height)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.clicked = False

    def draw(self, screen):
        mouse_pos = pyg.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pyg.mouse.get_pressed()[0] == 1:
                self.clicked = True

        if pyg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))