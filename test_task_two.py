from task_two import *
from task_one import create_file
import unittest

class TestTask2(unittest.TestCase):
    def test_basic_load_vector(self):
        create_file('test.csv', 1000, 50)
        vectors = load_vectors('test.csv')

        # количество векторов
        self.assertEqual(len(vectors), 1000)

        # Количество обьектов
        for v in vectors:
            self.assertEqual(len(list(v.componens)), 50)

    def test_swap(self):
        create_file('test.csv', 501, 11)
        vectors = load_vectors('test.csv')
        histogram_vector = gem_vector_histogram(vectors)
        # Проверка размера
        self.assertLessEqual(len(histogram_vector), 501 * 11)

    def test_histogram_vectors(self):
        create_file('test.csv', 501, 11)
        vectors = load_vectors('test.csv')
        histogram_vector = gem_vector_histogram(vectors)
        plt.bar(list(histogram_vector.keys()), histogram_vector.values(), color='g')
        plt.savefig('image')


if __name__ == '__main__':
    unittest.main()
