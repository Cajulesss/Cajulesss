import pygame

#INICIALIZAÇÃO
pygame.init()

#TELA/DIMENSÕES
largura = 800
altura = 480

janela = pygame.display.set_mode([largura,altura])


#NOME DA JANELA
pygame.display.set_caption("Testando Código")

imagemfundo = pygame.image.load("imagens/Projetopy.jpg")
#REDIMENSIONAR A IMAGEM
redimen = pygame.transform.scale(imagemfundo,(largura,altura))

#LOOP
gameloop = True
def draw():
    janela.fill([204,153,255])

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw()

    janela.blit(redimen,(0,0))
    #ATUALIZAR A JANELA A CADA FRAME (melhor que a update )
    pygame.display.flip()