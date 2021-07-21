def more_or_less_or_equal(message, my_num):
    if message > my_num:
        return 'Загаданное число меньше'
    if message < my_num:
        return 'Загаданное число больше'
    if message == my_num:
        return 'Ура! Ты угадал моё число'
