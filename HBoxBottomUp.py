from MultiPlacer import MultiPlacer


class HBoxBottomUp (MultiPlacer):

    def __init__(self, name):
        MultiPlacer.__init__(self,name)
        self.rect = None
        self.maxh = None
        self.xlast = None
        self.ylast = None

    def place_start(self, container,rect):
        if rect is None:
            rect = (0,0,0,0)
        self.rect = rect
        self.maxh = 0
        self.xlast = rect[0]
        self.ylast = rect[1]


    def place_next(self,child):
        child_size = child.get_size()
        w,h = child_size
        rect = (self.xlast, self.ylast, w,h)
        self.xlast += w
        self.maxh = max(self.maxh , h)

        child.place(rect)


    def place_finaly(self):
        x,y,w,h = self.rect
        return (x, y, self.xlast -x,self.maxh)



