import numpy as np

"""
Amostragem sistemática:
  - definir tamanho da amostra;
  - calcular distância;
  - definir índice inicial;
  - selecionar indivíduos que compões a amostra.
"""

def calc_distance(population, sample_size):
  return round(population.shape[0] / sample_size)

# initial_index value is fixed to validate implementation, but this value must be random.
def calc_sample_indexes(sample_size, population):
  initial_index = 2
  population_indexes = []
  distance = calc_distance(population, sample_size)

  for i in range(0, sample_size):
    index_value = initial_index + distance * i
    population_indexes.append(index_value)

  return population_indexes

def get_samples(sample_size, population, sample_indexes):
  samples = []

  for i in range(0, sample_size):
    sample_index = sample_indexes[i]
    samples.append(population[sample_index])

  return samples


population = np.array(
    [
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
      15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28
    ],
    np.uint8
)

sample_size = 5
sample_indexes = calc_sample_indexes(sample_size, population)
samples = get_samples(sample_size, population, sample_indexes)

print(samples)
