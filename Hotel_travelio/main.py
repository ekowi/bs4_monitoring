from scrapping import get_data, tampil_data, panda

#use this code to inform this main file

if __name__ == '__main__':
    print('This main file')
    data = get_data()
    panda(data)
    tampil_data(data)