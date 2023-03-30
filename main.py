def get_data(filename):
    with open(filename, 'r') as file:
        data = [line.strip().split(',') for line in file]
        return data


def get_area(country):
    return int(country[1])


def get_population(country):
    return int(country[2])


def area_sort(data):
    sorted_by_area = sorted(data, key=get_area, reverse=True)
    return sorted_by_area


def population_sort(data):
    sorted_by_population = sorted(data, key=get_population, reverse=True)
    return sorted_by_population


def print_data(data):
    for country in data:
        print(country)


def main():
    print_data(area_sort(get_data("population.txt")))
    print_data(population_sort(get_data("population.txt")))


if __name__ == '__main__':
    main()





