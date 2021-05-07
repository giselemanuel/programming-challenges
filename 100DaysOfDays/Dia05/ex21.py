"""
Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""
import pygame
print('-' * 40)
print(f'{"Toca mp3":^40}')
print('-' * 40)

pygame.init()
pygame.mixer.music.load("ex20.mp3")
pygame.mixer.music.play()
pygame.event.wait()