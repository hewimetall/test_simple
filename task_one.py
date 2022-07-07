import random

def get_nember():
    # Random float number [ -1, 1 ]
    return random.choice([1, -1]) * random.random()


def create_file(file_name: str, n: int, m: int):
    """ Функия генерации файла """
    if 500 > n or n > 1000:
        raise ValueError("число n должно быть в диапозоне 500≤1000.")
    if 10 > m or m > 50:
        raise ValueError("число m должно быть в диапозоне 10≤50.")

    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(n):
            # Генерация строки
            string = ",".join([str(get_nember()) for i in range(m)])
            f.write(string + '\n')

        print("Файл успешно создан.")


if __name__ == '__main__':
    n = int(input('\nВведите N:\t'))
    m = int(input('Введите m:\t'))
    create_file('vectors.csv', n, m)
