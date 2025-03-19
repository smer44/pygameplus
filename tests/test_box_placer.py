import pygame

from yge.turnbased_old.yboxplacer import yBoxPlacer
from yge.turnbased_old.yframe import yFrame
from yge.turnbased_old.ygame import yGame
from yge.turnbased_old.ynormoffset import yNormOffsetPlacer
from yge.turnbased_old.ynotcreaterthenimage import yNotGreaterThenImagePlacer
from yge.turnbased_old.ysametomany import ySamePlacer
from yge.turnbased_old.ysolid import ySolid
from yge.turnbased_old.ytextsequence import yTextSequence

from pygame.font import Font

texts = """
New game
New game pressed!
""".splitlines()
texts = [t.strip() for t in texts]
texts = [t for t in texts if t]
pygame.init()
font = Font(None, 74)

yte = yTextSequence("new game text", texts,font,(255,255,0))
yte.loop = True
texts = """
Load
Load pressed!
""".splitlines()
texts = [t.strip() for t in texts]
texts = [t for t in texts if t]

yte2 = yTextSequence("Load text", texts,font,(0,255,255))
yte2.loop = True
texts = """
save
save pressed!
""".splitlines()
texts = [t.strip() for t in texts]
texts = [t for t in texts if t]

yte3 = yTextSequence("save text", texts,font,(255,0,255))
yte3.loop = True
place_not_greater = yNotGreaterThenImagePlacer("test_not_greater_placer", yte)
place_not_greater2 = yNotGreaterThenImagePlacer("test_not_greater_placer2", yte2)
place_not_greater3 = yNotGreaterThenImagePlacer("test_not_greater_placer3", yte3)

place_same = ySamePlacer("boring same placer")
yte.placer = place_not_greater
yte2.placer = place_not_greater2
yte3.placer = place_not_greater3


#TODO - create placers as pure functions?
place_box = yBoxPlacer("test_box_placer", 3,3,100)


bg = ySolid("TestBackground",10, 10, 10)
bg.placer = place_same

scene = yFrame("bgscene", bg, yte, yte2, yte3)
scene.placer =place_box

w,h = 1920,1080
yg = yGame(scene,w,h)

yg.place()
yg.add_deep(scene)

print(f"{yg.mouse_listeners=}")
print(f"{yg.visible=}")
yg.run()










