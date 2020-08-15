from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print("\033[1;93m")
           print(" \033[1;92mPlease login to continue!")
           print("\033[1;93m")
           try:
                x = str(input('\033[1;92mUsername \033[1;93m: '))
                e = getpass('\033[1;92mPassword \033[1;93m: ')
                print ("")
                if x=="root" and e=="root":
                   print('Successfully logged in, please wait ....')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   os.system('figlet ' + x + ' | lolcat')
                   print("")
                   break
                else:
                      print("\033[1;91m Password / Username is wrong!")
                      time.sleep(2)
                      print("")
           except Exception:
                      print("\033[1;91m Password / Username is wrong!")
                      time.sleep(2)
           except KeyboardInterrupt:
                      os.system('killall -9 com.termux')
                      print("\033[1;91m Password / Username is wrong!")
                      time.sleep(2)
menu()
