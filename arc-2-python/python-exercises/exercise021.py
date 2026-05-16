#Challenge 021 - Create a program in Python that opens and plays the audio from a MP3 file.

import os

print('=' * 10, '[Challenge 021]', '=' * 10)
print('Playing your victory theme audio...')
os.system('start music.mp3')
input('...')
print('=' * 30)


#Didn't use playsound or pygame library because it's not updated yet for my Python version (3.14.5)

#To run this exercise, download any .mp3 file and place it in the root folder, rename it to 'music.mp3' or change "os.system('start music.mp3')" the music.mp3 line with the .mp3 name
# and run the code.