import pygame

from pygameplus.DefaultSizeDrawable import DefaultSizeDrawable


class Sprite(DefaultSizeDrawable):
    '''
    Stands for PyGame surface, on what something is draw, so it become a sprite.
    You may define clipping of given surface by defining source_rect.

    '''

    def __init__(self, name, source_rect=None):
        DefaultSizeDrawable.__init__(self,name)
        self.source_rect = None
        self.surface = None
        self.dest_rect = (0,0)


    def draw(self, surface, special_flags=0):
        surface.blit(self.surface, self.dest_rect, self.source_rect, special_flags)

    def load(self,filename):
        self.surface = pygame.image.load(filename)

    def get_size(self):
        return self.surface.get_size()
