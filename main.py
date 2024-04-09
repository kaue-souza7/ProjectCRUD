import json
import os
import importlib
from functions import add_product, command, list_product, update_product, remove_product



def list_command():
    print('Choose a option: ')
    for number, option in command.items():
        print(f'{number} - {option}')

def execute_command(option):
    if option not in ['1', '2', '3', '4', '5']:
        print('Only insert the existing option!')
        print()

    elif option == '1':
        add_product()
    elif option == '2':
        list_product()
    elif option == '3':
        update_product()
    elif option == '4':
        remove_product()
    else:
        pass


while True:
    list_command()
    option = input('Option: ')
    execute_command(option)

    if option == '5':
        os.system('cls')
        print('Leaving... Goodbye')
        break