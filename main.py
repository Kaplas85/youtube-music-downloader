# Time
from datetime import datetime

# PyTube
from pytube import Playlist


def download_playlist(playlist_url: str, folder_name: str) -> None:
    p: Playlist = Playlist(playlist_url)

    # Create Folder
    destination = f"./sounds_{folder_name}"

    # Downloading
    for video in p.videos:
        print(f"Descargando canción {video.title}")
        video.streams.filter(only_audio=True).first().download(output_path=destination)


if __name__ == "__main__":

    playlist_url = str(input("Playlist URL: "))
    folder_name = str(input("Nombre de la carpeta: "))

    start_time = datetime.now()
    download_playlist(playlist_url, folder_name)

    print("---------------\n\n")
    print(f"Playlist descargada en: {datetime.now() - start_time}")
    print("\n\n---------------")
