#!/usr/bin/env python
#-*- coding: utf-8 -*-
################################################################################
#                                                                              #
#                                                                              #
#                                   lKali                                      #
#                         Lazy script for kali linux                           #
#                              By: Assassin umz                                #
#                                                                              #
#                                                                              #
#                                                                              #
################################################################################

import os
from time import sleep
from sys import exit

red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'
type= '\33[38;5;47m' + '\033[1m' + 'lKali:~# ' + '\033[0m'

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
▀           ▀                      ▀
{0}'''.format(end, red, bold)

def finish():
    head()
    print('Until next time....')
    exit(0)

def kernel():
    head()
    choose = raw_input('1] update\n2] upgrade\n3] dist-upgrade\n4] update all\n0] Main Menu\n\n'+ type)
    clr()
    if choose == '0':
        main()
    elif choose == '1':
        os.system('apt-get update -y')
        raw_input('\n(Hit Return to coninue)')
    elif choose == '2':
        os.system('apt-get upgrade -y')
        raw_input('\n(Hit Return to coninue)')
    elif choose == '3':
        os.system('apt-get dist-upgrade -y')
        raw_input('\n(Hit Return to coninue)')
    elif choose == '4':
        os.system('apt-get update -y')
        os.system('apt-get upgrade -y')
        os.system('apt-get dist-upgrade -y')
        os.system('apt-get autoremove')
        raw_input('\n(Hit Return to coninue)')
    else:
        raw_input('\nPlease choose a valid option (Hit Return to coninue)')
        kernel()
    kernel()

def tools():
    head()
    print('Clones into /opt by default\n\n')
    choose = raw_input('1] SPG (Simple-Payload-Generator)\n2] cupp (Common)\n3] SocialFish\n4] torghost\n0] Main Menu\n\n' + type)
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
        raw_input('Please choose a valid option (Hit Return to coninue)')
        tools()
    tools()

def main():
    head()
    choose = raw_input('if] ifconfig\nmsfs] Start MSF Services\nmsf] Start MSF Console\ntor] Install and start tor service\n1] Kernel\n2] Tools\n0] Exit\n\n'+type)
    if choose == '0':
        finish()
    elif choose == 'if':
        clr()
        os.system('ifconfig')
        raw_input('Hit Return to continue')
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
        raw_input('Please choose a valid option (Hit Return to continue)')
    main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        finish()
