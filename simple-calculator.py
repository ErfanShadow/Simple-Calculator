import math
import os
import time
import art
from colorama import Fore, Back, Style, just_fix_windows_console

just_fix_windows_console()


def clear():
    os.system('cls')


def sleep(a):
    time.sleep(a)


Art = art.text2art('PY Calculator', 'rand')


sleep(2)

clear()
print(Fore.RED + Art)
print(Fore.YELLOW +
      '\n Hi Welcome My Calculator Python Project :)\n' + Fore.GREEN + 'MADE BY RIT4X: https://github.com/erfanshadow' + Fore.RESET)
sleep(5)

clear()
while True:
    first_num = input('[-]' + Fore.GREEN +
                      'WRITE YOUR FIRST NUMBER :>>>' + Fore.RESET)
    action = input(
        Fore.YELLOW + 'WHICH ACTION DO YOU WANT TO DO WITH THIS NUMBER? \n 1) + \n 2) - \n 3) * \n 4) / \n 5) ** \n 6) // \n 7) Sin \n 8) Cos \n 9) Tan \n 10) Cot \n' + Fore.RED + '[*]>>>' + Fore.RESET)
    if action == '1':
        sec_num = input('[-]' + Fore.GREEN +
                        'WRITE YOUR SECOND NUMBER :>>>' + Fore.RESET)
        print('[-]' + Fore.CYAN + 'ANSWER::>' + Fore.RESET,
              float(first_num) + float(sec_num))

    elif action == '2':
        sec_num = input('[-]' + Fore.GREEN +
                        'WRITE YOUR SECOND NUMBER :>>>' + Fore.RESET)
        print('[-]' + Fore.CYAN + 'ANSWER::>' + Fore.RESET,
              float(first_num) - float(sec_num))

    elif action == '3':
        sec_num = input('[-]' + Fore.GREEN +
                        'WRITE YOUR SECOND NUMBER :>>>' + Fore.RESET)
        print('[-]' + Fore.CYAN + 'ANSWER::>' + Fore.RESET,
              float(first_num) * float(sec_num))

    elif action == '4':
        sec_num = input('[-]' + Fore.GREEN +
                        'WRITE YOUR SECOND NUMBER :>>>' + Fore.RESET)
        print('[-]' + Fore.CYAN + 'ANSWER::>' + Fore.RESET,
              float(first_num) / float(sec_num))

    elif action == '5':
        sec_num = input('[-]' + Fore.GREEN +
                        'WRITE YOUR SECOND NUMBER :>>>' + Fore.RESET)
        print('[-]' + Fore.CYAN + 'ANSWER::>' + Fore.RESET,
              float(first_num) ** float(sec_num))

    elif action == '6':
        sec_num = input('[-]' + Fore.GREEN +
                        'WRITE YOUR SECOND NUMBER :>>>' + Fore.RESET)
        print('[-]' + Fore.CYAN + 'ANSWER::>' + Fore.RESET,
              float(first_num) // float(sec_num))

    elif action == '7':
        print('[-]' + Fore.CYAN + 'ANSWER::>' + Fore.RESET,
              math.sin(float(first_num)))

    elif action == '8':
        print('[-]' + Fore.CYAN + 'ANSWER::>' + Fore.RESET,
              math.cos(float(first_num)))

    elif action == '9':
        print('[-]' + Fore.CYAN + 'ANSWER::>' + Fore.RESET,
              math.tan(float(first_num)))

    elif action == '10':
        print('[-]' + Fore.CYAN + 'ANSWER::>' + For1e.RESET,
              1 / math.tan(float(first_num)))
    sleep(5)
    clear()
    continue
