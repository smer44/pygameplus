from yge.turnbased.AnimatedSprite import AnimatedSprite
from yge.turnbased.Game import Game

obj = AnimatedSprite("test_load_animated_image")


filenames = [f"../run_girl_images/running_girl_{n}.png" for n in range(1,9)]

obj.load_all(filenames)

game = Game()
game.root = obj
game.visible.append(obj)
game.updated.append(obj)



def stop_animate(self,event):
    #self.updated[0].updating ^= True
    obj.updating ^= True

game.keydown_react = stop_animate

game.run()