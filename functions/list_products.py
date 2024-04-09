import os
import json
from functions.dados_em_comum import path_json, clear_terminal

def list_product():
    clear_terminal()
    print('Existing products: ')
    print()

    size_of_file = os.path.getsize(path_json)
    if size_of_file == 0:
          print('No products found, first add a product!')
          print()
          return

    with open(path_json, 'r', encoding="utf8") as file:
        products = json.load(file)

        for product, description in products.items():
            print()
            print()
            print(product)
            for key, value in description.items():
                print(key, value)
    print()
    return True
                
