import pandas as pd

class NaiveBayes:
    ROUND_VALUE = 3

    # @param df [pd.DataFram]: a data frame with attributes and labels.
    # @param label_attribute [String]: column name with registers label value.
    def __init__(self, df, label_attribute):
        self.df = df
        self.label_attribute = label_attribute

    def predict(self, X_predict):
        probabilities = self.__calc_raw_probabilities(X_predict)
        transformed_probabilities = self.__transform_probabilities_into_pergentage(probabilities)
        return max(transformed_probabilities, key=transformed_probabilities.get)

    # TODO: add method predict_proba.
    # Returns a hash with class and probability
    def predict_proba(self, X_predict):
        probabilities = self.__calc_raw_probabilities(X_predict)
        transformed_probabilities = self.__transform_probabilities_into_pergentage(probabilities)
        return transformed_probabilities


    # Returns a list with all attribute names without class name attribue.
    def __attribute_names(self):
        columns = self.df.columns.values.tolist()
        columns.remove(self.label_attribute)
        return columns

    # Returns a list with possible class (label) values.
    def __labels_unique_values(self):
        labels_unique_values = self.df[self.label_attribute].unique()
        labels_unique_values.sort()
        return labels_unique_values

    # TODO: add doc
    # TODO: extract round level to const
    # calcula probabilidade de um atributo para o valor de entrada e uma das classes.
    def __calc_attribute_probability(self, attribute_name, attribute_value, label):
        attribute_count = self.df[
            (self.df[attribute_name] == attribute_value) & (df[self.label_attribute] == label)
        ].shape[0]
        class_total_count = self.__calc_class_total_count(label)
        return round(attribute_count / class_total_count, self.ROUND_VALUE)

    # TODO: add doc, usado no calculo da probabilidade do atributo
    def __calc_class_total_count(self, label):
        return self.df[self.df[self.label_attribute] == label].shape[0]

    # TODO: add doc
    # TODO: extract round level to const
    def __calc_class_probability(self, label):
        return round(
            self.df[self.df[self.label_attribute] == label].shape[0] / df.shape[0],
            self.ROUND_VALUE
        )

    # TODO: add doc
    # calcula as probabilidades de cada classe.
    def __calc_raw_probabilities(self, X_predict):
        probabilities = {}
        for label in self.__labels_unique_values():
            # NOTE: starts with value 1.0 becasue will be applied multiplications.
            probabilities[label] = 1.0
            for (index, attribute_name) in enumerate(self.__attribute_names()):
                attribute_value = X_predict[index]
                attribute_probability = self.__calc_attribute_probability(attribute_name, attribute_value, label)
                probabilities[label] *= attribute_probability

            label_probability = self.__calc_class_probability(label)
            probabilities[label] *= label_probability

        return probabilities

    # TODO: add doc
    # transforma valores de probabilidades em porcentagem
    def __transform_probabilities_into_pergentage(self, probabilities):
        transformed_probabilities = {}

        sum_values = sum(probabilities.values())
        for label in probabilities.keys():
            probability = (probabilities[label] / sum_values) * 100
            transformed_probabilities[label] = round(probability, self.ROUND_VALUE)

        return transformed_probabilities



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

model = NaiveBayes(df, CLASS_COLUMN_NAME)
print(model.predict(['Boa', 'Alta', 'Nenhuma', '> 35000']))
print(model.predict_proba(['Boa', 'Alta', 'Nenhuma', '> 35000']))

# TODO: calc 2 values para validar
# TODO: comparar com resultado do sklearn
