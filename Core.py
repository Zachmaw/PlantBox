import pygame
from defaults import *
# import random
# import time

# def next():### recombine the genomes?
#     pass

# def newGene(currentGenomeLength, parentalData: "str" = None):
#     if parentalData != None:
#         ### full random (int, int, int, int)
#         gene = (random.randint(0, currentGenomeLength + 1))### duplicate? I have no idea.
#         pass
#     elif parentalData[-2:] == "+m":
#         gene = next(parentalData[:-2])
#         # gene = mutate(gene)
#         pass
#     else:
#         gene = next(parentalData)
#     return gene

# class Organism():
#     def __init__(self, seed: "tuple") -> None:
#         self.energy = seed[0]
#         pass

class Tile(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__()
        self.image = 


class Token(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__()
    

class World():
    '''
    The world is a 2-D euclidean plane tiled with equivalent squares.
    Represented as a list of lists of strings?
    Represented as a world of rows of tiles.
    '''
    def __init__(self, hwGridSize:"pygame.surface._Coordinate") -> None:
        self.HEIGHT, self.WIDTH = hwGridSize
        ### build world full of air
        self.grid = list()# simple list to save data
        for row in range(self.WIDTH):# in every row
            self.grid.append(list()) # new column for the list
            if row >= gridHeight - groundLevel:
                for tile in range(self.HEIGHT):# and for every tile
                    self.grid[row][tile] = "earth"# soil.
            else:
                for tile in range(self.HEIGHT):# and for every tile
                    self.grid[row][tile] = "air"# air.

    def advance(self):
        ### everything gets processed
        # physics on each tile somehow
        # growth step( cycle through each plant. how to assign priority when competing for a tile?)
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

# def buildBackdrop(size:"pygame.surface._Coordinate"):
#     def flipColor(colorState, colorA:"tuple[int,int,int]", colorB:"tuple[int,int,int]"):
#         if not colorState or colorState == colorA:
#             colorState = colorB
#         else: 
#             colorState = colorA
#         return colorState
#     c = None
#     backdrop = pygame.surface.Surface(size)
#     backdrop.fill(BLACK)
#     for y in range(0,HEIGHT,cellSize): 
#         c = flipColor(c, RED, BLACK)
#         for x in range(0,WIDTH,cellSize):
#             c = flipColor(c, RED, BLACK)
#             pygame.draw.rect(backdrop, c, pygame.Rect(x, y, x+cellSize, y+cellSize))
#     return backdrop

def toggle(param: "bool"):
    if param:
        return False
    else:
        return True

# def gridDecode(mousePos):
#     tileCoordinate = mousePos### figure out which tile coordinate the mouse is on
#     return tileCoordinate

# def showTileSelection():### for a limited time with fade out.
#     pass# now = time.

def core():
    pygame.init()# initialize pygame and create window
    # pygame.mixer.init()
    debugFont = pygame.font.SysFont("monospace", 15)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Planter")
    clock = pygame.time.Clock()
    tiles = pygame.sprite.Group()# define groups
    plants = pygame.sprite.Group()
    ### build the world
    box = World((gridHeight, gridWidth))
    running = True# main loop
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()# pressedKeysDict
        # shiftKeys = [keys[pygame.K_LSHIFT], keys[pygame.K_RSHIFT]]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = (event.pos[0] // cellSize, event.pos[1] // cellSize)# Get tile coord from mouse location
                # if any(shiftKeys):
                #     pass
                # else:
                #     pass
                print(f"You clicked box {x}, {y}.")
                ### set selected box to selected tile
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    pass### increase current selection
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    pass### decrease current selection
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    pass### select previous option
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    pass### select next option
                elif event.key == pygame.K_SPACE:# toggle time paused
                    pauseToggle = toggle(pauseToggle)
                elif event.key == pygame.K_F1:# toggle debug HUD
                    debugHUDtoggle = toggle(debugHUDtoggle)

        # Update
        if not pauseToggle:
            box.advance()
            simRuntime += 1

        # Render
        screen.fill(BLACK)
        ###
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