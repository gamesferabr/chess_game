import pygame
from pygame.locals import *
import sys
from jogo.tabuleiro import Tabuleiro 
#from jogo.movimentos import Move
#from interface_grafica.pecas import Peca
from interface_grafica.tela import ALTURA_TELA,LARGURA_TELA
from interface_grafica.cores import BRANCO, PRETO


# Inicializa o Pygame
pygame.init()

# Cria a janela do jogo
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Tabuleiro de Xadrez")

# Cria um objeto de tabuleiro
tabuleiro = Tabuleiro()
tabuleiro.desenhar_tabuleiro(tela)
 
running = True
moving = False

# Loop principal do jogo
#peca_selecionada = None
img = pygame.image.load("interface_grafica/imagens/whitepanw.png")
img.convert()

# Transforma a imagem do tamanho que eu quero
img = pygame.transform.scale(img, (75,75))

#Provavelmente da o movimento da imagem, mas ainda é incerto
rect = img.get_rect()

largura_celula = LARGURA_TELA // 8
altura_celula = ALTURA_TELA // 8

#Determina a posição inicial do meu peão.
posicao = (0,1)

#Essa variavel ajusta a posição para o tamanho do tabuleiro
x, y = tabuleiro.convert_pos_to_coord(posicao)

#Essa variavel aqui ajusta a imagem peão.
rect = pygame.Rect(x, y, altura_celula, largura_celula)

while running:
     
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
              
          # Movimenta as peças com o mouse
          elif event.type == pygame.MOUSEBUTTONDOWN: #and not peca_selecionada:
            if rect.collidepoint(event.pos):
               moving = True  
           # Verifica se o jogador moveu a peça selecionada
          elif event.type == pygame.MOUSEBUTTONUP: #and peca_selecionada:
               moving = False
    
          elif event.type == pygame.MOUSEMOTION and moving:        
                  rect.move_ip(event.rel)     
          
               
          tabuleiro.desenhar_tabuleiro(tela)
          tela.blit(img,rect)
          
          
    # Atualiza a tela
          pygame.display.update()






