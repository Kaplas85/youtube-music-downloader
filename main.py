# Time
from datetime import datetime

# PyTube
from pytube import Playlist, YouTube


def download_playlist(playlist_url: str, folder_name: str) -> None:
    p: Playlist = Playlist(playlist_url)

    # Create Folder
    destination = f"./sounds_{folder_name}"

    # Downloading
    for video in p.videos:
        print(f"Dowloading song {video.title}")
        video.streams.filter(only_audio=True).first().download(
            output_path=destination, filename=f"{video.title}.mp3"
        )


def download_single(song_url: str, folder_name: str) -> None:
    yt = YouTube(song_url)
    destination = f"./sounds_{folder_name}"
    print(f"Dowloading {yt.title} song")
    yt.streams.filter(only_audio=True).first().download(
        output_path=destination, filename=f"{yt.title}"
    )


if __name__ == "__main__":

    is_single = str(input("Are you wanna download a single song? [y/n]: "))

    while not is_single:
        is_single = str(
            input('Write "y" or "n". Are you wanna download a single song? [y/n] : ')
        )

    url = str(input("Song or Playlist URL: "))
    folder_name = str(input("Folder Name: "))

    start_time = datetime.now()
    if is_single == "y":
        download_single(url, folder_name)
        item = "Song"
    elif is_single == "n":
        download_playlist(url, folder_name)
        item = "Playlist"

    print("---------------\n\n")
    print(f"{item} dowloaded in: {datetime.now() - start_time}")
    print("\n\n---------------")
