def add(song, playlist):
    if song in playlist:
        print(f"{song} is already in the playlist")
    else:
        playlist.append(song)
        print(f"Added song: {song}")

def remove(song, playlist):
    if song in playlist:
        playlist.remove(song)
        print(f"Removed song: {song}")
    elif len(playlist) == 0:
        print(f"The playlist is empty")
    else:
        print(f"{song} is not in the playlist")

def play(playlist):
    if len(playlist) != 0:
        print(f"Playing: {playlist.pop(0)}")
    else:
        print("Playlist is empty")

def show_all(playlist):
    if len(playlist) == 0:
        print("Playlist is empty")
    else:
        print(*playlist, sep="\n")

def playlist_app():
    playlist = []
    finish = False
    while not finish:
        user_choice = input("Select command: ")

        if user_choice == "add":
            new_song = input("Enter song name: ")
            add(new_song, playlist)
        elif user_choice == "remove":
            song_to_remove = input("Enter song name to remove: ")
            remove(song_to_remove, playlist)
        elif user_choice == "play":
            play(playlist)
        elif user_choice == "exit":
            finish = True
        elif user_choice == "show":
            show_all(playlist)
        else:
            print("Invalid command")

    print(playlist)

playlist_app()