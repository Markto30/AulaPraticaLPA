#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame
from pygame import Surface, SurfaceType, Rect
from pygame.rect import RectType


class Entity(ABC):
    rect: Rect | RectType
    surf: Surface | SurfaceType

#
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf: Surface = pygame.image.load('./asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass

