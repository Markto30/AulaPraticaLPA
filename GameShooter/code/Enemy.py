#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importações de Módulos e Classes
from code.Entity import Entity  # Importa a classe Entity do módulo Entity no diretório code
from code.Const import ENTITY_SPEED, \
    WIN_WIDTH  # Importa constantes específicas do jogo relacionadas à velocidade das entidades e à largura da janela


# Definição da Classe Enemy
class Enemy(Entity):  # Define a classe Enemy, que é uma subclasse de Entity
    def __init__(self, name: str, position: tuple):  # Define o construtor da classe Enemy
        super().__init__(name, position)  # Chama o construtor da classe pai (Entity) com o nome e a posição fornecidos

    def move(self):  # Define o método move, responsável por movimentar o inimigo
        self.rect.centerx -= ENTITY_SPEED[
            self.name]  # Move o inimigo para a esquerda subtraindo sua velocidade do eixo x
        if self.rect.right <= 0:  # Verifica se o lado direito do inimigo está fora da tela
            self.rect.left = WIN_WIDTH  # Reposiciona o inimigo para o lado direito da janela

# Importações de Módulos e Classes:
# from code.Entity import Entity: Importa a classe Entity do módulo Entity localizado no diretório code. Isso sugere
# que a classe Enemy está relacionada às entidades do jogo e provavelmente compartilha comportamentos comuns definidos
# na classe Entity.
# from code.Const import ENTITY_SPEED, WIN_WIDTH: Importa as constantes ENTITY_SPEED e WIN_WIDTH do módulo Const
# localizado no diretório code. Isso sugere que a classe Enemy usará a velocidade definida para as entidades e a
# largura da janela.

# Definição da Classe Enemy:
# class Enemy(Entity):: Define a classe Enemy, que herda da classe Entity. Isso significa que Enemy possui todos os
# atributos e métodos da classe Entity.

# Método __init__:
# def __init__(self, name: str, position: tuple):: Define o método __init__, o construtor da classe Enemy, que recebe
# um nome e uma posição inicial como argumentos.
# super().__init__(name, position): Chama o construtor da classe pai (Entity) com os argumentos name e position. Isso
# inicializa a instância de Enemy com um nome e uma posição.

# Método move:
# def move(self):: Define o método move, responsável por mover o inimigo.
# self.rect.centerx -= ENTITY_SPEED[self.name]: Move o inimigo para a esquerda subtraindo sua velocidade do eixo x.
# A velocidade é determinada pela constante ENTITY_SPEED associada ao nome do inimigo.
# if self.rect.right <= 0:: Verifica se o lado direito do inimigo está fora da tela.
# self.rect.left = WIN_WIDTH: Se o lado direito do inimigo estiver fora da tela, reposiciona o inimigo para a direita
# da janela, permitindo um movimento contínuo do inimigo.
# Em resumo, a classe Enemy é uma subclasse de Entity que representa um inimigo no jogo. Ela herda comportamentos
# básicos de entidade e implementa sua própria lógica de movimento específica para inimigos. O inimigo se move para
# a esquerda e, quando sai completamente da tela, é reposicionado para o lado direito da janela.
