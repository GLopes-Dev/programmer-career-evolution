#Challenge 021 - Create a program in Python that opens and plays the audio from a MP3 file.

import pygame
pygame.init()

print('=' * 10, '[Challenge 021]', '=' * 10)
print('Playing your PEAK audio.')
pygame.mixer.music.load('exercise021.mp3')
pygame.mixer.music.play()
input('Press ENTER to stop...')
print('=' * 30)


#Didn't use playsound or pygame library because it's not compatible with my Python Version (3.14.5)



#Changelog (2026-05-17) - Installed Python (3.12) and modified this code to run using PYGAME.