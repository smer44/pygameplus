

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

    # must implement place start and place next




