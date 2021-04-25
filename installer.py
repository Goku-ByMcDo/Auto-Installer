import os
os.system("cls")
os.system("pip install colorama")
os.system("cls")
from colorama import * 
banner = """
                      ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗ 
                      ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
                      ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝
                      ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
                      ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║
                      ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                 
                                           Installing requirements

"""


def discord():
    try:
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Installing discord")
        os.system('pip install discord')

    except:
        print(Fore.RED + " ! "+Fore.RESET+"Une erreur est survenue...")
        pass

def pyfiglet():
    try:
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Installing Pyfiglet")
        os.system('pip install pyfiglet')

    except:
        print(Fore.RED + " ! "+Fore.RESET+"Une erreur est survenue...")
        pass

def art():
    try:
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Installing ART")
        os.system('pip install art')

    except:
        print(Fore.RED + " ! "+Fore.RESET+"Une erreur est survenue...")
        pass


def json():
    try:
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Installing json")
        os.system('pip install json')

    except:
        print(Fore.RED + " ! "+Fore.RESET+"Une erreur est survenue...")
        pass


def bs4():
    try:
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Installing BS4")
        os.system('pip install bs4')
    except:
        print(Fore.RED + " ! "+Fore.RESET+"Une erreur est survenue...")

def requests():    
    try:
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Installing requests")
        os.system("pip install requests")
    except:
        print(Fore.RED + " ! "+Fore.RESET+"Une erreur est survenue...")

def installer():
    try:
        print(Fore.BLUE + banner + Fore.RESET)
        os.system("python -m pip install --upgrade pip")
        requests()
        art()
        bs4()
        print("["+Fore.GREEN+"INFO"+Fore.RESET+"] Succesfully installed you can close")
        input("")
    except:
        print(Fore.RED + " ! "+Fore.RESET+"Une erreur est survenue...")

installer()
