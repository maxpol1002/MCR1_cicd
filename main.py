def get_data(filename):
    with open(filename, 'r') as file:
        data = [line.strip().split(',') for line in file]
        return data

