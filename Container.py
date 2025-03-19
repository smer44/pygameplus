from AbstractDrawable import AbstractDrawable


class Container(AbstractDrawable):
    is_container = True
    def __init__(self, name, *children):
        AbstractDrawable.__init__(self, name)
        self.children = list(children)

    def extend(self,*children):
        self.children.extend(children)

    #TODO - what to do if place_scale_if_need is called for container?

    def place(self, rect = None):
        placer = self.placer
        placer.place_start(self,rect)
        for child in self.children:

            placer.place_next(child)

        outer_rect = placer.place_finaly()
        self.dest_rect = outer_rect




    def debug_places(self):
        return f"Container({self.dest_rect}):(" +   ", ".join(c.debug_places() for c in self.children) + ")"

    def get_size(self):
        return self.dest_rect[2:]

