# [
# | Developer : GabrielCtz
# | Information : Si jamais la fonction "package" intervient même lorsque vous avez cp le fichier dans le dossier, je vous conseille de delete la
# [

import os
import time
import getpass
import requests
import speech_recognition as sr
from colorama import Fore, Style, init
from easygui import fileopenbox
import sys

init()
os.system("title Speech To Text | Developer : GabrielCtz")
def package():
    folder = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\speech_recognition\\pocketsphinx-data\\fr-FR"
    folders = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\speech_recognition\\pocketsphinx-data"
    if not os.path.exists(folder):
        for countdown in range(3, 0, -1):
            os.system("cls")
            print(f"\n ╔\n ║ {Fore.GREEN} Speech to text {Fore.RED} 2k23{Fore.RESET}\n ║ {Fore.GREEN} Developer: {Fore.RED} GabrielCtz{Fore.RESET}\n ╚")
            print(f"\n [{Fore.RED}!{Fore.RESET}] Vous n'avez pas installé la langue française pour l'utilisation du module.")
            print(f"\n [{Fore.YELLOW}?{Fore.RESET}] Google Drive: https://drive.google.com/file/d/0Bw_EqP-hnaFNN2FlQ21RdnVZSVE/view?resourcekey=0-CEkuW10BcLuDdDnKDbzO4w")
            print(f'\n [{Fore.GREEN}+{Fore.RESET}] Infos: Ensuite il vous suffit de copier-coller le dossier "{folders}"')
            print(f"\n [{Fore.RED}X{Fore.RESET}] Fermeture du script dans {countdown}s ...")
            time.sleep(1)

        sys.exit()

def main():
    os.system("cls")
    print(f"\n ╔\n ║ {Fore.GREEN} Speech to text {Fore.RED} 2k23{Fore.RESET}\n ║ {Fore.GREEN} Developer: {Fore.RED} GabrielCtz{Fore.RESET}\n ╚")
    files = fileopenbox(msg="Sélectionnez votre audio à convertir.")

    if files.endswith(".wav"):
            r = sr.Recognizer()
            with sr.AudioFile(files) as source:
                audio = r.record(source)
                text = r.recognize_sphinx(audio, language="fr-FR")
                print(f"\n [ {text} ]")
    else:
        main()

main()
