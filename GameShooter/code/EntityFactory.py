#!/usr/bin/python
# -*- coding: utf-8 -*-
import random  # Importa o módulo random para geração de números aleatórios

from code.Background import Background  # Importa a classe Background do arquivo Background.py
from code.Const import WIN_WIDTH, WIN_HEIGHT  # Importa constantes de largura e altura da janela
from code.Enemy import Enemy  # Importa a classe Enemy do arquivo Enemy.py
from code.Player import Player  # Importa a classe Player do arquivo Player.py


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            # DEFININDO BACKGROUND.
            case 'Level1bg':
                list_bg = []  # Cria uma lista vazia para armazenar instâncias de Background
                for i in range(7):
                    list_bg.append(Background(f'Level1bg{i}', (
                        0, 0)))  # Adiciona instâncias de Background à lista com diferentes posições iniciais
                    list_bg.append(Background(f'Level1bg{i}', (
                        WIN_WIDTH, 0)))  # Adiciona instâncias de Background à lista com diferentes posições iniciais
                return list_bg  # Retorna a lista completa de instâncias de Background

            # DEFININDO PLAYER1.
            case 'Player1':
                return Player('Player1', (
                    10,
                    WIN_HEIGHT / 2 - 30))  # Retorna uma instância de Player com o nome 'Player1' e uma posição inicial

            # DEFININDO PLAYER2.
            case 'Player2':
                return Player('Player2', (
                    10,
                    WIN_HEIGHT / 2 + 30))  # Retorna uma instância de Player com o nome 'Player2' e uma posição inicial

            # DEFININDO ENEMY1.
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(0 + 40,
                                                                       WIN_HEIGHT - 40)))  # Retorna uma instância de
                # Enemy com o nome 'Enemy1' e uma posição inicial aleatória

            # DEFININDO ENEMY2.
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(0 + 40,
                                                                       WIN_HEIGHT - 40)))  # Retorna uma instância de
                # Enemy com o nome 'Enemy2' e uma posição inicial aleatória

# Importação de Módulos e Classes:
# import random: importa o módulo random, que será usado para gerar números aleatórios.
# From code.Background import Background: Importa a classe Background do arquivo Background.py. Esta classe
# provavelmente define objetos que representam o fundo do jogo.
# From code.Const import WIN_WIDTH, WIN_HEIGHT: Importa as constantes WIN_WIDTH e WIN_HEIGHT do arquivo Const.py.
# Essas constantes representam a largura e altura da janela do jogo.
# From code.Enemy import Enemy: Importa a classe Enemy do arquivo Enemy.py. Esta classe provavelmente define
# objetos que representam inimigos do jogo.
# From code.Player import Player: Importa a classe Player do arquivo Player.py. Esta classe provavelmente define
# objetos que representam os jogadores do jogo.

# Definição da Classe EntityFactory:
# class EntityFactory: Define a classe EntityFactory, responsável por criar instâncias de diferentes
# tipos de entidades do jogo.

# Método Estático get_entity():
# @staticmethod: Indica que o método get_entity() é estático, ou seja, pode ser chamado diretamente da classe sem a
# necessidade de criar uma instância dela.
# def get_entity(entity_name: str, position=(0, 0)):: Define o método get_entity(), que recebe o nome da entidade
# desejada e uma posição opcional como argumentos.
# match entity_name: Inicia uma estrutura de correspondência de padrões com base no valor de entity_name.

# Padrões para Criação de Entidades:
# 'Level1bg': Se entity_name for 'Level1bg', cria-se uma lista contendo várias instâncias de Background para simular
# um efeito de paralaxe no fundo do jogo. Isso é feito duplicando o fundo várias vezes e posicionando-o em diferentes
# locais na tela.
# 'Player1' e 'Player2': Se entity_name for 'Player1' ou 'Player2', retorna uma instância de Player com uma posição
# inicial específica. Isso provavelmente define a posição inicial dos jogadores no jogo.
# 'Enemy1' e 'Enemy2': Se entity_name for 'Enemy1' ou 'Enemy2', retorna uma instância de Enemy com uma posição inicial
# aleatória. Isso provavelmente define a posição inicial dos inimigos no jogo, garantindo que eles apareçam em
# diferentes locais na tela.
# Em resumo, a classe EntityFactory fornece um método conveniente para criar diferentes tipos de entidades do jogo
# com base em seus nomes. Isso facilita a criação dinâmica de entidades durante a execução do jogo, permitindo
# uma maior flexibilidade e modularidade na construção do jogo.
