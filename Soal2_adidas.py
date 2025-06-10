from termcolor import cprint, colored
from pyfiglet import figlet_format

def logo_adidas():
    logo = [
    "                                                                    ",
    "                           ###                                      ",
    "                        #########                                   ",
    "                     ###############                                ",
    "                       ###############                              ",
    "                  ###      ###############                          ",
    "               #########      ###############                       ",
    "            ###############      ###############                    ",
    "               ###############      ###############                 ",
    "         ###      ###############      ###############              ",
    "      #########      ###############      ###############           ",
    "   ###############      ###############      ###############        ",
    "      ###############      ###############      ###############     ",
    ]

    for baris in logo:
        for piksel in baris:
            if piksel == '#':
                cprint(' ', on_color='on_black', end='')
            else:
                cprint(' ', on_color='on_white', end='')
        print()

def teks_adidas():
    teks = figlet_format('adidas'.center(43))
    teks_background = ''
    for baris in teks.splitlines():
        background = colored(baris, 'black', 'on_white')  
        teks_background += background + '\n'
    print(teks_background)

logo_adidas()
teks_adidas()