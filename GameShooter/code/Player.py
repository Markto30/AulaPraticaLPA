#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame  # Importa o módulo pygame para lidar com entradas de teclado e outros recursos gráficos

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, \
    PLAYER_KEY_DOWN  # Importa constantes específicas do jogo relacionadas à velocidade, dimensões da janela e
# teclas de controle do jogador
from code.Entity import Entity  # Importa a classe Entity do arquivo Entity.py, que provavelmente define


# comportamentos básicos compartilhados por todas as entidades do jogo
class Player(Entity):  # Define a classe Player, que é uma subclasse de Entity
    def __init__(self, name: str, position: tuple):  # Define o construtor da classe Player
        super().__init__(name, position)  # Chama o construtor da classe pai (Entity) com o nome e a posição fornecidos

    def move(self):  # Define o método move, responsável por movimentar o jogador
        pressed_key = pygame.key.get_pressed()  # Obtém o estado atual de todas as teclas do teclado

        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:  # Verifica se a tecla de movimento para cima
            # está pressionada e se o jogador não ultrapassou o limite superior da janela
            self.rect.centery -= ENTITY_SPEED[self.name]  # Move o jogador para cima

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:  # Verifica se a tecla de
            # movimento para baixo está pressionada e se o jogador não ultrapassou o limite inferior da janela
            self.rect.centery += ENTITY_SPEED[self.name]  # Move o jogador para baixo

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:  # Verifica se a tecla de
            # movimento para a direita está pressionada e se o jogador não ultrapassou o limite direito da janela
            self.rect.centerx += ENTITY_SPEED[self.name]  # Move o jogador para a direita

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # Verifica se a tecla de movimento
            # para a esquerda está pressionada e se o jogador não ultrapassou o limite esquerdo da janela
            self.rect.centerx -= ENTITY_SPEED[self.name]  # Move o jogador para a esquerda

# Importação de Módulos e Constantes:
# import pygame: importa o módulo pygame, necessário para lidar com entradas de teclado.

# Importação de Constantes e Classes:
# From code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT,
# PLAYER_KEY_DOWN: Importa constantes relacionadas à velocidade das entidades, às dimensões da janela e às teclas
# de controle do jogador. Essas constantes são usadas posteriormente para definir o comportamento do jogador.
# From code.Entity import Entity: Importa a classe Entity do módulo Entity. Essa classe provavelmente define
# comportamentos básicos compartilhados por todas as entidades do jogo.

# Definição da Classe Player:
# class Player(Entity):: Define a classe Player como uma subclasse da classe Entity. Isso significa que Player herda
# todos os atributos e métodos de Entity.

# Método __init__:
# def __init__(self, name: str, position: tuple):: Define o construtor da classe Player, que recebe um nome e uma
# posição inicial como argumentos.
# super().__init__(name, position): Chama o construtor da classe pai (Entity) com os argumentos name e position.
# Isso inicializa a instância de Player com um nome e uma posição.

# Método move:
# def move(self):: Define o método move da classe Player, que é responsável por movimentar o jogador de acordo com
# as teclas pressionadas.
# pressed_key = pygame.key.get_pressed(): Obtém o estado atual de todas as teclas do teclado.
# Usa as constantes PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT para determinar as teclas de
# controle do jogador com base no nome do jogador.
# Verifica se uma determinada tecla está pressionada e se o jogador não atingiu as bordas da janela, então move o
# jogador na direção correspondente, com base na velocidade definida em ENTITY_SPEED.
# Em resumo, este código define a classe Player, que herda da classe Entity, e implementa a lógica para movimentar
# o jogador de acordo com as teclas pressionadas pelo usuário.
