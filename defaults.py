cellSize = 32
gridWidth = 10
gridHeight = 10
sunMult = 0.95
fogLevel = 0
groundLevel = 3
lightCycleDuration = 30
darknessDuration = 8
FPS = 60
# Switches
pauseToggle = False
debugHUDtoggle = False
mainLoop = True
# counters
simRuntime = 0
WIDTH = cellSize * gridWidth
HEIGHT = cellSize * gridHeight

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

tileColors = {
    "air": CYAN,
    "fire": RED,
    "water": BLUE,
    "earth": (67, 42, 25),# best brown I could get: like 6 minutes tweaking rgb sliders.
    "stone": (45, 45, 45)# Gray: 2 seconds.
}
tokenColors = {
    "outgrowth": WHITE,
    "branch": (67+35, 42+35, 25+35),# the other brown but lighter
    "seed": BLACK,
    "leaf": GREEN,
    "root": YELLOW
}