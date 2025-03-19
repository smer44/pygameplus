import pygame
from yge.turnbased_old.ysolid import ySolid
from yge.turnbased_old.yvariantitem import yVariantItem
from yge.turnbased_old.ytext import yText
from yge.turnbased_old.yscene_old import yScene_old
from yge.turnbased_old.ygame import yGame
from yge.turnbased_old.yframe import yFrame

print(pygame.K_w)
pygame.init()
font = pygame.font.Font(None, 74)

#pygame.font.init()

def display(ga):
    print("Key Pressed!")
    #new_text = font.render('Key  Pressed!', True, (0, 0, 255))
    #ga.display.blit(new_text, (200, 150))
    ga.item.items[0].toggle_children()

    ga.item.set_dirty_deep()
    print(f"display :{ga.item.items[0]} :: {ga.item.items[0].items}")




bg = ySolid("bg",255, 255, 255)

bg2 = ySolid("bg2",100, 100, 100)

switch_bg = yVariantItem("bg",bg, bg2)



new_text = font.render('New game', True, (0, 0, 255))
new_text2 = font.render('Tutorial', True, (0, 255,0))

ta = yText('New game','New game', font, (0, 0, 255))
ta2 = yText('Tutorial','Tutorial', font,(0, 255,0))

menu = yScene_old("menu",ta, ta2)

main_scene = yFrame("bg scene", switch_bg, menu)

ga  = yGame(main_scene,800,600,)



#ga.add_key_action(pygame.K_w, display, ga)
ga.run()


