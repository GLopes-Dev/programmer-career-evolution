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


#To run this exercise, download any .mp3 file and place it in the root folder, rename it to 'music.mp3' or change "os.system('start music.mp3')" the music.mp3 line with the .mp3 name
# and run the code.

#Changelog (2026-05-17) - Installed Python (3.12) and modified this code to run using PYGAME.