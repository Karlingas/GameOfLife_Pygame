import random, pygame
global SCREEN, CLOCK, blockSize, ev

class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.ogcol = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('Consolas', 24)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            self.color = (128, 128, 128)
            for event in ev:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
        else:
            self.color = self.ogcol
        return False

class Cell:
    def __init__(self, state, cords):
        self.state = state
        self.cords = cords

    def compruebaReglas(self, grid):
        neighbors = 0
        x, y = self.cords

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                nx, ny = (x + dx) % MAP_X, (y + dy) % MAP_Y
                if grid[nx][ny].state:
                    neighbors += 1

        new_state = self.state
        if self.state:  # Alive
            if neighbors < 2 or neighbors > 3:
                new_state = False  # Dies
        else:  # Dead
            if neighbors == 3:
                new_state = True  # Becomes alive

        return Cell(new_state, self.cords)

def fillGrid():
    SCREEN.fill(BLACK)
    for i in range(MAP_X):
        for j in range(MAP_Y):
            rect = pygame.Rect(i * blockSize, j * blockSize, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE if MAP[i][j].state else BLACK, rect)

def modifyMap(pos):
    x, y = pos[0] // blockSize, pos[1] // blockSize
    if x < MAP_X and y < MAP_Y:
        MAP[x][y].state = not MAP[x][y].state

def resizeGrid(new_width, new_height):
    global MAP_X, MAP_Y, MAP, blockSize

    MAP_X, MAP_Y = new_width // blockSize, new_height // blockSize
    new_map = [[Cell(False, [i, j]) for j in range(MAP_Y)] for i in range(MAP_X)]

    for i in range(min(MAP_X, len(MAP))):
        for j in range(min(MAP_Y, len(MAP[i]))):
            new_map[i][j].state = MAP[i][j].state

    return new_map

# Configuración inicial
WINDOW_WIDTH, WINDOW_HEIGHT = 750, 750
blockSize = 10

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

MAP_X, MAP_Y = WINDOW_WIDTH // blockSize, WINDOW_HEIGHT // blockSize
MAP = [[Cell(random.choice([True, False]) if random.randint(0, 2) == 1 else False, [i, j]) for j in range(MAP_Y)] for i in range(MAP_X)]

pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
CLOCK = pygame.time.Clock()
paused = False
btn = Button((255, 255, 0), 0, 0, 200, 50, text="PAUSE")

pygame.display.set_caption("Game of Life - Pygame")

# Bucle principal
while True:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN and not btn.isOver(pygame.mouse.get_pos()):
            modifyMap(pygame.mouse.get_pos())

        elif event.type == pygame.VIDEORESIZE:
            WINDOW_WIDTH, WINDOW_HEIGHT = event.w, event.h
            SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
            MAP = resizeGrid(WINDOW_WIDTH, WINDOW_HEIGHT)

    if btn.isOver(pygame.mouse.get_pos()):
        paused = not paused

    if not paused:
        NEXT_GEN = [[MAP[i][j].compruebaReglas(MAP) for j in range(MAP_Y)] for i in range(MAP_X)]
        MAP = [[Cell(NEXT_GEN[i][j].state, [i, j]) for j in range(MAP_Y)] for i in range(MAP_X)]

    fillGrid()
    btn.draw(SCREEN)

    CLOCK.tick(15)
    pygame.display.update()
