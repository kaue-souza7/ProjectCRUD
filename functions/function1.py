import os
import json
import random
from functions import path_json, command, validating_float, validating_int, creating_dict

def add_product():

    size_of_file = os.path.getsize(path_json)
    if size_of_file == 0:
          creating_dict()

    os.system('cls')
    print("Let's add the product")
    print()

    name = input('Enter product name: ')
    value = input('Enter value of product (!only number!): ')
    amount = input('Enter amount of product: ')
    os.system('cls')

    validating_float(value)
    validating_int(amount)
    
    
    try:
        if validating_int and validating_float:
            amount = int(amount)
            value = float(value)

            random_number = random.randint(1, 1000)
            product = {
                f'product{random_number}': {
                    'name': name,
                    'value': value,
                    'amount': amount
                }

            }
            

        with open(path_json, 'r+', encoding="utf8") as file:
            products = json.load(file)
            products = dict(products)

            products.update(product)

            with open(path_json, 'w+') as file:
                file.write('')

            with open(path_json, 'w', encoding="utf8") as file:
                json.dump(products, file, indent=2)
                print('Product added successfuly')

    except ValueError:
        print('Enter only valid entries!')