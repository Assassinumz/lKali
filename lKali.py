#!/usr/bin/env python
#-*- coding: utf-8 -*-
################################################################################
#                                                                              #
#                                                                              #
#                                   lKali                                      #
#                         Lazy script for kali linux                           #
#                              By: Assassin umz                                #
#                                                                              #
# Follow me :                                                                  #
# •YouTube: https://youtube.com/c/pixiters                                     #
# •Discord: https://discord.gg/3nfQadt                                         #
# •Website: http://pixiters.ga                                                 #
# •GitHub: https://github.com/Assassinumz                                      #
#                                                                              #
#                                                                              #
################################################################################

import os
from time import sleep
from sys import exit

red= '\033[91m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'
input= '\33[38;5;47m' + '\033[1m' + 'lKali:~# ' + '\033[0m'

def clr():
    os.system('clear')

def head():
    clr()
    print'''{1}{2}
 ▄█          ▄█   ▄█▄    ▄████████  ▄█        ▄█
███         ███ ▄███▀   ███    ███ ███       ███
███         ███▐██▀     ███    ███ ███       ███▌
███        ▄█████▀      ███    ███ ███       ███▌
███       ▀▀█████▄    ▀███████████ ███       ███▌
███         ███▐██▄     ███    ███ ███       ███
███▌    ▄   ███ ▀███▄   ███    ███ ███▌    ▄ ███
█████▄▄██   ███   ▀█▀   ███    █▀  █████▄▄██ █▀
▀           ▀                      ▀{0}
{2}By: Assassin umz{0}
Follow me:
{1}•{0}YouTube: {3}https://youtube.com/c/pixiters{0}
{1}•{0}Website: {3}http://pixiters.ga{0}\n'''.format(end, red, bold, cyan)

def finish():
    head()
    print('{1}{2}Until next time...{0}').format(end, bold, green)
    exit(0)

def kernel():
    head()
    choose = raw_input('1{1}]{0} update\n2{1}]{0} upgrade\n3{1}]{0} dist-upgrade\n4{1}]{0} update all\n0{1}]{0} Main Menu\n\n'.format(end, red)+ input)
    clr()
    if choose == '0':
        main()
    elif choose == '1':
        os.system('apt-get update -y')
        raw_input('\n{1}{2}(Hit Return to coninue){0}'.format(end, bold, green))
    elif choose == '2':
        os.system('apt-get upgrade -y')
        raw_input('\n{1}{2}(Hit Return to coninue){0}'.format(end, bold, green))
    elif choose == '3':
        os.system('apt-get dist-upgrade -y')
        raw_input('\n{1}{2}(Hit Return to coninue){0}'.format(end, bold, green))
    elif choose == '4':
        os.system('apt-get update -y')
        os.system('apt-get upgrade -y')
        os.system('apt-get dist-upgrade -y')
        os.system('apt-get autoremove')
        raw_input('\n{1}{2}(Hit Return to coninue){0}'.format(end, bold, green))
    else:
        raw_input('\n{1}Please choose a valid option {2}(Hit Return to coninue){0}'.format(end, bold, green))
        kernel()
    kernel()

def tools():
    head()
    print('[{2}*{0}]{1}Clones into /opt by default{0}\n\n'.format(end, bold, green))
    choose = raw_input('1{1}]{0} SPG (Simple-Payload-Generator)\n2{1}]{0} cupp (Common)\n3{1}]{0} SocialFish\n4{1}]{0} torghost\n0{1}]{0} Main Menu\n\n'.format(end, red) + input)
    if choose == '0':
        main()
    elif choose == '1':
        if os.path.isdir('/opt/simple-payload-generator') == False:
            os.system('cd /opt && git clone https://github.com/Assassinumz/simple-payload-generator.git')
        os.system('gnome-terminal -x bash -c "python /opt/simple-payload-generator/spg.py; bash"')
    elif choose == '2':
        if os.path.isdir('/opt/cupp') == False:
            os.system('cd /opt && git clone https://github.com/Mebus/cupp.git')
        os.system('gnome-terminal -x bash -c "python /opt/cupp/cupp.py -i; bash"')
    elif choose == '3':
        if os.path.isdir('/opt/SocialFish') == False:
            os.system('apt-get install python3 -y')
            os.system('cd /opt && git clone https://github.com/UndeadSec/SocialFish.git')
            os.system('cd /opt && pip install requirements.txt')
        os.system('gnome-terminal -x bash -c "python3 /opt/SocialFish/SocialFish.py; bash"')
    elif choose == '4':
        if os.path.isdir('/opt/torghost') == False:
            os.system('cd /opt && git clone https://github.com/susmithHCK/torghost.git')
            os.system('cd /opt && ./install.sh')
        os.system('gnome-terminal -x bash -c "torghost start; bash"')
    else:
        raw_input('{1}Please choose a valid option {2}(Hit Return to coninue){0}'.format(end, bold, green))
        tools()
    tools()

def main():
    head()
    choose = raw_input('if{1}]{0} ifconfig\nmsfs{1}]{0} Start MSF Services\nmsf{1}]{0} Start MSF Console\ntor{1}]{0} Install and start tor service\n1{1}]{0} Kernel\n2{1}]{0} Tools\n0{1}]{0} Exit\n\n'.format(end, red) + input)
    if choose == '0':
        finish()
    elif choose == 'if':
        clr()
        os.system('ifconfig')
        raw_input('{1}{2}(Hit Return to continue){0}'.format(end, bold, green))
    elif choose == 'msfs':
        os.system('service postgresql start')
        os.system('msfdb start')
        sleep(3)
    elif choose == 'msf':
        os.system('gnome-terminal -x msfconsole')
    elif choose == 'tor':
        os.system('apt-get install tor')
        os.system('gnome-terminal -x tor')
    elif choose == '1':
        kernel()
    elif choose == '2':
        tools()
    else:
        raw_input('{1}Please choose a valid option {2}(Hit Return to continue){0}'.format(end, bold, green))
    main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        finish()
