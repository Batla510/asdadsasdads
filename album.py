import random
class MusicAlbum:
    def __init__(self,title,artist,release_year,genre,tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist
    def info(self):
        print('Название: ', self.title)
        print('Исполнитель: ', self.artist)
        print('Год: ', self.release_year)
        print('Жанр: ', self.genre)
        print('Треки', self.tracklist)
    def play_random_track(self):
        return random.choice(self.tracklist)
ma = MusicAlbum('Album',"Artist",2020,"genre1",['first','second','third','fourth'])
ma.info()
print(ma.play_random_track())