import pygame as pg
import socket


pg.init()

TILESIZE = 64
WIDTH = TILESIZE * 18
HEIGHT = TILESIZE * 12

displaysurf = pg.display.set_mode((WIDTH, HEIGHT))

pg.display.set_caption("CAT and MOUSE")


class player_(object):
    global graph
    def __init__(self, node):
        self.node = node
    def animate(self, displaysurf, color):
        pg.draw.rect(displaysurf, color, (((self.node%18)*TILESIZE), ((self.node//18)*TILESIZE), TILESIZE, TILESIZE))
    def move(self, nextState):
        global turn, turn_i, turn_game
        if(nextState == 'LEFT'):
            if(self.node-1 in graph[self.node]):
                self.node = self.node-1
                turn_i += 1
                if(turn_i >= len(turn)):
                    turn_i = 0
        if(nextState == 'RIGHT'):
            if(self.node+1 in graph[self.node]):
                self.node = self.node+1
                turn_i += 1
                if(turn_i >= len(turn)):
                    turn_i = 0
        if(nextState == 'UP'):
            if(self.node-18 in graph[self.node]):
                self.node = self.node-18
                turn_i += 1
                if(turn_i >= len(turn)):
                    turn_i = 0
        if(nextState == 'DOWN'):
            if(self.node+18 in graph[self.node]):
                self.node = self.node+18
                turn_i += 1
                if(turn_i >= len(turn)):
                    turn_i = 0
                    
                

def ai_move(graph, ai_node, goal):
    path = BFS(graph, ai_node, goal)
    if(path[0]-ai_node == 1):
        return "RIGHT"
    if(path[0]-ai_node == -1):
        return "LEFT"
    if(path[0]-ai_node == 18):
        return "DOWN"
    if(path[0]-ai_node == -18):
        return "UP"
    


def events():
    if event.type == pg.KEYDOWN:
        pg.time.delay(100)
        if event.key == pg.K_LEFT:
            return("LEFT")
        if event.key == pg.K_RIGHT:
            return("RIGHT")
        if event.key == pg.K_UP:
            return("UP")
        if event.key == pg.K_DOWN:
            return("DOWN")

    
def redraw():
    global mode, turn, turn_i, turn_game, score1
    cat = pg.image.load('CAT.png')
    mouse = pg.image.load('MOUSE.png')
    displaysurf.fill((255, 255, 255))
        
    for wall in range(len(graph)):
        if(len(graph[wall]) == 0):
            pg.draw.rect(displaysurf, (0, 0, 0), (((wall%18)*64), ((wall//18)*64), TILESIZE, TILESIZE))
    if(mapp == map_choose[0]):
        displaysurf.blit(mapNo,(192,0))
    if(mapp == map_choose[1]):
        displaysurf.blit(mapEx,(0,0))
    
    score0 = 200 - turn_game
    score1 = score0//2
    text_score = font2.render('SCORE : ' + str(score1), 1, (0, 255, 0))
    displaysurf.blit(text_score,(5,5))
            
#    player_1.animate(displaysurf, RED)
    displaysurf.blit(mouse,(((player_1.node%18)*TILESIZE), ((player_1.node//18)*TILESIZE)))
    if(mode == 1):
#        player_2.animate(displaysurf, BLUE)
        displaysurf.blit(cat,(((player_2.node%18)*TILESIZE), ((player_2.node//18)*TILESIZE)))
    elif(mode == 0):
#        ai.animate(displaysurf, GREEN)
        displaysurf.blit(cat,(((ai.node%18)*TILESIZE), ((ai.node//18)*TILESIZE)))
        
#    for drawX in range(0, WIDTH, TILESIZE):
#        pg.draw.line(displaysurf, (0, 0, 0), (drawX, 0), (drawX, HEIGHT))
#    for drawY in range(0, HEIGHT, TILESIZE):
#        pg.draw.line(displaysurf, (0, 0, 0), (0, drawY), (WIDTH, drawY))
    pg.draw.rect(displaysurf, (204, 255, 255), ((turn[turn_i].node%18)*TILESIZE, (turn[turn_i].node//18)*TILESIZE, TILESIZE, TILESIZE), 5)

    pg.display.update()
    

def BFS(graph, start, goal):
    if(start == goal):
        return [start]
    queue = list()
    discovered = list()
    layer = list()
    parent = list()
    path = list()
    for i in range(len(graph)):
        discovered.append(False)
        layer.append(999)
        parent.append(i)
    queue.append(start)
    discovered[start] = True
    layer[start] = 0
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if(discovered[v] == False):
                queue.append(v)
                discovered[v] = True
                layer[v] = layer[u]+1
                parent[v] = u
                if(v == goal):
                    while(v != parent[v]):
                        path.append(v)
                        v = parent[v]
                    return path[::-1]
                
def createGraph(mapp):
    graph = list()
    node = 0
    for i in range(len(mapp)):
        for j in range(len(mapp[0])):
            graph.append(list())
            if(mapp[i][j] != '0'):
                if(j-1 >= 0):
                    if(mapp[i][j-1] != '0'):
                        graph[node].append(node-1)
                if(j+1 <= 17):
                    if(mapp[i][j+1] != '0'):
                        graph[node].append(node+1)
                if(i-1 >= 0):
                    if(mapp[i-1][j] != '0'):
                        graph[node].append(node-len(mapp[0]))
                if(i+1 <= 17):
                    if(mapp[i+1][j] != '0'):
                        graph[node].append(node+len(mapp[0]))
            node += 1
    return graph



map_choose = [['000000000000000000',
               '0000P......0..0000',
               '000000.000.0.00000',
               '0000....0.....0000',
               '0000.00...000.0000',
               '0000.0..0..0..0000',
               '0000.....0...00000',
               '0000..0....0..0000',
               '0000.00...00..0000',
               '0000....0..A.00000',
               '0000.0..00....G000',
               '000000000000000000'],
        
              ['000000000000000000',
               '0P......0........0',
               '0.0000000.000000.0',
               '0.0.....0......0.0',
               '0.0.000....000.0.0',
               '0.0.0...00.0.....0',
               '0.....0.00...0.0.0',
               '0.0.000....000.0.0',
               '0.0......0.....0.0',
               '0.000000.0000000.0',
               '0........0......AG',
               '000000000000000000']]


mapp = map_choose[0]

mapNo = pg.image.load('map1.png')
mapEx = pg.image.load('map2.png')

font = pg.font.SysFont('comicsans', 100)
font2 = pg.font.SysFont('comicsans', 38)

text_menu = [pg.image.load('START.png'), pg.image.load('QUIT.png')]
text_mode = [pg.image.load('SINGLE.png'), pg.image.load('MULTI.png'), pg.image.load('BACK1.png')]
text_map = [pg.image.load('NORMAL.png'), pg.image.load('EXPERT.png'), pg.image.load('BACK2.png')]
text_up = [pg.image.load('UP1.png'), pg.image.load('UP2.png'), pg.image.load('UP3.png'),
           pg.image.load('UP4.png'), pg.image.load('UP5.png'), pg.image.load('UP6.png')]
text_down = [pg.image.load('DOWN1.png'), pg.image.load('DOWN2.png'), pg.image.load('DOWN3.png'),
             pg.image.load('DOWN4.png'), pg.image.load('DOWN5.png'), pg.image.load('DOWN6.png')]
text_host_or_join = [pg.image.load('HOST.png'), pg.image.load('JOIN.png'), pg.image.load('BACK3.png')]
text_go_back = [pg.image.load('GO.png'), pg.image.load('BACK3.png')]

bg_start = pg.image.load('bg_start.jpg')
bg_quit = pg.image.load('bg_quit.jpg')
bg_single = pg.image.load('bg_single.jpg')
bg_multi = pg.image.load('bg_multi.jpg')
bg_map0 = pg.image.load('bg_map0.jpg')
bg_map1 = pg.image.load('bg_map1.jpg')
bg_back = pg.image.load('gb_back.png')
bg_host = pg.image.load('gb_host.png')
bg_join = pg.image.load('gb_join.png')

choose = 0
mode = 0

stage = 'title'  

sound_bg = pg.mixer.Sound('sound/bg.ogg')
run_sound_bg = False
sound_play = pg.mixer.Sound('sound/play.ogg')
run_sound_play = False
sound_win = pg.mixer.Sound('sound/win.ogg')
run_sound_win = False
sound_lose = pg.mixer.Sound('sound/lose.ogg')
run_sound_lose = False
sound_move = pg.mixer.Sound('sound/move.ogg')
sound_dead = pg.mixer.Sound('sound/dead.ogg')
sound_slide = pg.mixer.Sound('sound/slide.ogg')
sound_select = pg.mixer.Sound('sound/select.ogg')

run_all = True
run = False
run_end = False
run_into = True
run_host = False
run_join = False

count = 0

this_is = None

while run_all:
    while run_into:
        if(not run_sound_bg):
            sound_bg.play(-1)
            run_sound_bg = True
        
        pg.time.Clock().tick(30)
        pg.time.delay(60)
        displaysurf.fill((0, 0, 0))
        displaysurf.blit(text_up[count%6], (544, 448))
        displaysurf.blit(text_down[count%6], (544, 644))
        count += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_into = False
                run_all = False
                
        if(stage == 'title'):
            displaysurf.blit(text_menu[choose], (384, 512))
            if(choose == 0):
                displaysurf.blit(bg_start, (96, 32))
            if(choose == 1):
                displaysurf.blit(bg_quit, (96, 32))
            if event.type == pg.KEYDOWN:
                pg.time.delay(100)
                if event.key == pg.K_UP:
                    sound_slide.play()
                    choose -= 1
                    if(choose < 0):
                        choose = 1
                if event.key == pg.K_DOWN:
                    sound_slide.play()
                    choose += 1
                    if(choose > 1):
                        choose = 0
                if event.key == pg.K_SPACE:
                    sound_select.play()
                    if(choose == 0):
                        stage = 'mode'
                        choose = 0
                    if(choose == 1):
                        run_into = False
                        run_all = False
            
        elif(stage == 'mode'):
            displaysurf.blit(text_mode[choose], (224, 512))
            if(choose == 0):
                displaysurf.blit(bg_single, (96, 32))
            if(choose == 1):
                displaysurf.blit(bg_multi, (96, 32))
            if(choose == 2):
                displaysurf.blit(bg_back, (256, 32))
            if event.type == pg.KEYDOWN:
                pg.time.delay(100)
                if event.key == pg.K_UP:
                    sound_slide.play()
                    choose -= 1
                    if(choose < 0):
                        choose = 2
                if event.key == pg.K_DOWN:
                    sound_slide.play()
                    choose += 1
                    if(choose > 2):
                        choose = 0
                if event.key == pg.K_SPACE:
                    sound_select.play()
                    if(choose == 0):
                        stage = 'map'
                        choose = 0
                        mode = 0
                    if(choose == 1):
                        stage = 'multi'
                        choose = 0
                        mode = 1
                    if(choose == 2):
                        stage = 'title'
                        choose = 0
                        
        elif(stage == 'multi'):
            displaysurf.blit(text_host_or_join[choose], (416, 512))
            if(choose == 0):
                displaysurf.blit(bg_host, (320, 32))
            if(choose == 1):
                displaysurf.blit(bg_join, (320, 32))
            if(choose == 2):
                displaysurf.blit(bg_back, (256, 32))
            if event.type == pg.KEYDOWN:
                pg.time.delay(100)
                if event.key == pg.K_UP:
                    sound_slide.play()
                    choose -= 1
                    if(choose < 0):
                        choose = 2
                if event.key == pg.K_DOWN:
                    sound_slide.play()
                    choose += 1
                    if(choose > 2):
                        choose = 0
                if event.key == pg.K_SPACE:
                    sound_select.play()
                    if(choose == 0):
                        stage = 'host'
                        choose = 0
                    if(choose == 1):
                        stage = 'join'
                        choose = 0
                    if(choose == 2):
                        stage = 'mode'
                        choose = 0
                        
        elif(stage == 'host'):
            this_is = 'host'
            my_ip = socket.gethostbyname(socket.gethostname())
            textIP = font.render('IP : '+str(my_ip),1,(0,0,0))
            if(choose == 0):
                pg.draw.rect(displaysurf, (255, 255, 255), (224, 160, 704, 128))
                displaysurf.blit(textIP, (256, 200))
            if(choose == 1):
                displaysurf.blit(bg_back, (256, 32))
            displaysurf.blit(text_go_back[choose], (416, 512))
            if event.type == pg.KEYDOWN:
                pg.time.delay(100)
                if event.key == pg.K_UP:
                    sound_slide.play()
                    choose -= 1
                    if(choose < 0):
                        choose = 1
                if event.key == pg.K_DOWN:
                    sound_slide.play()
                    choose += 1
                    if(choose > 1):
                        choose = 0
                if event.key == pg.K_SPACE:
                    sound_select.play()
                    if(choose == 0):
                        sound_bg.stop()
                        run_sound_bg = False
                        run = True
                        run_into = False
                        mapp = map_choose[0]
                    if(choose == 1):
                        stage = 'multi'
                        choose = 0
                        
        elif(stage == 'join'):
            this_is = 'join'
            if(choose == 1):
                displaysurf.blit(bg_back, (256, 32))
            displaysurf.blit(text_go_back[choose], (416, 512))
            if event.type == pg.KEYDOWN:
                pg.time.delay(100)
                if event.key == pg.K_UP:
                    sound_slide.play()
                    choose -= 1
                    if(choose < 0):
                        choose = 1
                if event.key == pg.K_DOWN:
                    sound_slide.play()
                    choose += 1
                    if(choose > 1):
                        choose = 0
                if event.key == pg.K_SPACE:
                    sound_select.play()
                    if(choose == 0):
                        sound_bg.stop()
                        run_sound_bg = False
                        run = True
                        run_into = False
                        mapp = map_choose[0]
                    if(choose == 1):
                        stage = 'multi'
                        choose = 0
                        
        elif(stage == 'map'):
            displaysurf.blit(text_map[choose], (352, 512))
            if(choose == 0):
                displaysurf.blit(bg_map0, (96, 32))
            if(choose == 1):
                displaysurf.blit(bg_map1, (96, 32))
            if(choose == 2):
                displaysurf.blit(bg_back, (256, 32))
            if event.type == pg.KEYDOWN:
                pg.time.delay(100)
                if event.key == pg.K_UP:
                    sound_slide.play()
                    choose -= 1
                    if(choose < 0):
                        choose = 2
                if event.key == pg.K_DOWN:
                    sound_slide.play()
                    choose += 1
                    if(choose > 2):
                        choose = 0
                if event.key == pg.K_SPACE:
                    sound_select.play()
                    if(choose == 0):
                        stage = 'play'
                        mapp = map_choose[0]
                        choose = 0
                        run = True
                        run_into = False
                    if(choose == 1):
                        stage = 'play'
                        mapp = map_choose[1]
                        choose = 0
                        run = True
                        run_into = False
                    if(choose == 2):
                        stage = 'mode'
                        choose = 0
                        
#        for drawX in range(0, WIDTH, TILESIZE):
#            pg.draw.line(displaysurf, (0, 255, 0), (drawX, 0), (drawX, HEIGHT))
#        for drawY in range(0, HEIGHT, TILESIZE):
#            pg.draw.line(displaysurf, (0, 255, 0), (0, drawY), (WIDTH, drawY))
        
        pg.display.update()
    
    
    graph = createGraph(mapp)
    
    c = -1
    for a in range(len(mapp)):
        for b in range(len(mapp[0])):
            c += 1
            if mapp[a][b] == 'P':
                node_player_1 = c
            elif mapp[a][b] == 'A':
                node_ai = c
            elif mapp[a][b] == 'G':
                node_goal = c
    
#    node_player_1 = 22
#    node_goal = 194
#    node_ai = 173
    
    player_1 = player_(node_player_1)
    player_2 = player_(node_ai)
    ai = player_(node_ai)
    
    turn_choose = [[player_1, player_1, ai], [player_1, player_1, player_2]]
    turn = turn_choose[mode]
    turn_i = 0
    turn_game = 0
    score1 = 0
    
    while run:
        if(mode == 0):
            sound_bg.stop()
            run_sound_bg = False
            if(not run_sound_play):
                sound_play.play(-1)
                run_sound_play = True
            pg.time.Clock().tick(30)
            pg.time.delay(60)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    run_all = False
                    
                if(turn[turn_i] != ai):
                    pre_node = player_1.node
                    turn[turn_i].move(events())
                    if(pre_node != player_1.node):
                        turn_game += 1
                        sound_move.play()
                        
                if(turn[turn_i] == ai):
#                    turn[turn_i].move(ai_move(graph, ai.node, player_1.node))
                    playerToGoal = BFS(graph, player_1.node, node_goal)
                    if(len(playerToGoal) <= 4):
                        turn[turn_i].move(ai_move(graph, ai.node, player_1.node))
                    else:
                        aiToPlayer = BFS(graph, ai.node, player_1.node)
                        if(len(aiToPlayer) <= 4):
                            turn[turn_i].move(ai_move(graph, ai.node, player_1.node))
                        else:
                            turn[turn_i].move(ai_move(graph, ai.node, playerToGoal[3]))
                            
           
            redraw()
            
            if(player_1.node == node_goal):
                run = False
                run_end = True   
            if(ai.node in graph[player_1.node] or ai.node == player_1.node):
                sound_play.stop()
                run_sound_play = False
                sound_play.stop()
                run_sound_play = False
                sound_dead.play()
                pg.time.delay(2000)
                sound_dead.stop()
                score1 -= 100
                run = False
                run_end = True
            if(turn_game == 200):
                score1 = 0
                run = False
                run_end = True
                    
        elif(mode == 1):
            if(this_is == 'host'):
                my_ip = socket.gethostbyname(socket.gethostname())
                port = 7000
                server = socket.socket()
                server.bind((my_ip, port))
                server.listen(1)
                print(my_ip)
                print('Waiting for client...')
                client, addr = server.accept()
                print('Connected')
                run_host = True
                run = False
                
            if(this_is == 'join'):
                server_ip = input('Server ip : ')
                port = 7000
                server = socket.socket()
                server.connect((server_ip, port))
                print('Connected')
                run_join = True
                run = False
         
    sound_bg.stop()
    run_sound_bg = False
    if(not run_sound_play):
        sound_play.play(-1)
        run_sound_play = True
                
    while run_host:
        pg.time.Clock().tick(30)
        pg.time.delay(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_host = False
                run_all = False
        if event.type == pg.KEYDOWN:
            pg.time.delay(300)
            pre_node = player_1.node
            if event.key == pg.K_LEFT:
                message = "LEFT"
                turn[turn_i].move(message)
                if(pre_node != player_1.node):
                    turn_game += 1
                    sound_move.play()
                    client.send(message.encode('utf-8'))
            if event.key == pg.K_RIGHT:
                message = "RIGHT"
                turn[turn_i].move(message)
                if(pre_node != player_1.node):
                    turn_game += 1
                    sound_move.play()
                    client.send(message.encode('utf-8'))
            if event.key == pg.K_UP:
                message = "UP"
                turn[turn_i].move(message)
                if(pre_node != player_1.node):
                    turn_game += 1
                    sound_move.play()
                    client.send(message.encode('utf-8'))
            if event.key == pg.K_DOWN:
                message = "DOWN"
                turn[turn_i].move(message)
                if(pre_node != player_1.node):
                    turn_game += 1
                    sound_move.play()
                    client.send(message.encode('utf-8'))
                
        redraw()
        
        if(player_1.node == node_goal):
            run_host = False
            run_end = True
        if(player_2.node in graph[player_1.node] or player_2.node == player_1.node):
            sound_play.stop()
            run_sound_play = False
            sound_dead.play()
            pg.time.delay(2000)
            sound_dead.stop()
            score1 -= 100
            run_host = False
            run_end = True
        if(turn_game == 200):
            score1 = 0
            run_host = False
            run_end = True
                
        if(turn[turn_i] != player_1 and run_host == True):
            message = client.recv(1024)
            message = message.decode('utf-8')
            sound_move.play()
            turn[turn_i].move(message)
        
    
    while run_join:
        pg.time.Clock().tick(30)
        pg.time.delay(60)
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_join = False
                run_all = False
        if event.type == pg.KEYDOWN:
            pg.time.delay(300)
            pre_node = player_2.node
            if event.key == pg.K_LEFT:
                message = "LEFT"
                turn[turn_i].move(message)
                if(pre_node != player_2.node):
                    turn_game += 1
                    sound_move.play()
                    server.send(message.encode('utf-8'))
            if event.key == pg.K_RIGHT:
                message = "RIGHT"
                turn[turn_i].move(message)
                if(pre_node != player_2.node):
                    turn_game += 1
                    sound_move.play()
                    server.send(message.encode('utf-8'))
            if event.key == pg.K_UP:
                message = "UP"
                turn[turn_i].move(message)
                if(pre_node != player_2.node):
                    turn_game += 1
                    sound_move.play()
                    server.send(message.encode('utf-8'))
            if event.key == pg.K_DOWN:
                message = "DOWN"
                turn[turn_i].move(message)
                if(pre_node != player_2.node):
                    turn_game += 1
                    sound_move.play()
                    server.send(message.encode('utf-8'))
            
        redraw()
        
        if(player_1.node == node_goal):
            score1 -= 100
            run_join = False
            run_end = True
        if(player_2.node in graph[player_1.node] or player_2.node == player_1.node):
            sound_play.stop()
            run_sound_play = False
            sound_dead.play()
            pg.time.delay(2000)
            sound_dead.stop()
            run_join = False
            run_end = True
        if(turn_game == 200):
            score1 = 0
            run_join = False
            run_end = True
        
        if(turn[turn_i] != player_2 and run_join == True):
            message = server.recv(1024)
            message = message.decode('utf-8')
            sound_move.play()
            turn[turn_i].move(message)
            turn_game += 1
            redraw()
            if(player_1.node == node_goal):
                score1 -= 100
                run_join = False
                run_end = True
            if(player_2.node in graph[player_1.node] or player_2.node == player_1.node):
                sound_play.stop()
                run_sound_play = False
                sound_dead.play()
                pg.time.delay(2000)
                sound_dead.stop()
                run_join = False
                run_end = True
            if(turn_game == 200):
                score1 = 0
                run_join = False
                run_end = True
                
        if(turn[turn_i] != player_2 and run_join == True):
            message = server.recv(1024)
            message = message.decode('utf-8')
            sound_move.play()
            turn[turn_i].move(message)
            turn_game += 1
            redraw()
            if(player_1.node == node_goal):
                score1 -= 100
                run_join = False
                run_end = True   
            if(player_2.node in graph[player_1.node] or player_2.node == player_1.node):
                sound_play.stop()
                run_sound_play = False
                sound_dead.play()
                pg.time.delay(2000)
                sound_dead.stop()
                run_join = False
                run_end = True
            if(turn_game == 200):
                score1 = 0
                run_join = False
                run_end = True
                
    sound_play.stop()
    run_sound_play = False
    
                
    bg_win = pg.image.load('bg_win.jpg')
    bg_lose = pg.image.load('bg_lose.jpg')
    bg_draw = pg.image.load('bg_draw.jpg')
    text_space = pg.image.load('SPACETOMENU.jpg')
    
    while run_end:
        if(mode == 1):
            server.close()
            print('Disconnected')
            mode = 0
        displaysurf.fill((0, 0, 0))
        text_score = font.render('SCORE : '+str(score1), 1, (255, 255, 255))
        displaysurf.blit(text_space, (160, 600))
        if(score1 < 0):
            if(not run_sound_lose):
                sound_lose.play(-1)
                run_sound_lose = True
            displaysurf.blit(bg_lose, (96, 32))
        elif(score1 > 0):
            if(not run_sound_win):
                sound_win.play(-1)
                run_sound_win = True
            displaysurf.blit(text_score,(384, 480))
            displaysurf.blit(bg_win, (96, 32))
        elif(score1 == 0):
            if(not run_sound_lose):
                sound_lose.play(-1)
                run_sound_lose = True
            displaysurf.blit(bg_draw, (96, 32))
                
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_end = False
                run_all = False
        if event.type == pg.KEYDOWN:
            pg.time.delay(100)
            if event.key == pg.K_SPACE:
                run_into = True
                stage = 'title'
                run_end = False
                
        pg.display.update()

    sound_win.stop()
    run_sound_win = False
    sound_lose.stop()
    run_sound_lose = False
        
            
pg.quit()
