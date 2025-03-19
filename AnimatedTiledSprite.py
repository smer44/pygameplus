import pygame


from Sprite import Sprite

def get_current_source_rect(w_cells,h_cells,w_cell_size,h_cell_size,current_step):
    current_step = int(current_step)
    h = current_step // w_cells
    w = current_step  % w_cells
    return (w,h,w_cell_size,h_cell_size)

def to_2d_pos(w_cells, current_step):
    h = current_step // w_cells
    w = current_step  % w_cells
    return (w,h)


class AnimatedTiledSprite(Sprite):

    def __init__(self, name,w_cells,max_cells):
        Sprite.__init__(self, name)

        self.current_surface = 0.0
        self.updating = True
        self.w_cells = w_cells
        self.max_cells = max_cells
        self.h_cells = max_cells//w_cells + (max_cells % w_cells > 0)
        self.frame_speed = 0.3
        self.w_cell_size = None
        self.h_cell_size = None



    def load(self, filename):
        Sprite.load(self,filename)
        self.source_rect = to_2d_pos(self.w_cells,0)
        w,h = self.surface.get_size()
        self.w_cell_size = w // self.w_cells
        self.h_cell_size = h //self.h_cells
        self.update_source_rect()

    def get_size(self):
        return (self.w_cell_size, self.h_cell_size)


    def update_source_rect(self):
        xcell,ycell = to_2d_pos(self.w_cells, int(self.current_surface))
        x = xcell * self.w_cell_size
        y = ycell * self.h_cell_size
        self.source_rect = (x,y, self.w_cell_size, self.h_cell_size)

    def update(self):
        if self.updating:
            self.current_surface += self.frame_speed
            if self.current_surface >= self.max_cells:
                self.current_surface = 0.0
            self.update_source_rect()



    def __repr__(self):
        if not self.w_cell_size or not self.h_cell_size:
            return f"<AnimatedTiledSprite:{self.name}, cells:{self.w_cells}x{self.h_cells}, cell_size:IMAGE NOT LOADED "
        else:
            return f"<AnimatedTiledSprite:{self.name}, cells:{self.w_cells}x{self.h_cells}, cell_size:{self.w_cell_size}x {self.h_cell_size}>"

    def __str__(self):
        if not self.w_cell_size or not self.h_cell_size:
            return f"<AnimatedTiledSprite:{self.name}, cells:{self.w_cells}x{self.h_cells}, cell_size:IMAGE NOT LOADED "
        else:
            return f"<AnimatedTiledSprite:{self.name}, cells:{self.w_cells}x{self.h_cells}, cell_size:{self.w_cell_size}x {self.h_cell_size}>"










