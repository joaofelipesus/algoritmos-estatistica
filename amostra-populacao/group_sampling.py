import numpy as np
import random


"""
Amostragem por grupos:
  - dividir a populaçãom em N grupos;
  - definir aleatoriamente um dos grupos como amostra.
"""

def calc_group_size(popuation, n_groups):
    return int(popuation.shape[0] / n_groups)

def split_population_in_groups(population, n_groups):
    group_size = calc_group_size(population, n_groups)

    initial_group_index = 0
    final_grouop_index = group_size

    groups = []
    for _ in range(0, n_groups):
        groups.append(population[initial_group_index: final_grouop_index])
        initial_group_index += group_size
        final_grouop_index += group_size

    return groups


GROUPS_NUMBER = 4

population = np.array(
    [
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
      15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28
    ],
    np.uint8
)

groups = split_population_in_groups(population, GROUPS_NUMBER)
sample_group_index = random.randint(0, GROUPS_NUMBER - 1)
sample = groups[sample_group_index]
print('Sample:')
print(sample)

