import pygame
from defaults import *
import random

def next():### recombine the genomes
    pass

def newGene(dp1, parentalData: "str" = None):
    if parentalData != None:
        ### full random (int, int, int, int)
        gene = (random.randint(0, dp1))### duplicate and figure out the plus one? needs current genome length
        pass
    elif parentalData[-2:] == "+m":
        gene = next(parentalData[:-2])
        # gene = mutate(gene)
        pass
    else:
        gene = next(parentalData)
    return gene

class organism():
    def __init__(self, energy) -> None:
        self.energy = energy
        pass

class world():
    '''
    The world is a 2-D euclidean plane tiled with equivalent squares.
    Only render as much of the world as you need.
    '''
    def __init__(self, hwSize:"pygame.surface._Coordinate") -> None:
        self.HEIGHT, self.WIDTH = hwSize
        
        pass

def blit_text(surface, text, pos, font, color=pygame.Color("black")):
    # Got this incredibly helpful function from https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
    words = [word.split(" ") for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(" ")[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
        if y >= max_height + word_height / 2:# my edit started here
            print("Not all debug text could be displayed...")

def buildBackdrop(size:"pygame.surface._Coordinate"):
    def flipColor(colorState, colorA:"tuple[int,int,int]", colorB:"tuple[int,int,int]"):
        if not colorState or colorState == colorA:
            colorState = colorB
        else: 
            colorState = colorA
        return colorState
    c = None
    backdrop = pygame.surface.Surface(size)
    backdrop.fill(BLACK)
    for y in range(0,HEIGHT,cellSize): 
        c = flipColor(c, RED, BLACK)
        for x in range(0,WIDTH,cellSize):
            c = flipColor(c, RED, BLACK)
            pygame.draw.rect(backdrop, c, pygame.Rect(x, y, x+cellSize, y+cellSize))
    return backdrop

def core():
    pygame.init()# initialize pygame and create window
    # pygame.mixer.init()
    debugFont = pygame.font.SysFont("monospace", 15)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("AgentSim")
    clock = pygame.time.Clock()
    background = buildBackdrop(screen.get_rect().size)
    # define groups
    all_sprites = pygame.sprite.Group()
    plants = pygame.sprite.Group()
    ### build the world
    running = True# main loop
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()# pressedKeysDict
        shiftKeys = [keys[pygame.K_LSHIFT], keys[pygame.K_RSHIFT]]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                print(mousePos)
                if any(shiftKeys):
                    pass
                else:
                    pass
            elif event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_w or event.key == pygame.K_UP:
                #     pass
                if event.key == pygame.K_SPACE:# toggle time paused
                    if pauseToggle:
                        pauseToggle = False
                    else:
                        pauseToggle = True
                elif event.key == pygame.K_F1:
                    if debugHUDtoggle:
                        debugHUDtoggle = False
                    else:
                        debugHUDtoggle = True
        ### Check collisions

        # Update
        if not pauseToggle:
            all_sprites.update()
            simRuntime += 1

        # Render
        screen.fill(BLACK)
        all_sprites.draw(screen)
        if debugHUDtoggle:
            DebugText = f"Simulation Runtime: {simRuntime}\nFog Level: {fogLevel}\nLiving plants: {len(plants.sprites())}\nSun Energy: to be displayed per tile"
            blit_text(screen, DebugText, (20, 20), debugFont, color = pygame.Color("white"))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    core()


# either the int will match an index for which a gene exists or the int will be too high to activate a gene.
# When a mutation occurs, how much variation should an int have access to? (Min/Max)
# 
# 


# solid color background (grid color)
# draw tiles
    # "untouchables" tiles (air, fire)
    # "touchables" (water, earth)
    # tokens/solid tiles (stone, seed, outgrowth, leaf, branch, root)