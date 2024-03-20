#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED  # Importa constantes específicas de outros arquivos
from code.Entity import Entity  # Importa a classe Entity do arquivo Entity.py


class Background(Entity):  # Define uma classe Background que herda da classe Entity
    def __init__(self, name: str, position=(0, 0)):
        super().__init__(name, position)  # Chama o construtor da classe Entity com o nome e posição fornecidos

    def move(self):  # Define um método move para mover o fundo
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Move o fundo para a esquerda de acordo com a velocidade
        # definida no dicionário ENTITY_SPEED
        if self.rect.right <= 0:  # Se o lado direito do fundo estiver fora da tela
            self.rect.left = WIN_WIDTH  # Define o lado esquerdo do fundo para que ele reapareça do lado direito da
            # janela

# Importações de Módulos e Constantes:
# from code.Const import WIN_WIDTH, ENTITY_SPEED: Esta linha importa constantes específicas do jogo a partir do módulo
# Const. Isso inclui a largura da janela (WIN_WIDTH) e um dicionário de velocidades de entidades (ENTITY_SPEED), onde
# o nome da entidade é mapeado para sua velocidade.

# Importação da Classe Entity:
# from code.Entity import Entity: Aqui, estamos importando a classe Entity do arquivo Entity.py. Essa classe
# provavelmente define os comportamentos e propriedades básicas de todas as entidades do jogo.

# Definição da Classe Background:
# class Background(Entity): Define a classe Background, que herda da classe Entity. Isso significa que a classe
# Background possui todos os métodos e atributos da classe Entity, além dos próprios que serão definidos aqui.

# Método __init__:
# def __init__(self, name: str, position=(0, 0)):: Define o método de inicialização da classe Background. Ele recebe
# um parâmetro name que representa o nome da entidade e um parâmetro opcional position que representa a posição inicial
# da entidade (por padrão, a posição é (0, 0)).
# super().__init__(name, position): Chama o método __init__ da classe pai (Entity). Isso inicializa a entidade com o
# nome e a posição fornecidos.

# Método move:
# def move(self): Define o método move da classe Background. Este método é responsável por mover o fundo durante o jogo.
# self.rect.centerx -= ENTITY_SPEED[self.name]: Move o fundo para a esquerda subtraindo sua velocidade do eixo x.
# A velocidade é determinada pelo dicionário ENTITY_SPEED, onde a chave é o nome da entidade.
# if self.rect.right <= 0: Verifica se o lado direito do fundo está fora da tela.
# self.rect.left = WIN_WIDTH: Se o lado direito do fundo estiver fora da tela, reposiciona o fundo para a direita da
# janela, permitindo um movimento contínuo do fundo.
# Em resumo, este código define uma classe Background que herda da classe Entity e é responsável por gerenciar o
# movimento do fundo do jogo. Ele utiliza constantes definidas em Const.py para determinar a largura da janela e a
# velocidade de movimento do fundo. O método move desloca o fundo para a esquerda e, se o fundo sair completamente da
# tela, o reposiciona para o lado direito, criando um efeito de deslocamento contínuo do fundo.
