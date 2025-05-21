# Exercício Python 21: Faça um programa em Python que abre e reproduza o áudio de um arquivo MP3
import pygame
import os

pygame.init()
#pygame.mixer.music.load('C:/Users/barel/OneDrive/Área de Trabalho/CURSOS/CursoEmVideo/PYTHON/PhytonExercicios/PythonExercicios/PythonExercicios/ex021.mp3')
pygame.mixer.music.play()
input("Pressione Enter para parar...")
pygame.mixer.music.stop()

