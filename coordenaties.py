import pygame, sys
from Graph import*
from BFS import*
from tkinter import messagebox
from objects import*
from DFS import*
from UCS import*
from A_star import*
from BFS import*
import random
from pygame.locals import *

def move(windowG, start,goal, board, pacman, graph, cookies, lghost):
    if start == goal:
        pass
    else:
        r1 = shorted_path_bfs(board,graph, start, goal)
        r2 = shorted_path_ucs(board, graph, start, goal)
        r3 = shorted_path_a_star(board, graph, start, goal)
        #r4 = dfs_paths(board, graph, start, goal)
        roads = [r1,r2,r3]
        road = None
        for i in roads:
            if i != False:
                if road == None:
                    road = i
                elif len(i) < len(road):
                    road = i
        if road != None:
            while len(road) > 1: 
                current = road[0]
                nextt = road[1]
                road = road[1:]
                board[current[0]][current[1]] = 'x'
                board[nextt[0]][nextt[1]] = 'pacman'
                imagefondo = pygame.image.load('Images/fondogame.jpg')
                if current[1] != nextt[1]:
                    if current[1] < nextt[1]:
                        for i in range(30):
                            pacman.image =  pygame.image.load("Images/pacman2.png")
                            windowG.blit(imagefondo,(0,0))
                            pacman.rect.left += pacman.velocidad
                            y1 =50
                            cf = 0
                            Fuente = pygame.font.Font(None,30)
                            labelscore = Fuente.render("SCORE: "+str(pacman.score),0,(255,255,255))
                            windowG.blit(labelscore,(10,10))
                            for i in board:
                                x1 = 100
                                for j in i:
                                    if j == 1:
                                        obs = obstacle(x1,y1,"Images/obs.png")
                                        obs.dibujar(windowG)
                                        cf +=1
                                    x1+=30
                                y1+=30
                            for i in lghost:
                                i.dibujar(windowG)
                            for i in cookies:
                                if i.rect.colliderect(pacman.rect):
                                    cookies.remove(i)
                                    pacman.score+=10
                                else:
                                    i.dibujar(windowG)
                            for i in lghost:
                                i.dibujar(windowG)
                            pacman.dibujar(windowG)
                            pygame.display.update()
                    else:
                        for i in range(30):
                            pacman.image =  pygame.image.load("Images/pacman_left.png")
                            windowG.blit(imagefondo,(0,0))
                            pacman.rect.left -= pacman.velocidad
                            y1 = 50
                            cf = 0
                            Fuente = pygame.font.Font(None,30)
                            labelscore = Fuente.render("SCORE: "+str(pacman.score),0,(255,255,255))
                            windowG.blit(labelscore,(10,10))
                            for i in board:
                                x1 = 100
                                for j in i:
                                    if j == 1:
                                        obs = obstacle(x1,y1,"Images/obs.png")
                                        obs.dibujar(windowG)
                                    x1+=30
                                y1+=30
                            for i in lghost:
                                i.dibujar(windowG)
                            for i in cookies:
                                if i.rect.colliderect(pacman.rect):
                                    cookies.remove(i)
                                    pacman.score += 10
                                else:
                                    i.dibujar(windowG)
                            for i in lghost:
                                i.dibujar(windowG)
                            pacman.dibujar(windowG)
                            pygame.display.update()
                            
                elif current[0] != nextt[0]:
                    if current[0] < nextt[0]:
                        for i in range(30):
                            if i%1== 0:
                                pacman.image =  pygame.image.load("Images/pacman_down.png")
                            else:
                                pacman.image =  pygame.image.load("Images/pacman1.png")
                            windowG.blit(imagefondo,(0,0))
                            pacman.rect.top += pacman.velocidad
                            y1 =50
                            cf = 0
                            Fuente = pygame.font.Font(None,30)
                            labelscore = Fuente.render("SCORE: "+str(pacman.score),0,(255,255,255))
                            windowG.blit(labelscore,(10,10))
                            for i in board:
                                x1 = 100
                                for j in i:
                                    if j == 1:
                                        obs = obstacle(x1,y1,"Images/obs.png")
                                        obs.dibujar(windowG)
                                        cf +=1
                                    x1+=30
                                y1+=30
                            for i in lghost:
                                i.dibujar(windowG)
                            for i in cookies:
                                if i.rect.colliderect(pacman.rect):
                                    cookies.remove(i)
                                    pacman.score+=10
                                else:
                                    i.dibujar(windowG)
                            for i in lghost:
                                i.dibujar(windowG)
                            pacman.dibujar(windowG)
                            pygame.display.update()
                    else:
                        for i in range(30):
                            if i%1 == 0:
                                pacman.image =  pygame.image.load("Images/pacman_up.png")
                            else:
                                pacman.image =  pygame.image.load("Images/pacman1.png")
                            windowG.blit(imagefondo,(0,0))
                            pacman.rect.top -= pacman.velocidad
                            y1 =50
                            cf = 0
                            Fuente = pygame.font.Font(None,30)
                            labelscore = Fuente.render("SCORE: "+str(pacman.score),0,(255,255,255))
                            windowG.blit(labelscore,(10,10))
                            for i in board:
                                x1 = 100
                                for j in i:
                                    if j == 1:
                                        obs = obstacle(x1,y1,"Images/obs.png")
                                        obs.dibujar(windowG)
                                    x1+=30
                                y1+=30
                            for i in cookies:
                                if i.rect.colliderect(pacman.rect):
                                    cookies.remove(i)
                                    pacman.score+=10
                                else:
                                    i.dibujar(windowG)
                            for i in lghost:
                                i.dibujar(windowG)
                            pacman.dibujar(windowG)
                            pygame.display.update()
                


def give_coordenaties(board):
    pygame.init()
    imagefondo = pygame.image.load('Images/fondogame.jpg')
    x1 = 200 + 30*len(board[0])
    y1 = 80 + 30*len(board)
    windowG = pygame.display.set_mode((x1,y1))
    pygame.display.set_caption('pacman')
    y1 = 50
    fant = ["Images/green_center.png","Images/red_center.png","Images/pink_center.png","Images/yellow_center.png"]
    band = 0
    cookies = []
    cf = 0
    lghost = []
    for i in board:
        x1 = 100
        for j in i:
            if j == 'pacman':
                pacman = player(x1,y1,"Images/pacman2.png")
                pacman.dibujar(windowG)
            elif j == 1:
                obs = obstacle(x1,y1,"Images/obs.png")
                obs.dibujar(windowG)
            elif j == 'f' or j == 'F':
                if cf >= len(fant):
                    cf = 0
                ghost = enemy(x1+3,y1, fant[cf])
                ghost.dibujar(windowG)
                lghost.append(ghost)
                cf +=1
            else:
                cook = cookie(x1,y1,"Images/cookie.png")
                cook.dibujar(windowG)
                cookies.append(cook)
            x1+=30
        y1+=30
    if len(cookies) > 0:
        pygame.display.update()
    reloj = pygame.time.Clock()
    while True:
        reloj.tick(500)
        y1 = 50
        fant = ["Images/green_center.png","Images/red_center.png","Images/pink_center.png","Images/yellow_center.png"]
        band = 0
        windowG.blit(imagefondo,(0,0))
        Fuente = pygame.font.Font(None,30)
        labelscore = Fuente.render("SCORE: "+str(pacman.score),0,(255,255,255))
        windowG.blit(labelscore,(10,10))
        for i in board:
            x1 = 100
            for j in i:
                if j == 'pacman':
                    pacman.dibujar(windowG)
                elif j == 1:
                    obs = obstacle(x1,y1,"Images/obs.png")
                    obs.dibujar(windowG)
                x1+=30
            y1+=30
        for i in lghost:
            ghost=i
            i.dibujar(windowG)
        for i in cookies:
            i.dibujar(windowG)
        if len(cookies)==0:
            break
        for event in pygame.event.get():
            if event.type == QUIT:        
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicion = event.pos
                posy = posicion[0]-100
                posx = posicion[1]-50
                while posx%30 != 0:
                    posx-=1
                posx = posx//30
                while posy%30 != 0:
                    posy-=1
                posy = posy//30
                for i in range (len(board)):
                    for j in range(len(board[0])):
                        if board[i][j] == 'pacman':
                            start = (i,j)
                            break
                graph = list_ad(board)
                if len(cookies) > 0:
                    move(windowG, start, (posx,posy), board, pacman, graph, cookies, lghost)
        if len(cookies) == 0:
            messagebox.showinfo("Game over", "¡¡YOU WON THE GAME!!")
            break
        pygame.display.update()
    pygame.quit()
    sys.exit()            
