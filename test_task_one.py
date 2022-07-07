import random
import unittest
from task_one import *

class Task1Test(unittest.TestCase):
  def test_gen_number(self):
    # проверка генерации в пределах -1,1
    for i in range(10000):
      self.assertGreaterEqual(get_nember(),-1)
      self.assertLessEqual(get_nember(),1)

  def test_create_file_low(self):
    # проверка нижней границы
    create_file('test.csv', 501, 11)
    with open('test.csv') as myfile:
      count = sum(1 for line in myfile)
    self.assertEqual(count, 501)

  def test_create_file_high(self):
    # проверка верхней границы
    create_file('test.csv', 1000, 50)
    with open('test.csv') as myfile:
      count = sum(1 for line in myfile)
    self.assertEqual(count, 1000)

  def test_create_file_count_line(self):
    # проверка количество элементов в строке и файле
    create_file('test.csv', 1000, 50)
    count = 0
    with open('test.csv') as myfile:
      for line in myfile:
        str_cout = len(line.split(','))
        # Проверка кол-во элементов в строке
        self.assertEqual(str_cout, 50, msg=line)
        count += str_cout
    # Проверка общего кол-во элементов
    self.assertEqual(count, 1000 * 50)

  def test_input(self):
    """ Проверка для случайного ввода """
    n = int(input('\nВведите N:\t'))
    m = int(input('Введите m:\t'))
    create_file('test.csv', n, m)

if __name__ == '__main__':
    unittest.main()
