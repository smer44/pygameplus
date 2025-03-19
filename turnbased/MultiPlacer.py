

class MultiPlacer:
    '''
    Abstraction of a placer, what gains as input one rect
    and returns multiple rects - used for a yContainer what has children.
    Usually, those "inner" rects are inside of given rect, but it is not necessary.
    '''
    #TODO - there should be differences from MonoPlacer
    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name

    def place(self,rect):
        own_result = self.__place_inner__(rect)
        if self.nextPlacer:
            return self.nextPlacer.place(own_result)
        else:
            return own_result