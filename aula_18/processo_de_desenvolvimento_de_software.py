import random
import pygame

pygame.init()

largura = 600
altura = 400

tela = pygame.display.set_mode(largura, altura)

# carregar img

trex1 = pygame.image.load('assets\trex1.png')
trex2 = pygame.image.load('assets\trex2.png')
trex3 = pygame.image.load('assets\trex3.png')
cacto_img = pygame.image.load('assets\cacto.png')

chao = pygame.image.load('assets\chao.png')

tre_x = 100 
tre_x = 300

vel_y = 0
gravidade = 1 
pulando = False

cacto_x = 800
cacto_y = 300
frame = 0
score = 0 
font = pygame.font.SysFont('arial', 30)
game_over = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:        
        if event.key == pygame.K_SPACE and not pulando:
            vel_y = -22
            pulando = True

            if event.key == pygame.K_k and game_over:
                trex_y = 300
                cacto_x = 800
                score = 0 
                game_over = False
    if not game_over:
        # gravidade
        vel_y += gravidade
        trex_y += vel_y
        if trex_y >= 300:
            trex_y = 300
            pulando = False
        # chao infinto
        chao_x = -5
        if chao_x <= -800:
            chao_x = 0

    cacto_x -= 5 
    if cacto_x < -50:
        cacto_x = random.randint(800,100)
        score += 1

    # frame
    frame += 1
    if frame > 20:
        frame = 0
    if frame < 10:
        trex = trex1
    elif frame > 10 and frame <= 15:
        trex = trex2
    else : 
        trex = trex3

    trex_rect = trex.get_rect(topleft = (trex_x , trex_y))
    cacto_rect = cacto_img.get_rect(topleft = (cacto_x, cacto_y))
    if trex_rect.collidedict(cacto_rect):
        tela.fill('yellow')

        tela.blit(chao,(chao_x, 340))
        tela.blit(chao,(chao_x + 800,340))
        tela.blit(trex, (trex_x , trex_y))
        tela.blit(cacto_img1, (cacto_x, cacto_y))
        
        # pontuação

        texto = font.render('pontuação: ' + str(score), True,(0,0,0))
        tela.blit(texto2, (250, 200))
        pygame.display.update()
        clock.tyck(30)
    