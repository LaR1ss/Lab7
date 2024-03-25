import pygame
import os
pygame.init()
window = pygame.display.set_mode((300, 200))
pygame.display.set_caption('Music Player')
music_dir = 'C:/Users/Алексей/Music/'
songs = [file for file in os.listdir(music_dir) if file.endswith('.mp3')]
current_song_index = 0
def play_music(song_index):
    pygame.mixer.music.load(os.path.join(music_dir, songs[song_index]))
    pygame.mixer.music.play()
play_music(current_song_index)
playing = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(songs)
                play_music(current_song_index)
            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % len(songs)
                play_music(current_song_index)

    pygame.display.update()
