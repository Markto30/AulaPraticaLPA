#!/usr/bin/python
# -*- coding: utf-8 -*-
# Importação de Módulos e Classes
import random  # Importa o módulo random para escolha aleatória de inimigos
import sys  # Importa o módulo sys para finalizar o jogo corretamente
import pygame.display  # Importa o módulo pygame.display para controle da janela
from pygame import Surface, Rect  # Importa classes Surface e Rect do módulo pygame para manipulação de gráficos
from pygame.font import Font  # Importa a classe Font do módulo pygame.font para renderização de texto
from code.Const import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY  # Importa constantes específicas do jogo
from code.Entity import Entity  # Importa a classe Entity do arquivo Entity.py
from code.EntityFactory import EntityFactory  # Importa a classe EntityFactory do arquivo EntityFactory.py


# Definição da Classe Level
class Level:
    def __init__(self, window, name, menu_option):
        # Inicialização dos atributos da classe
        self.window: Surface = window  # Define a janela do jogo como uma superfície
        self.name = name  # Define o nome do nível
        self.mode = menu_option  # Define o modo de jogo (por exemplo, jogador único ou multiplayer)
        self.entity_list: list[Entity] = []  # Inicializa uma lista vazia para armazenar entidades do jogo
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))  # Adiciona entidades de fundo à lista
        self.entity_list.append(EntityFactory.get_entity('Player1'))  # Adiciona o jogador 1 à lista de entidades
        # Se o modo de jogo for multiplayer, adiciona o jogador 2 à lista de entidades
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        # Configura um temporizador para gerar inimigos periodicamente
        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self):
        # Carrega e reproduz a música de fundo do nível
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)  # Reproduz a música em loop
        clock = pygame.time.Clock()  # Cria um objeto Clock para controlar a taxa de quadros

        # Loop principal do jogo
        while True:
            clock.tick(80)  # Limita o número de quadros por segundo
            for ent in self.entity_list:
                # Renderiza cada entidade na janela do jogo e move-as
                self.window.blit(source=ent.surf, dest=ent.rect)
                self.level_text(14, f'fps: {clock.get_fps():.1f}', COLOR_WHITE,
                                (5, 5))  # Exibe a contagem de FPS na tela
                ent.move()  # Move a entidade

            # Verifica eventos de entrada do usuário e eventos do temporizador
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Se o evento for o fechamento da janela
                    pygame.quit()  # Encerra a pygame
                    sys.exit()  # Finaliza o programa
                if event.type == EVENT_ENEMY:  # Se o evento for a geração de inimigos
                    # Escolhe aleatoriamente entre os tipos de inimigos disponíveis e os adiciona à lista de entidades
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            pygame.display.flip()  # Atualiza a exibição da tela

    # Método para renderizar texto na tela
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        # Cria uma fonte com o tamanho especificado
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size=text_size)
        # Renderiza o texto na superfície com a cor especificada
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        # Define a posição do texto na tela
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        # Desenha o texto na janela do jogo
        self.window.blit(source=text_surf, dest=text_rect)

# Importação de Módulos e Classes:
# import random: Importa o módulo random, que será usado para escolher aleatoriamente entre diferentes tipos
# de entidades.
# import sys: Importa o módulo sys, que será usado para sair do jogo corretamente quando necessário.
# import pygame.display: Importa o módulo pygame.display, que é usado para controlar a janela de exibição.
# From pygame import Surface, Rect: Importa as classes Surface e Rect do módulo pygame, que serão usadas
# para trabalhar com superfícies gráficas e retângulos.
# From pygame.font import Font: Importa a classe Font do módulo pygame.font, que será usada para renderizar
# texto na tela.
# From code.Const import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY: Importa constantes específicas do jogo,
# como cor branca, opções do menu e o evento de inimigo.
# From code.Entity import Entity: Importa a classe Entity do módulo Entity, que provavelmente define
# comportamentos básicos para todas as entidades do jogo.
# From code.EntityFactory import EntityFactory: Importa a classe EntityFactory do módulo EntityFactory,
# usada para criar entidades do jogo de forma dinâmica.

# Definição da Classe Level:
# class Level: Define a classe Level, que representa um nível do jogo.
# def __init__(self, window, name, menu_option):: Define o construtor da classe Level, que recebe a janela do jogo,
# o nome do nível e a opção de menu como argumentos.
# self.window: Surface = window: Inicializa a janela do jogo como uma superfície.
# self.name = name: Define o nome do nível.
# self.mode = menu_option: Define o modo de jogo (por exemplo, modo de jogador único ou multiplayer).
# self.entity_list: list[Entity] = []: Inicializa uma lista de entidades do jogo.
# self.entity_list.extend(EntityFactory.get_entity('Level1bg')): Adiciona entidades de fundo à lista de entidades.
# self.entity_list.append(EntityFactory.get_entity('Player1')): Adiciona o jogador 1 à lista de entidades.
# if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]: Verifica se o modo de jogo é multiplayer e, se for,
# adiciona o jogador 2 à lista de entidades.
# pygame.time.set_timer(EVENT_ENEMY, 4000): Configura um temporizador para gerar inimigos periodicamente.

# Método run:
# def run(self): Define o método run, responsável por executar o nível.
# Carrega e reproduz a música de fundo do nível.
# Inicia um loop principal do jogo.
# Dentro do loop, atualiza a exibição do jogo, movimenta todas as entidades do jogo, verifica eventos do teclado
# e do temporizador e atualiza a exibição da janela.

# Método level_text:
# def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple): Define o método level_text,
# responsável por renderizar texto na tela.
# Usa uma fonte definida anteriormente para renderizar o texto com o tamanho, a cor e a posição especificados.
# Desenha o texto na janela do jogo.
# Em resumo, a classe Level é responsável por gerenciar a execução de um nível do jogo. Ele cria e controla entidades,
# como jogadores e inimigos, renderiza o fundo e o texto na tela e responde a eventos do teclado e do temporizador.
