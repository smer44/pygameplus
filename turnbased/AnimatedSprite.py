
import pygame

from yge.turnbased.DefaultSizeDrawable import DefaultSizeDrawable
from yge.turnbased.Sprite import Sprite


class AnimatedSprite(Sprite):

    def __init__(self, name, source_rect=None):
        Sprite.__init__(self,name)
        self.current_surface = 0.0
        self.updating = True
        self.frame_speed = 0.1


    def load_next(self,filename):
        surface = pygame.image.load(filename)
        self.surfaces.append(surface)

    def load_all(self,filenames):
        self.surfaces = []
        for f in filenames:
            self.load_next(f)
        self.surface = self.surfaces[0]

    def update(self):
        if self.updating:
            self.current_surface += self.frame_speed
            if self.current_surface >= len(self.surfaces):
                self.current_surface = 0
            self.surface = self.surfaces[int(self.current_surface)]




