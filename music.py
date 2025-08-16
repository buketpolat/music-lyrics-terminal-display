import time
import os
import sys
from colorama import init, Fore, Style

# Colorama başlat
init(autoreset=True)

if 'TERM' not in os.environ:
    os.environ['TERM'] = 'xterm-256color'

lyrics = [
    "(Wake me up)wake me up inside",
    "(I can't wake up)wake me up inside",
    "(Save me)call my name and save me from the dark",
    "","",
    "(Wake me up)bid my blood to run",
    "I can't wake up)before I come undone",
    "(Save me)save me from the nothing I've become",
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_lyrics(lyrics):
    clear_screen()
    print(Fore.CYAN + Style.BRIGHT + "== Bring Me To Life ==\n")

    colors = [Fore.YELLOW, Fore.MAGENTA, Fore.GREEN, Fore.CYAN]

    for i, line in enumerate(lyrics):
        color = colors[i % len(colors)]
        for char in line:
            sys.stdout.write(color + char)
            sys.stdout.flush()
            time.sleep(0.06)  # harf arası gecikme
        print()  # satır sonu
        time.sleep(0.55)  # satır arası gecikme

if __name__ == "__main__":
    display_lyrics(lyrics)