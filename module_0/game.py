import numpy as np


def game_core_v1(number):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число

        if number == predict:
            return count  # выход из цикла, если угадали


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
     больше оно или меньше нужного.
    Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    """
    Сначала устанавливем среднее значение в последовательности 0-101.
    Затем, если не угадали устанавливаем среднее значение между угадываемым и искомым.
    Функция принимает загаданное число и возвращает число попыток
    """
    max_number = 101

    count = 0
    predict = int(max_number / 2)
    while True:
        count += 1
        if predict == number:
            return count

        if predict > number:
            # we should to floor predict by casting to int
            predict = int((number + predict) / 2)
        elif predict < number:
            # we should to ceil predict by adding 0.5
            predict = int((number + predict) / 2 + 0.5)


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, 1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v1)
score_game(game_core_v2)
score_game(game_core_v3)
