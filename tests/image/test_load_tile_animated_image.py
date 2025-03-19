from yge.turnbased.Game import Game
from yge.turnbased.AnimatedTiledSprite import AnimatedTiledSprite


red_hat_w_cells = 12
red_hat_max_cells = 12*10 + 7

obj= AnimatedTiledSprite("test_load_tiled_animated_image",red_hat_w_cells, red_hat_max_cells)

obj.load("../knife_3.png")

print(obj)
print(obj.get_size())

game = Game()
game.root = obj
game.visible.append(obj)
game.updated.append(obj)

game.run()
