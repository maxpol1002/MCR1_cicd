def get_data(filename):
    with open(filename, 'r') as file:
        data = [line.strip().split(',') for line in file]
        return data


def get_area(country):
    return int(country[1])


def area_sort(data):
    sorted_by_area = sorted(data, key=get_area, reverse=True)
    return sorted_by_area



