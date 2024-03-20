#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys  # Importa o módulo 'sys' para manipulação do sistema

import pygame as pygame  # Importa a biblioteca Pygame com o alias 'pygame'

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION  # Importa constantes específicas do jogo
from code.Level import Level  # Importa a classe Level do jogo
from code.Menu import Menu  # Importa a classe Menu do jogo


class Game:
    def __init__(self):
        pygame.init()  # Inicializa o pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Cria uma janela de exibição

    def run(self):
        while True:
            menu = Menu(self.window)  # Cria uma instância da classe Menu
            menu_return = menu.run()  # Executa o menu e recebe o retorno

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:  # Verifica se a opção do menu é válida
                level = Level(self.window, 'Level1', menu_return)  # Cria uma instância da classe Level
                level_return = level.run()  # Executa o nível e recebe o retorno
            else:
                pygame.quit()  # Fecha o pygame
                sys.exit()  # Encerra o programa

# Importações de bibliotecas e módulos:
# import sys: Importa o módulo sys, que fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador e
# interação com o ambiente Python.
# import pygame: Importa a biblioteca Pygame, que é usada para criar jogos em Python.
# from pygame import Surface, Rect: Importa as classes Surface e Rect do Pygame, que são usadas para representar
# superfícies e retângulos, respectivamente.
# from pygame.font import Font: Importa a classe Font do Pygame, que é usada para manipular fontes de texto.

# Importações locais personalizadas:
# from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION: Importa constantes específicas do jogo localizadas no
# módulo Const.
# from code.Level import Level: Importa a classe Level do jogo localizada no módulo Level.
# from code.Menu import Menu: Importa a classe Menu do jogo localizada no módulo Menu.

# Classe Game:
# Define uma classe chamada Game.
# No método __init__, inicializa o Pygame com pygame.init() e cria uma janela de exibição com o tamanho especificado
# pelas constantes WIN_WIDTH e WIN_HEIGHT.
# No método run, inicia um loop principal do jogo.
# Dentro do loop:
# Cria uma instância da classe Menu, que é responsável por exibir o menu do jogo.
# Executa o menu e armazena o retorno.
# Verifica se a escolha do menu é uma das opções válidas.
# Se for uma opção válida, cria uma instância da classe Level, passando o nome do nível ('Level1') e a opção do menu
# como parâmetros.
# Executa o nível.
# Se a escolha do menu não for válida, encerra o jogo usando pygame.quit() e sys.exit().

# Uso das constantes e classes importadas:
# As constantes WIN_WIDTH, WIN_HEIGHT e MENU_OPTION são utilizadas para configurar o tamanho da janela e as opções
# do menu.
# As classes Level e Menu são instanciadas e utilizadas dentro do loop principal para exibir o menu e os níveis do jogo.
