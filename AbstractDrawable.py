class AbstractDrawable:
    '''
    The basic class of any component what is drawn by the engine.
    Child classes can do lazy or eager load.

    '''
    is_container = False
    is_filler = False
    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name
        self.placer = None

    def place(self, rect):
        if self.placer:
            self.dest_rect =self.placer.place(rect)
        else:
            self.dest_rect = rect

    def need_scale(self,rect):
        if self.is_filler:
            return False
        w0,h0 = self.get_size()
        x,y,w,h = rect
        return w0 != w or h0 != h




    def place_scale_if_need(self,rect):
        need_scale = self.need_scale(rect)
        AbstractDrawable.place(self,rect)
        if need_scale:
            self.__scale__(rect[2:])






    def check_placer(self, placer):
        #assert hasattr(self, 'placer') and self.placer is not None, f"{self}: has no placer"
        return  placer is None or (hasattr(placer, 'place') and callable(placer.place) and hasattr(placer, "__place_inner__") and callable(placer.__place_inner__)) or \
            (hasattr(placer, 'place_start') and hasattr(placer, 'place_next') and callable(placer.place_start) and callable(placer.place_next))
        #assert hasattr(placer, 'place'), f"{self}: placer {self.placer} has no method place"
        #assert callable(placer.place), f"{self}: placer {self.placer} has no method place"

    def set_placer(self,placer):
        assert self.check_placer(placer), f"{self} : trying to set wrong placer type {placer}"
        self.placer = placer

    def draw(self, surface,*args,**kwargs):
        raise NotImplementedError(f"{self.__class__.__name__} is subclass of yDraw and  does not implement __draw__ method")

    def __draw_lazy__(self,surface,*args,**kwargs):
        pass


    def mouse_react(self, game, mouse_pos):
        raise RuntimeError(f"{self.__class__}.mouse_react not implemented")

    def __repr__(self):
        #return f"<{type(self).__name__} '{self.name}': visible={self.pos_in_visible}, is_mouse_listener={self.pos_in_mouse_listeners}>"
        return f"<{self.__class__.__name__} : {self.name}>"

    def __str__(self):
        return f"<{self.__class__.__name__} : {self.name}>"

    def debug_places(self):
        return f"{self.dest_rect}"

