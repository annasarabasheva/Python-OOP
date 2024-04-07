from Spoopify.song import Song


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.args = args
        self.published = False
        self.songs = []
        for arg in self.args:
            self.songs.append(arg)

    def add_song(self, song: Song):
        if song in self.songs:
            return "Song is already in the album."

        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        for song in self.songs.copy():
            if song.name == song_name:
                if not self.published:
                    self.songs.remove(song)
                    return f"Removed song {song_name} from album {self.name}."
                else:
                    return "Cannot remove songs. Album is published."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"

        return result






