import time
import screen_functions as func

# Colour Class
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[93m'
    OKRED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# # # ART # # #
# Text Art

def gametitle_screen():
    print(f"""{bcolors.OKGREEN}
               ████████╗██╗  ██╗███████╗
               ╚══██╔══╝██║  ██║██╔════╝
                  ██║   ███████║█████╗  
                  ██║   ██╔══██║██╔══╝  
                  ██║   ██║  ██║███████╗

       ███████╗ ██████╗ ███╗   ███╗██████╗ ██╗███████╗
       ╚══███╔╝██╔═══██╗████╗ ████║██╔══██╗██║██╔════╝
         ███╔╝ ██║   ██║██╔████╔██║██████╔╝██║█████╗  
        ███╔╝  ██║   ██║██║╚██╔╝██║██╔══██╗██║██╔══╝  
        ███████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝██║███████╗
        ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝╚══════╝

     ██╗   ██╗ █████╗ ██████╗ ██╗ █████╗ ███╗   ██╗████████╗
     ██║   ██║██╔══██╗██╔══██╗██║██╔══██╗████╗  ██║╚══██╔══╝
     ██║   ██║███████║██████╔╝██║███████║██╔██╗ ██║   ██║   
     ╚██╗ ██╔╝██╔══██║██╔══██╗██║██╔══██║██║╚██╗██║   ██║   
      ╚████╔╝ ██║  ██║██║  ██║██║██║  ██║██║ ╚████║   ██║   
      ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                                       
    {bcolors.ENDC}
    """)

def bedroom_title_art():
    print(f"""{bcolors.OKRED}
     ██╗  ██╗ ██████╗ ███████╗██████╗ ██╗████████╗ █████╗ ██╗     
     ██║  ██║██╔═══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔══██╗██║     
     ███████║██║   ██║███████╗██████╔╝██║   ██║   ███████║██║     
     ██╔══██║██║   ██║╚════██║██╔═══╝ ██║   ██║   ██╔══██║██║     
     ██║  ██║╚██████╔╝███████║██║     ██║   ██║   ██║  ██║███████╗
     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝

    ██████╗ ███████╗██████╗ ██████╗  ██████╗  ██████╗ ███╗   ███╗
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║
    ██████╔╝█████╗  ██║  ██║██████╔╝██║   ██║██║   ██║██╔████╔██║
    ██╔══██╗██╔══╝  ██║  ██║██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║
    ██████╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
    ╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝
    {bcolors.ENDC}""")

def morgue_title_art():
    print(f"""{bcolors.OKRED}
    ███╗   ███╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗███████╗
    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝ ██║   ██║██╔════╝
    ██╔████╔██║██║   ██║██████╔╝██║  ███╗██║   ██║█████╗  
    ██║╚██╔╝██║██║   ██║██╔══██╗██║   ██║██║   ██║██╔══╝  
    ██║ ╚═╝ ██║╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝███████╗
    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
    {bcolors.ENDC}""")

def surgery_title_art():
    print(f"""{bcolors.OKRED}
    ███████╗██╗   ██╗██████╗  ██████╗ ███████╗██████╗ ██╗   ██╗
    ██╔════╝██║   ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗╚██╗ ██╔╝
    ███████╗██║   ██║██████╔╝██║  ███╗█████╗  ██████╔╝ ╚████╔╝ 
    ╚════██║██║   ██║██╔══██╗██║   ██║██╔══╝  ██╔══██╗  ╚██╔╝  
    ███████║╚██████╔╝██║  ██║╚██████╔╝███████╗██║  ██║   ██║   
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝
    {bcolors.ENDC}""")

def basement_title_art():
    print(f"""{bcolors.OKRED}
    ██████╗  █████╗ ███████╗███████╗███╗   ███╗███████╗███╗   ██╗████████╗
    ██╔══██╗██╔══██╗██╔════╝██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
    ██████╔╝███████║███████╗█████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
    ██╔══██╗██╔══██║╚════██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
    ██████╔╝██║  ██║███████║███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
    {bcolors.ENDC}""")

def gameover_art():
    print(f"""{bcolors.OKGREEN}
     ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                            CREATED BY: TEAM RED
        Lorell Boscoe, Thom Butterworth, Jordan Richmond, and John Rowbotham
    {bcolors.ENDC}""")

def gameover_screen():
    func.spacer(1)
    gameover_art()
    

def gamewin_art():
    print(f"""{bcolors.OKGREEN}
                                ______.........--=T=--.........______
                                .             |:|
                            :-. //           /""""""-.
                            ': '-._____..--""(""""""()`---.__
                            /:   _..__   ''  ":""""'[] |""`'' \
                            ': :'     `-.     _:._     '"""" :
                            ::          '--=:____:.___....-"
                                                O"       O"
    ██╗   ██╗ ██████╗ ██╗   ██╗    ███████╗███████╗ ██████╗ █████╗ ██████╗ ███████╗██████╗ 
    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ╚████╔╝ ██║   ██║██║   ██║    █████╗  ███████╗██║     ███████║██████╔╝█████╗  ██║  ██║
    ╚██╔╝  ██║   ██║██║   ██║    ██╔══╝  ╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝  ██║  ██║
     ██║   ╚██████╔╝╚██████╔╝    ███████╗███████║╚██████╗██║  ██║██║     ███████╗██████╔╝
     ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═════╝
                                CREATED BY: TEAM RED
        Lorell Boscoe, Thom Butterworth, Jordan Richmond, and John Rowbotham
    """)

def scanning_art():
    print(f"""{bcolors.OKRED}
                             _                   
                            (_)                  
     ___  ___ __ _ _ __  _ __  _ _ __   __ _       
    / __|/ __/ _` | '_ \| '_ \| | '_ \ / _` |      
    \__ \ (_| (_| | | | | | | | | | | | (_| |_ _ _ 
    |___/\___\__,_|_| |_|_| |_|_|_| |_|\__, (_|_|_)
                                        __/ |      
                                        |___/                                       
    {bcolors.ENDC}""")

def success_art():
    print(f"""{bcolors.OKGREEN}
                                  
     ___ _   _  ___ ___ ___  ___ ___ 
    / __| | | |/ __/ __/ _ \/ __/ __|
    \__ \ |_| | (_| (_|  __/\__ \__ \       
    |___/\__,_|\___\___\___||___/___/
                                  
    {bcolors.ENDC}""")

# Inventory Art
def zombiefinger_art():
    print("         /-\            ")
    print("        |\./|           ")
    print("        |   |           ")
    print("        |   |           ")
    print("        |>~<|           ")
    print("        |   |           ")
    print("        |   |           ")
    print("        |   |           ")
    print("        |   |           ")
    print(f"        -{bcolors.OKRED}~~~{bcolors.ENDC}-           ")
    print(f"        {bcolors.OKRED}; : ;{bcolors.ENDC}           ")
    print(f"          {bcolors.OKRED};{bcolors.ENDC}             ")

def terminatorhand_art():
    print("         /-\            ")
    print("     /-\|\./|/ \        ")
    print("    |\./|   |\./|       ")
    print("    |   |   |   |       ")
    print("    |   |>~<|   |/-\    ")
    print("    |>~<|   |>~<|\./|   ")
    print("    |   |   |   |   |   ")
    print("/~T\|   |   =[@]=   |   ")
    print("|_/ |   |   |   |   |   ")
    print("|   | ~   ~   ~ |   |   ")
    print("|~< |             ~ |   ")
    print("|   '               |   ")
    print("\                   |   ")
    print(" \   S K Y N E T   /    ")
    print("  \               /     ")
    print("   \.            /      ")
    print("     |          |       ")
    print("     |          |       ")
    print("                        ")

def scalpel_art():
    print("      ______________________________ ______________________   ")
    print("    .'                              | (_)     (_)    (_)   \  ")
    print("  .'                                |  __________________   } ")
    print(".'_.............................____|_(                  )_/  ")
    print("                                                              ")

def sceptre_art():
    print("               .::.                              ")
    print("            .      `.                            ")
    print(f"          :   {bcolors.OKCYAN}~*~{bcolors.ENDC}   :                           ") 
    print(f"          :    {bcolors.OKCYAN}***{bcolors.ENDC}   :       ::                 ")
    print(f"          :   {bcolors.OKCYAN}*****{bcolors.ENDC}  :         ::               ")
    print(f"          .   {bcolors.OKCYAN}***{bcolors.ENDC}   .          ::              ")
    print(f"           .  {bcolors.OKCYAN}~*~{bcolors.ENDC}  .              ::            ") 
    print("             `.    .                ::           ")
    print("              :/\/\:                :;          ")
    print("              :/\/\:                :;        ")
    print("              :/\/\:               :;       ")
    print("              :/\/\:              :;      ")
    print("              :/\/\:             :     ")
    print("              :/\/\:             :    ")
    print("              :/\/\:            :    ")
    print("              :/\/\:           :    ")
    print("              ::::::          :   ")
    print("              [LOKI]         :  ")
    print("              [POKI]        :   ")
    print("              [STIK]       :   ")
    print("              [____]     :    ")
    print("              [____]   .:`   ")

def lockclosed_image():
    print("                                    ████████                                  ")
    print("                              ██████        ██████                            ")
    print("                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░▓▓██                        ")
    print("                      ██░░░░░░░░▒▒▒▒████████▒▒▒▒░░░░░░░░██                    ")
    print("                    ██  ░░░░▒▒▒▒████        ████▒▒▒▒░░░░  ██                  ")
    print("                  ▓▓░░░░░░▒▒████                ████▒▒░░░░░░▓▓                ")
    print("                  ██░░░░▒▒██                        ██▒▒░░░░██                ")
    print("                ██░░░░▒▒██                            ██▒▒░░░░██              ")
    print("                ██░░▒▒██                                ██▒▒░░██              ")
    print("              ██░░░░▒▒██                                ██▒▒░░░░██            ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("      ▒▒▒▒▒▒██░░░░▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒░░░░██▒▒▒▒▒▒    ")
    print("    ██░░░░░░██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒██░░░░░░██  ")
    print("  ██░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░██")
    print("  ██▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒██")
    print("  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
    print("   ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██   ")
    print("      ████████████████████████████████████████████████████████████████████    ")

def lockopen_image():
    print("                                    ████████                                  ")
    print("                              ██████        ██████                            ")
    print("                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░▓▓██                        ")
    print("                      ██░░░░░░░░▒▒▒▒████████▒▒▒▒░░░░░░░░██                    ")
    print("                    ██  ░░░░▒▒▒▒████        ████▒▒▒▒░░░░  ██                  ")
    print("                  ▓▓░░░░░░▒▒████                ████▒▒░░░░░░▓▓                ")
    print("                  ██░░░░▒▒██                        ██▒▒░░░░██                ")
    print("                ██░░░░▒▒██                            ██▒▒░░░░██              ")
    print("                ██░░▒▒██                                ██▒▒░░██              ")
    print("              ██░░░░▒▒██                                ██▒▒░░░░██            ")
    print("            ██░░░░▒▒██                                                        ")
    print("            ██░░░░▒▒██                                                        ")
    print("            ██░░░░▒▒██                                                        ")
    print("            ██░░░░▒▒██                                                        ")
    print("            ██░░░░▒▒██                                                        ")
    print("      ▒▒▒▒▒▒██░░░░▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ")
    print("    ██░░░░░░██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░██")
    print("  ██▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒██")
    print("  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
    print("   ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██   ")
    print("      ████████████████████████████████████████████████████████████████████    ")

def lock_animation():   # Animates Lock Opening
    for i in range(1):
        func.clear_screen()
        lockclosed_image()
        time.sleep(2)
        func.clear_screen()
        lockopen_image()
        time.sleep(0.5)