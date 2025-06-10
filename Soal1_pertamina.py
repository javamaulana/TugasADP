from termcolor import cprint, colored
from pyfiglet import figlet_format

def logo_pertamina():
    logo = [
    "                                                  ",
    "                      ###############             ",
    "                       ###############            ",
    "                        ###############           ",
    "                          ###############         ",
    "                                                  ",
    "          ______________   ***************        ",
    "         ______________   ***************         ",
    "        ______________   ***************          ",
    "       ______________   ***************           ",
    "      ______________                              ",
    "     ______________                               ",
    "    ______________                                ",
    "   ______________                                 ",
    "                                                  "  
    ]

    for baris in logo:
        for piksel in baris:
            if piksel == '#':
                cprint(' ', on_color='on_red', end='')
            elif piksel == '*':
                cprint(' ', on_color='on_green', end='')
            elif piksel == '_':
                cprint(' ', on_color='on_blue', end='')
            else:
                cprint(' ', on_color='on_white', end='')
        print()

def teks_pertamina():
    teks = figlet_format('Pertamina'.center(10))
    teks_background = ''
    for baris in teks.splitlines():
        background = colored(baris, 'black', 'on_white')  
        teks_background += background + '\n'
    print(teks_background)

logo_pertamina()
teks_pertamina()
