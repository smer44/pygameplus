class Drawable:
    '''
    The basic class of any component what is drawn by the engine.
    Should i put lazyload variable here?
    '''

    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name
        self.placer = None

    def check_placer(self, placer):
        #assert hasattr(self, 'placer') and self.placer is not None, f"{self}: has no placer"
        return  placer is None or (hasattr(placer, 'place') and callable(placer.place))
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