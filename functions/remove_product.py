import os
import json
from functions.dados_em_comum import path_json
from functions.list_products import list_product




def remove_product():
    size_of_file = os.path.getsize(path_json)
    if size_of_file == 0:
          os.system('cls')
          print("File with nothing")
          print('First add a Product')
          print()
          return

    with open(path_json, 'r+', encoding="utf8") as file:
        products = json.load(file)
        products = dict(products)
        
        list_product()
        print()

        removed_product = input('Enter the product to be removed: ')
    


        if removed_product in products:
                os.system('cls')
                print('Removing product...')

                removed = products.pop(removed_product)
                print(removed)

                with open(path_json, 'w', encoding="utf8") as file:
                    json.dump(products, file, indent=2)
                    print('Product removed successfuly')
                    print()

        else:
             print('Product not found.')
             return False