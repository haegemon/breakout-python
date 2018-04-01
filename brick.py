import pygame
from game_object import GameObject


class Brick(GameObject):
    def __init__(self,
                 x,
                 y,
                 w,
                 h,
                 color,
                 special_effect = None):
        GameObject.__init__(self, x ,y ,w, h)
        self.special_effect = special_effect
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)
