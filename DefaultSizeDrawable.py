from pygameplus.AbstractDrawable import AbstractDrawable


class DefaultSizeDrawable(AbstractDrawable):
    '''
    Component what has default size,
    usually it is image or rendered text
    or some already rendered surface.
    This component gets clipped by resizing.
    This component may influence on the size of the
    container it is stored in.
    '''

    def __init__(self, name):
        AbstractDrawable.__init__(self,name)







