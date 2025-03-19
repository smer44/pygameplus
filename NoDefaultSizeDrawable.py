from yge.turnbased.Drawable import Drawable


class NoDefaultSizeDrawable(Drawable):
    '''
    Component what has no default size,
    usually it is some size not specific
    generated content
    like solid color or pattern.
    This component does not nave influence
    on the size of the container it is in.
    This component has no starting size.

    '''

    def __init__(self, name):
        Drawable.__init__(self,name)