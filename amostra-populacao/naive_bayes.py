import pandas as pd

def calc_class_probability(df, class_name):
    return round(df[df[CLASS_COLUMN_NAME] == class_name].shape[0] / df.shape[0], 3)

# TODO: add doc, usado no calculo da probabilidade do atributo
def calc_class_total_count(df, class_name):
    return df[df[CLASS_COLUMN_NAME] == class_name].shape[0]


# TODO: add doc
def calc_attribute_probability(df, class_name, attribute_name, attribute_value):
    attribute_count = df[
        (df[attribute_name] == attribute_value) & (df[CLASS_COLUMN_NAME] == class_name)
      ].shape[0]
    class_total_count = calc_class_total_count(df, class_name)

    return round(attribute_count / class_total_count, 3)

CLASS_COLUMN_NAME = 'Risco'

COLUMNS = ['História de crédito', 'Dívida', 'Garantias', 'Renda anual', 'Risco']

VALUES = [
    ['Ruim', 'Alta', 'Nenhuma', '< 15000', 'Alto'],
    ['Desconhecida', 'Alta', 'Nenhuma', '>= 15000 a <= 35000', 'Alto'],
    ['Desconhecida', 'Baixa', 'Nenhuma', '>= 15000 a <= 35000', 'Moderado'],
    ['Desconhecida', 'Baixa', 'Nenhuma', '< 15000', 'Alto'],
    ['Desconhecida', 'Baixa', 'Nenhuma', '> 35000', 'Baixo'],
    ['Desconhecida', 'Baixa', 'Adequada', '> 35000', 'Baixo'],
    ['Ruim', 'Baixa', 'Nenhuma', '< 15000', 'Alto'],
    ['Ruim', 'Baixa', 'Adequada', '> 35000', 'Moderado'],
    ['Boa', 'Baixa', 'Nenhuma', '> 35000', 'Baixo'],
    ['Boa', 'Alta', 'Adequada', '> 35000', 'Baixo'],
    ['Boa', 'Alta', 'Nenhuma', '< 15000', 'Alto'],
    ['Boa', 'Alta', 'Nenhuma', '>= 15000 a <= 35000', 'Moderado'],
    ['Boa', 'Alta', 'Nenhuma', '> 35000', 'Baixo'],
    ['Ruim', 'Alta', 'Nenhuma', '>= 15000 a <= 35000', 'Alto']
]

df = pd.DataFrame(VALUES, columns=COLUMNS)


# calcula a probabilidade da classe
class_probability = calc_class_probability(df, 'Alto')

print(class_probability)

# filtra probabilidade do atributo
print(df[(df['História de crédito'] == 'Boa') & (df['Risco'] == 'Alto')].shape[0])

# calcula a probabilidade de um atributo
print(calc_attribute_probability(df, 'Alto', 'História de crédito', 'Boa'))

# TODO: add loop que calcula para todos os atributos
# TODO: add loop que calcula para todas as classes
# NOTE: utilizar implementação através de classe
