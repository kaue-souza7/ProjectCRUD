import json
import os
from functions.list_products import list_product
from functions.dados_em_comum import path_json, validating_float, validating_int, clear_terminal


def update_product():
    os.system('cls')

    size_of_file = os.path.getsize(path_json)
    if size_of_file == 0:
          print('No products found, first add a product!')
          print()
          return
    
    list_product()



    product = input('Enter the product to be handled: ')

    with open(path_json, 'r+', encoding="utf8") as file:
        products = json.load(file)
        products = dict(products)

        if product in products:
            clear_terminal()

            print('Product:')
            print(products[product], '\n')
            

            print('Enter the updated data: ')

            name = input('Name: ')
            value = input('Value(!only number!): ')
            amount = input('Amount: ')

            clear_terminal()


            try:
        
                products[product] = {
                        'name': name,
                        'value': float(value),
                        'amount': int(amount)
                }

                with open(path_json, 'w+') as file:
                    file.write('')

                with open(path_json, 'w', encoding="utf8") as file:
                    json.dump(products, file, indent=2)
                    print('Product updated successfully')
                    print()
            except ValueError:
                print('Enter only valid entries!')
                return False


            
                
        else:
            print()
            print('Product not found!')
            print()

            