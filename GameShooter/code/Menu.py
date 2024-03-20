#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys  # Importa o módulo 'sys' para manipulação do sistema

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, \
    COLOR_YELLOW  # Importa constantes e cores do jogo


class Menu:
    def __init__(self, window):
        self.window: Surface = window  # Define a janela de exibição para o menu
        self.surf = pygame.image.load('./asset/MenuBG.png').convert_alpha()  # Carrega a imagem de fundo do menu
        self.rect = self.surf.get_rect(left=0, top=0)  # Obtém o retângulo que envolve a imagem de fundo

    def run(self):
        pygame.mixer_music.load('./asset/SoundMenuBG.mp3')  # Carrega a música de fundo do menu
        pygame.mixer_music.play(-1)  # Reproduz a música de fundo em loop
        menu_option = 0  # Inicializa a opção do menu selecionada como 0
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Desenha a imagem de fundo do menu na janela
            self.menu_text(50, "Shooter RPG", COLOR_ORANGE,
                           ((WIN_WIDTH / 2), 70))  # Adiciona texto "Shooter RPG" ao menu
            self.menu_text(30, "Multiplayer", COLOR_ORANGE,
                           ((WIN_WIDTH / 2), 110))  # Adiciona texto "Multiplayer" ao menu
            for i in range(len(MENU_OPTION)):  # Itera sobre as opções do menu
                if i == menu_option:  # Se esta é a opção do menu atualmente selecionada
                    self.menu_text(18, MENU_OPTION[i], COLOR_YELLOW,
                                   ((WIN_WIDTH / 2), 200 + 30 * i))  # Adiciona texto destacado para
                    # esta opção
                else:
                    self.menu_text(18, MENU_OPTION[i], COLOR_WHITE,
                                   ((WIN_WIDTH / 2), 200 + 30 * i))  # Adiciona texto normal para as
                    # outras opções
            pygame.display.flip()  # Atualiza a janela

            # Verificação de eventos:
            for event in pygame.event.get():  # Itera sobre os eventos na fila de eventos
                if event.type == pygame.QUIT:  # Se o evento for o fechamento da janela
                    pygame.quit()  # Encerra o Pygame
                    sys.exit()  # Sai do programa
                if event.type == pygame.KEYDOWN:  # Se uma tecla foi pressionada
                    if event.key == pygame.K_DOWN:  # Se a tecla para baixo foi pressionada
                        if menu_option <= len(MENU_OPTION) - 1:  # Se a opção do menu atual não é a última
                            menu_option += 1  # Avança para a próxima opção do menu
                        else:
                            menu_option = 0  # Volta para a primeira opção do menu
                    if event.key == pygame.K_UP:  # Se a tecla para cima foi pressionada
                        if menu_option >= 0:  # Se a opção do menu atual não é a primeira
                            menu_option -= 1  # Retrocede para a opção do menu anterior
                        else:
                            menu_option = len(MENU_OPTION) - 1  # Vai para a última opção do menu
                    if event.key == pygame.K_RETURN:  # Se a tecla Enter foi pressionada
                        return MENU_OPTION[menu_option]  # Retorna a opção do menu selecionada

    # Função para adicionar texto ao menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size=text_size)  # Define a fonte do texto
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # Renderiza o texto na
        # superfície
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)  # Obtém o retângulo envolvendo o texto
        self.window.blit(source=text_surf, dest=text_rect)  # Desenha o texto na janela

# Importações de Bibliotecas e Módulos:
# import sys: Importa o módulo 'sys', que é utilizado para interação com o sistema e encerramento do programa.
# import pygame.image: Importa o módulo image da biblioteca Pygame, que é usado para carregar imagens.
# From pygame import Surface, Rect: Importa as classes Surface e Rect da biblioteca Pygame, que são usadas para
# manipulação de superfícies e retângulos, respectivamente.
# From pygame.font import Font: Importa a classe Font da biblioteca Pygame, que é usada para renderizar texto na tela.

# Importações Locais Personalizadas:
# from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW: Importa constantes
# específicas do jogo do módulo Const, como a largura da janela, cores e opções de menu.

# Definição da Classe Menu:
# A classe Menu é responsável por exibir e interagir com o menu do jogo.
# No método __init__, a janela do menu é configurada, a imagem de fundo do menu é carregada e o retângulo que
# envolve essa imagem é obtido.
# O método run() controla a lógica do menu:
# Carrega e reproduz a música de fundo do menu.
# Exibe a imagem de fundo do menu e renderiza o texto das opções do menu.
# Responde aos eventos do teclado, permitindo ao jogador navegar pelas opções do menu usando as teclas de seta
# para cima e para baixo.
# Quando o jogador pressiona Enter, a opção selecionada é retornada.
# O método menu_text() é responsável por renderizar o texto na tela, utilizando a fonte e as cores especificadas.
