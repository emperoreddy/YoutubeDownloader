from pytube import YouTube 
import sys
from pytube.cli import on_progress
from rich.console import Console

console = Console()


# Downloading the video
def downloading_video():

    # Ask user for the link
    link = input("Enter the link: ")
    console.print(f"The title of the video is: [bold red]{YouTube(link).title}[/bold red]")

    # Ask user for the path
    to_path = input("Enter the path to save the video: ")

    # Getting the highest resolution
    yt = YouTube(link, on_progress_callback=on_progress)
    stream = yt.streams.get_highest_resolution()

    # Downloading the video
    stream.download(to_path)
    console.print("Download completed! :thumbs_up:")
    console.print(f"The video is saved in: [bold red]{to_path.upper()}[/bold red]")
    answer = input("Do you want to download another video? Y/N \n")
    
    # Ask user if he wants to download another video
    if answer == "Y" or answer == "y":
        downloading_video()
    else:
        console.print("Thank you for using the program! :smiley:")
        exit()



# Calling the function
downloading_video()
