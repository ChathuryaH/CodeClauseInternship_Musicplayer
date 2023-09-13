import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")

        self.playlist = []
        self.current_song_index = 0

        pygame.mixer.init()

        self.create_ui()

    def create_ui(self):
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.add_button = tk.Button(self.root, text="Add Music", command=self.add_music)
        self.next_button = tk.Button(self.root, text="Next", command=self.next_song)

        self.play_button.pack(fill="x")
        self.pause_button.pack(fill="x")
        self.stop_button.pack(fill="x")
        self.add_button.pack(fill="x")
        self.next_button.pack(fill="x")

    def add_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            self.playlist.append(file_path)

    def play_music(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_song_index])
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_song(self):
        if self.playlist:
            self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
            self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
