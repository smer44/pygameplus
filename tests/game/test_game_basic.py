

from yge.turnbased.Game import Game
from yge.turnbased.Sprite import Sprite

obj = Sprite("test_image_load")

obj.load("../mc_descengind_staircase.png")

game = Game()

game.root = obj
game.visible.append(obj)

game.run()