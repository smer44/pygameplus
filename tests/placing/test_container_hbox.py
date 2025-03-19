from Container import Container
from Game import Game
from HBox import HBox
from Sprite import Sprite

co = Container("test container")
hbox = HBox("text hbox")

co.placer = hbox



#load some images :

obj = Sprite("test_image_load")
obj.load("../mc_descengind_staircase.png")

obj2 = Sprite("test_image_load 2")
obj2.load(f"../run_girl_images/running_girl_1.png")

obj3 = Sprite("test_image_load 3")
obj3.load("../knife_3.png")


co.extend(obj,obj2,obj3)
co.place()
print(co.debug_places())



game = Game()
game.root = co
game.add(co)
#game.updated.append(obj)

game.run()




