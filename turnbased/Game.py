import pygame


class Game:

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.mouse_listeners = [] # list
        self.visible = [] # list of visible objects
        self.updated = [] # list of objects what get updated each tick
        self.root = None

    def mouse_react(self, mouse_pos):
        pass

    def draw_all_visible(self,surface):
        surface.fill((0, 0, 0))
        for item in self.visible:
            item.draw(surface)

    def update_all(self):
        for item in self.updated:
            item.update()

    def keydown_react(self,game,event):
        #self.updated[0].updating ^= True
        pass



    def run(self):
        assert self.root , f"Game : running with no root set"
        root = self.root
        size = root.get_size()
        pygame.init()
        surface = pygame.display.set_mode((size))
        clock = self.clock
        loop = True
        draw_visible = self.draw_all_visible
        update_all = self.update_all
        while loop:
            clock.tick(60)
            #currently onny root draws its content.
            draw_visible(surface)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    self.mouse_react(mouse_pos)
                if event.type == pygame.KEYDOWN:
                    self.keydown_react(self,event)

            update_all()





