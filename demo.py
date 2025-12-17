'''
Module Documentation
'''

def func1(a,b):
    '''
    Docstring for func1
    
    :param a: Description
    :param b: Description
    '''
    return a+b


products_prices = [25,67,89,45]

def add_10_pc():
    for idx in range(len(products_prices)):
        val = products_prices[idx] * 0.10
        products_prices[idx] += val


def add1_10_pc1(products_prices_lst: list, discount_rate: float):
    new_product_prices_lst = list()
    for idx in range(len(products_prices_lst)):
        val = products_prices_lst[idx] * discount_rate
        new_product_prices_lst.append(products_prices_lst[idx] + val)
    
    return new_product_prices_lst

add_10_pc()
new_product_prices = add1_10_pc1(products_prices_lst=products_prices,discount_rate=0.10)


