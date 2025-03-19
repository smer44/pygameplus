from Container import Container
from Game import Game
from HBoxTopDown import HBoxTopDown
from Sprite import Sprite


co = Container("test container")
hbox = HBoxTopDown("text hbox top down")

co.placer = hbox

#load some images :

obj = Sprite("test_image_load")
obj.load("../mc_descengind_staircase.png")

obj2 = Sprite("test_image_load 2")
obj2.load(f"../run_girl_images/running_girl_1.png")

obj3 = Sprite("test_image_load 3")
obj3.load("../knife_3.png")

co.extend(obj,obj2,obj3)
rect =(0,0,500,500)
co.place(rect)
print(co.debug_places())

game = Game()
game.root = co
game.add(co)
#game.updated.append(obj)

game.run()