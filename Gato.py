import pygame

# Inicialización de pygame

pygame.init()
screen = pygame.display.set_mode((450,450))
pygame.display.set_caption("tic tac toe")

# Imagenes
fondo=pygame.image.load('triki/Tablero.png')
circulo=pygame.image.load('triki/circulo.png')
equis=pygame.image.load('triki/equis.png')

# Variables
fondo = pygame.transform.scale(fondo,(450,450))
circulo = pygame.transform.scale(circulo,(125,125))
equies = pygame.transform.scale(equis,(125,125))

coor = [[(40,50),(165,50),(290,50)],
        [(40,175),(165,175),(290,175)],
        [(40,300),(165,300),(290,300)]]

tablero = [['','',''],
          ['','',''],
          ['','','']]

turno= 'x'
game_over = False
clock = pygame.time.Clock()

def graficar_board():
    screen.blit(fondo, (0,0))
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col]=='x':
                dibujar_x(fila,col)
            elif tablero[fila][col]=='o':
                dibujar_o(fila,col)
            
def dibujar_x(fila,col):
    screen.blit(equis, coor[fila][col])
    
def dibujar_o(fila,col):
    screen.blit(circulo, coor[fila][col])
    
def verificar_ganador():
    for i in range(3):
        if tablero[i][0]== tablero[i][1] == tablero[i][2] != '':
            return True 
        if tablero[0][i]== tablero[1][i] == tablero[2][i] != '':
            return True
        if tablero[0][0]== tablero[1][1] == tablero[2][2] != '': 
            return True
        if tablero[0][2]== tablero[1][1] == tablero[2][0]!= '':
            return True
        return False

while not game_over:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           game_over=True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if(mouseX >= 40 and mouseY < 415) and (mouseX >= 50 and mouseY <425):
                fila =(mouseY -50)//125
                col = (mouseX-40)//125
                if tablero[fila][col]== '':
                    tablero[fila][col] = turno
                    fin_juego = verificar_ganador()
                    if fin_juego:
                        print(f"el juagador {turno} ha ganado!!")
                        game_over = True
                turno ='o' if turno == 'x' else 'x'
    graficar_board()     
    pygame.display.update()
    
pygame.quit()