#server
import socket
import pygame as pg

pg.init()
displaysurf = pg.display.set_mode((400, 400))
pg.display.set_caption("SERVER")

my_ip = socket.gethostbyname(socket.gethostname())
port = 1234
server = socket.socket()
server.bind((my_ip, port))
server.listen(1)
print(my_ip)
print('Waiting for client...')
client, addr = server.accept()


run = True
count = 0
while run:   
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    if event.type == pg.KEYDOWN:
        pg.time.delay(300)
        if event.key == pg.K_SPACE:
            print('space')
        if event.key == pg.K_LEFT:
            message = "LEFT"
            client.send(message.encode('utf-8'))
            count += 1
        if event.key == pg.K_RIGHT:
            message = "RIGHT"
            client.send(message.encode('utf-8'))
            count += 1
        if event.key == pg.K_UP:
            message = "UP"
            client.send(message.encode('utf-8'))
            count += 1
        if event.key == pg.K_DOWN:
            message = "DOWN"
            client.send(message.encode('utf-8'))
            count += 1
    if(count == 2):
        message = client.recv(1024)
        message = message.decode('utf-8')
        print('B : ',message)
        count = 0