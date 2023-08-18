import pandas as pd

"""
A amostragem estratificada é feita de com base em um atributo que é utilizado para dividir a popu-
lação em grupos, e por fim selecionar uma amostra de forma a manter a representatividade da popula-
ção.

Passos:
  - calcular valor proporcional de cada grupo;
  - calcular o número de indivíduos de cada grupo;
  - selecionar elementos de cada grupo;
"""
SAMPLE_SIZE = 50

COLUMNS = [
    'Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
    'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
    'Normal Nucleoli', 'Mitoses', 'Class'
]

dataframe = pd.read_csv(
    '../datasets/breast-cancer/breast-cancer-wisconsin.data',
    names=COLUMNS
)

# possible class values: 2 (benign) and 4 (malignant)
values_counts = dataframe['Class'].value_counts().to_dict()

print('Benign: ', values_counts[2])
print('Malignat: ', values_counts[4])
population_size = dataframe.shape[0]

benign_propotion = round(values_counts[2] / population_size, 2)
malignat_propotion = round(values_counts[4] / population_size, 2)
print('Benign proportion: ', benign_propotion)
print('Malignant proportion: ', malignat_propotion)

benign_count = int(SAMPLE_SIZE * benign_propotion)
malignant_count = int(SAMPLE_SIZE * malignat_propotion)
print('Bening count: ', benign_count)
print('Malignant count: ', malignant_count)

benign_samples = dataframe[dataframe['Class'] == 2].sample(benign_count)
malignant_samples = dataframe[dataframe['Class'] == 4].sample(malignant_count)
print('Benign samples shape: ', benign_samples.shape)
print('Malignant samples shape: ', malignant_samples.shape)

sample = pd.concat([benign_samples, malignant_samples])
print('Samples: ', sample.shape)

print(sample)
