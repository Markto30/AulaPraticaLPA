import pygame  # Importa a biblioteca Pygame

# Constantes de cores
COLOR_ORANGE = (255, 128, 0)  # Define a cor laranja como (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)  # Define a cor amarela como (255, 255, 128)
COLOR_WHITE = (255, 255, 255)  # Define a cor branca como (255, 255, 255)

# Constantes para o menu de opções
MENU_OPTION = ('NEW GAME 1P',  # Define as opções do menu como tupla
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')

# Constantes para o tamanho da janela
WIN_WIDTH = 576  # Largura da janela
WIN_HEIGHT = 324  # Altura da janela

# Constante para evento de inimigos
EVENT_ENEMY = pygame.USEREVENT + 1  # Define um evento de usuário para inimigos

# Constante para velocidade de entidades
ENTITY_SPEED = {'Level1bg0': 0,  # Dicionário de velocidades para diferentes entidades
                'Level1bg1': 1,
                'Level1bg2': 2,
                'Level1bg3': 3,
                'Level1bg4': 4,
                'Level1bg5': 5,
                'Level1bg6': 6,
                'Player1': 3,
                'Player2': 3,
                'Enemy1': 2,
                'Enemy2': 1,
                }

# Constantes para as teclas de movimento dos jogadores
PLAYER_KEY_UP = {'Player1': pygame.K_UP,  # Dicionário de teclas de movimento para cima
                 'Player2': pygame.K_w}

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,  # Dicionário de teclas de movimento para a esquerda
                   'Player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,  # Dicionário de teclas de movimento para a direita
                    'Player2': pygame.K_d}

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,  # Dicionário de teclas de movimento para baixo
                   'Player2': pygame.K_s}

# Importação do módulo Pygame:
# import pygame: Importa a biblioteca Pygame, que é usada para criar jogos em Python.

# Constantes de Cores:
# COLOR_ORANGE, COLOR_YELLOW, COLOR_WHITE: Definem constantes para cores RGB laranja, amarela e branca, respectivamente.
# Essas cores podem ser usadas em elementos gráficos do jogo.

# Constante para o Menu de Opções:
# MENU_OPTION: Define uma tupla de opções de menu para o jogo. Isso pode ser usado para exibir opções de jogo para o
# jogador, como iniciar um novo jogo ou sair do jogo.

# Constantes para o Tamanho da Janela:
# WIN_WIDTH, WIN_HEIGHT: Definem constantes para a largura e altura da janela do jogo, respectivamente. Isso determina
# o tamanho da área onde o jogo será exibido na tela.

# Constante para o Evento de Inimigos:
# EVENT_ENEMY: Define um evento personalizado para inimigos. Isso pode ser usado para controlar o comportamento dos
# inimigos em diferentes partes do jogo.

# Constante para Velocidade de Entidades:
# ENTITY_SPEED: Define um dicionário que mapeia diferentes entidades do jogo para suas velocidades correspondentes.
# Isso pode ser útil para controlar a movimentação de personagens, inimigos ou outros elementos do jogo.

# Constantes para as Teclas de Movimento dos Jogadores:
# PLAYER_KEY_UP, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_DOWN: São dicionários que mapeiam os jogadores para as
# teclas de movimento associadas (por exemplo, para cima, esquerda, direita, baixo). Isso é usado para detectar e
# responder aos comandos de movimento dos jogadores durante o jogo.
# Essas constantes fornecem valores fixos que podem ser referenciados em várias partes do código do jogo. Isso torna o
# código mais legível, facilita a manutenção e permite ajustes rápidos e consistentes em elementos do jogo, como cores,
# tamanhos e comportamentos.
