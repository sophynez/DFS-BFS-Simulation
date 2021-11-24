import sys
import pygame as pygame
from collections import deque as queue

PC = (233,150,122)
BLACK = (108, 98, 113)
WHITE = (250, 250, 250)
BGC = (192,192,192)
OBSC = (220,20,60)
BC = (198, 192, 199)

blockSize = 50 
nbr_ycells = 0 #nombre de cases dans la grille sur l'axe y
nbr_xcells = 0 #nombre de cases dans la grille sur l'axe x
x_goal = 0 
y_goal = 0 
x_start = 0 
y_start = 0 
End = False
obstacles = []
visited = []
fathers = []
s=[]

def addObstacle(X, Y, color):
    obstacles.append((X, Y, color))


def Main():
    global SCREEN, CLOCK, WINDOW_WIDTH, WINDOW_HEIGHT, x_start, y_start, End
    WINDOW_WIDTH = nbr_xcells * 50
    WINDOW_HEIGHT = nbr_ycells * 50
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BGC)

    drawGrid()
    createTarget()
    createObstacles()
    colorblock(x_start, y_start, BLACK)
    pygame.display.update()

    while True:
        if not End:
            End = DFS() #changer entre BFS() et DFS() pour cahnger la methode de recherche
            print(visited)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def drawGrid():
    for x in range(0, WINDOW_HEIGHT, blockSize):
        for y in range(0, WINDOW_WIDTH, blockSize):
            rectan = pygame.Rect(y, x, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rectan, 1)  


def colorblock(X, Y, color):
    Xstep = X * 50
    Ystep = Y * 50
    for x in range(0, WINDOW_HEIGHT, blockSize):
        for y in range(0, WINDOW_WIDTH, blockSize):
            if Xstep == x and Ystep == y:
                rectan = pygame.Rect(y, x, 49, 49)
                pygame.draw.ellipse(SCREEN, color, rectan)
                if color in [WHITE, OBSC]:
                    pygame.draw.ellipse(SCREEN, BLACK, rectan, 1)



def createTarget():
    colorblock(x_goal, y_goal, WHITE)


def createObstacles():
    for i in range(len(obstacles)):
        x, y, color = obstacles[i]
        colorblock(x, y, color)


def Visited(X, Y):
    if (X, Y) in visited:
        return True
    return False


def isValid(X, Y):
    if X < 0 or Y < 0 or X >= nbr_ycells or Y >= nbr_xcells:
        return False

    for i in range(len(obstacles)):
        x, y, color = obstacles[i]
        if (x, y) == (X, Y):
            return False

    return True


# Function to perform the BFS traversal
def BFS():
    # Stores indices of the matrix cells
    q = queue()

    q.append((x_start, y_start))
    visited.append((x_start, y_start))
    

    while len(q) > 0:
        x, y = q.popleft()

        colorblock(x, y, PC)
        pygame.time.delay(500)
        pygame.display.update()

        if (x, y) == (x_goal, y_goal):
            return True

        adjy = y
        adjx = x - 1
        if isValid(adjx, adjy) and not Visited(adjx, adjy):
            q.append((adjx, adjy))
            visited.append((adjx, adjy))
            
        adjx = x + 1
        if isValid(adjx, adjy) and not Visited(adjx, adjy):
            q.append((adjx, adjy))
            visited.append((adjx, adjy))
            
        adjx = x
        adjy = y - 1
        if isValid(adjx, adjy) and not Visited(adjx, adjy):
            q.append((adjx, adjy))
            visited.append((adjx, adjy))
            
        adjy = y + 1
        if isValid(adjx, adjy) and not Visited(adjx, adjy):
            q.append((adjx, adjy))
            visited.append((adjx, adjy))
            

def DFS():
    st =[]
    st.append([x_start, y_start])
    

    while (len(st) > 0):
        # Pop the top pair

        x,y = st[len(st) - 1]
        st.remove(st[len(st) - 1])

        if isValid(x, y) and not Visited(x, y):
            visited.append((x,y))
            colorblock(x, y, PC)
            pygame.time.delay(100)
            pygame.display.update()
        if (x, y) == (x_goal, y_goal):
            return True
        adjy = y
        adjx = x - 1
        if isValid(adjx, adjy) and not Visited(adjx, adjy):
            st.append([adjx, adjy])
        adjx = x + 1
        if isValid(adjx, adjy) and not Visited(adjx, adjy):
            st.append([adjx, adjy])
        adjx = x
        adjy = y - 1
        if isValid(adjx, adjy) and not Visited(adjx, adjy):
            st.append([adjx, adjy])
        adjy = y + 1
        if isValid(adjx, adjy) and not Visited(adjx, adjy):
            st.append([adjx, adjy]) 


if __name__ == '__main__':
    nbr_xcells = 10
    nbr_ycells = 10

    x_start = 0
    y_start = 0

    x_goal = 8              
    y_goal = 3 
    
    addObstacle(3, 2, OBSC )
    addObstacle(5, 3, OBSC)
    addObstacle(2, 6, OBSC)
    Main() #changer dan sla fonction main la fonction DFS() ou bien BFS() pour executer
           #respectivement la methode de 



 

