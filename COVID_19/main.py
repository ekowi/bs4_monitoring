"""
this main file for take funtion from init.py to run program
"""
from monitoring import get_data,tampildata

if  __name__ == '__main__':
    result = get_data()
    tampildata(result)
