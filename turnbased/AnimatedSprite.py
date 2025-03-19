
import pygame

from yge.turnbased.DefaultSizeDrawable import DefaultSizeDrawable

class AnimatedSprite(DefaultSizeDrawable):

    def __init__(self, name, source_rect=None):
        DefaultSizeDrawable.__init__(self,name)
        self.source_rect = None
        self.surfaces = None
        self.current_surface = 0.0
        self.dest_rect = (0,0)
        self.updating = True

    def draw(self, surface, special_flags=0):
        current_surface = int(self.current_surface)
        surface.blit(self.surfaces[current_surface], self.dest_rect, self.source_rect, special_flags)


    def load_next(self,filename):
        surface = pygame.image.load(filename)
        self.surfaces.append(surface)

    def load_all(self,filenames):
        self.surfaces = []
        for f in filenames:
            self.load_next(f)

    def update(self):
        if self.updating:
            self.current_surface += 0.1
            if self.current_surface >= len(self.surfaces):
                self.current_surface = 0

    def get_size(self):
        return self.surfaces[int(self.current_surface)].get_size()



