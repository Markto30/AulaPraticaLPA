# CONSTANTE PARA COR.
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)

# MENU DE OPÇÕES.

MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')

# CONSTANTES COM PARA O TAMANHO DA JANELA.
WIN_WIDTH = 576
WIN_HEIGHT = 324

# VARIÁVEL IMAGEM LEVEL.
# IMAGE_LEVEL = {'Level1bg': 7}

EVENT_ENEMY = pygame.USEREVENT + 1

# VARIÁVEL PARA VELOCIDADE.
ENTITY_SPEED = {'Level1bg0': 0,
                'Level1bg1': 1,
                'Level1bg2': 2,
                'Level1bg3': 3,
                'Level1bg4': 4,
                'Level1bg5': 5,
                'Level1bg6': 6,
                'Player1': 3,
                'Player1Shot': 4,
                'Player2': 3,
                'Player2Shot': 4,
                'Enemy1': 2,
                'Enemy1Shot': 7,
                'Enemy2': 1,
                'Enemy2Shot': 6}

# VARIÁVEL PARA VIDA.
ENTITY_HEALTH = {'Level1bg0': 999,
                 'Level1bg1': 999,
                 'Level1bg2': 999,
                 'Level1bg3': 999,
                 'Level1bg4': 999,
                 'Level1bg5': 999,
                 'Level1bg6': 999,
                 'Player1': 300,
                 'Player1Shot': 1,
                 'Player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 200,
                 'Enemy1Shot': 200,
                 'Enemy2': 200,
                 'Enemy2Shot': 200}

ENTITY_SHOT_DELAY = {'Player1': 5,
                     'Player2': 5,
                     'Enemy1': 50,
                     'Enemy2': 50}

PLAYER_KEY_UP = {'Player1': pygame.K_w,
                 'Player2': pygame.K_UP}

PLAYER_KEY_LEFT = {'Player1': pygame.K_a,
                   'Player2': pygame.K_LEFT}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_d,
                    'Player2': pygame.K_RIGHT}

PLAYER_KEY_DOWN = {'Player1': pygame.K_s,
                   'Player2': pygame.K_DOWN}

PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE,
                    'Player2': pygame.K_RALT}
