from genericpath import exists
from pytube import YouTube 
import sys, os
from pytube.cli import on_progress
from rich.console import Console
from rich.markdown import Markdown
import time

from rich.traceback import install
install() # traceback error

console = Console()


# Downloading the video
def downloading_video():

    # Ask user for the link
    link = console.input("\n[bold cyan]Enter the link: ")
    console.print(f"[bold cyan]The title of the video is:[/bold cyan] [bold red]{YouTube(link).title}[/bold red]")
    time.sleep(0.2)

    # Ask user for the path
    to_path = console.input("[bold cyan]Enter the path to save the video: ")
    file_exists = exists(to_path + f"\\{YouTube(link).title}.mp4")

    # Check if the file exists
    if file_exists:
        console.print("[bold red]The file already exists![/bold red]")
        time.sleep(0.2)
        sys.exit()

    # Getting the highest resolution
    yt = YouTube(link, on_progress_callback=on_progress)
    stream = yt.streams.get_highest_resolution()

    # Downloading the video
    stream.download(to_path)
    console.print("\n[bold green]Download completed! :thumbs_up:\n")
    console.print(f"[bold cyan]The video is saved in:[/] [bold red]{to_path.upper()}" + "\\" + f"{YouTube(link).title}[/bold red]")
    time.sleep(0.2)
    answer = console.input("[bold cyan]Do you want to download another video? Y/N \n")
    
    # Ask user if he wants to download another video
    if answer == "Y" or answer == "y":
        downloading_video()
    else:
        console.print("[bold yellow]Thank you for using the program! :smiley:")
        sys.exit()


# ---------------------------- Main ---------------------------- #

MARKDOWN = """
# Youtube Downloader

Steps to use the program:

1. Enter the link of the video you want to download
2. Enter the path where you want to save the video
3. The video will be downloaded in the highest resolution
4. Enjoy! :smiley:
"""
md = Markdown(MARKDOWN)
console.print(md)
time.sleep(1)

# Calling the function
downloading_video()
