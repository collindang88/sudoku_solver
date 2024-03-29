# Third Party
import pygame


# button class
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, window):
        # get mouse pos
        pos = pygame.mouse.get_pos()
        # print(pos)

        # check mouseover and clicked condition
        if (
            self.rect.collidepoint(pos)
            and pygame.mouse.get_pressed()[0] == 1
            and not self.clicked
        ):
            self.clicked = True
            # print('click down')
            return self.clicked

        if pygame.mouse.get_pressed()[0] == 0 and self.clicked:
            # print('click up')
            self.clicked = False
            return self.clicked

        # draw button on screen
        window.blit(self.image, (self.rect.x, self.rect.y))
