class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}' ({self.genre}) is ready!")

    # STEP 2 - Add a song to the playlist
    def add_song(self, song, singer, lyricist, lyrics):
        song_details = {
            "song": song,
            "singer": singer,
            "lyricist": lyricist,
            "lyrics": lyrics
        }
        self.songs.append(song_details)
        print(f"'{song}' added to {self.name}.")

    # STEP 3 - Remove a song from the playlist
    def remove_song(self, song):
        for item in self.songs:
            if item["song"].lower() == song.lower():
                self.songs.remove(item)
                print(f"'{song}' removed.")
                return
        print(f"'{song}' not found in playlist.")

    # STEP 4 - Display all songs
    def display(self):
        print(f"\n--- {self.name} ({self.genre}) ---")

        if self.songs:
            for i, item in enumerate(self.songs, 1):
                print(f"\n{i}. Song: {item['song']}")
                print(f"   Singer: {item['singer']}")
                print(f"   Lyricist: {item['lyricist']}")
                print(f"   Lyrics: {item['lyrics']}")
        else:
            print("No songs yet. Add some!")

    # STEP 5 - Destructor
    def _del_(self):
        print(f"Playlist '{self.name}' has been deleted. Goodbye!")


# Object creation
my_playlist = Playlist("Road Trip Mix", "Pop")

# STEP 6 - Menu-driven program
while True:
    print("1. Add Song  2. Remove Song  3. View Playlist  4. Delete & Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        song = input("Enter song name: ")
        singer = input("Enter singer's name: ")
        lyricist = input("Enter lyricist's name: ")
        lyrics = input("Enter a short lyrics note: ")
        my_playlist.add_song(song, singer, lyricist, lyrics)

    elif choice == "2":
        song = input("Enter song to remove: ")
        my_playlist.remove_song(song)

    elif choice == "3":
        my_playlist.display()

    elif choice == "4":
        del my_playlist
        break

    else:
        print("Invalid choice. Enter 1, 2, 3, or 4.")