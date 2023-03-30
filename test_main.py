import pytest
from main import get_data, get_area, get_population, area_sort, population_sort



test_data = [
    ['usa', '1000', '12849'],
    ['ukraine', '18472', '12345'],
    ['germany', '12345', '28367']
]


def test_get_data():
    with open('population.txt', 'w') as f:
        for line in test_data:
            f.write(','.join(line) + '\n')

    assert get_data('population.txt') == test_data