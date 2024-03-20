#!/usr/bin/python
# -*- coding: utf-8 -*-
# Importação de Módulos e Classes
from abc import ABC, abstractmethod  # Importa as classes ABC e abstractmethod do módulo abc para definição de
# classes abstratas e métodos abstratos

# Importação de Módulos e Classes
import pygame  # Importa o módulo pygame para manipulação de gráficos e eventos
from pygame import Surface, SurfaceType, Rect  # Importa as classes Surface, SurfaceType e Rect do módulo
# pygame para manipulação de gráficos e retângulos
from pygame.rect import RectType  # Importa o tipo de dados RectType do módulo pygame.rect para representar retângulos


class Entity(ABC):  # Define a classe Entity como uma subclasse de ABC (classe base para classes abstratas)
    rect: Rect | RectType  # Define um atributo rect para representar a área ocupada pela entidade
    surf: Surface | SurfaceType  # Define um atributo surf para representar a imagem da entidade

    def __init__(self, name: str, position: tuple):  # Define o construtor da classe Entity
        self.name = name  # Inicializa o atributo name com o nome fornecido
        # Carrega a imagem da entidade a partir do arquivo PNG correspondente e a converte
        # para uma superfície com transparência
        self.surf: Surface = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        # Obtém o retângulo delimitador da superfície e define sua posição inicial com
        # base na tupla de posição fornecida
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0  # Inicializa a velocidade da entidade como zero

    @abstractmethod  # Indica que o método move é abstrato e deve ser implementado pelas subclasses
    def move(self):  # Define o método abstrato move, responsável por movimentar a entidade
        pass  # A implementação do método move é deixada para as subclasses

# Importação de Módulos e Classes:
# from abc import ABC, abstractmethod: Importa as classes ABC e abstractmethod do módulo abc, que são usadas
# para definir classes abstratas e métodos abstratos, respectivamente.
# import pygame: Importa o módulo pygame, que será usado para carregar imagens e criar superfícies gráficas.

# Definição da Classe Entity:
# class Entity(ABC): Define a classe Entity como uma subclasse de ABC, que é a classe base para todas as classes
# abstratas em Python.
# rect: Rect | RectType: Define um atributo rect que pode ser do tipo Rect do módulo pygame.rect ou RectType do módulo
# pygame. Isso sugere que rect representa a área ocupada pela entidade no jogo.
# surf: Surface | SurfaceType: Define um atributo surf que pode ser do tipo Surface do módulo pygame ou SurfaceType do
# mesmo módulo. Isso sugere que surf representa a imagem da entidade.
# def __init__(self, name: str, position: tuple):: Define o construtor da classe Entity, que recebe um nome e uma
# posição inicial como argumentos.
# self.name = name: Inicializa o atributo name com o nome fornecido.
# self.surf: Surface = pygame.image.load('./asset/' + name + '.png').convert_alpha(): Carrega a imagem correspondente
# ao nome da entidade a partir de um arquivo PNG localizado no diretório asset e a converte para um objeto Surface
# com transparência.
# self.rect = self.surf.get_rect(left=position[0], top=position[1]): Obtém o retângulo delimitador da superfície e
# define sua posição inicial com base na tupla de posição fornecida.
# self.speed = 0: Inicializa a velocidade da entidade como zero.

# Método Abstrato move:
# @abstractmethod1: Define o decorador abstractmethod, indicando que o método move é abstrato e deve ser
# implementado pelas subclasses de Entity.
# def move(self):: Define o método abstrato move, responsável por movimentar a entidade. Este método
# deve ser implementado nas subclasses para fornecer o comportamento de movimento específico para cada tipo de entidade.
# Em resumo, a classe Entity serve como uma classe base para outras entidades do jogo. Ela define atributos
# comuns, como a imagem da entidade e sua posição, e um método abstrato move que deve ser implementado pelas
# subclasses para fornecer o comportamento de movimento específico para cada tipo de entidade.
