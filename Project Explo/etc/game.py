import pygame as pg

TILESIZE = 64
WIDTH = TILESIZE * 18
HEIGHT = TILESIZE * 12

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (255, 255, 255)
W็HITE = (0, 0, 0)

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)


node00,node01,node02,node03,node04,node05,node06,node08,node09 = (0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,8),(0,9)
node12,node16,node18 = (1,2),(1,6),(1,8)
node20,node21,node22,node23,node25,node26,node27,node28,node29 = (2,0),(2,1),(2,2),(2,3),(2,5),(2,6),(2,7),(2,8),(2,9)
node30,node33,node34,node35,node39 = (3,0),(3,3),(3,4),(3,5),(3,9)
node40,node42,node43,node45,node46,node48,node49 = (4,0),(4,2),(4,3),(4,5),(4,6),(4,8),(4,9)
node50,node51,node52,node53,node54,node56,node57,node58 = (5,0),(5,1),(5,2),(5,3),(5,4),(5,6),(5,7),(5,8)
node60,node61,node63,node64,node65,node66,node68,node69 = (6,0),(6,1),(6,3),(6,4),(6,5),(6,6),(6,8),(6,9)
node70,node73,node74,node75,node78,node79 = (7,0),(7,3),(7,4),(7,5),(7,8),(7,9)
node80,node81,node82,node83,node85,node86,node87,node88 = (8,0),(8,1),(8,2),(8,3),(8,5),(8,6),(8,7),(8,8)
node90,node92,node93,node96,node97,node98,node99 = (9,0),(9,2),(9,3),(9,6),(9,7),(9,8),(9,9)

graph = {node00 : set([node01]),
         node01 : set([node00, node02]),
         node02 : set([node01, node03, node12]),
         node03 : set([node02, node04]),
         node04 : set([node03, node05]),
         node05 : set([node04, node06]),
         node06 : set([node05, node16]),
         node08 : set([node09, node18]),
         node09 : set([node08]),
         node12 : set([node02, node22]),
         node16 : set([node06, node26]),
         node18 : set([node08, node28]),
         node20 : set([node21, node30]),
         node21 : set([node20, node22]),
         node22 : set([node21, node23, node12]),
         node23 : set([node22, node33]),
         node25 : set([node26, node35]),
         node26 : set([node25, node27, node16]),
         node27 : set([node26, node28]),
         node28 : set([node27, node29, node18]),
         node29 : set([node28, node39]),
         node30 : set([node20, node40]),
         node33 : set([node34, node23, node43]),
         node34 : set([node33, node35]),
         node35 : set([node34, node25, node45]),
         node39 : set([node29, node49]),
         node40 : set([node30, node50]),
         node42 : set([node43, node52]),
         node43 : set([node42, node33, node53]),
         node45 : set([node46, node35]),
         node46 : set([node45, node56]),
         node48 : set([node49, node58]),
         node49 : set([node48, node39]),
         node50 : set([node51, node40, node60]),
         node51 : set([node50, node52, node61]),
         node52 : set([node51, node53, node42]),
         node53 : set([node52, node54, node43, node63]),
         node54 : set([node53, node64]),
         node56 : set([node57, node46, node66]),
         node57 : set([node56, node58]),
         node58 : set([node57, node48, node68]),
         node60 : set([node61, node50, node70]),
         node61 : set([node60, node51]),
         node63 : set([node64, node53, node73]),
         node64 : set([node63, node65, node54, node74]),
         node65 : set([node64, node66, node75]),
         node66 : set([node65, node56]),
         node68 : set([node69, node58, node78]),
         node69 : set([node68, node79]),
         node70 : set([node60, node80]),
         node73 : set([node74, node63, node83]),
         node74 : set([node73, node75, node64]),
         node75 : set([node74, node65, node85]),
         node78 : set([node79, node68, node88]),
         node79 : set([node78, node69]),
         node80 : set([node81, node70, node90]),
         node81 : set([node80, node82]),
         node82 : set([node81, node83, node92]),
         node83 : set([node82, node73, node93]),
         node85 : set([node86, node75]),
         node86 : set([node85, node87, node96]),
         node87 : set([node86, node88, node97]),
         node88 : set([node87, node78, node98]),
         node90 : set([node80]),
         node92 : set([node93, node82]),
         node93 : set([node92, node83]),
         node96 : set([node97, node86]),
         node97 : set([node96, node98, node87]),
         node98 : set([node97, node99, node88]),
         node99 : set([node98])}

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
                
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None
    
#lst_path = bfs_paths(graph, node00, node99)
#for i in lst_path:
#    print(i)
#    print('___')


pg.init()
displaysurf = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("POLICE")

class player_(object):
    def __init__(self, x, y):
        self.hitbox = pg.Rect(x, y, TILESIZE, TILESIZE)
    def animate(self, displaysurf, color):
        pg.draw.rect(displaysurf, color, (self.hitbox.x, self.hitbox.y, TILESIZE, TILESIZE))
    def move(self, nextState):
        global turn, turn_i, turn_game
        self.hitbox.x += nextState[0]*TILESIZE
        self.hitbox.y += nextState[1]*TILESIZE
        turn_i += 1
        turn_game += 1
        if(turn_i >= len(turn)):
            turn_i = 0
        for wall in walls:
            if self.hitbox.colliderect(wall.rect):
                if nextState[0] > 0:
                    self.hitbox.right = wall.rect.left
                    turn_i -= 1
                    turn_game -= 1
                if nextState[0] < 0:
                    self.hitbox.left = wall.rect.right
                    turn_i -= 1
                    turn_game -= 1
                if nextState[1] > 0:
                    self.hitbox.bottom = wall.rect.top
                    turn_i -= 1
                    turn_game -= 1
                if nextState[1] < 0:
                    self.hitbox.top = wall.rect.bottom
                    turn_i -= 1
                    turn_game -= 1

class AI_(object):
    def __init__(self, x, y):
        self.startState = (x, y)
        self.hitbox = pg.Rect(x, y, TILESIZE, TILESIZE)
    def animate(self, displaysurf):
        pg.draw.rect(displaysurf, BLUE, (self.hitbox.x, self.hitbox.y, TILESIZE, TILESIZE))
    def move(self, nextState):
        self.hitbox.x += nextState[0]*TILESIZE
        self.hitbox.y += nextState[1]*TILESIZE
    def move_to(self, ai):
        global turn, turn_i, turn_game
        
        ptog = len(shortest_path(graph, player_node['PLAYER'], player_node['goalPY']))
        if(ptog > 3):
            player_node['goalAI'] = shortest_path(graph, player_node['PLAYER'], player_node['goalPY'])[3]
        else:
            player_node['goalAI'] = shortest_path(graph, player_node['PLAYER'], player_node['goalPY'])[-1]
        
        atop = len(shortest_path(graph, player_node['AI'], player_node['PLAYER']))
        if(atop <= 3):
            lst_path = shortest_path(graph, player_node['AI'], player_node['PLAYER'])
        else:
            lst_path = shortest_path(graph, player_node['AI'], player_node['goalAI'])
        if(player_node['AI'] == player_node['goalAI']):
            player_node['goalAI'] = player_node['PLAYER']
            lst_path = shortest_path(graph, player_node['AI'], player_node['goalAI'])
            
        if(player_node['AI'] != player_node['goalAI']):
            if(player_node['AI'][1] < lst_path[1][1]):
                ai.move(RIGHT)
#                player_node['AI'] = lst_path[1]
            elif(player_node['AI'][1] > lst_path[1][1]):
                ai.move(LEFT)
#                player_node['AI'] = lst_path[1]
            elif(player_node['AI'][0] < lst_path[1][0]):
                ai.move(DOWN)
#                player_node['AI'] = lst_path[1]
            elif(player_node['AI'][0] > lst_path[1][0]):
                ai.move(UP)
#                player_node['AI'] = lst_path[1]
                
            turn_i += 1
            if(turn_i >= len(turn)):
                turn_i = 0
            
class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pg.Rect(pos[0], pos[1], TILESIZE, TILESIZE)
    
def events(player):
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            player.move(LEFT)
        if event.key == pg.K_RIGHT:
            player.move(RIGHT)
        if event.key == pg.K_UP:
            player.move(UP)
        if event.key == pg.K_DOWN:
            player.move(DOWN)
        if event.key == pg.K_SPACE:
            print(player.hitbox.x ,' ', player.hitbox.y)
            
def drawGrid():
    for drawX in range(0, WIDTH, TILESIZE):
        pg.draw.line(displaysurf, (0, 0, 0), (drawX, 0), (drawX, HEIGHT))
    for drawY in range(0, HEIGHT, TILESIZE):
        pg.draw.line(displaysurf, (0, 0, 0), (0, drawY), (WIDTH, drawY))
        
def redraw():
    global turn_i, turn, text_score
    displaysurf.fill((255, 255, 255))
    
    for wall in walls:
        pg.draw.rect(displaysurf, (0, 0, 0), wall.rect)
        
    player_.animate(displaysurf, RED)
#    player_2.animate(displaysurf, GREEN)
#    player_3.animate(displaysurf, BLUE)
#    pg.draw.rect(displaysurf, (188, 188, 188), ((player_node['goal'][1]+11)*TILESIZE, (player_node['goal'][0]+1)*TILESIZE, TILESIZE, TILESIZE))
    ai_.animate(displaysurf)
    
    drawGrid()
    pg.draw.rect(displaysurf, (204, 255, 255), (turn[turn_i].hitbox.x, turn[turn_i].hitbox.y, TILESIZE, TILESIZE), 5)
    
    displaysurf.blit(text_score,(5,5))
    
    pg.display.update()
    

walls = []
mapp = ['000000000000000000',
        '0000P......0..0000',
        '000000.000.0.00000',
        '0000....0.....0000',
        '0000.00...000.0000',
        '0000.0..0..0..0000',
        '0000.....0...00000',
        '0000..0....0..0000',
        '0000.00...00..0000',
        '0000....0..A.00000',
        '0000.0..00...G0000',
        '000000000000000000']

x = y = 0
for row in mapp:
    for col in row:
        if col == '0':
            Wall((x, y))
        if col == 'P':
            player_ = player_(x, y)
        if col == 'A':
            ai_ = AI_(x, y)
        if col == 'G':
            win = (x, y)
        x += TILESIZE
    y += TILESIZE
    x = 0
    
font = pg.font.SysFont('comicsans',40)
    
turn = [player_, player_, ai_]
turn_i = 0

turn_game = 0

run = True

#player_node = {'AI' : (((ai_.hitbox.y-64)/64),((ai_.hitbox.x-256)/64)),
#               'PLAYER' : (((player_.hitbox.y-64)/64),((player_.hitbox.x-256)/64)),
#               'goalAI' : (0, 0),
#               'goalPY' : ((win[1]-64)/64, (win[0]-256)/64)}

while run:
    pg.time.Clock().tick(30)
    pg.time.delay(200)
    
    player_node = {'AI' : (((ai_.hitbox.y-64)/64),((ai_.hitbox.x-256)/64)),
                   'PLAYER' : (((player_.hitbox.y-64)/64),((player_.hitbox.x-256)/64)),
                   'goalAI' : (0, 0),
                   'goalPY' : ((win[1]-64)/64, (win[0]-256)/64)}
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
    if(turn[turn_i] != ai_):
        events(turn[turn_i])
    if(turn[turn_i] == ai_):
        ai_.move_to(ai_)
        
    score0 = 200 - turn_game
    score1 = score0//2
    text_score = font.render('SCORE : '+str(score1), 1, (0, 255, 0))
        
    if((player_.hitbox.x, player_.hitbox.y) == win):
        print('WIN!!! \nTHE SCORE IS '+str(score1))
        run = False
        
    if((player_.hitbox.x, player_.hitbox.y) == (ai_.hitbox.x, ai_.hitbox.y+64) or 
       (player_.hitbox.x, player_.hitbox.y) == (ai_.hitbox.x, ai_.hitbox.y-64) or 
       (player_.hitbox.x, player_.hitbox.y) == (ai_.hitbox.x+64, ai_.hitbox.y) or 
       (player_.hitbox.x, player_.hitbox.y) == (ai_.hitbox.x-64, ai_.hitbox.y) or
       (player_.hitbox.x, player_.hitbox.y) == (ai_.hitbox.x, ai_.hitbox.y)):
        print('LOSE!!!')
        run = False

    redraw()
    
        
pg.quit()