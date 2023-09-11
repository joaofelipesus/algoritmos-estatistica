import numpy as np

"""
As métricas referentes a média, mediana e moda são aplicadas em conjunto para sumarizar um conjunto
de dados.
  - Média: somatório de todos os valores / número de elementos;
  - Mediana:
    - ordena-seo conjunto de dados;
    - caso o o conjunto possua um número par de exemplares a mediana se da pela média dos dois
      elementos centrais;
    - caso o conjunto possua um número ímpar de exemplares a mediana se da pelo valor presente no
      índice central.
  - Moda: é o valor que mais se repete na distribuição.
"""

def average(dataset):
  return round(np.sum(dataset) / dataset.shape[0], 2)


def mean(dataset):
  dataset.sort()
  index = round(dataset.shape[0] / 2)
  if (dataset.shape[0] % 2) == 0:
    median_values = dataset[index - 1: index + 1]
    return round(median_values.sum() / 2)
  else:
    return dataset[index]

def mode(dataset):
  dataset.sort()
  values_counts = {}
  index = 0
  current_value = dataset[0]
  current_value_count = 0

  while True:
    if index >= dataset.shape[0]:
      break

    if current_value == dataset[index]:
      current_value_count += 1
      index += 1
    else:
      values_counts[current_value] = current_value_count
      current_value_count = 1
      current_value = dataset[index]

  return max(values_counts, key=values_counts.get)

dataset = np.array([1, 2, 3, 1, 1, 4, 5, 1, 3 , 2, 1, 2, 3, 1])
print('Média:', average(dataset))
print('Mediana:', mean(dataset))
print('Mode', mode(dataset))
