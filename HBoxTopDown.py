from MultiPlacer import MultiPlacer

class HBoxTopDown (MultiPlacer):

    def __init__(self, name):
        MultiPlacer.__init__(self, name)
        self.rect = None
        self.xlast = None
        self.ylast = None


    def place_start(self, container,rect):
        assert rect , f"HBoxTopDown : wrong {rect=}, can not be None for TopDown placer"
        x,y,w,h = rect
        assert w > 0 and h > 0 , f"HBoxTopDown : wront {rect=} dimentions for TopDown placer"
        self.rect = rect
        self.amount = len(container.children)
        self.xlast = x
        self.ylast = y
        self.xstep = w / self.amount
        self.xstepint = int(self.xstep)
        self.h = h

    def place_next(self, child):
        rect = (int(self.xlast), self.ylast, self.xstepint, self.h)
        self.xlast +=self.xstep

        child.place_scale_if_need(rect)

    def place_finaly(self):
        return self.rect







