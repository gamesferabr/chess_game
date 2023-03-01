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

img = pygame.image.load("meu_jogo_de_xadrez/interface_grafica/imagens/whitepanw.png")
img.convert()

# Transforma a imagem do tamanho que eu quero
img = pygame.transform.scale(img, (75,75))

#Provavelmente da o movimento da imagem, mas ainda é incerto
rect = img.get_rect()

largura_celula = LARGURA_TELA // 8
altura_celula = ALTURA_TELA // 8

posicao_inicial = (0,1)

posicao_atual = posicao_inicial

#Essa variavel ajusta a posição para o tamanho do tabuleiro
x, y = tabuleiro.convert_pos_to_coord(posicao_atual)

#Essa variavel aqui ajusta a imagem peão.
rect = pygame.Rect(x, y, altura_celula, largura_celula)

while running:
     
     for event in pygame.event.get():
          
          #pecas = []
          #for i in range(0,8):
          #  pecas.append(Peca("whitepanw.png", (i, 1), tabuleiro, BRANCO))
          #  pecas.append(Peca("blackpanw.png", (i, 6), tabuleiro, PRETO))
          #  tabuleiro.desenhar_tabuleiro(tela)   
          #  for peca in pecas:
          #      peca.Pecas(tela)
        #
          
          if event.type == pygame.QUIT:
              running = False
              
          # Movimenta as peças com o mouse
          elif event.type == pygame.MOUSEBUTTONDOWN: #and not peca_selecionada:
            if rect.collidepoint(event.pos):
               moving = True  

           # Verifica se o jogador moveu a peça selecionada
          elif event.type == pygame.MOUSEBUTTONUP: #and peca_selecionada:
               if moving: 
                 posicao_nova = (rect.x//tabuleiro.tamanho_quadrado,rect.y//tabuleiro.tamanho_quadrado)
                                                             #Essa parte aqui da variavel resolve o passant
                 if posicao_nova[1] == posicao_atual[1]+1 or posicao_nova[1] == 3 and max(round(posicao_nova[0]), 0) == posicao_atual[0]:
                     posicao_atual = (max(round(posicao_nova[0]), 0),posicao_nova[1] if posicao_nova[1] < 8 else posicao_atual[1])          
                     print(posicao_atual)
                     #Essa linha aqui faz a casa do tabuleiro atrair a imagem
                     rect.topleft = tabuleiro.convert_pos_to_coord(posicao_atual)
                    
                 else:                 
                    
                    #Isso que faz a peça não poder ir para outras casas se a condição anterior não for cumprida
                    rect.topleft = tabuleiro.convert_pos_to_coord(posicao_atual)
                    print(rect.topleft)
                 #Isso faz com que a peça seja solta do mouse
                 moving = False
  
          
          elif event.type == pygame.MOUSEMOTION and moving:
             #if rect.left < -40:             
             #    rect = pygame.Rect(x, y, altura_celula, largura_celula)
             #    #print(event.rel)

            #Isso me faz ter a possibilidade de poder mover a peça com o mouse
            rect.move_ip(event.rel)    
             
          tabuleiro.desenhar_tabuleiro(tela)
          tela.blit(img,rect)
          
              
    # Atualiza a tela
          pygame.display.update()






