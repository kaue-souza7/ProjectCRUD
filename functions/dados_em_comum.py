import os
import json
path_json = 'db.json'


def clear_terminal():
    os.system('cls')

def creating_dict():
    fixed = {
        'product_fixed':{
            'name': 'DO NOT REMOVE',
            'value': 0,
            'amount': 0,
        }
    }

    with open(path_json, 'w', encoding="utf8") as file:
        json.dump(fixed, file)


# print(product)

command = {
    '1': 'add_product',
    '2': 'list_product',
    '3': 'update_product',
    '4': 'remove_product',
    '5': 'exit'
}

def validating_int(*args):
    for arg in args:
        try:
           int(arg)
           continue      
        except ValueError:
            print('Enter only valid entries!')
            return False
        except:
            print('Erro não reconhecido, tente novamente!')
    return True  

def validating_float(*args):
    for arg in args:
        try:
            arg = float(arg)
            continue
        except ValueError:
            print('Enter only valid entries!')
            return False
        except:
            print('Erro não reconhecido, tente novamente!')
    return True