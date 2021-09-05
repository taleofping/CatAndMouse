#client
import pygame as pg
import socket

pg.init()
displaysurf = pg.display.set_mode((400, 400))
pg.display.set_caption("CLIENT")
#
server_ip = input('Server ip : ')
port = 7000

server = socket.socket()
server.connect((server_ip,port))
run = True       
count = 1 
while run:
    if(count == 1):
        message = server.recv(1024)
        message = message.decode('utf-8')
        print('B : ',message)
        message = server.recv(1024)
        message = message.decode('utf-8')
        print('B : ',message)
        count = 0
        
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    if event.type == pg.KEYDOWN:
        pg.time.delay(300)
        if event.key == pg.K_SPACE:
            print('space')
        if event.key == pg.K_LEFT:
            message = "LEFT"
            server.send(message.encode('utf-8'))
            count += 1
        if event.key == pg.K_RIGHT:
            message = "RIGHT"
            server.send(message.encode('utf-8'))
            count += 1
        if event.key == pg.K_UP:
            message = "UP"
            server.send(message.encode('utf-8'))
            count += 1
        if event.key == pg.K_DOWN:
            message = "DOWN"
            server.send(message.encode('utf-8'))
            count += 1


pg.quit()
