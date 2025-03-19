

class MonoPlacer:
    '''
    Placer, what takes outer bounding rectangle
    and returns one and only one  inner bounding
    rectangle, for example with offset or in specific
    place inside.
    All placer support chaining to the next placer.

    '''

    def __init__(self,name):
        assert isinstance(name, str) , f"yOneToOnePlacer.__init__: wrong {name=}"
        #assert self.check_implementation()
        self.name = name
        self.nextPlacer = None

    def place(self,rect):
        own_result = self.__place_inner__(rect)
        if self.nextPlacer:
            return self.nextPlacer.place(own_result)
        else:
            return own_result

    def check_implementation(self):
        return hasattr(self, "__place_inner__") and callable(self.__place_inner__)

        