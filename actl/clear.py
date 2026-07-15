import os
import platform

def clear():
    """
    Clears the terminal screen regardless of whether 
    the user is on Windows, Linux, macOS, or Android.
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
