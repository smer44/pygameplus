import pygame
from Sprite import Sprite


obj = Sprite("test_image_load")

obj.load("../mc_descengind_staircase.png")


pygame.init()

# Set window size
w,h = obj.surface.get_size()
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Pygame Surface Example")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Blit (draw) the surface onto the screen at position (150, 125)
    screen.blit(obj.surface, (0, 0))

    # Update the display
    pygame.display.flip()

pygame.quit()