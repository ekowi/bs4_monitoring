"""
Run this Program to get data from e-commerce
"""
from monitoring import get_data, show_data

if __name__ == '__main__':
    print('this main program')
    result = get_data()
    show_data(result)
