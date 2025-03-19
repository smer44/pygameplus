from AbstractDrawable import AbstractDrawable


class Container(AbstractDrawable):
    is_container = True
    def __init__(self, name, *children):
        AbstractDrawable.__init__(self, name)
        self.children = list(children)

    def extend(self,*children):
        self.children.extend(children)

    def place(self, rect = (0,0,0,0)):
        placer = self.placer
        placer.place_start(rect)
        for child in self.children:
            # TODO - this is bottom-up placing approach:
            child_size = child.get_size()
            child_rect = placer.place_next(child_size)
            child.place(child_rect)
        outer_rect = placer.place_finaly()
        self.dest_rect = outer_rect


    def debug_places(self):
        return ", ".join(c.debug_places() for c in self.children)

    def get_size(self):
        return self.dest_rect[2:]

