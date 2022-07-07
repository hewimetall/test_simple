import math
import matplotlib.pyplot as plt


class Vector:
    def __init__(self, componens):
        self._componens = list(map(float, componens.split(',')))
        self._max_len = len(self._componens)

    def calculate(self, v2: "Vector"):
        """ Вычисляем растояния в эвкоидовом пространстве. """
        return math.sqrt(
            sum((self._componens[i] - v2._componens[i])**2
                for i in range(self._max_len)))

    @property
    def componens(self):
        return self._componens


def load_vectors(file_name):
    """ Загрузка файла с данными """
    vectors = []
    with open(file_name, 'r', encoding='utf-8') as myfile:
        for line in myfile:
            vectors.append(Vector(line))
    return vectors


def gem_vector_histogram(list_vectors:list):
    """ Генерация частотной выборки на основе растояний между векторами """
    diogramm = {}
    for vector in list_vectors:
        vectors_scalart = map(lambda x: round(vector.calculate(x), 1),
                              list_vectors)
        for scalar in vectors_scalart:
            try:
                diogramm[scalar] += 1
            except KeyError:
                diogramm[scalar] = 1
    # Удаляем произведения вектора на себя
    diogramm[0.0] = 0
    return diogramm


if __name__ == '__main__':
    vectors = load_vectors('vectors.csv')
    histogram_vector = gem_vector_histogram(vectors)
    plt.bar(list(histogram_vector.keys()),
            histogram_vector.values(),
            color='g')
    plt.savefig('histogram')
